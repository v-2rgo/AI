import shutil
import os

# Source and destination folders
source_folder = r"C:\source_path"
destination_folder = r"C:\destination_path"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Copy all files from source to destination
try:
    shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
    print(f"Successfully copied all files from {source_folder} to {destination_folder}")
except Exception as e:
    print(f"Error copying files: {e}")
