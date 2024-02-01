import zipfile

def list_png_files_in_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        # Initialize a counter
        counter = 1

        # List all file names in the zip file
        for filename in z.namelist():
            if filename.endswith('.png'):
                # Print the counter and the name and path of the PNG file in the ZIP archive
                print("{:4d}   {}".format(counter, filename))

                # Increment the counter
                counter += 1

# Example usage
zip_file_path = '/scratch/tomasz/crimacstereo/D2023008/download_initiated_2023-12-03_14-41-59.zip'
list_png_files_in_zip(zip_file_path)
