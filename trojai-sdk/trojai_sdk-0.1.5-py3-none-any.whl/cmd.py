from pathlib import Path
from trojsdk.config.base import BaseTrojConfig
from trojsdk.config.tabular import TabularTrojConfig
from trojsdk.core import client_utils
from trojsdk.core.data_utils import load_json_from_disk
from trojsdk.core.client_utils import TrojJobHandler


def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog="trojsdk", description="Troj sdk command line utils"
    )
    parser.add_argument(
        "-config", metavar="-c", type=str, help="Path to the config file"
    )
    parser.add_argument(
        "-test", action="store_true", help="Runs test with TrojAI supplied configs"
    )
    # parser.add_argument(
    #     "-endpoint", metavar="-e", type=str, help="Endpoint to post the config to"
    # )
    # parser.add_argument(
    #     "-jobstatus", metavar="-js", type=str, help="Get status of the specified job"
    # )
    args = parser.parse_args()
    config = None
    if args.test:
        docker_metadata = {
            "docker_image_url": "trojai/troj-engine-base-tabular:b4e7733771d798ce18b6421d009c11fb3a6b5eef",
            "docker_secret_name": "trojaicreds",
        }
        config = {
            "name": "small_classification_job_tabular",
            "task_type": "tabular",
            "subtask": "classification",
            "attacks": [
                {"attack_name": "NumberToString", "column_names": ["Temperature_log"]},
                {"attack_name": "FeatureToNan", "column_names": ["Temperature_log"]},
                {"attack_name": "FloatToInt", "column_names": ["Temperature_log"]},
                {"attack_name": "AbsurdValue", "column_names": ["Temperature_log"]},
                {"attack_name": "NewFeature", "column_names": ["N/A"]},
                {"attack_name": "MissingFeature", "column_names": ["Temperature_log"]},
                {"attack_name": "EmptyString", "column_names": ["Color"]},
                {
                    "attack_name": "UnseenCategory",
                    "column_names": ["Color"],
                    "attack_kwargs": {"unseen_value": "green"},
                },
                {
                    "attack_name": "AdditiveNoise",
                    "column_names": ["Temperature_log"],
                    "attack_kwargs": {"dev": 0.1},
                },
                {"attack_name": "ScaleShift", "column_names": ["Temperature_log"]},
            ],
            "dataset": {
                "name": "stars_validation",
                "path_to_data": "s3://trojai-test-file-storage/stars_validation.csv",
                "data_loader_config": {"batch_size": 3, "shuffle": False},
                "label_column": "Type",
                "classes_dictionary": {
                    "red dwarf": 0,
                    "brown dwarf": 1,
                    "white dwarf": 2,
                    "main sequence": 3,
                    "super giants": 4,
                    "hyper giants": 5,
                },
            },
            "model": {
                "name": "StarKNN",
                "path_to_model_file": "s3://trojai-test-file-storage/StarKNNWrapper.py",
                "model_args_dict": {
                    "model_file": "s3://trojai-test-file-storage/StarKNNPipe.pkl"
                },
            },
            "random_seed": 42,
            "auth_config": {
                "api_endpoint": "http://localhost/api/v1",
                "auth_keys": {
                    "id_token": "eyJraWQiOiI1dTQ5OGF1cXZDUWhyNWc3aGZCaDZpVzVya2J6UUF6N1MzdTlEaXFqXC91TT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzYjNhZDY0NS02ZDNiLTRkODItOTA1NC0yYWU1MGM1ODc0ZGEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmNhLWNlbnRyYWwtMS5hbWF6b25hd3MuY29tXC9jYS1jZW50cmFsLTFfakpMd0M4a1RJIiwiY29nbml0bzp1c2VybmFtZSI6InRyb2prOHMiLCJjdXN0b206Y3VzdG9tX3BsYW4iOiJmcmVlIiwiYXVkIjoiNDZjYTNxcWhoa29zMThrM2hqcW4xMGI0dWMiLCJldmVudF9pZCI6IjVkOWFhMmJkLWRiZDItNGNhYy04MTkxLTc4MmZiMDNiMmZlOCIsImN1c3RvbTpjdXN0b21fYXBpa2V5IjoiV2xhMkZERGJqTDFqVzNmaWpoejZJMXAyUlc0eFNwdkUxVmFiYTUwWCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjYzMjQ5MDI1LCJleHAiOjE2NjMyNTI2MjUsImlhdCI6MTY2MzI0OTAyNSwiZW1haWwiOiJzaGF3bi5tY2NhdWdoYW5AdHJvai5haSJ9.AdlFHKIkcaH26MOa2nuLhUMAIdq3kiCjkjSkJJpPkF5oU3gGUywN6Ut-fGntqT7YdLenrypLRJ02AygO3SLrQM6bZvIerVce1AYRSaLo3hVW2w7Ge1aqIWWwUKOS6UaUPBB5RtvBpxUY6LKPQdgIbSyU9HSdFNAUlqi_mpnu7SDSYjtfzE7ct5CS4-vW-EBwQiN6AFdEQXpX_-2Lf5Zgb99UQpaekzKQqc2qBPtwphZnMp5t7NbJoAENdu0gqfu-efEF2yJvfu-fhsaENpSn8czSw9HkM-mkGleUWZzDXgUXYgOuyMROnMFV8S1ygfQLij7sPV7pn_sNx9x2cCxtLw",
                    "refresh_token": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.kMRu8ANHvCeIjhgb7RDbCo2DQXq3RkNMX83fIDMptsLHAoYsQBAZHyn5wzNxyTouztOlwbYUkWXkPMX83WLuyYeSgtqwYvGommO3PnHtKRBSthHcCfuWWy4QSfayKGvWIbS1yQ58_FyVftYGEm6OCMLBR46joNbDosnocjM79SrvD-zUzOlwGipm-fFGDDiG88XfM7nzJaOFwF4W1p-6bwhqaw5xVwJ1tJj9W24F-6ENj14piXUBG4tR3jWrIAj5EL5PQY6IqeX_woDj-NMdk9A2LTZg3DhsMpGlXynV6ibEsVxow9k1zYvxP7L8kOmXaEyQ-sY4D4o3JLF_zK3lrA.TzIXyptDkaBI_Jv6.VnT25wU0GMKOf7mrnu1q9fWZ_rs8UN2LQVBazTpph-ILekeOOQKpCfaZbxlsTqpjk7RryaoB1eFz2YNyckWzQh_WyDYRd_B-Iba3If_DqHcVxqHH084K7F2xYG59LEadChGrIoRmT4isr6tc3KgwbH8qXoEge3Voc5IfGd7inCXvYn8iKdVMlJpGyo93OIigkLA2vwlaHhEI5lK6kTyXolSg8ZrSd5T4LQcj6DL6Ab1E5aNyklN6X8ql2zq55hEwloioZDTkoWmqoHBva4_vFS3di47AmWGButwBENYia2akFyKCuDxaKRsmDbiuAgKVfmHi5KJyh_agPh0qpMzWK9GI3dJgAIrgzE4ni3vCLiJGcIcayI4r1O9VnVAswBuJ-7IqsRRtqLHPpLbSu-T1pIiNMvoARatJDFHcy3kiZdhHHa9lBoYX7Uvjkszg4aY9dzx23kRt2NngEgTbpK9fIHqsJnG8Dksh3lluIVqiTaREQvR1xL6-PRO7D5YyveFAzNCMkdLaawvyVAqLaTalbAakrnW-9QAGiRdViRaMnwXCn1eYg9tgZY8Fkidfs0jkAtn40Elj3AvtG6LmWnk1dcfIkKhCsWDq-spyikUAs7W1u2WCZxaqYXXjTvUaOJVPMwmoU5fV5FecnfLU8YHQq-BvrmY4HvxrNxjD3ZkNmvF-KeKtb5pSw7mihfJ-DuerOGu1wQDcPIM3EieL-6PzrWkQjfQbu1VtjreVAnFrHOg4PkFNmUmzHh0z1WO_rL5iu364VHHk0T-CTAl3TNbLgRYSlwooCjGHeIDg8Xjwh-gjtr2K2fMdG8Rb1QzEZS3YYbtEslz2BjOS86l8n7pggBRYbx8ovK5mBh4LF_sGKsJkwWjZtHTJX-_goGavnJz6gI2GzCMkBPB1IOSVN-BcpK4uOlbu_ukl27QhMc9Mb7GPYOVMMgjrDA7OUPvHu2rAOxxQv0sKrOL9ElocEtcqTWJuUm-Wes8yxQKlG6GeA3HxzYyzA4qst4MmuhqmqdtdlFNd76S7kpIIaBUScj_XX6E_Djabu0YPdoSKsMCtRNYEG6GhPTOYfOzlNglGC8Gtoh69Ky_3cDMSoSK_YINrL6_mHyLSNE9K2ecYQaS1RQNt6b0dt46KWhHFTZcpoHXn4I6a45mc_Us7AUOOeG8BxlycS41kchbxwlei2iMieIEQ9dE1fT2MBQvo5BKgXRDDfqOpMhTnDMIojKy7NSfhnMnJxkf0G92mwKT8Aq7PBi5KTklkuBeK3DZyaYmye_PTF2cFln_sFVlzY2yrgA.LZcXV8fM-uknxBhJ_VLKYg",
                    "api_key": "Wla2FDDbjL1jW3fijhz6I1p2RW4xSpvE1Vaba50X",
                },
                "project_name": "SDKTESTPROJECT",
                "dataset_name": "SDKTESTDATASET_4",
                "secrets": {
                    "AWS_ACCESS_KEY_ID": "AKIAYHCWQVNI4O5RODCR",
                    "AWS_SECRET_ACCESS_KEY": "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",
                },
            },
        }
        client_utils.submit_evaluation(config, docker_metadata)
        print("Test finished")
        exit()

    if args.config is not None:
        client_utils.submit_evaluation(args.config)

    else:
        print("No config path supplied")
        print("Exiting")


if __name__ == "__main__":
    main()
