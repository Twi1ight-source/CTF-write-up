import torch
from torch import nn
import numpy as np
from functools import reduce
import base64


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.stack = nn.Sequential(*([nn.Linear(8, 8, bias=False)] * 7)) 
        #nn.Linear(8, 8, bias=False) -->convert 8x8 input into 8x8 output by matrix multiplication
        #Sequential() -->take the output of matrix multiplication and multiply again with input (repeated 7 times)
    def forward(self, x):
        x = self.stack(x)
        return x


device = "cuda" if torch.cuda.is_available() else "cpu"

model = NeuralNetwork().to(device)
torch.save(model.state_dict(), "model.pth")

flag = b"buckeye{???????????????????????????????????????????????????????}"
assert len(flag) == 64
X = np.reshape(list(flag), (8, 8)).astype(np.float32) #create a 8x8 matrix with flag 

Xt = torch.from_numpy(X).to(device)   #convert from numpy array to tensor
Y = model(Xt).detach().numpy()

print(base64.b64encode(Y).decode())