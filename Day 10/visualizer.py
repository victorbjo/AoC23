from PIL import Image
import numpy as np

def create_collage(image_files, arrangement):
    img_path = "Day 10/sprites/"
    pipe2img = {"F":("L",90),"7":("L",180),"L":("L",270),"J":("L",0),"|":("I",0),"-":("I",90),".":("dot",0),"O":("dot",0),"K":("fill",0),"S":("S",0)}
    img_path = "Day 10/sprites/"
    images = {}
    for key in pipe2img:
        pass
    """
    Creates a collage from a set of images, with specified rotations and arrangement.

    :param image_files: List of Image objects (3 different 10x10 images).
    :param rotations: List of rotation angles for each cell in the arrangement.
    :param arrangement: 2D list representing the arrangement of images.
    :return: Image object of the final collage.
    """

    # Define the size of each cell and initialize a blank canvas
    cell_size = (10, 10)
    rows = len(arrangement)
    cols = len(arrangement[0])
    collage_size = (cols * cell_size[0], rows * cell_size[1])
    collage = Image.new('RGB', collage_size)

    # Iterate through the arrangement
    for row_index, row in enumerate(arrangement):
        for col_index, cell in enumerate(row):
            # Get the corresponding image and its rotation
            img = image_files[cell].rotate(rotations[row_index][col_index])
            # Calculate position
            position = (col_index * cell_size[0], row_index * cell_size[1])
            # Paste the rotated image onto the collage
            collage.paste(img, position)

    return collage
img_path = "Day 10/sprites/"
straight = "I"
corner = "L"


images = [img0, img1, img2]
rotations = [[0, 90, 180], [270, 0, 90], [180, 180, 180]]
arrangement = [[0, 2, 1], [1, 0, 2], [1, 1, 1]]
collage = create_collage(images, rotations, arrangement)
collage.show()

arrangment_letter = [["F","_","7"],["|","|","0"],["L","J","."]]
