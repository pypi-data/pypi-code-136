from pathlib import Path
from src.axa_fr_ml_cli.run import run_ml_cli_pipeline
import argparse

BASE_PATH = Path(__file__).resolve().parent


def main():
    # Arguments for CI (Continuous Integration)
    parser = argparse.ArgumentParser("register")
    parser.add_argument(
        "--skip_train_execution",
        action="store_true",
        help=(
            "Do not trigger the execution. "
            "Use this in Azure DevOps when using a server job to trigger"
        ),
    )
    parser.add_argument("--build_id", type=str, default="", help="build id")
    parser.add_argument("--build_tags", type=str, default="", help="add tags")
    parser.add_argument(
        "--config_aml_path",
        type=str,
        default=str(BASE_PATH / "aml" / "config_aml_AFA_PRD_02_ML_CNI.json"),
        help="configuration azure ml path",
    )

    args = parser.parse_args()
    CONFIG_PATH = BASE_PATH / "aml/config_env.json"
    MLCLI_TEMPLATE_PATH = BASE_PATH / "aml/ml-cli.template"
    run_ml_cli_pipeline(args, CONFIG_PATH, MLCLI_TEMPLATE_PATH)

if __name__ == "__main__":
    main()
