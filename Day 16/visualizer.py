from PIL import Image
import numpy as np
from enum import Enum
class directions(Enum):
    up = (-1,0)
    down = (1,0)
    left = (0,-1)
    right = (0,1)

def create_collage(arrangement, visited):
    img_path = "Day 10/sprites/"
    #pipe2img = {"F":("L",0),"7":("L",270),"L":("L",90),"J":("L",180),"|":("I",0),"-":("I",90),".":("dot",0),"O":("dot",0),"k":("fill",0),"S":("S",0)}
    pipe2img = {"\\":("/",-90),"/":("/",0),"|":("|",0),"-":("|",90),".":(".",0), "#0":("#",0), "#1":("#",90), "#+":("+",180), 
                "#|":("#|", 0),"#-":("#|", 90),"-#":("#|", -90),"#-#":("#|#", 90), 
                "#/":("#/",0), "/#":("#/",180), "#\\":("#/",90), "\\#":("#/",-90), "#/#":("#/#",0), "#\\#":("#/#",180)}
    img_path = "Day 16/sprites/"
    mirror = Image.open(img_path+"mirror.png")
    split = Image.open(img_path+"split.png")
    empty = Image.open(img_path+"empty.png")
    laser = Image.open(img_path+"straight.png")
    cross = Image.open(img_path+"t.png")
    mirror_laser = Image.open(img_path+"angle.png")
    mirror_laser_double = Image.open(img_path+"angle_double.png")
    split_straight = Image.open(img_path+"split_straight.png")
    split_side = Image.open(img_path+"split_side.png")
    split_side_double = Image.open(img_path+"split_side_both.png")
    
    #images = {"L":l_img,"S":s_img,"I":i_img,"fill":fill_img,"dot":dot_img}
    #images = {"L":mirror,"S":split,"I":empty,"fill":empty,"dot":empty}
    images ={"/":mirror,"|":split,".":empty, "#":laser, "+":cross, "#/":mirror_laser, "#\#":mirror_laser_double,
              "#|":split_straight, "#-":split_side, "#/#":split_side_double, "#\\#":split_side_double}
    lasered_images = {
        "/":{directions.up:(mirror_laser, 0), directions.down:(mirror_laser, 90), directions.left:(mirror_laser, 180), directions.right:(mirror_laser, 0), (directions.left, directions.right):(mirror_laser_double, 0)},

        "\\" : {directions.left:(mirror_laser, -90), directions.right:(mirror_laser, 90),(directions.left, directions.right):(mirror_laser_double, 0)},

        "|"  : {directions.up:(split_straight, 0), directions.down:(split_straight, 0), directions.left:(split_side, 0), directions.right:(split_side, 180), 
                (directions.left, directions.right):(split_side_double, 0)},

        "-"  : {directions.up:(split_side, -90), directions.down:(split_side, 90), directions.left:(split_straight, 90), directions.right:(split_straight, 90), 
                (directions.up, directions.down):(split_side_double, 90)},
        "." : {directions.up:(laser, 90), directions.left:(laser, 0), (directions.down, directions.left):(cross, 0)}
    }
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
            position = (col_index * cell_size[0], row_index * cell_size[1])
            if visited[row_index][col_index] != []:
                vis = visited[row_index][col_index]

                if cell[0] == "\\":
                    if (directions.up in vis or directions.right in vis) and (directions.left in vis or directions.down in vis):
                        img = lasered_images[cell[0]][(directions.left, directions.right)]
                        pass
                    elif directions.left in vis or directions.down in vis:
                        img = lasered_images[cell[0]][directions.left]
                        pass
                    else:
                        img = lasered_images[cell[0]][directions.right]
                        #Single
                    img = img[0].rotate(img[1])#img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                    collage.paste(img, position)
                elif cell[0] == "/":
                    if (directions.up in vis or directions.left in vis) and (directions.right in vis or directions.down in vis):
                        img = lasered_images[cell[0]][(directions.left, directions.right)]
                        pass
                    elif directions.left in vis or directions.up in vis:
                        img = lasered_images[cell[0]][directions.left]
                        pass
                    else:
                        img = lasered_images[cell[0]][directions.right]
                        #Single
                    img = img[0].rotate(img[1])#img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                    collage.paste(img, position)
                elif cell[0] == "-":
                    if col_index == 4 and row_index == 4:
                        print("FUCCCCCCCCCCk", cell, vis)
                        print(visited[4][4], "VISITED",vis)
                    if directions.up in vis and directions.down in vis:
                        img = lasered_images[cell[0]][(directions.up, directions.down)]
                    elif directions.up in vis:
                        img = lasered_images[cell[0]][directions.up]
                    elif directions.down in vis:
                        img = lasered_images[cell[0]][directions.down]
                    else:
                        img = lasered_images[cell[0]][directions.right]
                    img = img[0].rotate(img[1])#img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                    collage.paste(img, position)


                elif cell[0] == "|":
                    if directions.left in vis and directions.right in vis:
                        img = lasered_images[cell[0]][(directions.left, directions.right)]
                    elif directions.left in vis:
                        img = lasered_images[cell[0]][directions.left]
                    elif directions.right in vis:
                        img = lasered_images[cell[0]][directions.right]
                    else:
                        img = lasered_images[cell[0]][directions.up]
                    img = img[0].rotate(img[1])#img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                    collage.paste(img, position) 

                elif cell[0] == ".":
                    #print(vis)
                    if col_index == 3 and row_index == 2:
                        print((directions.up or directions.down in vis) and (directions.left or directions.right) in vis)
                        print(cell)
                        print(visited[2][3], "VISITED",vis)
                    if (directions.up in vis or directions.down in vis) and (directions.left in vis or directions.right in vis):
                        if col_index == 3 and row_index == 2:
                            print("KJASKDJASKJD")
                            print(vis)
                        img = lasered_images[cell[0]][(directions.down, directions.left)]
                    elif directions.up in vis or directions.down in vis:
                        img = lasered_images[cell[0]][directions.up]
                    else:# directions.left in vis or directions.right in vis:
                        img = lasered_images[cell[0]][directions.left]
                    img = img[0].rotate(img[1])#img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                    collage.paste(img, position) 

            else:
                # Get the corresponding image and its rotation
                
                #img = pipe2img[cell]#.rotate(rotations[row_index][col_index])
                img = images[pipe2img[cell][0]].rotate(pipe2img[cell][1])
                # Calculate position
                #position = (col_index * cell_size[0], row_index * cell_size[1])
                # Paste the rotated image onto the collage
                collage.paste(img, position)

    return collage
if __name__ == "__main__":
    img_path = "Day 16/sprites/"
    straight = "I"
    corner = "L"


    #images = [img0, img1, img2]
    rotations = [[0, 90, 180], [270, 0, 90], [180, 180, 180]]
    visited = [[[] for y in range(3)] for x in range(3)]
    visited[1][1] = [directions.up]
    visited[1][0] = [directions.right, directions.up, directions.down]
    visited[2][1] = [directions.left, directions.right, directions.up, directions.down]
    visited[2][0] = [directions.right]
    visited[0][0] = [directions.right, directions.left]
    arrangement = [[0, 2, 1], [1, 0, 2], [1, 1, 1]]
    arrangement_letter = [["/","-","\\"],["|",".","|"],["\\","-","/"]]
    collage = create_collage(arrangement_letter, visited)
    collage.show()