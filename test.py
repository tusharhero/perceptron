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
import algorithm as algo
import argparse

parser = argparse.ArgumentParser(
                                 prog='perceptron-trainer',
                                 description="""
                                 This program will train perceptron and generate the weight file.
                                 """
)

parser.add_argument(
                    'weightpath',
                    help='filepath of weight',
                    action='store'
)
parser.add_argument(
                    'imgpath',
                    help='filepath of image',
                    action='store'
)

args = parser.parse_args()

weight = eval(algo.getfilecontent(args.weightpath))

print(algo.guess(args.imgtpath, weight, size=(100,100)))
