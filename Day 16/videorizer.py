import cv2
import os
import glob

# Directory containing images
image_folder = 'Day 16/images' # Replace with your image folder path
video_name = 'output_video.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort(key=lambda x: int(x.split('.')[0]))  # Sorting the images by number

# Determine the width and height from the first image
image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(image_path)
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well.
video = cv2.VideoWriter(video_name, fourcc, 24, (width, height))  # 1 is the frame rate

for x, image in enumerate(images):
    if x == 0:
        for _ in range(15):
            video.write(cv2.imread(os.path.join(image_folder, image)))
    elif x == len(images) - 1:
        for _ in range(40):
            video.write(cv2.imread(os.path.join(image_folder, image)))
    else:
        video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
