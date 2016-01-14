# -*- coding: utf-8 -*-

from app.home import homecontroller
from app.application import Application



# home page
homePageOpened = True
while homePageOpened:
    user = homecontroller.executeHome()
    
    if user != '':
        print('\n' + '\033[1;35m' + 'Bienvenue {} !'.format(user) + '\033[0m')
        homePageOpened = False
    else:
        print('\n' + '\033[1;31m' + 'ENTREZ VRAIMENT UN PSEUDO !' + '\033[0m')

# game
gameOpened = True
while gameOpened:
    app = Application(user)
    gameOpened = app.run()