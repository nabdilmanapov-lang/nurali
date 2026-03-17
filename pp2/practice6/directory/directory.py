import os
import shutil
# Create nested directories
# Creates: project/data/raw
os.makedirs("project/data/raw", exist_ok=True)

# List files and folders
# Lists everything in current directory
items = os.listdir(".")
print("Files and folders:", items)

# Find files by extension
# Finds all .txt files in the current directory
files = os.listdir(".")
txt_files = [file for file in files if file.endswith(".txt")]
print("TXT files:", txt_files)

# Move files between directories
# Moves example.txt into project/data/raw/
# (Make sure example.txt exists first)
shutil.move("example.txt", "project/data/raw/example.txt")

# Copy files between directories
# Copies example.txt into project/data/
shutil.copy("example.txt", "project/data/example_copy.txt")
