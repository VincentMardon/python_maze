# -*- coding: utf-8 -*-

from lib.vendors.model.usermanager import UserManager
from lib.vendors.model.mazemanager import MazeManager

def executeMenu(user):
    """Show main options menu"""
    with open('app/options/views/menu.txt') as file:
        content = file.read()
    
    select = input(content)
    
    # User statistics
    if select == 'S' or select == 's':
        statsOpened = True
        while statsOpened:
            statsOpened = executeStats(user)
    
    # Mazes list
    elif select == 'L' or select == 'l':
        listOpened = True
        while listOpened:
            listOpened = executeList()
    
    # game rules
    elif select == 'C' or select == 'c':
        rulesOpened = True
        while rulesOpened:
            rulesOpened = executeRules()
    
    # Back to main menu
    elif select == '':
        return False
        
    else:
        print('\n' + '\033[1;31m' + 'VEUILLEZ SAISIR UNE LETTRE VALIDE OU APPUYEZ SUR ENTREE !' + '\033[0m')
        
    return True

def errorMessage():
    """Define error message and for the functions below"""
    return '\n' + '\033[1;91m' + 'ENTREE SUFFIRA !' + '\033[0m'

def executeStats(user):
    """Show user statistics"""
    # Define a new User object
    stats = UserManager(user)
    stats = stats.isRegister()
    
    with open('app/options/views/statistics.txt') as file:
        content = file.read()
        
    end = input(content.format(stats.name, stats.score, stats.gamesPlayed, stats.bestScores['Welcome'], stats.bestScores['Two_ways'], stats.bestScores['The_vault'], stats.bestScores['Ride'], stats.bestScores['Right_or_left'], stats.bestScores['The_bank'], stats.bestScores['Round-trip'], stats.bestScores['The_pyramid'], stats.bestScores['Fort_Knox']))
    
    if end != '':
        print(errorMessage())
        return True
    else:
        return False

def executeRules():
    """show game rules"""
    with open('app/options/views/rules.txt') as file:
        content = file.read()
    
    end = input(content)
    
    if end != '':
        print(errorMessage())
        return True
    else:
        return False

def executeList():
    """show mazes list"""
    mazes = MazeManager()
    print(mazes.getAllMazes())
    
    end = input('Appuyer sur ENTREE pour revenir au menu des options : ')
    
    if end != '':
        print(errorMessage())
        return True
    else:
        return False