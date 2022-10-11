import sys
from typing import Optional
import logging
import numpy as np
from scipy import optimize as opt
from Qcover.optimizers import Optimizer
from Qcover.exceptions import ArrayShapeError

logger = logging.getLogger(__name__)


class L_BFGS_B(Optimizer):
    """
    L-BFGS-B: a numerical optimization method for constrained problems

    based on scipy.optimize.minimize L-BFGS-B.
    For further detail, please refer to
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
    """

    # pylint: disable=unused-argument
    def __init__(self,
                 options: dict = None,
                 initial_point: Optional[np.ndarray] = None) -> None:
        """
        Args:
            options: some optional setting parameters such as:
                maxiter: Maximum number of function evaluations.
                disp: Set to True to print convergence messages.
                rhobeg: Reasonable initial changes to the variables.
                tol: Final accuracy in the optimization (not precisely guaranteed).
                     This is a lower bound on the size of the trust region.
        """
        super().__init__()
        self._p = None
        self._options = options
        self._initial_point = initial_point

    def optimize(self, objective_function):
        if self._initial_point is None:
            self._initial_point = np.array([np.random.random() for x in range(2 * self._p)])
        else:
            try:
                if len(self._initial_point) != 2 * self._p:
                    raise ArrayShapeError("The shape of initial parameters is not match with p")
            except ArrayShapeError as e:
                print(e)
                sys.exit()

        res = opt.minimize(
                            objective_function,
                            x0=np.array(self._initial_point),
                            args=self._p,
                            method='L-BFGS-B',
                            jac=None,
                            options=self._options
                           )
        return res.x, res.fun, res.nfev


# optl = L_BFGS_B(options={'disp': None,
#     'maxcor': 10,
#     'ftol': 2.220446049250313e-09,
#     'gtol': 1e-05,
#     'eps': 1e-08,
#     'maxfun': 15000,
#     'maxiter': 15000,
#     'iprint': - 1,
#     'maxls': 20,
#     'finite_diff_rel_step': None})  #
