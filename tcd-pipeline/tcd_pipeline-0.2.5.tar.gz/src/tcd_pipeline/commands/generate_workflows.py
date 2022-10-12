"""
Command generate-workflow
"""
import json
import sys

import click
import yaml
from tcd_pipeline import pipeline as pipeline_tool


@click.command(help="Generate workflows from pipelines")
@click.option("--pipelines",
  default=".",
  type=click.Path(),
  show_default=True,
  help="Path to pipeline file or directory contains *-pipelines.yaml"
  )
@click.option("--git-ref-type",
  help="Git ref type",
  type=click.Choice(["branch", "tag"])
  )
@click.option("--git-ref-name",
  help="Branch name or Tag name"
  )
@click.option("--change",
  help='Changed file(s). Example Dockerfile  or JSON format ["Dockerfile","README.md"]',
  multiple=True,
  default=[list]
  )
@click.option("--output",
  help="Output workflows file. [Default: stdout]",
  type=click.Path()
  )
def generate_workflows(pipelines: str,
                      git_ref_type: str,
                      git_ref_name: str,
                      change: list[str],
                      output: str):
    """Generate workflows from pipelines"""
    if output == "" or output == "stdout":
        output = None

    fact: dict = yaml.safe_load(f"""
      refType: {git_ref_type}
      refName: {git_ref_name}
      changes: []
    """)

    # Add change to fact
    for file in change:
        if file.__contains__("["):
            # for item_file in re.sub(r"[\[\]]", "", file).split(","):
            #     fact.get("changes").append(item_file)
            try:
                file_list: list[str] = json.loads(file)
                for item in file_list:
                    fact.get("changes").append(item)
            except json.decoder.JSONDecodeError:
                pass
        else:
            fact.get("changes").append(file)

    try:
        pipeline_tool.generate_workflows(
          pipeline_path=pipelines,
          event=fact,
          output=output
        )
    except Exception as err:
        print(err)
        sys.exit(1)
