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
import algorithm as algo
import sys

weightpath = sys.argv[1]
weight = algo.getfilecontent(weightpath)

imagepath = sys.argv[2]
image = im.open(imagepath)

if algo.guess(image, weight) == 0:
    print("It's a circle!")
else:
    print("It's a rectangle!")
