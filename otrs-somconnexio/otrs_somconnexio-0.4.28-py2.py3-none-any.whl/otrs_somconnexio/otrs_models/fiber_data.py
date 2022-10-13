from otrs_somconnexio.otrs_models.internet_data import InternetData


class FiberData(InternetData):
    service_type = 'fiber'

    def __init__(self, **args):
        self.previous_contract_pon = args.get("previous_contract_pon", "")
        self.previous_contract_fiber_speed = args.get("previous_contract_fiber_speed", "")
        self.activation_notes = args.get("activation_notes", "")
        for key in ["previous_contract_pon", "previous_contract_fiber_speed", "activation_notes"]:
            args.pop(key, None)
        super().__init__(**args)
