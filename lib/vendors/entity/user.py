# -*- coding: utf-8 -*-

from math import ceil

class User:
    """User class represent the user with his data :
    
      - name : The user name
      - score : the user score
      - gamesPlayed : the parties played by user
      - divisor : the divisor defined whether size maze choose (None if user have'nt stored maze)
      - move : the user number of move in a maze (None if user have'nt stored maze)
      - items : the $ number collected (None is user have'nt stored maze)
      - currentScore : the current score in a maze (None if user have'nt stored maze)
      - currentMaze : a dictionnary contains the maze as string and maze name stored in data (None if user have'nt stored maze)
    """
    
    def __init__(self, name, score, gamesPlayed, bestScores, divisor, items, move, currentScore, currentMaze):
        self.name = name
        self.score = score
        self.gamesPlayed = gamesPlayed
        self.bestScores = bestScores
        self.divisor = divisor
        self.items = items
        self.move = move
        self.currentScore = currentScore
        self.currentMaze = currentMaze
    
    def getCurrentScore(self):
        """Return the ceiling current score whether move and nbItems"""
        self.currentScore += ceil(self.items * 10 - self.move / self.divisor)
        
        # Prevent self.currentScore to go below 0
        if self.currentScore < 0:
            self.currentScore = 0
        
        return self.currentScore