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

import algorithm as ag
import argparse

parser = argparse.ArgumentParser(prog='perceptron-trainer'
                                 description="""
                                 This program will train perceptron and generate the weight file.
                                 """
                                 )

parser.add_argument('-w', default='weight', action='store', help="location of the weight file.")
parser.add_argument('-e', default=10**7, action='store', help="Enouchs, the number of times it will train.")

args = parser.parse_args()

ag.train(enouchs=int(args.e), weightpath=args.w)
