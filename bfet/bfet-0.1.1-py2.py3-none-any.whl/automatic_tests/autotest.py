from .create_tests import CreateTests


class Autotest(CreateTests):
    @classmethod
    def start(cls, folder_path: str = "", app: str = ""):
        cls().create_test_file(
            cls().inspect_folder_for_tests(**{"folder_path": folder_path, "app": app})
        )
