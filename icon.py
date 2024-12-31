import os
import shutil

# Paths
logo_path = r"C:\Users\hp\Desktop\JARVIS2.0\media\img\icons\JARVIS_ICON_1.ico"
target_directory = r"C:\Users\hp\Desktop\JARVIS2.0"
desktop_ini_path = os.path.join(target_directory, "desktop.ini")
target_icon_path = os.path.join(target_directory, "JARVIS_ICON_1.ico")

# Copy the icon file to the target directory
shutil.copy(logo_path, target_icon_path)

# Change file permissions if necessary
os.chmod(target_directory, 0o777)

# Write desktop.ini to set folder icon
with open(desktop_ini_path, "w") as f:
    f.write("[.ShellClassInfo]\n")
    f.write(f"IconResource={target_icon_path},0\n")

# Make desktop.ini a system and hidden file
os.system(f'attrib +h +s "{desktop_ini_path}"')

# Apply folder attributes
os.system(f'attrib +r "{target_directory}"')

print("Icon set for the directory.")
