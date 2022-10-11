import os

from conan.api.output import ConanOutput
from conan.cli.command import conan_command, COMMAND_GROUPS
from conan.cli.commands import make_abs_path
from conan.cli.commands.install import graph_compute, _get_conanfile_path
from conan.cli.common import _add_common_install_arguments, _help_build_policies, \
    get_multiple_remotes, add_lockfile_args, add_reference_args, save_lockfile_out
from conan.api.conan_app import ConanApp
from conans.client.conanfile.build import run_build_method


@conan_command(group=COMMAND_GROUPS['creator'])
def build(conan_api, parser, *args):
    """
    Install + calls the build() method
    """
    parser.add_argument("path", nargs="?",
                        help="Path to a folder containing a recipe (conanfile.py "
                             "or conanfile.txt) or to a recipe file. e.g., "
                             "./my_project/conanfile.txt.")
    add_reference_args(parser)
    parser.add_argument("-of", "--output-folder",
                        help='The root output folder for generated and build files')
    _add_common_install_arguments(parser, build_help=_help_build_policies.format("never"))
    add_lockfile_args(parser)
    args = parser.parse_args(*args)

    cwd = os.getcwd()
    path = _get_conanfile_path(args.path, cwd, py=True)
    folder = os.path.dirname(path)
    remote = get_multiple_remotes(conan_api, args.remote)

    deps_graph, lockfile = graph_compute(args, conan_api, partial=args.lockfile_partial)

    out = ConanOutput()
    out.title("Installing packages")
    conan_api.install.install_binaries(deps_graph=deps_graph, remotes=remote, update=args.update)

    source_folder = folder
    output_folder = make_abs_path(args.output_folder, cwd) if args.output_folder else None
    out.title("Finalizing install (deploy, generators)")
    conan_api.install.install_consumer(deps_graph=deps_graph, source_folder=source_folder,
                                       output_folder=output_folder)

    # TODO: Decide API to put this
    app = ConanApp(conan_api.cache_folder)
    conanfile = deps_graph.root.conanfile
    conanfile.folders.set_base_package(conanfile.folders.base_build)
    run_build_method(conanfile, app.hook_manager)

    save_lockfile_out(args, deps_graph, lockfile, cwd)
