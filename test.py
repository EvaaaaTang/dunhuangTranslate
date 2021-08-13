
import pickle
import numpy as np
import json
path='./model_transfer/smplx2smpl_deftrafo_setup.pkl'   #path='/root/……/aus_openface.pkl'   pkl文件所在路径
f=open(path,'rb')
data=pickle.load(f)
print(data)