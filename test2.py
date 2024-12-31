import os

# Set the folder path
folder_path = r"C:\Users\hp\Desktop\JARVIS2.0\media\img\icons"

# Initialize counters for images and icons
image_counter = 1
icon_counter = 1

# Supported file extensions for images and icons
valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".ico", ".bmp")

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if it is a valid file
    if os.path.isfile(file_path) and filename.lower().endswith(valid_extensions):
        # Determine if it's an image or icon based on extension
        if filename.lower().endswith(".ico"):
            new_name = f"JARVIS_ICON_{icon_counter}.ico"
            icon_counter += 1
        else:
            new_name = f"JARVIS_LOGO_{image_counter}.png"
            image_counter += 1

        # Rename the file
        new_file_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_file_path)

print("Renaming completed.")
