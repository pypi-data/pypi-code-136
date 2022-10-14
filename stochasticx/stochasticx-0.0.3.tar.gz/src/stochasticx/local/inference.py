import sys
import tritonclient.grpc as grpcclient

class StochasticModel:
    """Class to make inferences in a Stochastic model deployed locally"""
    
    def __init__(self, model_name: str, server_url: str = "localhost:8001"):
        """Initilizer

        :param model_name: model name
        :param server_url: URL in which the server is listening, defaults to "localhost:8001"
        """
        self.model_name = model_name
        self.server_url = server_url
        
        try:
            self.triton_client = grpcclient.InferenceServerClient(
                url=server_url,
            )

        except Exception as e:
            print("Error: Model server is not running. Aborting execution..." + str(e))
            sys.exit()
            
        model_metadata = self.triton_client.get_model_metadata(
            model_name=self.model_name, 
            model_version="1"
        )
        self.outputs = []
            
        for outp in model_metadata.outputs:
            self.outputs.append(grpcclient.InferRequestedOutput(outp.name))
            
    def predict(self, **kwargs):
        """Do the inference

        :return: the predictions
        """
        inputs = []
        outputs = []
        for name, value in kwargs.items():
            input = grpcclient.InferInput(name, value.shape, "INT32")
            input.set_data_from_numpy(value)
            inputs.append(input)
            
        # Output
        results = self.triton_client.infer(
            model_name=self.model_name,
            inputs=inputs,
            outputs=self.outputs,
            client_timeout=None,
            compression_algorithm=None) 

        for output in self.outputs:
            outputs.append(results.as_numpy(output.name()))
        
        return outputs

    def __call__(self, **kwargs):
        """It is equivalent to the predict method.

        :return: the outputs of the model
        """
        return self.predict(**kwargs)