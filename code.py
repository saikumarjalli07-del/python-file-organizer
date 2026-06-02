import os
import shutil
from datetime import datetime

# Log file
LOG_FILE = "file_organizer.log"

def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist!")
            return

        categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv", ".avi"],
            "Others": []
        }

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()

                destination = "Others"

                for category, extensions in categories.items():
                    if ext in extensions:
                        destination = category
                        break

                dest_folder = os.path.join(folder_path, destination)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.move(file_path,
                            os.path.join(dest_folder, file))

                print(f"Moved: {file} -> {destination}")
                write_log(f"Moved {file} to {destination}")

        print("File organization completed.")

    except Exception as e:
        print("Error:", e)
        write_log(f"ERROR: {e}")

folder = input("Enter folder path: ")
organize_files(folder)