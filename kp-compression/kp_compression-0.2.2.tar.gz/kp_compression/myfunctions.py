from torch.nn.parameter import Parameter
import numpy as np
import torch
from torch import nn
import copy
import inspect

class convert_for_training:
  def convert_train(self,om,trainfunc,data,params,factor):
    nm = copy.deepcopy(om)
    mem = inspect.getmembers(nm, lambda a:not(inspect.isroutine(a)))
    lstms = [i for i in mem if type(i[1])==nn.LSTM]
    for i in lstms:
      inp_size = i[1].input_size
      hid_size = i[1].hidden_size
      layers = i[1].num_layers
      setattr(nm,i[0],CustomLSTM2(inp_size,hid_size,i[1],layers,factor))
    nm = trainfunc(nm,data,params)
    return nm


class Gru2(nn.Module):

  def forward(self, x, 
                init_states):
        """Assumes x is of shape (batch, sequence, feature)"""
        b, seq_sz, _ = x.size()
        hidden_seq = []
        HS = self.hidden_size
        if not init_states:
          h = (torch.zeros(self.layer,b,HS),torch.zeros(self.layer,b,HS))
        else:
          h = init_states
        #h1_t = h[0,:,:] #(num_layers, batch_size,hidden) (2,64,1024)
        #print(b)
        hnew = []
        for t in range(seq_sz):
            x_t = x[:, t, :] #(b,seq_len,features)(64,25,1024)-> (64,1024)
            for i in range(self.layer):
              if t == 0:
                h_t = h[i,:,:]
              else:
                h_t = hnew[i]
              gates = torch.kron( getattr(self, 'W{}1'.format(i+1)) , getattr(self, 'W{}2'.format(i+1)) @ x_t.T) + torch.kron(getattr(self, 'U{}1'.format(i+1)) , getattr(self, 'U{}2'.format(i+1)) @ h_t.T) + getattr(self, 'bias{}1'.format(i+1)) +getattr(self, 'bias{}2'.format(i+1)) + torch.kron( getattr(self, 'del_W{}1'.format(i+1)) , getattr(self, 'del_W{}2'.format(i+1)) @ x_t.T) + torch.kron(getattr(self, 'del_U{}1'.format(i+1)) , getattr(self, 'del_U{}2'.format(i+1)) @ h_t.T)
              r_t, z_t, n_t = (
                  torch.sigmoid(gates[:HS, :]),
                  torch.sigmoid(gates[HS:HS*2,:]),
                  torch.tanh(gates[HS*2:,:]),
              )
              h_t = (1 - z_t)*n_t + z_t * h_t
              
              if len(hnew)<(i+1):
                hnew.append(h_t.T.reshape(b,HS))
              else:
                hnew[i] = h_t.T.reshape(b,HS)
              if i==(self.layer-1):
                hidden_seq.append(h_t.T.unsqueeze(0))
        hidden_seq = torch.cat(hidden_seq, dim=0)
        # reshape from shape (sequence, batch, feature) to (batch, sequence, feature)
        hidden_seq = hidden_seq.transpose(0,1).contiguous() #(50,b,1024) -> (b,50,1024)
        #print(hidden_seq.shape)
        state = torch.cat([i.reshape(1,b,HS) for i in hnew])#((h1_t,c1_t),(h2_t,c2_t))
        return hidden_seq, state

