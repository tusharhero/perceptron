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

# config
size = (100, 100)
center = 100
step = 5


def genrectangle(a, b, p, q, size, filename):
    rectangle = im.new("L", size, 0)
    for x in range(size[0]):
        for y in range(size[1]):
            if (abs(x - a) <= p) and (abs(y - b) <= q):
                rectangle.putpixel((x, y), 255)
    rectangle.save(filename)


# permutate through every config.
for a in range(0, size[0], step):
    for b in range(0, size[1], step):
        for p in range(0, center, step):
            for q in range(0, center, step):
                genrectangle(a, b, p, q, size, f"rectangles/({a},{b},{p},{q}).png")
