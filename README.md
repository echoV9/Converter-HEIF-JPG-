# Converter-HEIF-JPG-
Simple HEIC -> JPG conversion tool
=======================================
HEIC to JPG Image Converter (Cat Edition)
=======================================

This simple application converts all .HEIC image files in a folder 
to .JPG format using a user-friendly terminal interface — complete 
with fun ASCII cats for progress, errors, and completion!

---------------------------------------
REQUIREMENTS
---------------------------------------

1. Windows or macOS system

2. Python 3.7 or later installed
   (https://www.python.org/downloads/)
	- Can download from Microsoft store
	- https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=en-us&gl=US&ocid=pdpshare

3. Required Python packages:
   - Pillow
   - pillow-heif

Install these packages by running the following command in your terminal:

    pip install pillow pillow-heif

---------------------------------------
HOW TO USE
---------------------------------------

Step 1:
Download or clone this application folder.

Step 2:
Open a terminal (Command Prompt or *PowerShell* on Windows, Terminal on macOS).

Step 3:
Navigate to the folder where the script is saved. Example:

    cd C:\Users\YourName\Downloads\heic_converter

Step 4:
Run the script using Python:

    python heic-jpg.py

Step 5:
When prompted, enter the full path to the folder that contains your .HEIC files. 
For example:

    C:\Users\YourName\Pictures\iPhone

Step 6:
The script will begin converting all .HEIC files to .JPG format.
You’ll see friendly cats during the process.

Step 7:
Once completed, a summary will be shown:
 - Number of files found
 - Number successfully converted
 - Any failed files
 - Location of the error log (if any)

Press ENTER to close the application when you're done.

---------------------------------------
NOTES
---------------------------------------

- Converted JPGs are saved in the same folder structure as the original HEICs.
- A log file will be created if any images fail to convert.
- The original HEIC files are NOT deleted or modified.

---------------------------------------
TROUBLESHOOTING
---------------------------------------

If you get a ModuleNotFoundError when running the script:

    pip install pillow pillow-heif

If Python isn't recognized, ensure it's added to your system PATH.

Still stuck? Try restarting your terminal or checking your Python installation.

---------------------------------------
SUPPORT
---------------------------------------

This tool is free to use and modify. For issues or suggestions, feel free to reach out!

Enjoy converting your photos 🐱📸
