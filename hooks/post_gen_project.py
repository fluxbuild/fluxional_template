import os

with open("Test.txt", "w") as f:
    f.write(str(os.listdir()))