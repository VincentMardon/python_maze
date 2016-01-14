# -*- coding: utf-8 -*-

class Maze:
    """Maze class represent the choosen map :
    
      - name : The maze name
      - lines : The maze lines
      - charLists : The lists of maze characters listed by lines
      - oldPosition : The list of old x, y coordinates
      - newPosition : The list of new x, y coordinates (always equal to oldPosition after any processing)
    """
     
    def __init__(self, name, maze):
        self.name = name
        self.lines = maze.split('\n')
        self.charLists = []
        
        for e in self.lines:
            self.charLists.append(list(e))
        
        self.oldPosition = []
        
        # Define x coordinates
        for i, e in enumerate(self.lines):
            if 'X' in e:
                self.oldPosition.append(i)
        
        # Define y coordinates
        for i, e in enumerate(self.charLists[self.oldPosition[0]]):
            if e == 'X':
                self.oldPosition.append(i)
        
        self.newPosition = [self.oldPosition[0], self.oldPosition[1]]
    
    def printMaze(self):
        """Return maze from self.charLists"""
        self.lines = []
        for e in self.charLists:
            self.lines.append(''.join(e))
        
        return '\n'.join(self.lines)
    
    def move(self, direction, moveNumber):
        """Move user if self.checkPath() method return True, check items number and if user reach exit"""
        path = []
        nbItems = 0
        
        # North direction
        if direction == 'N' or direction == 'n':
            # browse each box
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0] - e - 1][self.oldPosition[1]]
                
                # Check if move is'nt too long
                try:
                    path.append(box)
                except IndexError:
                    return False
            
            # Check obstacles
            try:
                assert self.checkPath(path)
            except AssertionError:
                return False
            
            # Define self.newPosition
            self.newPosition[0] -= moveNumber
            
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0] - e - 1][self.oldPosition[1]]
                
                # Reach $
                if box == '$':
                    self.charLists[self.oldPosition[0] - e - 1][self.oldPosition[1]] = ' '
                    nbItems += 1
                
                # open door
                if box == '.':
                    self.charLists[self.oldPosition[0] - e - 1][self.oldPosition[1]] = ' '
        
        # East direction
        if direction == 'E' or direction == 'e':
            # browse each box
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0]][self.oldPosition[1] + e + 1]
                
                # Check if move is'nt too long
                try:
                    path.append(box)
                except IndexError:
                    return False
            
            # Check obstacles
            try:
                assert self.checkPath(path)
            except AssertionError:
                return False
            
            # Define self.newPosition
            self.newPosition[1] += moveNumber
            
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0]][self.oldPosition[1] + e + 1]
                
                # Reach $
                if box == '$':
                    self.charLists[self.oldPosition[0]][self.oldPosition[1] + e + 1] = ' '
                    nbItems += 1
                
                # open door
                if box == '.':
                    self.charLists[self.oldPosition[0]][self.oldPosition[1] + e + 1] = ' '
        
        # South direction
        if direction == 'S' or direction == 's':
            # browse each box
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0] + e + 1][self.oldPosition[1]]
                
                # Check if move is'nt too long
                try:
                    path.append(box)
                except IndexError:
                    return False
            
            # Check obstacles
            try:
                assert self.checkPath(path)
            except AssertionError:
                return False
            
            # Define self.newPosition
            self.newPosition[0] += moveNumber
                
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0] + e + 1][self.oldPosition[1]]
                
                # Reach $
                if box == '$':
                    self.charLists[self.oldPosition[0] + e + 1][self.oldPosition[1]] = ' '
                    nbItems += 1
                
                # open door
                if box == '.':
                    self.charLists[self.oldPosition[0] + e + 1][self.oldPosition[1]] = ' '
        
        # West direction
        if direction == 'O' or direction == 'o':
            # browse each box
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0]][self.oldPosition[1] - e - 1]
                
                # Check if move is'nt too long
                try:
                    path.append(box)
                except IndexError:
                    return False
            
            # Check obstacles
            try:
                assert self.checkPath(path)
            except AssertionError:
                return False
            
            # Define self.newPosition
            self.newPosition[1] -= moveNumber
            
            for e in range(moveNumber):
                box = self.charLists[self.oldPosition[0]][self.oldPosition[1] - e - 1]
                
                # Reach $
                if box == '$':
                    self.charLists[self.oldPosition[0]][self.oldPosition[1] - e - 1] = ' '
                    nbItems += 1
                
                # open door
                if box == '.':
                    self.charLists[self.oldPosition[0]][self.oldPosition[1] - e - 1] = ' '
        
        # Check target value to define end
        if self.charLists[self.newPosition[0]][self.newPosition[1]] == 'O':
            end = True
        else:
            end = False
        
        # Move user
        self.charLists[self.oldPosition[0]][self.oldPosition[1]] = ' '
        self.charLists[self.newPosition[0]][self.newPosition[1]] = 'X'
        
        # Make self.oldPosition and self.newPosition equals for the next move
        self.oldPosition = [self.newPosition[0], self.newPosition[1]]
        
        return nbItems, end
    
    def checkPath(self, path):
        """Check if there's an obstacle in path"""
        for e in path:
            if e == '-' or e == '|' or e == '+':
                return False
        
        return True