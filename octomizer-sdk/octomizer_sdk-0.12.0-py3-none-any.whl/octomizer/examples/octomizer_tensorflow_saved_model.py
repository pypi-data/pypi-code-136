#!/usr/bin/env python3

"""
This is a simple example of use of the OctoML API. It creates a Project named My Project,
uploads a TensorFlow version of the MNIST model, benchmarks it on TensorFlow's runtime,
accelerates it, and returns both the accelerated model benchmark results and a Python
package for the optimized model.

After installing the OctoML SDK, run as:
  % export OCTOMIZER_API_TOKEN=<your API token>
  % ./octomizer_example.py

Windows-based users should set their API token as an environment
variable rather than use the export command, which is not supported
in some versions of Windows.

Typical output will look like this:

Uploading model tests/testdata/mnist.tgz...
Benchmarking using TensorFlow runtime...
TensorFlow runtime benchmark metrics:
latency_mean_ms: 0.1281123161315918
latency_std_ms: 0.3681384027004242

Waiting for OctoML to complete...
TVM benchmark metrics:
latency_mean_ms: 0.07081685215234756
latency_std_ms: 0.019525768235325813
compile_ms: 1084.7218017578125
full_metrics_dataref_uuid: "7df384b3-1d3d-4ef0-ae25-e57588090876"

Saved packaged model to ./mnist_accelerated-0.1.0-py3-none-any.whl
"""

from __future__ import annotations

import octomizer.client
import octomizer.models.tensorflow_saved_model as tf_model
import octomizer.project as project
from octomizer.model_variant import AutoschedulerOptions


def main():
    # Specify the model file and input layer parameters.
    tf_model_file = "tests/testdata/mnist.tgz"

    # Specify the Python package name for the resulting model.
    model_package_name = "mnist_accelerated"

    # Specify the platform to target.
    platform = "broadwell"

    # Create the OctoML Client instance.
    client = octomizer.client.OctomizerClient()

    # Create a Project named My Project.
    my_project = project.Project(
        client,
        name="My Project",
        description="Created by octomizer_tensorflow_saved_model.py",
    )

    # Upload the TensorFlow model file.
    # Note: TensorFlowSavedModel supports both TF SavedModels and
    # Keras SavedModel formats.
    print(f"Uploading model {tf_model_file}...")
    model = tf_model.TensorFlowSavedModel(
        client,
        name=model_package_name,
        model=tf_model_file,
        description="Created by octomizer_tensorflow_saved_model.py",
        project=my_project,
    )
    model_variant = model.get_uploaded_model_variant()

    # Benchmark the model and get results. MNIST is a small and simple model,
    # so this should return quickly.
    benchmark_workflow = model_variant.benchmark(platform)
    print("Benchmarking using TensorFlow runtime...")
    benchmark_workflow.wait()
    if not benchmark_workflow.completed():
        raise RuntimeError(
            f"Workflow did not complete, status is {benchmark_workflow.status()}"
        )
    metrics = benchmark_workflow.metrics()
    print(f"TensorFlow runtime benchmark metrics:\n{metrics}")

    # Accelerate the model. Since this is a small model and this is only an example,
    # we set the values in `tuning_options` ridiculously low so it does not take too long to
    # complete. Normally these values would be much higher (the defaults are 1000 and 250,
    # respectively).
    #
    # See the python API documentation for the full list of tuning options.
    accelerate_workflow = model_variant.accelerate(
        platform,
        tuning_options=AutoschedulerOptions(
            trials_per_kernel=3, early_stopping_threshold=1
        ),
    )
    print("Waiting for OctoML to complete...")
    accelerate_workflow.wait()
    if not accelerate_workflow.completed():
        raise RuntimeError(
            f"Workflow did not complete, status is {accelerate_workflow.status()}"
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
