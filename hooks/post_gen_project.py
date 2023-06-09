import os
import shutil


def move_files():
    files =  os.listdir()

    for file in files:
        # Check if file exists in the moving directory do not overwrite
        if os.path.exists("../" + file):
            print("File " + file + " already exists in the destination directory - Skipping.")
        else:
            shutil.move("./" + file , "../")

    try:
        # Delete original directory 
        shutil.rmtree("../" + "{{cookiecutter.project_name}}")
    except OSError as e:
        print(e)

if __name__ == "__main__":
    move_files()