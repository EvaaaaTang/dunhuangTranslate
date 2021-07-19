
import pickle
import numpy as np
path='./testresults/output_0.pkl.npy'   #path='/root/……/aus_openface.pkl'   pkl文件所在路径
	   
# f=open(path,'rb')
# data=pickle.load(f)
data=np.load(path)
data=data[0]
print(data.shape)
