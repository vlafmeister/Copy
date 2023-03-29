import os
import subprocess

# Path to the folder where you want to save the copied files
save_folder = "/path/to/folder"

# Execute the adb command to list all files in the phone's DCIM folder
cmd = ["adb", "shell", "ls", "/sdcard/DCIM"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
output, error = process.communicate()

# Loop through each file in the DCIM folder and copy to the save folder
for file_name in output.splitlines():
    # Ignore any non-image or non-video files
    if not file_name.endswith((".jpg", ".jpeg", ".png", ".mp4")):
        continue

    # Execute the adb pull command to copy the file to the save folder
    cmd = ["adb", "pull", f"/sdcard/DCIM/{file_name}", f"{save_folder}/{file_name}"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Check if the file was successfully copied
    if os.path.isfile(f"{save_folder}/{file_name}"):
        print(f"Copied {file_name}")
    else:
        print(f"Error copying {file_name}")
