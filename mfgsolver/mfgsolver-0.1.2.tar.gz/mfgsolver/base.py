import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve, LinearOperator, gmres
from scipy.linalg import norm
from scipy.sparse import diags
import matplotlib.pyplot as plt


# generic class only implement algo. didn't implement detail func about M0, UT, F1 or F2
class MfgBase(object):
    # it's a base class which implements the policy iteration and fixed point iteration
    def __init__(
        self, Q_guess=None, nv=0.05, Nx=200, Nt=200, T=1.0, alpha=1.5, zeta=0.5
    ):
        self.Nx = Nx
        self.Nt = Nt
        self.xs = np.linspace(0, 1, self.Nx + 1)[:-1]  # grid on space
        self.dx = self.xs[1] - self.xs[0]
        self.ts = np.linspace(0, T, Nt + 1)  # grid on time
        self.dt = self.ts[1] - self.ts[0]
        self.nv = nv  # diffusion paramter
        # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
        #         = 0.5*|Du|^2/(1+m)^alpha - zeta*m
        self.alpha = alpha
        self.zeta = zeta

        # initail condition and terminal condition
        M0 = self.M0_func(self.xs)
        self.M0 = M0 / np.sum(M0) / self.dx
        self.UT = self.UT_func(self.xs)

        # array to store solution
        self.U = np.zeros((self.Nt, self.Nx))  # t = 0 ... (T-dt)
        self.M = np.ones((self.Nt, self.Nx))  # t = dt ... T
        self.M_bar = np.copy(self.M)  # using in fp
        self.M_old = np.copy(self.M)
        self.U_old = np.copy(self.U)

        # initial guess about Q
        if Q_guess:
            self.QL = np.copy(Q_guess[0])
            self.QR = np.copy(Q_guess[1])
        else:
            self.QL = np.zeros((self.Nt, self.Nx))
            self.QR = np.zeros((self.Nt, self.Nx))
        self.QL_old = np.copy(self.QL)
        self.QR_old = np.copy(self.QR)

        # some lists to log residual or something else
        self.residual_FP_history = []  # list to store history of residual
        self.residual_HJB_history = []  # list to store history of residual
        self.sol_M_history = []  # list to store history of L-inf disatance
        self.sol_U_history = []  # list to store history of L-2 disatance
        self.Laplace = self.build_Laplace()
        self.DL, self.DR = self.build_D()
        self.A_fixp = sparse.eye(self.Nx) - self.dt * self.Laplace
        return

    def build_Laplace(self):
        dim_one_laplace = diags(
            [1, 1, -2, 1, 1], [1 - self.Nx, -1, 0, 1, self.Nx - 1], format="csr"
        )
        dim_one_laplace = self.nv / self.dx**2 * dim_one_laplace
        return dim_one_laplace

    def build_D(self):
        DL = (
            diags(
                [-1, 1, -1],
                [-1, 0, self.Nx - 1],
                shape=(self.Nx, self.Nx),
                format="csr",
            )
            / self.dx
        )
        DR = (
            diags(
                [1, -1, 1], [1 - self.Nx, 0, 1], shape=(self.Nx, self.Nx), format="csr"
            )
            / self.dx
        )
        return DL, DR

    # initial condition
    def M0_func(self, x):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # final condition
    def UT_func(self, x):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # hamilton
    # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
    def F1_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    def F2_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    def hjb_rhs(self, un, q, mn):
        """
        rhs of HJB equation
        """
        ql, qr = q  # unpack
        return un + self.dt * (
            0.5 * self.F1_func(mn) * (ql**2 + qr**2) + self.F2_func(mn)
        )

    def hjb_rhs_fixp(self, un, du2, mn):
        """
        rhs of HJB equation
        """
        rhs = un - self.dt * (0.5 * du2 / self.F1_func(mn) - self.F2_func(mn))
        return rhs

    def logging_solution(self, M, U):
        self.sol_M_history.append(np.copy(M))
        self.sol_U_history.append(np.copy(U))
        return

    def linearOP_FP(self, q):
        ql, qr = q  # unpack
        tmp1 = sparse.eye(self.Nx)
        tmp2 = self.Laplace
        tmp3 = self.DL @ sparse.diags(qr) + self.DR @ sparse.diags(ql)
        return tmp1 - self.dt * (tmp2 + tmp3)

    def solve_FP(self, Q):
        """
        solve FP with drift Q (self.QL and self.QR)
        this method should only update self.M
        """
        QL, QR = Q  # unpack
        mn = self.M0
        for ti in range(self.Nt):
            ql = QL[ti, :]
            qr = QR[ti, :]
            q = [ql, qr]
            A = self.linearOP_FP(q)
            rhs = mn
            self.M[ti, :] = spsolve(A, rhs)
            mn = self.M[ti, :]
        return

    def linearOP_HJB(self, q):
        ql, qr = q
        tmp1 = sparse.eye(self.Nx)
        tmp2 = self.Laplace
        tmp3 = diags(ql) @ self.DL + diags(qr) @ self.DR
        return tmp1 - self.dt * (tmp2 - tmp3)

    def solve_HJB(self, M, Q):
        """
        solve linearize HJB with hamilton:
        qDu - 0.5*F1(m)*|q|^2 - F2(m)

        this method should only update self.U
        """
        QL, QR = Q  # unpack
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            ql = QL[ti, :]
            qr = QR[ti, :]
            q = [ql, qr]
            A = self.linearOP_HJB(q)
            rhs = self.hjb_rhs(un, q, mn)
            self.U[ti, :] = spsolve(A, rhs)
            un = self.U[ti, :]
        return

    def solve_HJB_fixp(self, M):
        """
        solve linearize HJB with hamilton:
        0.5*|Du|^2/F1(m) - F2(m)
        where Du is frezz with U_old

        this method should only update self.U
        """
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            u_old = self.U_old[ti, :]
            dul_old = np.maximum(self.DL @ u_old, 0.0)
            dur_old = np.minimum(self.DR @ u_old, 0.0)
            du2_old = dul_old**2 + dur_old**2
            mn = M[ti, :]
            lhsM = self.A_fixp
            rhs = self.hjb_rhs_fixp(un, du2_old, mn)
            self.U[ti, :] = spsolve(lhsM, rhs)
            un = self.U[ti, :]
        self.U_old = np.copy(self.U)
        return

    def update_Q(self, U, M):
        """
        this method should only update self.QL and self.QR
        """
        for ti in range(self.Nt):
            mn = M[ti, :]
            un = U[ti, :]
            self.QL[ti, :] = np.maximum((self.DL @ un) / self.F1_func(mn), 0.0)
            self.QR[ti, :] = np.minimum((self.DR @ un) / self.F1_func(mn), 0.0)
        # compute the diff bettwen Q and Q_old
        diff_QL = np.max(np.abs(self.QL - self.QL_old))
        diff_QR = np.max(np.abs(self.QR - self.QR_old))
        diff = np.max([diff_QL, diff_QR])
        # print(f"diff between Q = {diff}")
        self.QL_old = np.copy(self.QL)
        self.QR_old = np.copy(self.QR)
        return

    def default_fp_pn(n):
        return (1 - 1 / n, 1 / n)

    def solve(self, maxit=10, fp=False, pn=default_fp_pn):
        # fp: bool, use fictious play or not
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(1, maxit + 1):
            # solve FP with Q
            Q = (self.QL, self.QR)
            self.solve_FP(Q)
            # update M_bar if use fictious play
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            # update U with M_bar and Q
            self.solve_HJB(self.M_bar, Q)
            # update Q with U and M_bar
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)
            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_fp1_pn(n):
        return (n / (n + 1), 1 / (n + 1))

    def solve_with_fp1(self, maxit=10, pn=default_fp1_pn):
        self.diff_M = []
        # init
        QL_bar = np.copy(self.QL)
        QR_bar = np.copy(self.QR)
        for i in range(1, maxit + 1):
            # solve FP with Q_bar
            Q_bar = (QL_bar, QR_bar)
            self.solve_FP(Q_bar)
            # update U with M and Q_bar
            self.solve_HJB(self.M, Q_bar)
            # update Q with U and M
            self.update_Q(self.U, self.M_bar)
            # update Q_bar
            p1, p2 = pn(i)
            QL_bar = p1 * QL_bar + p2 * self.QL
            QR_bar = p1 * QR_bar + p2 * self.QR
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_fp2_pn(n):
        return (1 - 1 / n, 1 / n)

    def solve_with_fp2(self, maxit=10, pn=default_fp2_pn):
        self.diff_M = []
        # init
        QL_hat = np.copy(self.QL)
        QR_hat = np.copy(self.QR)
        self.M_bar = np.copy(self.M)
        # init W_bar, but never use this init value
        # update W_bar in first iteration with M*q
        # and average W in later iteration
        WL_bar = np.copy(self.QL)
        WR_bar = np.copy(self.QR)
        for i in range(1, maxit + 1):
            # solve FP with Q
            Q = [self.QL, self.QR]
            self.solve_FP(Q)
            # update M_bar
            p1, p2 = pn(i)
            self.M_bar = p1 * self.M_bar + p2 * self.M
            # update Q_hat(firt compute W_bar)
            if i == 1:
                WL_bar = self.M * self.QL
                WR_bar = self.M * self.QR
                QL_hat = np.copy(self.QL)  # avoid error here
                QR_hat = np.copy(self.QR)
            else:
                WL_bar = p1 * WL_bar + p2 * self.M * self.QL
                WR_bar = p1 * WR_bar + p2 * self.M * self.QR
                QL_hat = WL_bar / self.M_bar  # be careful when M_bar is too small
                QR_hat = WR_bar / self.M_bar
            # update U with M and Q_hat
            Q_hat = [QL_hat, QR_hat]
            self.solve_HJB(self.M_bar, Q_hat)
            # update Q with U and M(don't consider M here)
            self.update_Q(self.U, self.M)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def solve_with_fixpoint(self, maxit=10, fp=True, pn=default_fp_pn):
        print("solving with fixed point method")
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(1, maxit + 1):
            Q = [self.QL, self.QR]
            self.solve_FP(Q)
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            self.solve_HJB_fixp(self.M_bar)
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)

            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def compute_residual(self, M, U):
        res_fp = self.residual_FP(M, U)
        res_hjb = self.residual_HJB(M, U)
        self.residual_FP_history.append(res_fp)
        self.residual_HJB_history.append(res_hjb)
        return res_fp, res_hjb

    def residual_FP(self, M, U):
        residual_ = np.zeros_like(M)  # residual in every point
        mn = self.M0
        for ti in range(self.Nt):
            m = M[ti, :]
            un = U[ti, :]
            # q here is only a temp variable to compute residual
            ql = np.maximum((self.DL @ un) / self.F1_func(m), 0.0)
            qr = np.minimum((self.DR @ un) / self.F1_func(m), 0.0)
            q = [ql, qr]
            lhsM = self.linearOP_FP(q) / self.dt
            rhs = mn / self.dt
            residual_[ti, :] = lhsM @ m - rhs
            mn = M[ti, :]
        residual = np.sqrt(self.dx * self.dt) * norm(residual_)
        return residual

    def residual_HJB(self, M, U):
        residual_ = np.zeros_like(U)  # residual in every point
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            u = U[ti, :]
            # q here is only a temp variable to compute residual
            ql = np.maximum((self.DL @ u) / self.F1_func(mn), 0.0)
            qr = np.minimum((self.DR @ u) / self.F1_func(mn), 0.0)
            q = [ql, qr]
            lhsM = self.linearOP_HJB(q) / self.dt
            rhs = self.hjb_rhs(un, q, mn) / self.dt
            residual_[ti, :] = lhsM @ u - rhs
            un = U[ti, :]
        residual = np.sqrt(self.dx * self.dt) * norm(residual_)
        return residual


