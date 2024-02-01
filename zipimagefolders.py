import os
import subprocess

def zip_subfolders(parent_folder, output_directory):
    # Change the current working directory to the parent folder
    os.chdir(parent_folder)

    # Get a list of subdirectories in the parent folder
    subfolders = [f for f in os.listdir('.') if os.path.isdir(os.path.join('.', f))]

    # Loop through each subfolder and create a ZIP archive using the command line
    for subfolder in subfolders:
        zip_filename = "{}.zip".format(subfolder)
        zip_filepath = os.path.join(output_directory, zip_filename)

        # Use the 'zip' command to create the ZIP archive
        cmd = ["zip", "-r", zip_filepath, subfolder]

        try:
            print(cmd)
            subprocess.run(cmd, check=True)
            print("ZIP archive created for {}".format(subfolder))
        except subprocess.CalledProcessError as e:
            print("Error creating ZIP archive for {}: {}".format(subfolder, e))

if __name__ == "__main__":
    source_directory = "/data/nmdstorage/SCRATCH/2023_CRIMAC_SALMON_AUSTEVOLL/D2023008_NOVEMBER_AUSTEVOLL/OBSERVATION_PLATFORMS/STEREOPROBE"
    output_directory = "/scratch/tomasz/crimacstereo/D2023008"

    if os.path.isdir(source_directory) and os.path.isdir(output_directory):
        zip_subfolders(source_directory, output_directory)
        print("ZIP archives created successfully.")
    else:
        print("Please provide valid source and output directory paths.")

    source_directory = "/data/nmdstorage/SCRATCH/2023_CRIMAC_SALMON_AUSTEVOLL/D2023009_DECEMBER_AUSTEVOLL/OBSERVATION_PLATFORMS/STEREOPROBE"
    output_directory = "/scratch/tomasz/crimacstereo/D2023009"

    if os.path.isdir(source_directory) and os.path.isdir(output_directory):
        zip_subfolders(source_directory, output_directory)
        print("ZIP archives created successfully.")
    else:
        print("Please provide valid source and output directory paths.")
