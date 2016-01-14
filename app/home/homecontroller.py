# -*- coding: utf-8 -*-

from lib.vendors.model.usermanager import UserManager

def executeHome():
    """Return welcome view where user enter his name."""
    with open('app/home/views/home.txt', 'r') as file:
        content = file.read()
    
    return input(content.format('\033[1;5;34m', '\033[0m'))

def executeMenu(name):
    """Define if user is registered in data/players
    If user has a saved maze in his data, show a load option in menu.
    Return menu view, saveMaze and user instance."""
    userManager = UserManager(name)
    user = userManager.isRegister()
    load = ''
    
    with open('app/home/views/menu.txt') as file:
        content = file.read()
    
    if user.currentMaze is not None:
        load = '\n|  C - Charger partie'
    
    return user, input(content.format(load))