import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class ROUTENET(nn.Module):
    def __init__(self, input_dim=64,input_size=3, input_fps=60,hid_dim=64, n_layers=1, dropout=0,bidirectional=True,scene_model_ckpt=True,device='cuda'):
        super().__init__()
        self.input_dim = input_dim
        self.hid_dim = hid_dim
        self.n_layers = n_layers
        self.input_size=input_size
        self.input_fps=input_fps
        self.lstm = nn.LSTM(input_dim, hid_dim, n_layers, dropout=dropout,bidirectional=bidirectional,batch_first=True)
        self.fc_scene = nn.Linear(256,32)
        self.fc = nn.Linear(hid_dim*2*2*input_size,hid_dim*2*2)
        self.fc2 = nn.Linear(hid_dim*2*2,input_fps*input_dim)


    def forward(self, x):
        #print("Forward")
        #print(x.shape)
        batch_size = x.shape[0]    
        
        outputs, (hidden, cell) = self.lstm(x)
        
        outputs = outputs.reshape(batch_size,-1)
        #print("output",outputs.shape)
        outputs = F.relu(self.fc(outputs))
        outputs = self.fc2(outputs)
        
        outputs = outputs.reshape(batch_size,self.input_fps,self.input_dim) 

        return outputs