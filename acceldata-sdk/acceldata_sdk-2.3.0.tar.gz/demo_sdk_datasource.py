
from torch_client import TorchClient

torch_client = TorchClient(url="https://torch.acceldata.local:5443/torch",
                           access_key="P04IM8FNQRUCRTU", secret_key="E6LL9YUPMG4BDTJHT2VZD75HW0B8E5")

datasource_id = 2
import pdb;pdb.set_trace()
datasource_details = torch_client.get_datasource_by_id(datasource_id)
print(datasource_details)
