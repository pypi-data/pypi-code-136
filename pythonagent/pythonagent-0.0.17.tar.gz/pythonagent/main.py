""""
Local Testing for Python Agent on AWS Lambda
"""

import sys
import os

python_agent_parent_dir = os.path.abspath(os.path.join(__file__, "../.."))
sys.path.append(python_agent_parent_dir)

from pythonagent.bootstrap.cavagent_lambda_wrapper import handler


if __name__ == "__main__":

    event = {"path": "test_local_application"}

    class Context:
        def __init__(self):
            self.log_stream_name = "test_request_id_localapp"
            self.aws_request_id = "test_request_id_localapp"
            self.function_name = "test_function_localapp"

    context = Context()

    response = handler(event, context)

