import os
from datetime import datetime
from pillow_heif import register_heif_opener
from PIL import Image

# Enable HEIC support
register_heif_opener()

# --- ASCII CATS ---

intro_cat = r"""
 /\_/\  
( o.o )   Meow! Time to convert...
 > ^ <   

        HEIC → JPG
"""

complete_cat = r"""
 /\_/\  
( ^.^ )   All done! Conversion complete.
 > ^ <   

        Your JPGs are ready.
"""

error_cat = r"""
 /\_/\  
( x_x )   Uh-oh! Error encountered.
 > ^ <   

       Something went wrong...
"""

# --- FUNCTIONS ---

def convert_heic_to_jpg(root_dir, output_dir=None, log_errors=True):
    total_files = 0
    success_count = 0
    failed_files = []

    log_path = os.path.join(root_dir, f"conversion_errors_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log") if log_errors else None
    log_file = open(log_path, "w") if log_errors else None

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".heic"):
                total_files += 1
                heic_path = os.path.join(dirpath, filename)

                # Determine output path
                relative_path = os.path.relpath(dirpath, root_dir)
                out_dir = os.path.join(output_dir or root_dir, relative_path)
                os.makedirs(out_dir, exist_ok=True)
                jpg_path = os.path.join(out_dir, os.path.splitext(filename)[0] + ".jpg")

                try:
                    img = Image.open(heic_path)
                    img.save(jpg_path, "JPEG")
                    print(f"[✓] Converted: {heic_path} → {jpg_path}")
                    success_count += 1
                except Exception as e:
                    print(error_cat)
                    print(f"[✗] Failed to convert: {heic_path}")
                    print(f"     Reason: {e}")
                    failed_files.append(heic_path)
                    if log_file:
                        log_file.write(f"{heic_path} - {e}\n")

    if log_file:
        log_file.close()

    return total_files, success_count, failed_files, log_path

# --- EXECUTION ---

print(intro_cat)
input_directory = input("Enter the full path of the folder containing HEIC files: ").strip('"')

if not os.path.isdir(input_directory):
    print(error_cat)
    print(f"[!] Error: '{input_directory}' is not a valid directory.")
else:
    total, success, failures, logfile = convert_heic_to_jpg(input_directory)

    print("\n--- Conversion Summary ---")
    print(f"Total HEIC files found   : {total}")
    print(f"Successfully converted   : {success}")
    print(f"Failed conversions       : {len(failures)}")

    if failures:
        print("\nList of failed files:")
        for f in failures:
            print(f" - {f}")
        print(f"\nError details saved to: {logfile}")

    print("\n" + complete_cat)
    print("Thank you for using HEIC to JPG converter!")
    input("\nPress Enter to close the application...")

