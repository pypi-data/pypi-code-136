from enum import unique, Enum


@unique
class DeploymentAction(str, Enum):
    create = "CREATE"
    destroy = "DESTROY"
    none = "NONE"
    reconcile = "RECONCILE"


@unique
class DeploymentStatus(str, Enum):
    check = "CHECK"
    create = "CREATE"
    created = "CREATED"
    destroy = "DESTROY"
    destroyed = "DESTROYED"
    error = "ERROR"
    initialize = "INITIALIZE"
    none = "NONE"
    reconcile = "RECONCILE"
    reconciled = "RECONCILED"
    validate = "VALIDATE"


@unique
class Visibility(str, Enum):
    community = "COMMUNITY"
    private = "PRIVATE"
    public = "PUBLIC"
    shared = "SHARED"
