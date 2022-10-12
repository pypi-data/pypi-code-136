#!/usr/bin/env python3

"""
This is a simple example of use of the OctoML API. It creates a Project named
Project, uploads a TFLite model, benchmarks it on TVM, accelerates it, and
returns both the accelerated model benchmark results and a Python package for
the optimized model.

After installing the OctoML SDK, run as:
  % export OCTOMIZER_API_TOKEN=<your API token>
  % ./octomizer_example_tflite.py

Windows-based users should set their API token as an environment variable
rather than use the export command, which is not supported in some versions
of Windows.

Typical output will look like this:

Uploading model tests/testdata/mnist.tflite...
Benchmarking using TFLite Runtime
TFLite runtime benchmark metrics:
latency_mean_ms: 0.10985320061445236
latency_std_ms: 0.00474481750279665

Waiting for OctoML to complete...
TVM benchmark metrics:
latency_mean_ms: 0.0573916994035244
latency_std_ms: 0.007800986059010029

Saved packaged model to ./mnist_tflite_accelerated-0.1.0-py3-none-any.whl
"""

from __future__ import annotations

import octomizer.client
import octomizer.models.tflite_model as tflite_model
import octomizer.project as project
from octomizer.model_variant import AutoschedulerOptions


def main():
    # Specify the model file and input layer parameters.
    tflite_model_file = "tests/testdata/mnist.tflite"

    # Specify the Python package name for the resulting model.
    model_package_name = "mnist_tflite_accelerated"

    # Specify the platform to target.
    platform = "rasp4b"

    # Create the OctoML Client instance.
    client = octomizer.client.OctomizerClient()

    # Create a Project named My Project.
    my_project = project.Project(
        client,
        name="My Project",
        description="Created by octomizer_example_tflite.py",
    )

    # Upload the TFLite model file.
    print(f"Uploading model {tflite_model_file}...")
    model = tflite_model.TFLiteModel(
        client,
        name=model_package_name,
        model=tflite_model_file,
        description="Created by octomizer_example_tflite.py",
        project=my_project,
    )
    model_variant = model.get_uploaded_model_variant()

    # Benchmark the model and get results. MNIST is a small and simple model,
    # so this should return quickly. By default, TFLite models will be benchmarked
    # using TFLite runtime unless otherwise specified by using the `use_onnx_engine`
    # or `untuned_tvm` flags.
    benchmark_workflow = model_variant.benchmark(platform)
    print("Benchmarking using TFLite runtime")

    # To benchmark using ONNX-RT:
    # benchmark_workflow = model_variant.benchmark(platform, use_onnx_engine=True)

    # To benchmark using TVM (untuned):
    # benchmark_workflow = model_variant.benchmark(platform, untuned_tvm=True)

    benchmark_workflow.wait(timeout=1200)
    if not benchmark_workflow.completed():
        raise RuntimeError(
            f"Workflow has not completed, status is {benchmark_workflow.status()}"
        )
    metrics = benchmark_workflow.metrics()
    print(f"TFLite runtime benchmark metrics:\n{metrics}")

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
    )

    # Save the workflow uuid somewhere so you can use it later
    print(accelerate_workflow.uuid)

    # After you receive an email notification about the completion of the acceleration workflow,
    # you can view performance benchmark metrics on the hardware you chose and download a packaged
    # version of the accelerated model, either by invoking the following code or visiting the UI::

    # Look up the workflow you previously launched using the workflow uuid
    accelerate_workflow = client.get_workflow(accelerate_workflow.uuid)

    print("Waiting for OctoML to complete...")
    accelerate_workflow.wait()
    if not accelerate_workflow.completed():
        raise RuntimeError(
            f"Workflow has not completed, status is {accelerate_workflow.status()}"
        )
    metrics = accelerate_workflow.metrics()
    # Don't be surprised if the TVM numbers are slower than TensorFlow runtime -- we didn't
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
