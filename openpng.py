import zipfile
from PIL import Image
import io

def read_png_from_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        # List all file names in the zip file
        for filename in z.namelist():
            if filename.endswith('.png'):
                with z.open(filename) as file:
                    # Read the file as bytes, then use PIL to open it as an image
                    image_data = file.read()
                    image = Image.open(io.BytesIO(image_data))
                    
                    # Print the image size, type, mode
                    print("Image: {}, Size: {}, Type: {}, Mode: {}".format(
                        filename, image.size, image.format, image.mode))

# Example usage
zip_file_path = '/scratch/tomasz/crimacstereo/D2023008/download_initiated_2023-12-03_14-41-59.zip'
read_png_from_zip(zip_file_path)
