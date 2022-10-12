#!/usr/bin/env python3

"""
This is a simple example of use of the OctoML API. It creates a Project named My Project,
uploads two ONNX models, and adds them to the Project, and finally lists all Models
belonging to the Project.

After installing the OctoML SDK, run as:
  % export OCTOMIZER_API_TOKEN=<your API token>
  % ./octomizer_project_example.py

Windows-based users should set their API token as an environment
variable rather than use the export command, which is not supported
in some versions of Windows.
"""

from __future__ import annotations

import octomizer.client
import octomizer.models.onnx_model as onnx_model
import octomizer.project as project


def __main__():
    # Specify the model files.
    onnx_model_files = [
        ("tests/testdata/mnist.onnx", "mnist"),
        ("tests/testdata/mobilenet.onnx", "mobilenet"),
    ]

    # Create the OctoML Client instance.
    client = octomizer.client.OctomizerClient()

    # Create a Project named My Project.
    my_project = project.Project(
        client,
        name="My Project",
        description="Created by octomizer_project_example.py",
    )

    # Upload the ONNX model files.
    for onnx_model_file, model_package_name in onnx_model_files:
        print(f"Uploading model {onnx_model_file}...")
        _ = onnx_model.ONNXModel(
            client,
            name=model_package_name,
            model=onnx_model_file,
            description="Created by octomizer_project_example.py",
            project=my_project,
        )

    # List all the Models belonging to the Project, which should be the two uploaded above.
    project_models = my_project.list_models()

    # Print all the Models belonging to the Project.
    print(
        f"Models belonging to the Project: {list(model.uuid for model in project_models)}"
    )

    # It is possible to create detached Models. Simply ignore the project parameter or pass
    # None as an argument.
    detached_model = onnx_model.ONNXModel(
        client,
        name=model_package_name,
        model=onnx_model_file,
        description="Created by octomizer_project_example.py",
    )
    assert detached_model.project is None


if __name__ == "__main__":
    __main__()
