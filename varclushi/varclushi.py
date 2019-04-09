
import pandas as pd
import numpy as np
import random
import collections
import math
from factor_analyzer import Rotator



class VarClusHi(object):

    def __init__(self,df,feat_list=None,maxeigval2=1,maxclus=None,n_rs=0):

        if feat_list is None:
            self.df = df
            self.feat_list = df.columns.tolist()
        else:
            self.df = df[feat_list]
            self.feat_list = feat_list
        self.maxeigval2 = maxeigval2
        self.maxclus = maxclus
        self.n_rs = n_rs

    @staticmethod
    def correig(df, feat_list=None, n_pcs=2):

        if feat_list is None:
            feat_list = df.columns.tolist()
        else:
            df = df[feat_list]

        if len(feat_list) <= 1:
            corr = [len(feat_list)]
            eigvals = [len(feat_list)] + [0] * (n_pcs - 1)
            eigvecs = np.array([[len(feat_list)]])
            varprops = [sum(eigvals)]
        else:
            corr = np.corrcoef(df.values.T)
            raw_eigvals, raw_eigvecs = np.linalg.eig(corr)
            idx = np.argsort(raw_eigvals)[::-1]
            eigvals, eigvecs = raw_eigvals[idx], raw_eigvecs[:, idx]
            eigvals, eigvecs = eigvals[:n_pcs], eigvecs[:, :n_pcs]
            varprops = eigvals / sum(raw_eigvals)

        corr_df = pd.DataFrame(corr, columns=feat_list, index=feat_list)

        return eigvals, eigvecs, corr_df, varprops


    @staticmethod
    def pca(df, feat_list=None, n_pcs=2):

        if feat_list is None:
            feat_list = df.columns.tolist()
        else:
            df = df[feat_list]

        stand_df = (df - df.mean()) / df.std()

        eigvals, eigvecs, _, varprops = VarClusHi.correig(df, feat_list, n_pcs=n_pcs)

        if len(feat_list) <= 1:
            princomps = stand_df.values
        else:
            princomps = np.dot(stand_df.values, eigvecs)

        return eigvals, eigvecs, princomps, varprops


    @staticmethod
    def _calc_tot_var(df, *clusters):

        tot_len, tot_var, tot_prop = (0,) * 3

        for clus in clusters:
            if clus == []:
                continue

            c_len = len(clus)
            c_eigvals, _, _, c_varprops = VarClusHi.correig(df[clus])
            tot_var += c_eigvals[0]
            tot_prop = (tot_prop * tot_len + c_varprops[0] * c_len) / (tot_len + c_len)
            tot_len += c_len

        return tot_var, tot_prop


    @staticmethod
    def _reassign(df, clus1, clus2, feat_list=None):

        if feat_list is None:
            feat_list = clus1 + clus2

        init_var = VarClusHi._calc_tot_var(df, clus1, clus2)[0]
        fin_clus1, fin_clus2 = clus1[:], clus2[:]
        check_var, max_var = (init_var,) * 2

        while (True):

            for feat in feat_list:
                new_clus1, new_clus2 = fin_clus1[:], fin_clus2[:]
                if feat in new_clus1:
                    new_clus1.remove(feat)
                    new_clus2.append(feat)
                elif feat in new_clus2:
                    new_clus1.append(feat)
                    new_clus2.remove(feat)
                else:
                    continue

                new_var = VarClusHi._calc_tot_var(df, new_clus1, new_clus2)[0]
                if new_var > check_var:
                    check_var = new_var
                    fin_clus1, fin_clus2 = new_clus1[:], new_clus2[:]

            if max_var == check_var:
                break
            else:
                max_var = check_var

        return fin_clus1, fin_clus2, max_var


    @staticmethod
    def _reassign_rs(df, clus1, clus2, n_rs=0):

        feat_list = clus1 + clus2
        fin_rs_clus1, fin_rs_clus2, max_rs_var = VarClusHi._reassign(df, clus1, clus2)

        for _ in range(n_rs):
            random.shuffle(feat_list)
            rs_clus1, rs_clus2, rs_var = VarClusHi._reassign(df, clus1, clus2, feat_list)
            if rs_var > max_rs_var:
                max_rs_var = rs_var
                fin_rs_clus1, fin_rs_clus2 = rs_clus1, rs_clus2

        return fin_rs_clus1, fin_rs_clus2, max_rs_var


    def _varclusspu(self):

        ClusInfo = collections.namedtuple('ClusInfo', ['clus', 'eigval1', 'eigval2', 'eigvecs','varprop'])
        c_eigvals, c_eigvecs, c_corrs, c_varprops = VarClusHi.correig(self.df[self.feat_list])

        self.corrs = c_corrs

        clus0 = ClusInfo(clus=self.feat_list,
                         eigval1=c_eigvals[0],
                         eigval2=c_eigvals[1],
                         eigvecs=c_eigvecs,
                         varprop=c_varprops[0]
                         )
        self.clusters = collections.OrderedDict([(0, clus0)])

        while (True):

            if self.maxclus is not None and len(self.clusters) >= self.maxclus:
                break

            idx = max(self.clusters, key=lambda x: self.clusters.get(x).eigval2)
            if self.clusters[idx].eigval2 > self.maxeigval2:
                split_clus = self.clusters[idx].clus
                c_eigvals, c_eigvecs, split_corrs, _ = VarClusHi.correig(self.df[split_clus])
            else:
                break

            if c_eigvals[1] > self.maxeigval2:
                clus1, clus2 = [], []
                rotator = Rotator()
                r_eigvecs = rotator.fit_transform(pd.DataFrame(c_eigvecs), 'quartimax')#[0].values

                comb_sigma1 = math.sqrt(np.dot(np.dot(r_eigvecs[:, 0], split_corrs.values), r_eigvecs[:, 0].T))
                comb_sigma2 = math.sqrt(np.dot(np.dot(r_eigvecs[:, 1], split_corrs.values), r_eigvecs[:, 1].T))

                for feat in split_clus:

                    comb_cov1 = np.dot(r_eigvecs[:, 0], split_corrs[feat].values.T)
                    comb_cov2 = np.dot(r_eigvecs[:, 1], split_corrs[feat].values.T)

                    corr_pc1 = comb_cov1/comb_sigma1
                    corr_pc2 = comb_cov2/comb_sigma2

                    if abs(corr_pc1) > abs(corr_pc2):
                        clus1.append(feat)
                    else:
                        clus2.append(feat)

                fin_clus1, fin_clus2, _ = VarClusHi._reassign_rs(self.df, clus1, clus2,self.n_rs)
                c1_eigvals, c1_eigvecs, _, c1_varprops = VarClusHi.correig(self.df[fin_clus1])
                c2_eigvals, c2_eigvecs, _, c2_varprops = VarClusHi.correig(self.df[fin_clus2])

                self.clusters[idx] = ClusInfo(clus=fin_clus1,
                                              eigval1=c1_eigvals[0],
                                              eigval2=c1_eigvals[1],
                                              eigvecs=c1_eigvecs,
                                              varprop=c1_varprops[0]
                                              )
                self.clusters[len(self.clusters)] = ClusInfo(clus=fin_clus2,
                                                             eigval1=c2_eigvals[0],
                                                             eigval2=c2_eigvals[1],
                                                             eigvecs=c2_eigvecs,
                                                             varprop=c2_varprops[0]
                                                             )
            else:
                break

        return self


    def varclus(self,speedup=True):
        
        self.speedup = speedup

        if self.speedup is True:
            return self._varclusspu()

        ClusInfo = collections.namedtuple('ClusInfo', ['clus','eigval1','eigval2','pc1','varprop'])
        c_eigvals, _, c_princomps, c_varprops = VarClusHi.pca(self.df[self.feat_list])
        clus0 = ClusInfo(clus=self.feat_list,
                         eigval1=c_eigvals[0],
                         eigval2=c_eigvals[1],
                         pc1=c_princomps[:, 0],
                         varprop=c_varprops[0]
                         )
        self.clusters = collections.OrderedDict([(0, clus0)])

        while (True):

            if self.maxclus is not None and len(self.clusters) >= self.maxclus:
                break

            idx = max(self.clusters, key=lambda x: self.clusters.get(x).eigval2)
            if self.clusters[idx].eigval2 > self.maxeigval2:
                split_clus = self.clusters[idx].clus
                c_eigvals, c_eigvecs, _, _ = VarClusHi.pca(self.df[split_clus])
            else:
                break

            if c_eigvals[1] > self.maxeigval2:
                clus1, clus2 = [], []
                rotator = Rotator()
                r_eigvecs = rotator.fit_transform(pd.DataFrame(c_eigvecs), 'quartimax')#[0]
                stand_df = (self.df - self.df.mean()) / self.df.std()
                r_pcs = np.dot(stand_df[split_clus].values, r_eigvecs)

                for feat in split_clus:

                    corr_pc1 = np.corrcoef(self.df[feat].values.T, r_pcs[:, 0])[0, 1]
                    corr_pc2 = np.corrcoef(self.df[feat].values.T, r_pcs[:, 1])[0, 1]

                    if abs(corr_pc1) > abs(corr_pc2):
                        clus1.append(feat)
                    else:
                        clus2.append(feat)

                fin_clus1, fin_clus2, _ = VarClusHi._reassign_rs(self.df, clus1, clus2,self.n_rs)
                c1_eigvals, _, c1_princomps, c1_varprops = VarClusHi.pca(self.df[fin_clus1])
                c2_eigvals, _, c2_princomps, c2_varprops = VarClusHi.pca(self.df[fin_clus2])

                self.clusters[idx] = ClusInfo(clus=fin_clus1,
                                              eigval1=c1_eigvals[0],
                                              eigval2=c1_eigvals[1],
                                              pc1=c1_princomps[:, 0],
                                              varprop=c1_varprops[0]
                                              )
                self.clusters[len(self.clusters)] = ClusInfo(clus=fin_clus2,
                                                             eigval1=c2_eigvals[0],
                                                             eigval2=c2_eigvals[1],
                                                             pc1=c2_princomps[:, 0],
                                                             varprop=c2_varprops[0]
                                                             )
            else:
                break

        return self


    @property
    def info(self):

        cols = ['Cluster', 'N_Vars' ,'Eigval1', 'Eigval2', 'VarProp']
        info_table = pd.DataFrame(columns=cols)

        n_row = 0
        for i, clusinfo in self.clusters.items():
            row = [repr(i), repr(len(clusinfo.clus)), clusinfo.eigval1, clusinfo.eigval2, clusinfo.varprop]
            info_table.loc[n_row] = row
            n_row += 1

        return info_table


    def _rsquarespu(self):

        cols = ['Cluster', 'Variable', 'RS_Own', 'RS_NC', 'RS_Ratio']
        rs_table = pd.DataFrame(columns=cols)

        sigmas = []
        for _, clusinfo in self.clusters.items():
            c_eigvec = clusinfo.eigvecs[:, 0]
            c_sigma = math.sqrt(np.dot(np.dot(c_eigvec, self.corrs.loc[clusinfo.clus,clusinfo.clus].values), c_eigvec.T))
            sigmas.append(c_sigma)

        n_row = 0
        for i, clus_own in self.clusters.items():
            for feat in clus_own.clus:
                row = [i, feat]

                cov_own = np.dot(clus_own.eigvecs[:,0], self.corrs.loc[feat, clus_own.clus].values.T)
                rs_own = (cov_own/sigmas[i]) ** 2

                rs_others = []
                for j, clus_other in self.clusters.items():
                    if j == i: continue

                    cov_other = np.dot(clus_other.eigvecs[:,0], self.corrs.loc[feat, clus_other.clus].values.T)
                    rs = (cov_other/sigmas[j]) ** 2

                    rs_others.append(rs)

                rs_nc = max(rs_others) if len(rs_others) > 0 else 0
                row += [rs_own, rs_nc, (1 - rs_own) / (1 - rs_nc)]
                rs_table.loc[n_row] = row
                n_row += 1

        return rs_table


    @property
    def rsquare(self):

        if self.speedup is True:
            return self._rsquarespu()

        cols = ['Cluster', 'Variable', 'RS_Own', 'RS_NC', 'RS_Ratio']
        rs_table = pd.DataFrame(columns=cols)

        pcs = [clusinfo.pc1 for _, clusinfo in self.clusters.items()]

        n_row = 0
        for i, clusinfo in self.clusters.items():
            for feat in clusinfo.clus:
                row = [i, feat]

                rs_own = np.corrcoef(self.df[feat].values.T, clusinfo.pc1)[0, 1] ** 2

                rs_others = []

                for j, pc in enumerate(pcs):
                    if j == i: continue

                    rs = np.corrcoef(self.df[feat].values.T, pc)[0, 1] ** 2

                    rs_others.append(rs)

                rs_nc = max(rs_others) if len(rs_others) > 0 else 0
                row += [rs_own, rs_nc, (1 - rs_own) / (1 - rs_nc)]
                rs_table.loc[n_row] = row
                n_row += 1

        return rs_table
		

	
if __name__ == '__main__':
	demo_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
	demo_df.drop('quality', axis=1,inplace=True)
	demo_vc = VarClusHi(demo_df)
	demo_vc.varclus()
	print(demo_vc.info)
	print(demo_vc.rsquare)

    