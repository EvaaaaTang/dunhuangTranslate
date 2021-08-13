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

dataset = ROUTEDATA(folder='.\\traindata',fps=25,sample=1)
# train_set_size = int(len(dataset) * 0.95)
# valid_set_size = len(dataset) - train_set_size
# train_set, valid_set = data.random_split(dataset, [train_set_size, valid_set_size])
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
#val_loader = torch.utils.data.DataLoader(valid_set,batch_size=1, shuffle=True)

model = ROUTENET(input_dim=72,hid_dim=256,input_size=1,input_fps=25)
model = model.cuda()

lrate = 0.001
optimizer = optim.Adam(model.parameters(), lr=lrate)
# saved_dict=torch.load('./saved_model/route_smpltotal_29.model')
# model.load_state_dict(saved_dict)
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
    
    save_path = './saved_model/route_smplzjnew_'+str(epoch)+'.model'
    torch.save(model.state_dict(),save_path) 
# saved_dict=torch.load('./saved_model/route_smpltotalnew_49.model')
# model.load_state_dict(saved_dict)
# framenum=[0,60,120,180,240,360,480]
# for i in range(len(framenum)-1):
#     with open(f".\\kinectRivised\\fps{framenum[i]}.pkl",'rb') as f:
#         with open(f".\\kinectRivised\\fps{framenum[i+1]}.pkl",'rb') as f1:
#                 data=pickle.load(f)['pose']
#                 data2=pickle.load(f1)['pose']
#                 data=data.to(torch.float32)
#                 data2=data2.to(torch.float32)
#                 x=torch.stack((data,data2),0)
#                 print(x.shape)
#                 #y=data[183:243]
#                 x=x[np.newaxis,:]
#                 #y=y[np.newaxis,:]
#                 #x=torch.tensor(x)
#                 #y=torch.tensor(y)
#                 x=x.cuda()
#                 print(x.shape)
#                 #print(y.shape)
#                 with torch.no_grad():
#                     out=model(x)
#                 # np.save('input3',x.cpu(),allow_pickle=True)
#                 # np.save('expect3',y,allow_pickle=True)
#                 np.save(f'./testResults/kinect_outputnew1_{framenum[i]}_{framenum[i+1]}',out.cpu().numpy(),allow_pickle=True)
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