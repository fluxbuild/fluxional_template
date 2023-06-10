import os
import shutil

files =  os.listdir()

for file in files:
    shutil.move("./" + file , "../")