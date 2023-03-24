"""
The GPLv3 License (GPLv3)

Copyright (c) 2023 Tushar Maharana

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PIL import Image as im
import random as ran
import sys

def image_conversion(image,size):
    image.convert("RGBA").convert("L")
    return image.resize(size)

def getfilename(shape, var=100, step=5):  # select random files from dataset. (This is possible because they follow a specific naming rule.)
    filename = ""
    if shape == "circle":
        a = ran.randrange(0, var, step)
        b = ran.randrange(0, var, step)
        r = ran.randrange(0, var, step)
        filename = f"circles/({a},{b},{r}).png"
    if shape == "rectangle":
        a = ran.randrange(0, var, step)
        b = ran.randrange(0, var, step)
        c = ran.randrange(0, var, step)
        d = ran.randrange(0, var, step)
        filename = f"rectangles/({a},{b},{c},{d}).png"
    return filename

def genrandomcircle(size):
    image_list = []
    radius = ran.randint(0,max(size))
    center = (
            ran.randint(0,size[0]),
            ran.randint(0,size[1]),
            )

    for x in range(size[0]):
        for y in range(size[1]):
            if (x - center[0])**2 + (y - center[1])**2 <= radius**2:
                image_list.append(1)
            else:
                image_list.append(0)
    return image_list

def genrandomrectangle(size):
    image_list = []
    a = ran.randint(0,max(size))
    b = ran.randint(0,max(size))
    p = ran.randint(0,max(size))
    q = ran.randint(0,max(size))

    for x in range(size[0]):
        for y in range(size[1]):
            if (abs(x - a) <= p) and (abs(y - b) <= q):
                image_list.append(1)
            else:
                image_list.append(0)
    return image_list

def list_float2int(list):  # convert each elemenet of the list into an integer
    intlist = []
    for i in list:
        intlist.append(int(i))
    return intlist


def genrandweight(size):  # randomly generate weight for first run
    weight = []
    for i in range(size[0] * size[1]):
        weight.append(ran.randint(-1, 1))
    return weight


def createfile(filepath, size):
    with open(filepath, 'w') as fp:
        fp.write(str(genrandweight(size)))


def getfilecontent(filepath, size):
    def readfile():
        with open(filepath, 'r') as fp:
            return fp.read()
    try:
        weights = eval(readfile())
    except FileNotFoundError:
        print(f'file "{filepath}" does not exists\ncreating "{filepath}"')
        createfile(filepath, size)
        print('done')
        weights = eval(readfile())
    except SyntaxError:
        print('SyntaxError occured while parsing file')
        choice = input('do you want to rewrite file by destorying its content? Y/n [Y]: ').lower()
        while not choice in ('y', 'n', ''):
            print(f'invalid input "{choice}"')
            choice = input('do you want to rewrite file by destorying its content? Y/n [Y]: ').lower()
        if choice in ('y', ''):
            print(f'rewriting {filepath}')
            createfile(filepath, size)
            print('done')
            weights = eval(readfile())
        else:
            sys.exit()
    return weights


def multiply(weight, image_list, size=(100, 100)):
    product = 0
    for i in range(size[0] * size[1]):
        product += weight[i] * image_list[i]
    return product


def addition(weight, image_list, SubOrAdd=1, size=(100, 100)):
    sum = []
    for i in range(size[0] * size[1]):
        sum.append(weight[i] + (image_list[i] * SubOrAdd))
    return sum


def normalize(list, factor):  # fit it in the range of [0,1]
    normalized_list = []
    for i in list:
        normalized_list.append(i / 255 * factor)
    return normalized_list


def getimage_list(image):
    image_list = normalize(list((image.getdata())), 1)
    return image_list


def guess(imagepath, weight, bias=100, shapes=("circle", "rectangle"),size=(100,100)):
    image_list = getimage_list(image_conversion(im.open(imagepath),size))
    product = multiply(weight, image_list)

    if product + bias > 0:
        predict_shape = shapes[1]
    else:
        predict_shape = shapes[0]
    return predict_shape 


def train(
    bias=1000,
    enouchs=10000,
    weightpath="",
    size=(100, 100),
    shapes=("circle", "rectangle"),
    no_visualize_weight=False,
    verbose=False
):
    # load weight from file or generate randomly
    if len(weightpath) == 0:
        weight = genrandweight(size)
        weightpath = "weight"
    else:
        weight = getfilecontent(weightpath, size)

    correct_guesses = 0

    # Read Wikipedia article linked in README.md
    for i in range(enouchs):
        shape = shapes[ran.randrange(2)]
        filename = getfilename(shape)
        if shape == "circle":
            image_list = genrandomcircle(size)
        else:
            image_list = genrandomrectangle(size)

        product = multiply(weight, image_list)

        print(product)

        if product + bias > 0:
            predict_shape = shapes[0]
            if shape != predict_shape:
                weight = addition(weight, image_list, +1)
        else:
            predict_shape = shapes[1]
            if shape != predict_shape:
                weight = addition(weight, image_list, -1)

        if shape == predict_shape:
            correct_guesses += 1

        if i % 1000 == 0:  # log and save every 1000 enouchs
            if not no_visualize_weight:
                weight_viz = im.new("RGB", size)
                weight_viz.putdata(list_float2int(weight))
                weight_viz.save("weight.png")

            with open(weightpath, "w") as w:
                w.write(str(weight))

            with open("log", "a") as log:
                log.write(
                    f"{correct_guesses/(1000)}; {i/(enouchs+1) * 100}% := {filename}\n"
                )
                correct_guesses = 0
        if verbose:
            print(i, correct_guesses, predict_shape, shape, f"\n{correct_guesses/(1000)}; {i/(enouchs+1) * 100}% := {filename}\n")
        else:
            print(i, correct_guesses, predict_shape, shape)
