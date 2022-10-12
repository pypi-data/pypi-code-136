# internal
from tier.cli.parser import parser
from tier.internal.git.git import Git
from tier.internal.logging import set_verbosity


def root():

    args = parser.parse_args()

    kwargs = vars(args)
    subcommand = kwargs.pop('subcommand')
    handler = kwargs.pop('handler')
    verbosity = kwargs.pop('verbose')
    dirty = kwargs.pop('dirty')
    _ = kwargs.pop('dry_run')

    if verbosity:
        set_verbosity(verbosity)

    dirty_ignore_list = ('deps', 'develop', 'version')
    if subcommand not in dirty_ignore_list and not dirty:
        git = Git()
        git.expect_clean()

    handler(**kwargs)
