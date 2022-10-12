#!/usr/bin/env python3

"""
This is a simple example of use of the OctoML API. It creates a Project named My Project,
uploads an ONNX version of the mobilenet model, benchmarks it on ONNX-RT, accelerates it,
and returns both the accelerated model benchmark results and a Python package for the
optimized model.

After installing the OctoML SDK, run as:
  % export OCTOMIZER_API_TOKEN=<your API token>
  % ./octomizer_example.py

Windows-based users should set their API token as an environment variable rather than use the
export command, which is not supported in some versions of Windows.

Typical output will look like this:

Uploading model tests/testdata/mobilenet.onnx...
Benchmarking using ONNX-RT...
ONNX-RT benchmark metrics:
latency_mean_ms: 0.1281123161315918
latency_std_ms: 0.3681384027004242

Waiting for OctoML to complete...
TVM benchmark metrics:
latency_mean_ms: 0.07081685215234756
latency_std_ms: 0.019525768235325813
compile_ms: 1084.7218017578125
full_metrics_dataref_uuid: "7df384b3-1d3d-4ef0-ae25-e57588090876"

Saved packaged model to ./mobilenet_accelerated-0.1.0-py3-none-any.whl
"""

from __future__ import annotations

import octomizer.client
import octomizer.models.onnx_model as onnx_model
import octomizer.project as project
from octomizer.model_variant import AutoschedulerOptions


def main():
    # Specify the model file and input layer parameters.
    onnx_model_file = "tests/testdata/mobilenet.onnx"

    # Specify the Python package name for the resulting model.
    model_package_name = "mobilenet_accelerated"

    # Specify the platform to target.
    platform = "broadwell"

    # Create the OctoML Client instance.
    client = octomizer.client.OctomizerClient()

    # Create a Project named My Project.
    my_project = project.Project(
        client,
        name="My Project",
        description="Created by octomizer_dynamic_example.py",
    )

    # Upload the ONNX model file.
    print(f"Uploading model {onnx_model_file}...")
    model = onnx_model.ONNXModel(
        client,
        name=model_package_name,
        model=onnx_model_file,
        description="Created by octomizer_dynamic_example.py",
        project=my_project,
    )
    model_variant = model.get_uploaded_model_variant()

    # Inputs are not fully inferrable
    inferred_input_shapes, inferred_input_dtypes = model_variant.inputs
    assert inferred_input_shapes == {"input:0": [-1, 3, 224, 224]}
    assert inferred_input_dtypes == {"input:0": "float32"}

    # Disambiguate the inputs. Notice the -1 has been replaced by 1.
    input_shapes = {"input:0": [1, 3, 224, 224]}
    input_dtypes = {"input:0": "float32"}

    # Benchmark the model and get results. Mobilenet is a small and simple model,
    # so this should return quickly.
    benchmark_workflow = model_variant.benchmark(
        platform=platform,
        input_shapes=input_shapes,
        input_dtypes=input_dtypes,
        create_package=False,
    )
    print("Benchmarking using ONNX-RT...")
    benchmark_workflow.wait()
    if not benchmark_workflow.completed():
        raise RuntimeError(
            f"Workflow has not completed, status is {benchmark_workflow.status()}"
        )
    metrics = benchmark_workflow.metrics()
    print(f"ONNX-RT benchmark metrics:\n{metrics}")

    # Accelerate the model. Since this is a small model and this is only an example,
    # we set the values in `tuning_options` ridiculously low so it does not take too long to
    # complete. Normally these values would be much higher (the defaults are 1000 and 250,
    # respectively).
    #
    # See the python API documentation for the full list of tuning and packaging options.
    accelerate_workflow = model_variant.accelerate(
        platform,
        tuning_options=AutoschedulerOptions(
            trials_per_kernel=3, early_stopping_threshold=1
        ),
        input_shapes=input_shapes,
        input_dtypes=input_dtypes,
    )

    # Save the workflow uuid somewhere so you can use it later
    print(accelerate_workflow.uuid)

    # After you receive an email notification about the completion of the acceleration workflow,
    # you can view performance benchmark metrics on the hardware you chose and download a packaged
    # version of the accelerated model, either by invoking the following code or visiting the UI::

    # Look up the workflow you previously launched using the workflow uuid
    accelerate_workflow = client.get_workflow("<INSERT WORKFLOW ID>")

    if not accelerate_workflow.completed():
        raise RuntimeError(
            f"Workflow has not completed, status is {accelerate_workflow.status()}"
        )
    metrics = accelerate_workflow.metrics()

    # Don't be surprised if the TVM numbers are slower than ONNX-RT -- we didn't
    # run enough rounds of autotuning to ensure great performance!
    print(f"TVM benchmark metrics:\n{metrics}")

    # Download the package for the optimized model.
    # If you want to save a specific type of package type (default is Python) you can add
    # package_type=octomizer.package_type.PackageType.PYTHON_PACKAGE or LINUX_SHARED_OBJECT.
    # Note that not all package types may be available for a given engine.
    output_filename = accelerate_workflow.save_package(out_dir=".")
    print(f"Saved packaged model to {output_filename}")


if __name__ == "__main__":
    main()
