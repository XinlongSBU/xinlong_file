#!/usr/bin/env python


import yt
import sys

print("================ test.py start from here =====================")
print("sys.path :")
print("----------")
for addr in sys.path:
    print(addr)
print("--------------------------------------------------------------")
ds = yt.load("/global/homes/x/xinlong/github_folder/xinlong_file/initial-model_prepare/plt_after_InitProj")
print("The directory of plotfile is at :")
print("---------------------------------")
print(ds.fullpath)
print("========================== End ===============================")

