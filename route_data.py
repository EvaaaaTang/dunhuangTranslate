from torch.utils.data import Dataset
import numpy as np
import pickle
import os
class ROUTEDATA(Dataset):
    def __init__(self,folder='.\\jointsWTrans\\jointsWTrans',fps=60,sample=3):
        # with open(filename,'rb') as f:
        #     Content= pickle.load(f)
        #     self.smpldata=Content['smpl_poses']
        files=os.listdir(folder)
        self.smpldata=[]
        mark=0
        for file in files:
            if mark==0:
                mark+=1
                continue
            mark+=1
            with open(folder+'\\'+file,'rb') as f:
                Content=pickle.load(f)
                if folder=='.\\ballet_jazz':
                    Content=Content['smpl_poses']
                else:
                    means=np.mean(Content,axis=0)
                    #print("means",means.shape)
                    for i in range(Content.shape[0]):
                        #print("content",Content[i].shape)
                        Content[i]-=means
                    Content=np.float32(Content.reshape(Content.shape[0],-1))
                self.smpldata.append(Content)
        self.fps=fps
        self.sample=sample
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
