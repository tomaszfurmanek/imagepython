import cv2
import os

# uses opencv
#conda install conda-forge::opencv


def extract_one_frame_per_minute(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Failed to open the video file.")
        return

    fps = 30  # Frames per second
    frames_per_minute = 60 * fps

    frame_count = 0
    minute_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frames_per_minute == 0:
            output_image_path = os.path.join(output_folder, f"20231006_stang_bot__GX030255.MP4_frame_at_minute_{minute_count}.jpg")
            cv2.imwrite(output_image_path, frame)
            print(f"Frame at minute {minute_count} saved.")
            minute_count += 1

        frame_count += 1

    cap.release()
    print("Done extracting frames.")

# Example usage

video_path = '/scratch/tomasz/CRIMACVIDEO/week3-del2/20231006_stang_bot/GX030255.MP4'
output_folder = '/scratch/tomasz/CRIMACVIDEO/pythontest/'
extract_one_frame_per_minute(video_path, output_folder)
