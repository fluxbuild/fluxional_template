import os
import shutil

files =  os.listdir()

for file in files:
    # Check if file exists in the moving directory do not overwrite
    if os.path.exists("../" + file):
        print("File " + file + " already exists in the destination directory - Skipping.")
        shutil.move("./" + file , "../")