import os
import glob

print()
# dirs = os.listxattr("./")


for filename in glob.glob("./*"):
    filename = filename[2:]
    print(f"![{filename}](./static/{filename})")