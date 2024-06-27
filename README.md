# Windows Temporary Files Cleanup Script

## Overview

This Python script is designed to clean up temporary files and caches on a Windows 11 PC. It helps in freeing up disk space and potentially improving system performance.

## Requirements

- Python 3.x
- Windows 11

## Installation

### Step 1: Download and Install Python

If you don't have Python installed, follow these steps to download and install it using Command Prompt:

1. Open Command Prompt (cmd).
2. Download the Python installer:

    ```sh
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
    ```

3. Run the installer:

    ```sh
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    ```

4. Verify the installation:

    ```sh
    python --version
    ```

### Step 2: Download the Script

1. Clone this repository or download the script file directly.
2. Save the script as `cleanup_script.py`.

## Usage

1. Open Command Prompt (cmd).
2. Navigate to the directory where you saved `cleanup_script.py`. For example:

    ```sh
    cd C:\Users\YourUsername\Desktop
    ```

3. Run the script:

    ```sh
    python cleanup_script.py
    ```

### Administrator Privileges

Some files in the temporary directories may require administrator privileges to delete. Run the Command Prompt as an administrator by right-clicking on the Command Prompt icon and selecting "Run as administrator."

## Script Details

The script performs the following actions:

- Deletes contents of the system's temporary directories, including:
  - `%TEMP%`
  - `C:\Windows\Temp`
  - `C:\Users\<YourUsername>\AppData\Local\Temp`

### Script Code

```python
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

You can copy and paste this Markdown content into your GitHub repository's `README.md` file. This format will make your repository look professional and informative.
