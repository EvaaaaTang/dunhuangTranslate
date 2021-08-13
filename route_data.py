from torch.utils.data import Dataset
import numpy as np
import pickle
import os
import json

def get_pose(folder):
    filenames = os.listdir(folder)
    poses=[]
    for file in filenames:
        filepath=folder+'\\'+file
        print(filepath)
        f=open(filepath)
        data=json.load(f)
        poses.append(data[0]['poses'][0])
    return np.array(poses)

class ROUTEDATA(Dataset):
    def __init__(self,folder='.\\jointsWTrans\\jointsWTrans',fps=60,sample=3):
        # with open(filename,'rb') as f:
        #     Content= pickle.load(f)
        #     self.smpldata=Content['smpl_poses']
        files=os.listdir(folder)
        self.smpldata=[]
        mark=0
        self.fps=fps
        self.sample=sample  
        if folder=='.\\traindata':
            for file in files:
                poses=[]
                path=folder+'\\'+file+'\\smplx'
                Content=get_pose(path)
                print(Content.shape)
                self.smpldata.append(Content)
            return         
        for file in files:
            if mark==0:
                mark+=1
                continue
            mark+=1
            with open(folder+'\\'+file,'rb') as f:
                Content=pickle.load(f)
                if folder=='.\\ballet_jazz' or folder=='.\\motions\\train':
                    Content=Content['smpl_poses']
                    #print(Content.type)
                else:
                    means=np.mean(Content,axis=0)
                    #print("means",means.shape)
                    for i in range(Content.shape[0]):
                        #print("content",Content[i].shape)
                        Content[i]-=means
                    Content=np.float32(Content.reshape(Content.shape[0],-1))
                self.smpldata.append(Content)

        #print (self.smpldata.shape)


    def __len__(self):
        length=0
        for data in self.smpldata:
            length+=len(data)-self.fps-2*self.sample+1
        return length
    
    def __getitem__(self, index):
        start=index
        end=start+self.fps+self.sample
        cur=0
        while not (start<len(self.smpldata[cur])-self.fps-2*self.sample+1):
            start-=len(self.smpldata[cur])-self.fps-2*self.sample+1
            end-=len(self.smpldata[cur])-self.fps-2*self.sample+1
            cur+=1
        x=np.concatenate((self.smpldata[cur][start:(start+self.sample)],self.smpldata[cur][end:(end+self.sample)]))
        y=self.smpldata[cur][(start+self.sample):end]
        #print(x.shape)
        #print(y.shape)
        return x,y
