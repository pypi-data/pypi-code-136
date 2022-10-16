try:
    import starlette

    from .application import FastAPIApplication
    from .model import ApiModelMixin
    from .permissions import HttpPermission, PermDepends, Authenticated, Admin

except ImportError:
    pass
