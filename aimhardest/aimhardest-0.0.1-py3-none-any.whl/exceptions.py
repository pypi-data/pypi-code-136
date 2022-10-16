class AimHardestError(Exception):
    pass


class SignInError(AimHardestError):
    def __init__(self) -> None:
        super().__init__("Wrong mail and/or password")


class CannotBookClass(AimHardestError):
    def __init__(self) -> None:
        super().__init__("Cannot book class")


class NoCreditAvailable(CannotBookClass):
    def __init__(self) -> None:
        super().__init__("User has no credits available")


class NoMoreOfTheSameClass(CannotBookClass):
    def __init__(self, max) -> None:
        super().__init__(f"Cannot book more than {max} of the same class")


class ProbablyInWaitList(CannotBookClass):
    def __init__(self) -> None:
        super().__init__("User has no credits available")
