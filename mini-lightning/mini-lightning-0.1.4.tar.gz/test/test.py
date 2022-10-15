import mini_lightning as ml

from libs import *

model = nn.Linear(10, 10).cuda()
ckpt_fpath = "./asset/1.ckpt"
torch.save(model.state_dict(), ckpt_fpath)
a  = torch.load(ckpt_fpath, map_location=Device("cpu"))
b  = torch.load(ckpt_fpath)
print(a)
print(b)


