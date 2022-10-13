# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['capture', 'cuwb_stream', 'cuwb_stream.tools']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'cachetools>=5.2.0,<6.0.0',
 'click>=8.1.3,<9.0.0',
 'ffmpeg-python>=0.2.0,<0.3.0',
 'jmespath>=1.0.1,<2.0.0',
 'minio>=7.1.12,<8.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'watchdog>=2.1.9,<3.0.0']

entry_points = \
{'console_scripts': ['wf_capture_tools = capture.cli:main']}

setup_kwargs = {
    'name': 'wf-camera-capture',
    'version': '1.0.3',
    'description': 'Capture code for rapspi cameras',
    'long_description': "# Camera-node\n\nAll software needed for a camera node in an environment. Includes pieces for both capture and delivery as well as proxy node that handles centralized processing of video, upload, and queuing in case of slow or down connectivity.\n\n## Proxy\n\nFlask service that receives data from all other camera nodes and feeds and internal queue and that sends data to honeycomb and optionally processes videos to pull out frames that are also sent to honeycomb.\n\n## Capture\n\nService that runs on nodes that have cameras. Captures video clips in short segments and sends them to their internal queue where workers send the to the proxy.\n\n## Workers\n\nCelery service that performs tasks from the internal queue. Capture work is processed and sent to the proxy, unless it is a the proxy-node in which case it forwards the work to another task. Video segments are processes and sent to honeycomb. Processing includes tagging etc. Once uploaded the next set of processing happens, key frames are extracted at those are sent to honeycomb as child datapoint objects of the video.\n\nIf running on more capable hardware the keyframes could be evaluated for things like pose detection or object tracking. This is not planned yet but isn't out of scope specifically.\n\n## Radio-Monitor\n\nA python service that connects to a network of DWM1001 modules over BLE to collect data. That data is queued to be sent to honeycomb. It is expected that this service runs on the proxy node.\n\n## CUWB-Stream\n\nLeverages fluentd to move Ciholas sensor data to S3\n\nBefore deploying the service, update the Ciholas network config as follows:\n\n|        | IP                | Port   | Interface |\n|--------|-------------------|--------|-----------|\n| Config | 239.255.76.67     | 7671   | 0.0.0.0   |\n| Input  | 239.255.76.67     | 7667   | 0.0.0.0   |\n| Output | 0.0.0.0           | 32222  | 0.0.0.0   |\n\nPS: In order to resolve an issue with the anchors disconnecting and not reconnecting, you may need to set the interface IPs of the Config and Input rows to the ethernet device's IP (Use `ifconfig`) \n\n### Build and push service\n\n```\nmake build-cuwb-stream\n```\n\n### Deploy streaming service to k8\n\n```\n# Install envsubtr, on MacOS install through the gettext pkg\nbrew install gettext\nbrew link --force gettext \n\n# Create a config and secrets file with S3 and AWS ENV keys\nkubectl apply -f ./k8s/kube-logging.yml\nkubectl apply -f ./private/aws-s3-write-auth-config.yml\nkubectl apply -f ./private/aws-s3-write-auth-secret.yml\nkubectl apply -f ./k8s/fluentd.yml\nkubectl apply -f ./k8s/fluentd-s3-config.yml\nkubectl apply -f ./k8s/fluentd-s3.yml\n\nTIMEZONE=US/Pacific envsubst < ./k8s/fluentd-s3-scheduler.yml | kubectl apply -f -\n\nkubectl apply -f ./k8s/cuwb-service.yml \n```\n\n## Setup cluster with Docker Hub robot\n\nFirst login and then copy creds into the cluster:\n\n    docker login\n    # Provide username and PAT (personal access token)\n\n    kubectl create secret generic regcred --from-file=.dockerconfigjson=/home/wildflowertech/.docker/config.json --type=kubernetes.io/dockerconfigjson\n",
    'author': 'Paul J DeCoursey',
    'author_email': 'paul@decoursey.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
