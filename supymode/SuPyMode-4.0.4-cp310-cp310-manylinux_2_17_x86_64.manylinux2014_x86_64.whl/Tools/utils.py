import numpy, logging

def animate_plots(base_directory, fname_prefix):
    """
    This function creates a movie of the plots using ffmpeg

    Args:
        base_directory (str): the directory with the plots.
        fname_prefix (str): the filename for the model run

    Returns:
        none but creates mp4 from pngs in base directory

    Author: FJC
    """
    import subprocess

    # animate the pngs using ffmpeg
    system_call = "ffmpeg -framerate 5 -pattern_type glob -i '"+base_directory+"*.png' -vcodec libx264 -s 1000x1000 -pix_fmt yuv420p "+base_directory+fname_prefix+"_movie.mp4"
    subprocess.call(system_call, shell=True)


def Index2NA(nCore, nClad):
    return numpy.sqrt(nCore**2 - nClad**2)


def NA2nCore(NA, nClad):
    return numpy.sqrt(NA**2+nClad**2)


def DebugFunction(func):
    def wrapper(self, *args, **kwargs):
        logging.info(f" | Function: {func.__name__}\t-> args: {args}\t kwargs: {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper








# -
