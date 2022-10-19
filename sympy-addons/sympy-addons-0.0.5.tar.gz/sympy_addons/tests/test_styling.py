from sympy import Derivative, latex, sin, cos
from sympy.abc import x, y, z, f

from sympy_addons.styling import apply_style


def test_style_derivative():

    # Apply styling by instance
    df_dx = Derivative(f, x)
    df_dx._latex = lambda printer: r'\frac{d %s}{d %s}' % (df_dx.args[0], df_dx.args[1][0])
    #apply_style(df_dx, r'\frac{d %0}{d %1}')
    assert latex(df_dx) == r'\frac{d f}{d x}'

    # Other instances should not be affected
    df_dy = Derivative(f, y)
    assert latex(df_dx) == r'\frac{d f}{d x}'
    assert latex(df_dy) == r'\frac{d}{d y} f'

    # Unless we set the styling for the whole class
    Derivative._latex = lambda self, printer: r'\frac{d %s}{d %s}' % (self.args[0], self.args[1][0])
    df_dz = Derivative(f, z)
    assert latex(df_dx) == r'\frac{d f}{d x}'
    assert latex(df_dy) == r'\frac{d f}{d y}'
    assert latex(df_dz) == r'\frac{d f}{d z}'


def test_rewrite():

    expr = sin(2*x)
    expr.rewrite(cos)