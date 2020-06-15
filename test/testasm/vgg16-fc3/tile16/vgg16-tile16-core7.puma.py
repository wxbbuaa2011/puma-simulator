
import sys, os
import numpy as np
import math
sys.path.insert (0, '/home/plinio/puma-simulator/include/')
sys.path.insert (0, '/home/plinio/puma-simulator/src/')
sys.path.insert (0, '/home/plinio/puma-simulator/')
from data_convert import *
from instrn_proto import *
from tile_instrn_proto import *
dict_temp = {}
dict_list = []
i_temp = i_set(d1=513, imm=4800, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=641, imm=1920, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=641, r1=513, counter=7, store_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=641, imm=4672, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=641, r1=641, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=769, imm=1792, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=769, r1=641, counter=7, store_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=128, r1=513, vec=128, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['01'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=513, r1=384, vec=104, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=641, vec=128, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=617, r1=256, vec=104, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=721, imm=2672, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=721, r1=721, load_width=13, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=617, r1=617, r2=721, vec=104)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=513, r1=513, r2=617, vec=104)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=617, imm=2776, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=617, r1=513, counter=1, store_width=13, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_hlt()
dict_list.append(i_temp.copy())
filename = 'vgg16/tile16/core_imem7.npy'
np.save(filename, dict_list)
