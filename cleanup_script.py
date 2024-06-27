import os
import shutil

def delete_folder_contents(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"Deleted contents of {folder_path}")
    except Exception as e:
        print(f"Failed to delete contents of {folder_path}. Reason: {e}")

def main():
    # Paths to common temporary directories
    temp_dirs = [
        os.getenv('TEMP'),
        os.path.join(os.getenv('SystemRoot'), 'Temp'),
        os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp')
    ]
    
    # Clean up temp directories
    for temp_dir in temp_dirs:
        if temp_dir and os.path.exists(temp_dir):
            delete_folder_contents(temp_dir)
    
    print("Cleanup complete. Consider restarting your PC for best performance.")

if __name__ == "__main__":
    main()
