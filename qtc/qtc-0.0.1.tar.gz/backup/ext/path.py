import platform
import typing as T
import re


SHARED_DRIVES = {'BAM_DIR':  {'Windows': r'\\fountainhead\bam', 'Linux': '/bam'},
                 'RISK_DIR': {'Windows': r'\\fountainhead\risk', 'Linux': '/mnt/rsk'},
                 'SYSEQUITY_DIR': {'Windows': r'\\aws-prod-nas\team_sysequity', 'Linux': '/bam/aws/prod/team_sysequity'}}


def _infer_path(*parts: str,
                base_dir_type,
                platform_system: T.Optional[str] = None) -> str:
    base_dir_type = base_dir_type.upper()
    if base_dir_type not in SHARED_DRIVES:
        raise Exception(f"base_dir_type={base_dir_type} is not supported in [{'|'.join(list(SHARED_DRIVES.keys()))}]")

    if platform_system is None:
        platform_system = platform.system()
    base_dir = SHARED_DRIVES[base_dir_type][platform_system]
    sep = '\\' if platform_system == 'Windows' else '/'

    return sep.join([base_dir] + list(parts))


# def check_shared_drives():
#     """
#     >>> from bamrisk_common.ext.path import check_shared_drives
#     >>> check_shared_drives()
#     """
#
#     [f"{y}: {x // (2 ** 30)} GiB" for x, y in zip(shutil.disk_usage('/'), shutil.disk_usage('/')._fields)]
#
#     return SHARED_DRIVES
# #


def bam_dir(*parts: str,
            platform_system: T.Optional[str] = None) -> str:
    """
    Builds a path/filename on the "BAM_DIR" network drive.
    In Windows world, this is known as `\\fountainhead\bam`.
    In Linux world, this is known as `/bam`.

    :param parts: A list of subdirectories, e.g. `B:\\DataApi` would be `bam_dir('DataApi')` .
    :param platform_system: If not set, a system (Windows or Linux) will be inferred automatically.
    :return: The path/filename

    >>> from qtc.ext.path import bam_dir
    >>> bam_dir(platform_system='Windows')
    '\\fountainhead\bam'
    >>> bam_dir(platform_system='Linux')
    '/bam'
    >>> bam_dir('DataApi', 'config_shared', platform_system='Windows')
    '\\fountainhead\bam\DataApi\config_shared'
    >>> bam_dir('DataApi', 'config_shared', platform_system='Linux')
    '/bam/DataApi/config_shared'
    """
    return _infer_path(*parts,
                       base_dir_type='BAM_DIR', platform_system=platform_system)


def sysequity_dir(*parts: str,
                  platform_system: T.Optional[str] = None) -> str:
    """
    Builds a path/filename on the "SYSEQUITY_DIR" network drive.
    In Windows world, this is known as `\\aws-prod-nas\team_sysequity`.
    In Linux world, this is known as `/bam/aws/prod/team_sysequity`.

    :param parts: A list of subdirectories, e.g. `S:\\data` would be `sysequity_dir('data')` .
    :param platform_system: If not set, a system (Windows or Linux) will be inferred automatically.
    :return: The path/filename

    >>> from qtc.ext.path import sysequity_dir
    >>> sysequity_dir(force_platform_system='Windows')
    '\\\\aws-prod-nas\\team_sysequity'
    >>> sysequity_dir(force_platform_system='Linux')
    '/bam/aws/prod/team_sysequity'
    """
    return _infer_path(*parts,
                       base_dir_type='SYSEQUITY_DIR', platform_system=platform_system)


def risk_dir(*parts: str,
             platform_system: T.Optional[str] = None) -> str:
    """
    Builds a path/filename on the shared risk network drive.
    In Windows world, this is known as R: or `\\fountainhead\risk`.
    In the Linux world, this is known as `/mnt/rsk`.

    The parts argument is a list of subdirectories. For instance, `R:\Risk\RiskReports\Equity` would be `risk_dir('Risk', 'RiskReports', 'Equity')`

    force_platform_system is used to force a system (Windows or Linux) instead of autodetecting.
    This is mainly only useful for unit testing and can normally be omitted.

    >>> risk_dir(force_platform_system='Windows')
    '\\\\fountainhead\\risk'
    >>> risk_dir(force_platform_system='Linux')
    '/mnt/rsk'
    >>> risk_dir('Risk', 'RiskReports', 'Equity', force_platform_system='Windows')
    '\\\\fountainhead\\risk\\Risk\\RiskReports\\Equity'
    >>> risk_dir('Risk', 'RiskReports', 'Equity', force_platform_system='Linux')
    '/mnt/rsk/Risk/RiskReports/Equity'
    """
    return _infer_path(*parts, base_dir_type='RISK_DIR', platform_system=platform_system)


def eval_shared_folder(folder):
    if isinstance(folder, str):
        if re.match('bam_dir(.*)', folder) or \
           re.match('sysequity_dir(.*)', folder):
            return eval(folder)

    return folder
