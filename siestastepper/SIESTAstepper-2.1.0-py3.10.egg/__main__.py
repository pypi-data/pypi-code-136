"""
SIESTAstepper terminal client
"""
from __future__ import absolute_import
import sys
from .core import (
    run,
    single_run,
    run_next,
    run_interrupted,
    single_run_interrupted,
    make_directories,
    copy_files,
    ani_to_fdf,
    xyz_to_fdf,
    xv_to_fdf,
    log_to_fdf,
    xv_to_ani,
    merge_ani,
    energy_analysis,
    force_analysis,
    energy_diff,
    force_diff,
    pair_correlation_function,
    settings
)


def main(*, args):
    """Main function"""
    function = args[1]
    for arg in args:
        independents(arg)
    if function not in ["run", "single_run", "run_next", "run_interrupted",
                        "single_run_interrupted", "make_directories",
                        "copy_files", "ani_to_fdf", "xyz_to_fdf", "xv_to_fdf",
                        "log_to_fdf", "xv_to_ani", "merge_ani", "energy_analysis",
                        "force_analysis", "energy_diff", "force_diff",
                        "pair_correlation_function"]:
        raise AttributeError(
            """Command not found. Please use 'run',
            'single_run', 'run_next', 'run_interrupted',
            'single_run_interrupted', 'make_directories',
            'copy_files', 'ani_to_fdf', 'xyz_to_fdf',
            'xv_to_fdf', 'log_to_fdf', 'xv_to_ani',
            'merge_ani', 'energy_analysis', 'force_analysis',
            'energy_diff', 'force_diff',
            'pair_correlation_function'""".replace("           ", "").replace("\n", "")
        )
    if function == "run":
        settings.set_log(args[2])
        run(args[3])
    elif function == "single_run":
        settings.set_log(args[2])
        single_run(args[3], args[4])
    elif function == "run_next":
        settings.set_log(args[2])
        run_next(args[3], args[4])
    elif function == "run_interrupted":
        settings.set_log(args[2])
        run_interrupted(args[3], args[4])
    elif function == "single_run_interrupted":
        settings.set_log(args[2])
        single_run_interrupted(args[3], args[4])
    elif function == "make_directories":
        make_directories(int(args[2]))
    elif function == "copy_files":
        copy_files(
            [_ for _ in args[5:] if not _.startswith("contfiles=")],
            args[2],
            args[3],
            args[4]
        )
    elif function == "ani_to_fdf":
        ani_to_fdf(args[2], args[3], args[4])
    elif function == "xyz_to_fdf":
        xyz_to_fdf(args[2], args[3], args[4])
    elif function == "xv_to_fdf":
        xv_to_fdf(args[2], args[3], args[4])
    elif function == "log_to_fdf":
        log_to_fdf(args[2], args[3], args[4])
    elif function == "xv_to_ani":
        if len(args) == 3:
            xv_to_ani(label=args[2])
        elif len(args) > 3:
            for arg in args[3:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
            xv_to_ani(label=args[2], path=path)
    elif function == "merge_ani":
        path = "i*"
        if len(args) == 3:
            merge_ani(label=args[2])
        elif len(args) > 3:
            for arg in args[3:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
            merge_ani(label=args[2], path=path)
    elif function == "energy_analysis":
        settings.set_log(args[2])
        plot_ = True
        path = "i*"
        if len(args) > 5:
            for arg in args[4:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
                if arg == "noplot":
                    plot_ = False
            energy_analysis(energytype=args[3], path=path, plot_=plot_)
        else:
            energy_analysis(energytype=args[3])
    elif function == "force_analysis":
        settings.set_log(args[2])
        plot_ = True
        path = "i*"
        if len(args) > 6:
            for arg in args[5:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
                if arg == "noplot":
                    plot_ = False
            force_analysis(atomindex=args[4], forcetype=args[3], path=path, plot_=plot_)
        else:
            force_analysis(atomindex=args[4], forcetype=args[3])
    elif function == "energy_diff":
        settings.set_log(args[2])
        path = "i*"
        if len(args) > 5:
            for arg in args[4:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
            energy_diff(energytype=args[3], path=path)
        else:
            energy_diff(energytype=args[3])
    elif function == "force_diff":
        settings.set_log(args[2])
        path = "i*"
        if len(args) > 6:
            for arg in args[5:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
            force_diff(atomindex=args[4], forcetype=args[3], path=path)
        else:
            force_diff(atomindex=args[4], forcetype=args[3])
    elif function == "pair_correlation_function":
        path = "i*"
        dr = 0.1
        plot_ = True
        if len(args) > 4:
            for arg in args[3:]:
                if arg.startswith("path="):
                    path = arg.split("=")[1]
                if arg.startswith("dr="):
                    dr = arg.split("=")[1]
                if arg == "noplot":
                    plot_ = False
            pair_correlation_function(label=args[2], path=path, dr=dr, plot_=plot_)
        else:
            pair_correlation_function(label=args[2])


def independents(arg):
    """Sets independent variables"""
    if arg.startswith("mpirun="):
        settings.set_cores(int(arg.split("=")[1]))
    if arg.startswith("conda="):
        settings.set_conda(arg.split("=")[1])
    if arg.startswith("cont="):
        settings.set_cont(arg.split("=")[1])
    if arg.startswith("contfrom="):
        settings.set_contfrom(arg.split("=")[1])
    if arg.startswith("contfiles="):
        settings.contfiles.extend(arg.split("=")[1].split(","))
    if arg.startswith("contextensions="):
        settings.contextensions.extend(arg.split("=")[1].split(","))
    if arg.startswith("siesta="):
        settings.set_siesta(arg.split("=")[1])


if __name__ == "__main__":
    main(args=sys.argv)
