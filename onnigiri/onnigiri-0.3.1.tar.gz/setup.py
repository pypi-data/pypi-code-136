# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onnigiri']

package_data = \
{'': ['*']}

install_requires = \
['onnx-simplifier>=0.4,<0.5', 'onnx>=1.9.0,<2.0.0', 'onnxruntime>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['onnigiri = onnigiri.main:main']}

setup_kwargs = {
    'name': 'onnigiri',
    'version': '0.3.1',
    'description': 'onnx-divider',
    'long_description': "# onnigiri\nonnx-divider\n\nThe purpose of this package is to create subgraphs by partitioning computational graphs in order to facilitate the development of applications.\n\nOne of the problems in developing applications using deep learning models is that the DL model is not applicable by itself.\nFor example, they may be have unnecessary nodes and some nodes are not supported some DL tools.\nThis tool enable us to edit an onnx model freely and easily.\n\n## Installation\nFrom [PyPI](https://pypi.org/project/onnigiri/):\n\n```\n$ pip3 install onnigiri\n```\n\nFrom [Dockerhub](https://hub.docker.com/repository/docker/idein/onnigiri)\n\n```\n$ docker pull idein/onnigiri:YYYYMMDD # YYYYMMDD is released date.\nor\n$ docker pull idein/onnigiri:latest\n```\n\n\n## Usage\n[SSD](https://github.com/onnx/models/tree/main/vision/object_detection_segmentation/ssd)\n\n```\n$ onnigiri ssd-10.onnx -o ssd-10-main.onnx --from image --to Transpose_472 Transpose_661\n$ onnigiri ssd-10.onnx -o ssd-10-post.onnx --from Transpose_472 Transpose_661 --to bboxes labels scores\n```\n\nWith docker:\n\n```\n$ docker run --rm -it -u $UID:$GID -v $(pwd):/work idein/onnigiri:latest ssd-10.onnx -o ssd-10-main.onnx --from image --to Transpose_472 Transpose_661\n$ docker run --rm -it -u $UID:$GID -v $(pwd):/work idein/onnigiri:latest ssd-10.onnx -o ssd-10-post.onnx  --from Transpose_472 Transpose_661 --to bboxes labels scores\n```\n\n[UltraFace](https://github.com/onnx/models/tree/main/vision/body_analysis/ultraface)\n\n```\n$ onnigiri version-RFB-640.onnx -o version-RFB-640-main.onnx --from input --to 460 scores\n$ onnigiri version-RFB-640.onnx -o version-RFB-640-post.onnx --from 460 --to boxes\n```\n\n[tiny-yolov3](https://github.com/onnx/models/tree/main/vision/object_detection_segmentation/tiny-yolov3)\n\n```\n$ onnigiri tiny-yolov3-11.onnx --fix-input-shape 'input_1' '1,3,256,256' 'image_shape' '1,2' -o tiny-yolov3-11-main.onnx --from input_1 --to 'TFNodes/yolo_evaluation_layer_1/Reshape_3:0' 'model_1/leaky_re_lu_10/LeakyRelu:0' 'model_1/leaky_re_lu_5/LeakyRelu:0'\n$ onnigiri tiny-yolov3-11.onnx --fix-input-shape 'input_1' '1,3,256,256' 'image_shape' '1,2' -o tiny-yolov3-11-post.onnx --from image_shape 'TFNodes/yolo_evaluation_layer_1/Reshape_3:0' 'model_1/leaky_re_lu_10/LeakyRelu:0' 'model_1/leaky_re_lu_5/LeakyRelu:0' --to 'yolonms_layer_1' 'yolonms_layer_1:1' 'yolonms_layer_1:2'\n```\n\n## Q&A\n\n- How to get the name of values?\n\nUse [Netron](https://netron.app).\n\n- Why is the extracted subgraph different from the original subgraph?\n\nonnigiri apply [onnx-simplifier](https://github.com/daquexian/onnx-simplifier) before extraction.\n\n## Development Guide\n\n```\n$ poetry install\n```\n\n### Build docker image\n\n```\n$ nix build '.#dockerimage' -o image\n$ docker load < ./image\n```\n\n## Related project\n\n- [onnion](https://github.com/Idein/onnion)\n",
    'author': 'Idein Inc.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Idein/onnigiri',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
