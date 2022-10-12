"""
Plot Morris elementary effects
"""
import openturns as ot
from openturns.viewer import View


def PlotEE(result, output_marginal=0, absolute_mean=True, title="Elementary effects"):
    """
    Plot elementary effects
    -----------------------

    The class perform the plot of sensitivity indices issued from Morris class.

    Parameters
    ----------
    morris: :class:`~otmorris.Morris`
        A Morris object.

    output_marginal: int
        Index of output marginal of interest.
        Default value is 0

    absolute_mean: bool
        Interest is mean of absolute elementary effects .
        Default value is True

    title: str
        Title for the graph

    """
    ot.Log.Warn('PlotEE is deprecated in favor of Morris.drawElementaryEffects')
    if not (hasattr(result, 'getStandardDeviationElementaryEffects') and hasattr(result, 'getClassName')):
        raise TypeError(" `result` should be of class Morris ")
    graph = result.drawElementaryEffects(output_marginal, absolute_mean)
    graph.setTitle(title)
    return View(graph)
