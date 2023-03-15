'''
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
'''

from PIL import Image as im

#config
size = (20,20)
max_radius = 20

def gencircle(a,b,radius,filename,size):
    circle = im.new("L",size,0)
    for x in range(size[0]):
        for y in range(size[1]):
            if (x-a)**2 + (y-b)**2 <= radius**2:
                circle.putpixel((x,y),255)
    circle.save(filename)

#loop through all permutations of a,b,r
for a in range(size[0]):
    for b in range(size[1]):
        for r in range(max_radius):
            gencircle(a,b,r,f"circles/({a},{b},{r}).png",size)
