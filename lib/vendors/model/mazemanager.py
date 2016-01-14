# -*- coding: utf-8 -*-

import os

from lib.vendors.entity.maze import Maze
    
class MazeManager:
    """Maps class contains all maps stored in maps repository with this properties :
    
    size : a list of size repositories name
    maps : a list of maze filenames grouped into lists by size
    """
    def __init__(self):
        """Define size and maps properties for labyrinth user selection"""
        self.sizes = os.listdir("data/maps")
        self.maps = []
        
        for e in self.sizes:
            self.maps.append(os.listdir("data/maps/" + e))
    
    def getMaze(self, sizeIndex, fileIndex):
        """Return maze instance from user select"""
        path = 'data/maps/' + self.sizes[sizeIndex -1] + '/' + self.maps[sizeIndex - 1][fileIndex - 1]
        name = self.maps[sizeIndex - 1][fileIndex - 1][2:-4]
        
        with open(path, 'r') as file:
            maze = file.read()
        
        maze = Maze(name, maze)
        
        return maze
        
    def getAllMazes(self):
        """Return the mazes list ordered by size"""
        string = '\nLabyrinthes\n|\n|  - Petit (26 X 13) :\n|\n|    '
        
        for e in self.maps[0]:
            string += e[:-4].replace('_', ' ') + '\n|    '
        
        string += '\n|  - Moyen (53 X 25) :\n|\n|    '
        
        for e in self.maps[1]:
            string += e[:-4].replace('_', ' ') + '\n|    '
        
        string += '\n|  - Grand (101 X 43) :\n|\n|    '
        
        for e in self.maps[2]:
            string += e[:-4].replace('_', ' ') + '\n|    '
        
        string += '\n|  - Personnalisés :\n|\n|    '
        
        if len(self.maps[3]) > 0:
            for e in self.maps[3]:
                string += e.replace('_', ' ') + '\n|    '
        else:
            string += "Aucun labyrinthe personnalisé pour le moment...\n|    "
        
        return string