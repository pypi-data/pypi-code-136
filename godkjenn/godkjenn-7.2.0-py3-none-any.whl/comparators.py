
def exact(accepted, received):
    "Exact byte-wise comparison."
    return accepted == received


def ignore_line_endings(accepted, received):
    "Exact byte-wise comparison, but ignoring line-ending differences."
    return exact(accepted.replace(b'\r\n', b'\n'), received.replace(b'\r\n', b'\n'))
