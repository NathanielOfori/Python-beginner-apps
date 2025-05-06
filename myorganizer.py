import os
import shutil

def my_downloads_organizer():
    # defining the download folder path
    downloads_path = os.path.expanduser(r"C:\Users\PC\Downloads")

    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(downloads_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    break #Stop checking if there's a first match


    print("Downloads folder organized successfully")

# Run the script
my_downloads_organizer()