
import torch

def access_output_params(net):
    return list(net.parameters())[-1].data


def init_output_params(net, init_val) -> None:
    """Modify the network in-place to alter the output init."""
    if isinstance(init_val, type(None)):
        return
    out_params = access_output_params(net)
    if init_val == 0:
        list(net.parameters())[-1].data = torch.zeros_like(out_params)
    else:
        list(net.parameters())[-1].data = torch.full_like(out_params, init_val)