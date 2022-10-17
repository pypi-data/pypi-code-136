from os import remove
from os.path import dirname

from warnings import warn

__all__ = [
    'audit_and_repair_wheel',
]

try:
    from auditwheel.patcher import Patchelf
    from auditwheel.policy import get_policy_by_name
    from auditwheel.repair import repair_wheel
    from auditwheel.wheel_abi import NonPlatformWheel, WheelAbIInfo, \
        analyze_wheel_abi


    def audit_and_repair_wheel(wheel_filepath: str) -> str:
        try:
            wheel_abi_info: WheelAbIInfo = analyze_wheel_abi(wheel_filepath)

        except NonPlatformWheel:
            warn(
                f'{wheel_filepath!r} does not look like a platform wheel.',
                UserWarning,
            )
            return wheel_filepath

        policy = get_policy_by_name(wheel_abi_info.sym_tag)
        filepath = repair_wheel(
            wheel_filepath,
            [policy['name'], *policy['aliases']],
            '.libs',
            dirname(wheel_filepath),
            True,
            patcher=Patchelf(),
        )
        remove(wheel_filepath)
        return filepath

except ImportError:

    def audit_and_repair_wheel(wheel_filepath: str) -> str:
        warn(
            'There is no auditwheel package installed. '
            'Thats why you can not audit and repair wheel.',
            UserWarning,
        )
        return wheel_filepath
