# -*- coding: utf-8 -*-

import pickle

from lib.vendors.entity.user import User

class UserManager:
    """UserManager class create, read and update data user this property :
    
      filename : the user file name
    """
    def __init__(self, filename):
        """Define filename property"""
        self.filename = filename
        
    def isRegister(self):
        """Test if data file exists and return a Robot instance and currentMaze"""
        # this trick's explained here : http://www.journaldunet.com/developpeur/pratique/developpement/12309/comment-verifier-qu-un-fichier-existe-en-python.html
        try:
            with open('data/players/' + self.filename): pass
        except IOError:
            data = {
                'score': 0,
                'gamesPlayed': 0,
                'bestScores': {
                    'Welcome': 0,
                    'Two_ways': 0,
                    'The_vault': 0,
                    'Ride': 0,
                    'Right_or_left': 0,
                    'The_bank': 0,
                    'Round-trip': 0,
                    'The_pyramid': 0,
                    'Fort_Knox': 0
                },
                'divisor': 0,
                'items': 0,
                'move': 0,
                'currentScore': 0,
                'currentMaze': None
            }
            
            self.saveData(data)
            
            return User(self.filename, data['score'], data['gamesPlayed'], data['bestScores'], data['divisor'], data['items'], data['move'], data['currentScore'], data['currentMaze'])
        else:
            data = self.readData()
            
            return User(self.filename, data['score'], data['gamesPlayed'], data['bestScores'], data['divisor'], data['items'], data['move'], data['currentScore'], data['currentMaze'])
    
    def readData(self):
        """Return dictionnary of data file"""
        with open('data/players/' + self.filename, 'rb') as file:
            unpickler = pickle.Unpickler(file)
            data = unpickler.load()
            
        return data
    
    def resetData(self):
        """Reset move, items and currentScore of user data"""
        data = self.readData()
        
        data['divisor'] = 0
        data['move'] = 0
        data['items'] = 0
        data['currentScore'] = 0
        data['currentMaze'] = None
        
        self.saveData(data)
    
    def saveData(self, data):
        """save data in datafile"""
        with open('data/players/' + self.filename, 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(data)