class MfgBase2D(object):
    # it's a base class which implements the policy iteration and fixed point iteration
    def __init__(
        self, Q_guess=None, nv=0.05, Nx=200, Nt=200, T=1.0, alpha=0.0, zeta=0.0
    ):
        self.Nx = Nx
        self.Nt = Nt
        self.xs1 = np.linspace(0, 1, self.Nx + 1)[:-1]  # grid on space
        self.xs2 = np.linspace(0, 1, self.Nx + 1)[:-1]  # grid on space
        self.dx = self.xs1[1] - self.xs1[0]
        self.ts = np.linspace(0, T, Nt + 1)  # grid on time
        self.dt = self.ts[1] - self.ts[0]
        self.nv = nv  # diffusion paramter
        # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
        #         = 0.5*|Du|^2/(1+m)^alpha - zeta*m
        self.alpha = alpha
        self.zeta = zeta

        # initail condition and terminal condition
        M0 = self.M0_func(self.xs1, self.xs2)
        self.M0 = M0 / np.sum(M0) / (self.dx) ** 2
        self.UT = self.UT_func(self.xs1, self.xs2)

        # array to store solution
        self.U = np.zeros((self.Nt, (self.Nx) ** 2))  # t = 0 ... (T-dt)
        self.M = np.ones((self.Nt, (self.Nx) ** 2))  # t = dt ... T
        self.M_bar = np.copy(self.M)  # using in fp
        self.M_old = np.copy(self.M)
        self.U_old = np.copy(self.U)

        # initial guess about Q
        if Q_guess:
            self.QL1 = np.copy(Q_guess[0])
            self.QR1 = np.copy(Q_guess[1])
            self.QL2 = np.copy(Q_guess[2])
            self.QR2 = np.copy(Q_guess[3])
        else:
            self.QL1 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QR1 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QL2 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QR2 = np.zeros((self.Nt, (self.Nx) ** 2))
        self.QL1_old = np.copy(self.QL1)
        self.QR1_old = np.copy(self.QR1)
        self.QL2_old = np.copy(self.QL2)
        self.QR2_old = np.copy(self.QR2)
        self.Q = [self.QL1, self.QR1, self.QL2, self.QR2]
        self.Q_old = [self.QL1_old, self.QR1_old, self.QL2_old, self.QR2_old]

        # some lists to log residual or something else
        self.residual_FP_history = []  # list to store history of residual
        self.residual_HJB_history = []  # list to store history of residual
        self.sol_M_history = []  # list to store history of L-inf disatance
        self.sol_U_history = []  # list to store history of L-2 disatance
        self.Laplace = self.build_Laplace()
        self.DL1, self.DR1, self.DL2, self.DR2 = self.build_D()
        self.A_fixp = sparse.eye(self.Nx**2) - self.dt * self.Laplace
        return

    def build_Laplace(self):
        dim_one_laplace = diags(
            [1, 1, -2, 1, 1], [1 - self.Nx, -1, 0, 1, self.Nx - 1], format="csr"
        )
        dim_two_laplace = sparse.kron(
            dim_one_laplace, sparse.eye(self.Nx)
        ) + sparse.kron(sparse.eye(self.Nx), dim_one_laplace)
        dim_two_laplace = self.nv / self.dx**2 * dim_two_laplace
        return dim_two_laplace

    def build_D(self):
        DL = diags(
            [-1, 1, -1], [-1, 0, self.Nx - 1], shape=(self.Nx, self.Nx), format="csr"
        )
        DR = diags(
            [1, -1, 1], [1 - self.Nx, 0, 1], shape=(self.Nx, self.Nx), format="csr"
        )
        DL1 = sparse.kron(sparse.eye(self.Nx), DL) / self.dx
        DR1 = sparse.kron(sparse.eye(self.Nx), DR) / self.dx
        DL2 = sparse.kron(DL, sparse.eye(self.Nx)) / self.dx
        DR2 = sparse.kron(DR, sparse.eye(self.Nx)) / self.dx
        return DL1, DR1, DL2, DR2

    # initial condition
    # should return array with shape (self.Nx*self.Nx, )
    def M0_func(self, x1, x2):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # final condition
    # should return array with shape (self.Nx*self.Nx, )
    def UT_func(self, x1, x2):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # hamilton
    # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
    def F1_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    def F2_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    def hjb_rhs(self, un, q, mn):
        ql1, qr1, ql2, qr2 = q
        rhs = un + self.dt * (
            0.5 * self.F1_func(mn) * (ql1**2 + qr1**2 + ql2**2 + qr2**2)
            + self.F2_func(mn)
        )
        return rhs

    def hjb_rhs_fixp(self, un, du2, mn):
        """
        rhs of HJB equation in fixpoint method
        """
        rhs = un - self.dt * (0.5 * du2 / self.F1_func(mn) - self.F2_func(mn))
        return rhs

    def logging_solution(self, M, U):
        self.sol_M_history.append(np.copy(M))
        self.sol_U_history.append(np.copy(U))
        return

    def linearOP_FP(self, q):
        ql1, qr1, ql2, qr2 = q  # unpack
        tmp1 = sparse.eye(self.Nx**2)
        tmp2 = self.Laplace
        tmp3 = (
            self.DL1 @ sparse.diags(qr1)
            + self.DR1 @ sparse.diags(ql1)
            + self.DL2 @ sparse.diags(qr2)
            + self.DR2 @ sparse.diags(ql2)
        )
        return tmp1 - self.dt * (tmp2 + tmp3)

    def solve_FP(self, Q):
        """
        solve FP with drift Q (self.QL and self.QR)
        this method should only update self.M
        """
        QL1, QR1, QL2, QR2 = Q  # unpack
        mn = self.M0
        for ti in range(self.Nt):
            ql1 = QL1[ti, :]
            qr1 = QR1[ti, :]
            ql2 = QL2[ti, :]
            qr2 = QR2[ti, :]
            q = [ql1, qr1, ql2, qr2]
            A = self.linearOP_FP(q)
            rhs = mn
            self.M[ti, :] = spsolve(A, rhs)
            mn = self.M[ti, :]
        return

    def linearOP_HJB(self, q):
        ql1, qr1, ql2, qr2 = q
        tmp1 = sparse.eye(self.Nx**2)
        tmp2 = self.Laplace
        tmp3 = (
            diags(ql1) @ self.DL1
            + diags(qr1) @ self.DR1
            + diags(ql2) @ self.DL2
            + diags(qr2) @ self.DR2
        )
        return tmp1 - self.dt * (tmp2 - tmp3)

    def solve_HJB(self, M, Q):
        QL1, QR1, QL2, QR2 = Q  # unpack
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            ql1 = QL1[ti, :]
            qr1 = QR1[ti, :]
            ql2 = QL2[ti, :]
            qr2 = QR2[ti, :]
            q = [ql1, qr1, ql2, qr2]
            A = self.linearOP_HJB(q)
            rhs = self.hjb_rhs(un, q, mn)
            self.U[ti, :] = spsolve(A, rhs)
            un = self.U[ti, :]
        return

    def solve_HJB_fixp(self, M):
        """
        solve linearize HJB with hamilton:
        0.5*|Du|^2/F1(m) - F2(m)
        where Du is frezz with U_old

        this method should only update self.U
        """
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            u_old = self.U_old[ti, :]
            dul1_old = np.maximum(self.DL1 @ u_old, 0.0)
            dur1_old = np.minimum(self.DR1 @ u_old, 0.0)
            dul2_old = np.maximum(self.DL2 @ u_old, 0.0)
            dur2_old = np.minimum(self.DR2 @ u_old, 0.0)
            du2_old = dul1_old**2 + dur1_old**2 + dul2_old**2 + dur2_old**2
            mn = M[ti, :]
            lhsM = self.A_fixp
            rhs = self.hjb_rhs_fixp(un, du2_old, mn)
            self.U[ti, :] = spsolve(lhsM, rhs)
            un = self.U[ti, :]
        self.U_old = np.copy(self.U)
        return

    def update_Q(self, U, M):
        """
        this method should only update self.QL and self.QR
        """
        for ti in range(self.Nt):
            mn = M[ti, :]
            un = U[ti, :]
            self.QL1[ti, :] = np.maximum((self.DL1 @ un) / self.F1_func(mn), 0.0)
            self.QR1[ti, :] = np.minimum((self.DR1 @ un) / self.F1_func(mn), 0.0)
            self.QL2[ti, :] = np.maximum((self.DL2 @ un) / self.F1_func(mn), 0.0)
            self.QR2[ti, :] = np.minimum((self.DR2 @ un) / self.F1_func(mn), 0.0)
        self.QL1_old = np.copy(self.QL1)
        self.QR1_old = np.copy(self.QR1)
        self.QL2_old = np.copy(self.QL2)
        self.QR2_old = np.copy(self.QR2)
        self.Q_old = [self.QL1_old, self.QR1_old, self.QL2_old, self.QR2_old]
        return

    def default_fp_pn(n):
        return (1 - 1 / n, 1 / n)

    def solve(self, maxit=10, fp=False, pn=default_fp_pn):
        # fp: bool, use fictious play or not
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(1, maxit + 1):
            # solve FP with Q
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            # update M_bar if use fictious play
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            # update U with M_bar and Q
            self.solve_HJB(self.M_bar, Q)
            # update Q with U and M_bar
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)
            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_fp1_pn(n):
        return (n / (1 + n), 1 / (1 + n))

    def solve_with_fp1(self, maxit=10, pn=default_fp1_pn):
        self.diff_M = []
        # init
        QL1_bar = np.copy(self.QL1)
        QR1_bar = np.copy(self.QR1)
        QL2_bar = np.copy(self.QL2)
        QR2_bar = np.copy(self.QR2)
        for i in range(1, maxit + 1):
            # solve FP with Q_bar
            Q_bar = [QL1_bar, QR1_bar, QL2_bar, QR2_bar]
            self.solve_FP(Q_bar)
            # update U with M and Q_bar
            self.solve_HJB(self.M, Q_bar)
            # update Q with U and M
            self.update_Q(self.U, self.M_bar)
            # update Q_bar
            p1, p2 = pn(i)
            QL1_bar = p1 * QL1_bar + p2 * self.QL1
            QR1_bar = p1 * QR1_bar + p2 * self.QR1
            QL2_bar = p1 * QL2_bar + p2 * self.QL2
            QR2_bar = p1 * QR2_bar + p2 * self.QR2
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_fp2_pn(n):
        return (1 - 1 / n, 1 / n)

    def solve_with_fp2(self, maxit=10, pn=default_fp2_pn):
        self.diff_M = []
        # init
        QL1_hat = np.copy(self.QL1)
        QR1_hat = np.copy(self.QR1)
        QL2_hat = np.copy(self.QL2)
        QR2_hat = np.copy(self.QR2)
        self.M_bar = np.copy(self.M)
        # init W_bar, but never use this init value
        # update W_bar in first iteration with M*q
        # and average W in later iteration
        WL1_bar = np.copy(self.QL1)
        WR1_bar = np.copy(self.QR1)
        WL2_bar = np.copy(self.QL2)
        WR2_bar = np.copy(self.QR2)
        for i in range(1, maxit + 1):
            # solve FP with Q
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            # update M_bar
            p1, p2 = pn(i)
            self.M_bar = p1 * self.M_bar + p2 * self.M
            # update Q_hat(firt compute W_bar)
            if i == 1:
                WL1_bar = self.M * self.QL1
                WR1_bar = self.M * self.QR1
                WL2_bar = self.M * self.QL2
                WR2_bar = self.M * self.QR2
                QL1_hat = np.copy(self.QL1)  # avoid error here
                QR1_hat = np.copy(self.QR1)
                QL2_hat = np.copy(self.QL2)
                QR2_hat = np.copy(self.QR2)
            else:
                WL1_bar = p1 * WL1_bar + p2 * self.M * self.QL1
                WR1_bar = p1 * WR1_bar + p2 * self.M * self.QR1
                WL2_bar = p1 * WL2_bar + p2 * self.M * self.QL2
                WR2_bar = p1 * WR2_bar + p2 * self.M * self.QR2
                QL1_hat = WL1_bar / self.M_bar  # be careful when M_bar is too small
                QR1_hat = WR1_bar / self.M_bar
                QL2_hat = WL2_bar / self.M_bar
                QR2_hat = WR2_bar / self.M_bar
            # update U with M and Q_hat
            Q_hat = [QL1_hat, QR1_hat, QL2_hat, QR2_hat]
            self.solve_HJB(self.M_bar, Q_hat)
            # update Q with U and M(don't consider M here)
            self.update_Q(self.U, self.M)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def solve_with_fixpoint(self, maxit=10, fp=False, pn=default_fp_pn):
        print("solving with fixed point method")
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(1, maxit + 1):
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            self.solve_HJB_fixp(self.M_bar)
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)

            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def compute_residual(self, M, U):
        res_fp = self.residual_FP(M, U)
        res_hjb = self.residual_HJB(M, U)
        self.residual_FP_history.append(res_fp)
        self.residual_HJB_history.append(res_hjb)
        return res_fp, res_hjb

    def residual_FP(self, M, U):
        residual_ = np.zeros_like(M)  # residual in every point
        mn = self.M0
        for ti in range(self.Nt):
            m = M[ti, :]
            un = U[ti, :]
            # q here is only a temp variable to compute residual
            ql1 = np.maximum((self.DL1 @ un) / self.F1_func(m), 0.0)
            qr1 = np.minimum((self.DR1 @ un) / self.F1_func(m), 0.0)
            ql2 = np.maximum((self.DL2 @ un) / self.F1_func(m), 0.0)
            qr2 = np.minimum((self.DR2 @ un) / self.F1_func(m), 0.0)
            q = [ql1, qr1, ql2, qr2]
            lhsM = self.linearOP_FP(q) / self.dt
            rhs = mn / self.dt
            residual_[ti, :] = lhsM @ m - rhs
            mn = M[ti, :]
        residual = np.sqrt(self.dx**2 * self.dt) * norm(residual_)
        return residual

    def residual_HJB(self, M, U):
        residual_ = np.zeros_like(U)  # residual in every point
        un = self.UT
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            u = U[ti, :]
            ql1 = np.maximum((self.DL1 @ u) / self.F1_func(mn), 0.0)
            qr1 = np.minimum((self.DR1 @ u) / self.F1_func(mn), 0.0)
            ql2 = np.maximum((self.DL2 @ u) / self.F1_func(mn), 0.0)
            qr2 = np.minimum((self.DR2 @ u) / self.F1_func(mn), 0.0)
            q = [ql1, qr1, ql2, qr2]
            lhsM = self.linearOP_HJB(q) / self.dt
            rhs = self.hjb_rhs(un, q, mn) / self.dt
            residual_[ti, :] = lhsM @ u - rhs
            un = U[ti, :]
        residual = np.sqrt(self.dx**2 * self.dt) * norm(residual_)
        return residual


def plot_residual(result, iterations: int):
    plt.plot(range(iterations), result.residual_FP_history, label="residual fp")
    plt.plot(range(iterations), result.residual_HJB_history, label="residual hjb")
    plt.yscale("log")
    plt.legend()
    plt.grid()
    plt.show()


def plot_sol_diff(bcmk, result):
    iterations = len(result.sol_M_history)
    diff_M = []
    diff_U = []
    for i in range(iterations):
        diff_M.append(np.max(np.abs(result.sol_M_history[i] - bcmk.M)))
        diff_U.append(np.max(np.abs(result.sol_U_history[i] - bcmk.U)))
    plt.plot(range(iterations), diff_M, label="|M^(n) - M^*|")
    plt.plot(range(iterations), diff_U, label="|U^(n) - U^*|")
    plt.yscale("log")
    plt.legend()
    plt.grid()
    plt.show()
