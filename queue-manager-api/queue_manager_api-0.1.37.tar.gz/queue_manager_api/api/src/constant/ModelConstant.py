try:
    from enumeration.ModelStatus import ModelStatus
    from enumeration.ModelState import ModelState
except:
    from queue_manager_api.api.src.enumeration import ModelState
    from queue_manager_api.api.src.enumeration import ModelStatus


DEFAULT_STATUS = ModelStatus.NOT_INFORMED
DEFAULT_STATE = ModelState.NOT_INFORMED
