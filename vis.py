import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
#data=np.load('0429_train_3_120_mocap.npy',allow_pickle=True)
with open('.\\jointsWTrans\\jointsWTrans\\clip0_intersect.pkl','rb') as f:
     Content=pickle.load(f)
     data=Content
     print(data.shape)
for jjj in range(1):
    data_list=data
    #use=[0,1,2,3,6,7,8,14,16,17,18,20,24,25,27]
    data_list=data_list.reshape(-1,720,20,3)#num_person, frames, num_joints, xyz
    # data_list=data_list*0.1*1.8/3
    # data_list=data_list[:,:,[0,1,4,7,2,5,8,12,15,16,18,20,17,19,21],:]
    body_edges = np.array(
    [[0,1], [0,2],[1,4],[4,7],
    [7,10],[2,5],[5,8],[8,11],[0,3],[3,6],[6,9],[9,14],[9,13],[9,12],
    [12,15],[14,17],[17,19],[19,21],[21,23],[13,16],[16,18],[18,20],[20,22]])

    body_edges = np.array(
    [[0,1], [1,2],[2,3],[0,4],
    [4,5],[5,6],[0,7],[7,8],[7,9],[9,10],[10,11],[7,12],[12,13],[13,14]]
    )
    body_edges = np.array(
    [[0,1], [1,2],[2,3],[3,4],
    [4,5],[0,6],[6,7],[7,8],[8,9],[9,10],[0,11],[11,12],[12,13],[13,14],[14,15],[15,16],[13,17],[17,18],[18,19],[19,20],[21,22],[20,23],[13,24],[24,25],[25,26],[26,27],[27,28],[28,29],[27,30]]
    )
    body_edges=np.array(
        [[0,1],[0,2],[0,3],[1,4],[2,5],[4,6],[5,7],[6,8],[7,9],[3,10],[10,11],[10,12],[10,13],[12,14],[13,15],[14,16],[15,17],[16,18],[17,19]]
    )

    fig = plt.figure(figsize=(16, 9))
                
    ax = fig.add_subplot(111, projection='3d')
    #ax.figure(figsize=(10, 10))
    plt.ion()

    length=data_list.shape[1]
    length_=data_list.shape[1]
    i=0
    length_=1
    while i < length_:
        ax.lines = []
        for j in range(1):
            
            xs=data_list[j,i,:,0]#.numpy()
            ys=data_list[j,i,:,1]#.numpy()
            zs=data_list[j,i,:,2]#.numpy()
            #print(xs)
            ax.plot( zs,xs, ys, 'y.')

            
            #print('x',np.mean(abs(x-xs)))
            #print('y',np.mean(abs(y-ys)))
            #print('z',np.mean(abs(z-zs)))
            
            plot_edge=True
            if plot_edge:
                for edge in body_edges:
                    x=[data_list[j,i,edge[0],0],data_list[j,i,edge[1],0]]
                    y=[data_list[j,i,edge[0],1],data_list[j,i,edge[1],1]]
                    z=[data_list[j,i,edge[0],2],data_list[j,i,edge[1],2]]
                    if i>=0.5*length:
                        ax.plot(z,x, y, 'green')
                        #print('1111111')
                    else:
                        ax.plot(z,x, y, 'green')
            #ax.set_xlim3d([-5 , 5])
            #ax.set_ylim3d([-5 , 5])
            #ax.set_zlim3d([0, 2])
            
            ax.set_xlim3d([-2 , 2])
            ax.set_ylim3d([-2 , 2])
            ax.set_zlim3d([-0, 2])
            ax.set_axis_off()
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")
            
        plt.pause(0.01)
        i += 1
        
        #if i == length_:
        #    i = 0

    plt.ioff()
    plt.show()