import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import torch.optim as optim
from torch.optim import lr_scheduler
from route import ROUTENET
from route_data import ROUTEDATA
#from utils import GeometryTransformer
import torch.utils.data as data
import pickle

batch_size = 512

dataset = ROUTEDATA(folder='.\\ballet_jazz',fps=60,sample=3)
# train_set_size = int(len(dataset) * 0.95)
# valid_set_size = len(dataset) - train_set_size
# train_set, valid_set = data.random_split(dataset, [train_set_size, valid_set_size])
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
#val_loader = torch.utils.data.DataLoader(valid_set,batch_size=1, shuffle=True)

model = ROUTENET(input_dim=72,hid_dim=256,input_size=3,input_fps=60)
model = model.cuda()

lrate = 0.001
optimizer = optim.Adam(model.parameters(), lr=lrate)
for epoch in range(50):
    model.train()
    total_loss=0
    
    for j,data in enumerate(dataloader,0):
        optimizer.zero_grad()

        x,y = data
        # print(x.shape)
        # print(y.shape)
        #x: [batch size, seq len, input dim]
        #y: [batch size, seq len, input dim]   
        x=x.cuda()
        y=y.cuda()
        out = model(x)
        loss = torch.mean(torch.abs(out-y))
        
        loss.backward()
        optimizer.step()

        total_loss = total_loss+loss

    print('loss:',total_loss/(j+1))
    
    save_path = './saved_model/route_smplnew2_'+str(epoch)+'.model'
    torch.save(model.state_dict(),save_path) 

with open(".\\ballet_jazz\\gJB_sBM_cAll_d07_mJB0_ch01.pkl",'rb') as f:
    data=pickle.load(f)['smpl_poses']
    x=np.concatenate(data[0:3],data[63:66])
    y=data[3:63]
    x=x[np.newaxis,:]
    y=y[np.newaxs,:]
    out=model(x)
    np.save('input1',x,allow_pickle=True)
    np.save('expect1',y,allow_pickle=True)
    np.save('output1',out.numpy(),allow_pickle=True)
# for j,data in enumerate(val_loader,0):

#         x,y = data
#         # print(x.shape)
#         # print(y.shape)
#         #x: [batch size, seq len, input dim]
#         #y: [batch size, seq len, input dim]   
#         x=x.cuda()
#         with torch.no_grad():
#             out = model(x)
#         np.save('input_'+str(j),x.cpu(),allow_pickle=True)
#         np.save('expect_'+str(j),y.cpu(),allow_pickle=True)
#         np.save('output_'+str(j),out.cpu().numpy(),allow_pickle=True)