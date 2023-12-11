from PIL import Image
import numpy as np

def create_collage(arrangement):
    img_path = "Day 10/sprites/"
    pipe2img = {"F":("L",0),"7":("L",270),"L":("L",90),"J":("L",180),"|":("I",0),"-":("I",90),".":("dot",0),"O":("dot",0),"k":("fill",0),"S":("S",0)}
    img_path = "Day 10/sprites/"
    l_img = Image.open(img_path+"L0.png")
    s_img = Image.open(img_path+"S0.png")
    i_img = Image.open(img_path+"I0.png")
    fill_img = Image.open(img_path+"fill.png")
    dot_img = Image.open(img_path+"dot.png")
    images = {"L":l_img,"S":s_img,"I":i_img,"fill":fill_img,"dot":dot_img}
    #for key in pipe2img:
        #pass
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
            
            #img = pipe2img[cell]#.rotate(rotations[row_index][col_index])
            img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
            # Calculate position
            position = (col_index * cell_size[0], row_index * cell_size[1])
            # Paste the rotated image onto the collage
            collage.paste(img, position)

    return collage
if __name__ == "__main__":
    img_path = "Day 10/sprites/"
    straight = "I"
    corner = "L"


    #images = [img0, img1, img2]
    rotations = [[0, 90, 180], [270, 0, 90], [180, 180, 180]]
    arrangement = [[0, 2, 1], [1, 0, 2], [1, 1, 1]]
    arrangement_letter = [["F","F","7"],["-","S","-"],["L","L","J"]]
    collage = create_collage(arrangement_letter)
    collage.show()

