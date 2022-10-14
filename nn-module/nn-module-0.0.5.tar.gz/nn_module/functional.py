from typing import Callable, Optional

from nn_module import Module


class Functional(Module):
    """
    Functional: wrapper for function
    """

    def __init__(self, f: Callable, name: Optional[str] = None):
        super(Functional, self).__init__()
        self.f = f
        if name is None:
            self.name = f
        else:
            self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def forward(self, *args, **kwargs):
        return self.f(*args, **kwargs)
