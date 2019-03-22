import numpy as np

import sys,os

gro_fn=sys.argv[1]
atom_indexes=sys.argv[2:]
N=len(atom_indexes)
gro_arr=[line.split() for line in open(gro_fn)][2:-1]

gro_file=np.array([i[-4:] for i in gro_arr])
x_coordinates=[]
y_coordinates=[]
z_coordinates=[]
for i,atom_index in enumerate(atom_indexes):

    if str(atom_index) in gro_file[:,0]:
        x_coordinates.append(float([i[-3] for i in gro_file[gro_file[:, 0]==str(atom_index)]][0]))
        y_coordinates.append(float([i[-2] for i in gro_file[gro_file[:, 0] == str(atom_index)]][0]))
        z_coordinates.append(float([i[-1] for i in gro_file[gro_file[:, 0] == str(atom_index)]][0]))
        print gro_file[gro_file[:, 0]==str(atom_index)]
    else:
        print "Index %s not found in the molecule"%atom_index
print "X: ",x_coordinates
print "Y: ",y_coordinates

print "Z: ",z_coordinates

print "COM coordinates: x = %s    y = %s    z = %s"%(np.mean(x_coordinates),np.mean(y_coordinates),np.mean(z_coordinates))
