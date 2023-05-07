import sys
import numpy as np;
import re; # regexp
import matplotlib.pyplot as ma;


class Element:
    def __init__(self, name, start_x, start_y, end_x=None, end_y=None):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def __repr__(self):
        coords = f"({self.start_x},{self.start_y})"
        if self.end_x is not None and self.end_y is not None:
            coords += f" ;({self.end_x},{self.end_y})"
        return f"Element(name='{self.name}', coords={coords})"

def parse_elements_file(file_path):
    elements = []

    with open(file_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split(':')

            if len(parts) == 2:
                name = parts[0].strip()
                raw_coordinates = parts[1].strip().split(';')

                try:
                    coordinates = []
                    for coord in raw_coordinates:
                        coord = coord.strip('()').split(',')
                        coordinates.append((int(coord[0].strip()), int(coord[1].strip())))

                    if len(coordinates) == 1:
                        elements.append(Element(name, coordinates[0][0], coordinates[0][1]))
                    elif len(coordinates) == 2:
                        elements.append(Element(name, coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]))
                except ValueError:
                    pass

    return elements

"""
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print( "Veuillez donner le chemin d'un fichier en arguments du programme")
        exit(1)
        
        
    elements = parse_elements_file(sys.argv[1])
    print(elements)
"""