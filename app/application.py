# -*- coding: utf-8 -*-
from lib.vendors.model.usermanager import UserManager

from app.home import homecontroller
from app.options import optionscontroller
from app.maze import mazecontroller

class Application:
    """Application class show main menu and define game routes
    
    user : the user object defined to show load option if user has a save maze
    select : the values entered by user during the game
    """
    def __init__(self, user):
        """Define default attributes, user is just a string and become an User instance in run() function"""
        self.user = user
        self.select = ''
        self.error = '\n' + '\033[1;31m' + 'VEUILLEZ SAISIR UNE LETTRE VALIDE !' + '\033[0m'
    
    
    def run(self):
        """Define the game behavior and routes"""
        
        # Show main menu
        self.user, self.select = homecontroller.executeMenu(self.user)
        
        # New game
        if self.select == 'N' or self.select == 'n':
            mazeName, maze, sizeIndex = mazecontroller.selectMaze()
            
            gameOpened = True
            while gameOpened:
                # Reset divisor, move, currentScore and items user attributes if currentMaze is not None and if user is ok with that
                if self.user.currentMaze is not None:
                    select = input('\n' + '\033[1;31m' + 'Vous êtes sur le point de supprimer votre labyrinthe sauvegardé. Voulez-vous vraiment continuer (o/n) ? ' + '\033[0m')
                
                    if select == 'O' or select == 'o':    
                        userManager = UserManager(self.user.name)
                        userManager.resetData()
                    elif select == 'N' or select == 'n':
                        gameOpened = False
                    else:
                        print(self.error)
                        continue
                
                gameOpened = mazecontroller.play(mazeName, maze, self.user.name, sizeIndex)
        
        # Load game if data user contains a saved maze
        elif self.user.currentMaze is not None and (self.select == 'C' or self.select =='c'):
            gameOpened = True
            while gameOpened:
                gameOpened = mazecontroller.play(self.user.currentMaze['mazeName'], self.user.currentMaze['maze'], self.user.name)
        
        # Options menu
        elif self.select == 'O' or self.select == 'o':
            optionsOpened = True
            while optionsOpened:
                optionsOpened = optionscontroller.executeMenu(self.user.name)
        
        # Quit the game
        elif self.select == 'Q' or self.select == 'q':
            select = input('Voulez-vous vraiment quitter la partie (o/n) ? ')
            if select == 'O' or select == 'o':
                print('\n' + '\033[1;35m' + 'Au revoir {0} !'.format(self.user.name) + '\033[0m')
                return False
            elif select == 'N' or select == 'n':
                return True
            else:
                print(self.error)
        else:
            print(self.error)
        
        return True
