# GET NPY DATA FROM ORIGINAL DFAUST DATA
import numpy
datas = numpy.load("./50021_one_leg_jump_poses.npz")
print(datas['poses'].shape)
res=numpy.empty([0,66])
for i in range(datas['poses'].shape[0]):
    row=datas['poses'][i][:66]
    res=numpy.append(res,[row],axis=0)
res=numpy.pad(res,((0,0),(0,6)),'constant',constant_values = (0,0))
numpy.save("testonelegjump.npy",res)
print(res.shape)
    