from collections.abc import Sequence


def _quote_string_if_needed(string):
    """Add enclosing quotation marks if string not already enclosed with
    quotation marks.

    Prefers single quote marks since that's what's used in URScript
    documentation.

    No smart parsing or tokenizing, only checks the start and end of string.
    """
    if string[0] in ('"', "'"):
        if string[-1] == string[0]:
            # already quoted
            return string

    return "'" + string + "'"


def _get_func(
    func_name: str, urscript_args: str = None, urscript_kwargs: str = None
) -> str:
    # if both args and kwargs, join with ", "
    if urscript_args and urscript_kwargs:
        args = ", ".join([urscript_args, urscript_kwargs])
    else:
        # either or both args and kwargs are none
        args = urscript_args or ""  # add args if args
        args += urscript_kwargs or ""  # add kwargs if kwargs

    return f"{func_name}({args})"


def _get_pose(x: float, y: float, z: float, ax: float, ay: float, az: float) -> str:
    return f"p[{x:.5f}, {y:.5f}, {z:.5f}, {ax:.5f}, {ay:.5f}, {az:.5f}]"


def _get_conf(joint_conf: Sequence[float]) -> str:
    if len(joint_conf) != 6:
        raise RuntimeError("Wrong amount of joint positions, should be 6.")

    j1, j2, j3, j4, j5, j6 = joint_conf

    return f"[{j1:.5f}, {j2:.5f}, {j3:.5f}, {j4:.5f}, {j5:.5f}, {j6:.5f}]"


def _get_move_kwargs(**kwargs) -> str:
    ok_keywords = ("v", "a", "t", "r")

    urscript_kwargs = []

    for key in kwargs:
        if key in ok_keywords:
            if kwargs[key]:
                urscript_kwargs.append(f"{key}={kwargs[key]:.5f}")
        else:
            raise RuntimeError(f"Keyword name {key} not recognized.")

    if len(urscript_kwargs) == 0:
        return ""
    else:
        return ", ".join(urscript_kwargs)


class Motion(object):
    LINEAR = 0
    JOINT = 1


def set_tcp(x: float, y: float, z: float, rx: float, ry: float, rz: float) -> str:
    """Create a set TCP function call

    Arguments
    ---------
    x
        X coordinate (m)
    y
        Y coordinate (m)
    z
        Z coordinate (m)
    rx
        X component of axis angle vector
    ry
        X component of axis angle vector
    rz
        X component of axis angle vector

    Returns
    -------
    str
        URScript function call
    """
    return _get_func("set_tcp", _get_pose(x, y, z, rx, ry, rz))


def move_to_pose(
    x: float,
    y: float,
    z: float,
    rx: float,
    ry: float,
    rz: float,
    mode=Motion.JOINT,
    v: float = None,
    a: float = None,
    t: float = None,
    r: float = None,
) -> str:
    """Create a move to pose function call

    Arguments
    ---------
    x
        X coordinate (m)
    y
        Y coordinate (m)
    z
        Z coordinate (m)
    rx
        X component of axis angle vector
    ry
        X component of axis angle vector
    rz
        X component of axis angle vector
    mode
        Motion.LINEAR or Motion.JOINT. Defaults to Motion.JOINT
    a
        Tool acceleration (m/s²)
    v
        tool speed (m/s)
    t
        time (s)
    r
        blend radius (m)

    Returns
    -------
    str
        URScript function call

    """
    func_name = "movel" if mode == Motion.LINEAR else "movej"

    pose = _get_pose(x, y, z, rx, ry, rz)
    move_kwargs = _get_move_kwargs(v=v, a=a, t=t, r=r)

    return _get_func(func_name, pose, move_kwargs)


def move_to_conf(
    joint_conf: Sequence[float],
    v: float = None,
    a: float = None,
    t: float = None,
    r: float = None,
) -> str:
    """Create a move to configuration function call

    Arguments
    ---------
    joint_conf
        A list of joint positions (rad)
    a
        Joint acceleration of leading axis (rad/s²)
    v
        Joint speed of leading axis (rad/s)
    t
        time (s)
    r
        blend radius (m)

    Returns
    -------
    str
        URScript function call
    """
    conf = _get_conf(joint_conf)
    move_kwargs = _get_move_kwargs(v=v, a=a, t=t, r=r)

    return _get_func("movej", conf, move_kwargs)


def text_msg(string: str) -> str:
    """Create a log function call

    Arguments
    ---------
    string
        Message to print in log

    Returns
    -------
    str
        URScript function call
    """
    return f'textmsg("{string}")'


def popup(string: str) -> str:
    """Construct a function call that opens a popup on the teach pendant.

    Arguments
    ---------
    string
        Message to print

    Notes
    -----
    Popup arguments title, error & warning is not implemented in URScript.
    """
    return f'popup("{string}")'


def set_DO(pin: int, state: bool) -> str:
    """Construct a function call that sets the state of a digital out.

    Arguments
    ---------
    pin
        Pin number
    state
        True or False

    Returns
    -------
    str
        URScript function call
    """
    # bool(state) should convert numeric representation to boolean value and
    # then into True or False as string.
    return _get_func("set_digital_out", f"{pin:d}, {bool(state)}")


def read_DO(pin: int) -> bool:
    raise NotImplementedError()


def set_AO(pin: int, value: float) -> str:
    raise NotImplementedError()


def read_AO(pin: int) -> float:
    raise NotImplementedError()


def sleep(seconds: int) -> str:
    """Construct a function call that instructs the controller to sleep."""
    return _get_func("sleep", str(seconds))


def socket_open(address: str, port: int, socket_name=None):
    urscript_kwargs = (
        f"socket_name={_quote_string_if_needed(socket_name)}" if socket_name else None
    )
    return _get_func(
        "socket_open",
        urscript_args=f"{_quote_string_if_needed(address)}, {port}",
        urscript_kwargs=urscript_kwargs,
    )


def socket_close(socket_name=None):
    urscript_kwargs = (
        f"socket_name={_quote_string_if_needed(socket_name)}" if socket_name else None
    )
    return _get_func(
        "socket_close",
        urscript_kwargs=urscript_kwargs,
    )


def socket_send_string(string_or_var_name: str, socket_name=None):
    urscript_kwargs = (
        f"socket_name={_quote_string_if_needed(socket_name)}" if socket_name else None
    )
    return _get_func(
        "socket_send_string",
        urscript_args=string_or_var_name,
        urscript_kwargs=urscript_kwargs,
    )
