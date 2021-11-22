import pickle
import torch  
with open('../motions/test/gMH_sBM_cAll_d22_mMH0_ch06.pkl', 'rb') as f:
    info = pickle.load(f)  
    print (info['smpl_poses'].shape)   #shows
    for i in range(400):
        frame=info['smpl_poses'][i]
        frame_torch=torch.from_numpy(frame)
        print(frame_torch.shape)
        with open(f'../testdata/gMH/pkl/fps_{i}.pkl', 'wb') as handle:
            pickle.dump(frame_torch, handle)

# with open('../testdata/fps_0.pkl', 'rb') as f:
#     info = pickle.load(f)  
#     print (info)   #shows