def register_new_environment(self, system_name: str, environment_url: str):
    return PegaEnvironment(self, system_name=system_name, environment_url=environment_url)