class CustomLSTM2(nn.Module):
    def __init__(self, input_sz, hidden_sz, om, num_layers, factor, num_classes=1, peephole=False):
        super().__init__()
        self.input_sz = input_sz
        self.hidden_size = hidden_sz
        self.peephole = peephole
        self.W11 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.W12 = nn.Parameter(torch.Tensor(factor,input_sz))
        self.U11 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.U12 = nn.Parameter(torch.Tensor(factor,hidden_sz))
        self.del_W11 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.del_W12 = nn.Parameter(torch.Tensor(factor,input_sz))
        self.del_U11 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.del_U12 = nn.Parameter(torch.Tensor(factor,hidden_sz))
        self.bias11 = nn.Parameter(torch.Tensor(hidden_sz,1))
        self.bias12 = nn.Parameter(torch.Tensor(hidden_sz,1))

        self.W21 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.W22 = nn.Parameter(torch.Tensor(factor,input_sz))
        self.U21 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.U22 = nn.Parameter(torch.Tensor(factor,hidden_sz))
        self.del_W21 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.del_W22 = nn.Parameter(torch.Tensor(factor,input_sz))
        self.del_U21 = nn.Parameter(torch.Tensor(hidden_sz*4//factor,1))
        self.del_U22 = nn.Parameter(torch.Tensor(factor,hidden_sz))
        self.bias21 = nn.Parameter(torch.Tensor(hidden_sz,1))
        self.bias22 = nn.Parameter(torch.Tensor(hidden_sz,1))
        
        self.layer = num_layers
        self.init_weights(om, input_sz, hidden_sz, factor)

    def nkp(self, A , Bshape):
      blocks = map(lambda blockcol: np.split(blockcol, Bshape[0], 0),
                                np.split(A,        Bshape[1], 1))
      #print(blocks)
      Atilde = np.vstack([block.ravel() for blockcol in blocks
                                        for block in blockcol])
      #print("~")
      U, s, V = np.linalg.svd(Atilde)
      #print("2")
      Cshape = A.shape[0] // Bshape[0], A.shape[1] // Bshape[1]
      idx = np.argmax(s)
      B = np.sqrt(s[idx]) * U[:,idx].reshape(Bshape)
      C = np.sqrt(s[idx]) * V[idx,:].reshape(Cshape)
      return B, C

    def init_weights(self,om, input_sz, hidden_sz, factor):
      for i in range(self.layer):
        x = getattr(om,'weight_ih_l{}'.format(i))
        x = x.detach().cpu().numpy()
        om1,om2 = self.nkp(x,(hidden_sz*4//factor,1))
        om2 = om2.reshape(factor,input_sz if i==0 else hidden_sz)
        o_ih1,o_ih2 = self.nkp(x-np.kron(om1,om2),(hidden_sz*4//factor,1))
        setattr(self,'W{}1'.format(i+1),Parameter(torch.Tensor(om1)))
        setattr(self,'W{}2'.format(i+1),Parameter(torch.Tensor(om2)))
        setattr(self,'del_W{}1'.format(i+1),Parameter(torch.Tensor(o_ih1)))
        setattr(self,'del_W{}2'.format(i+1),Parameter(torch.Tensor(o_ih2)))

        x = getattr(om,'weight_hh_l{}'.format(i))
        x = x.detach().cpu().numpy()
        om1,om2 = self.nkp(x,(hidden_sz*4//factor,1))
        om2 = om2.reshape(factor,hidden_sz)
        o_ih1,o_ih2 = self.nkp(x-np.kron(om1,om2),(hidden_sz*4//factor,1))
        setattr(self,'U{}1'.format(i+1),Parameter(torch.Tensor(om1)))
        setattr(self,'U{}2'.format(i+1),Parameter(torch.Tensor(om2)))
        setattr(self,'del_U{}1'.format(i+1),Parameter(torch.Tensor(o_ih1)))
        setattr(self,'del_U{}2'.format(i+1),Parameter(torch.Tensor(o_ih2)))

        setattr(self,'bias{}1'.format(i+1),Parameter(getattr(om,'bias_hh_l{}'.format(i)).reshape(hidden_sz*4,1)))
        setattr(self,'bias{}2'.format(i+1),Parameter(getattr(om,'bias_ih_l{}'.format(i)).reshape(hidden_sz*4,1)))

         
    def forward(self, x, 
                init_states):
        """Assumes x is of shape (batch, sequence, feature)"""
        b, seq_sz, _ = x.size()
        hidden_seq = []
        HS = self.hidden_size
        if not init_states:
          h,c = (torch.zeros(self.layer,b,HS),torch.zeros(self.layer,b,HS))
        else:
          h,c = init_states
        #h1_t = h[0,:,:] #(num_layers, batch_size,hidden) (2,64,1024)
        #print(b)
        hnew,cnew = [],[]
        l_t = None
        for t in range(seq_sz):
            x_t = x[:, t, :] #(b,seq_len,features)(64,25,1024)-> (64,1024)
            for i in range(self.layer):
              if t == 0:
                h_t = h[i,:,:]
                c_t = c[i,:,:]
              else:
                h_t = hnew[i]
                c_t = cnew[i]
              if i!=0:
                x_t = l_t
              gates = torch.kron( getattr(self, 'W{}1'.format(i+1)) , getattr(self, 'W{}2'.format(i+1)) @ x_t.T) + torch.kron(getattr(self, 'U{}1'.format(i+1)) , getattr(self, 'U{}2'.format(i+1)) @ h_t.T) + getattr(self, 'bias{}1'.format(i+1)) +getattr(self, 'bias{}2'.format(i+1)) + torch.kron( getattr(self, 'del_W{}1'.format(i+1)) , getattr(self, 'del_W{}2'.format(i+1)) @ x_t.T) + torch.kron(getattr(self, 'del_U{}1'.format(i+1)) , getattr(self, 'del_U{}2'.format(i+1)) @ h_t.T)
              i_t, f_t, g_t, o_t = (
                torch.sigmoid(gates[:HS, :]), # input
                torch.sigmoid(gates[HS:HS*2,:]), # forget
                torch.tanh(gates[HS*2:HS*3,:]),
                torch.sigmoid(gates[HS*3:,:]), # output
              )
              #print(i_t.shape, f_t.shape, g_t.shape, o_t.shape, c1_t.shape)
              c_t = f_t * c_t.T + i_t * g_t
              h_t = o_t * torch.tanh(c_t)
              l_t = h_t.T
              if len(hnew)<(i+1):
                hnew.append(h_t.T.reshape(b,HS))
                cnew.append(c_t.T.reshape(b,HS))
              else:
                hnew[i] = h_t.T.reshape(b,HS)
                cnew[i] = c_t.T.reshape(b,HS)
              if i==(self.layer-1):
                hidden_seq.append(h_t.T.unsqueeze(0))
        hidden_seq = torch.cat(hidden_seq, dim=0)
        # reshape from shape (sequence, batch, feature) to (batch, sequence, feature)
        hidden_seq = hidden_seq.transpose(0,1).contiguous() #(50,b,1024) -> (b,50,1024)
        #print(hidden_seq.shape)
        state = (torch.cat([i.reshape(1,b,HS) for i in hnew]),torch.cat([i.reshape(1,b,HS) for i in cnew]))#((h1_t,c1_t),(h2_t,c2_t))
        return hidden_seq, state  
