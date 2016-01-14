# -*- coding: utf-8 -*-

from lib.vendors.entity.maze import Maze
from lib.vendors.model.mazemanager import MazeManager
from lib.vendors.model.usermanager import UserManager

def selectMaze():
    """Allow user to select a maze"""
    mazeManager = MazeManager()
    error = '\n' + '\033[1;31m' + 'VEUILLEZ SAISIR UN CHIFFRE VALIDE !' + '\033[0m'
    
    with open('app/maze/views/sizes.txt', 'r') as file:
        content = file.read()
    
    # Show sizes menu
    sizesMenuOpened = True
    while sizesMenuOpened:
        # Add custom option if data/maps/4_custom is'nt empty
        if len(mazeManager.maps[3]) > 0:
            custom = '\n|  4 - Labyrinthes personnalisés'
        else:
            custom = ''
        
        sizeIndex = input(content.format(custom))
        
        try:
            sizeIndex = int(sizeIndex)
        except ValueError:
            print(error)
            continue
    
        if sizeIndex > len(mazeManager.sizes) or sizeIndex < 1:
            print(error)
        else:
            sizesMenuOpened = False
        
    # Define mazes menu
    mazes = '\nLabyrinthes de cette catégorie :\n|\n'
    
    for e in mazeManager.maps[sizeIndex - 1]:
        mazes += '|  ' + e.replace('_', ' - ', 1).replace('_', ' ') + '\n'
    
    mazes += '|\nEntrez le chiffre correspondant : '
    
    # Show mazes menu
    mazesMenuOpened = True
    while mazesMenuOpened:
        mazeIndex = input(mazes)
        
        try:
            mazeIndex = int(mazeIndex)
        except ValueError:
            print(error)
            continue
        
        if mazeIndex > len(mazeManager.maps[sizeIndex - 1]) or mazeIndex < 1:
            print(error)
        else:
            mazesMenuOpened = False
    
    maze = mazeManager.getMaze(sizeIndex, mazeIndex)
    
    return maze.name, maze.printMaze(), sizeIndex

def play(nameMaze, maze, userName, sizeIndex=None):
    """Define gameplay and all elements to use in this game"""
    mazeManager = MazeManager()
    userManager = UserManager(userName)
    maze = Maze(nameMaze, maze)
    user = userManager.isRegister()
    error = '\n' + '\033[1;31m' + 'VEUILLEZ SAISIR UNE VALEUR VALIDE (ex : N5 ou Q) !' + '\033[0m'
    
    # Define divisor if sizeIndex is defined
    if sizeIndex == 1:
        user.divisor = 10
    elif sizeIndex == 2:
        user.divisor = 5
    elif sizeIndex == 3:
        user.divisor = 2
    
    # get game interface
    with open('app/maze/views/game.txt', 'r') as file:
        game = file.read()
    
    # Define current maze
    user.currentMaze = {
        'mazeName': maze.name,
        'maze': maze.printMaze(),
    }
    
    allowMove = True
    while allowMove:
        # Define user data with currentMaze and save it to allow user to reload
        data = {
            'score': user.score,
            'gamesPlayed': user.gamesPlayed,
            'bestScores': {
                'Welcome': user.bestScores['Welcome'],
                'Two_ways': user.bestScores['Two_ways'],
                'The_vault': user.bestScores['The_vault'],
                'Ride': user.bestScores['Ride'],
                'Right_or_left': user.bestScores['Right_or_left'],
                'The_bank': user.bestScores['The_bank'],
                'Round-trip': user.bestScores['Round-trip'],
                'The_pyramid': user.bestScores['The_pyramid'],
                'Fort_Knox': user.bestScores['Fort_Knox']
            },
            'divisor': user.divisor,
            'items': user.items,
            'move': user.move,
            'currentScore': user.currentScore,
            'currentMaze': user.currentMaze
        }
    
        userManager.saveData(data)
        
        # Print maze, game informations and allow user to move
        select = input(game.format(maze.printMaze(), user.items, user.move, user.currentScore))
        
        # Quit option
        if select == 'Q' or select == 'q':
            select = input('Voulez-vous vraiment quitter la partie (o/n) ? ')
            if select == 'O' or select == 'o':
                userManager.saveData(data)
                allowMove = False
                return False
            elif select == 'N' or select == 'n':
                continue
            else:
                userManager.saveData(data)
                print('\n' + '\033[1;31m' + 'VEUILLEZ SAISIR UNE LETTRE VALIDE !' + '\033[0m')
                continue
        
        # check select length and define direction and move number
        if len(select) == 1:
            direction = select
            moveNumber = 1
        elif len(select) > 1:
            direction = select[0]
            
            try:
                moveNumber = int(select[1:])
            except ValueError:
                print(error)
                continue
        else:
            print(error)
            continue
        
        # Move user and modify informations
        if direction == 'N' or direction == 'n' or direction == 'E' or direction == 'e' or direction == 'S' or direction == 's' or direction == 'O' or direction == 'o':
            try:
                nbItems, end = maze.move(direction, moveNumber)
            except:
                print('\n' + '\033[1;31m' + 'AÏE ! VOUS VOUS HEURTEZ À UN MUR !' + '\033[0m')
                continue
            else:
                user.items += nbItems
                user.move += moveNumber
                user.currentMaze['maze'] = maze.printMaze()
        else:
            print(error)
            continue
        
        # game end
        if end:
            # Add 20 points and add currentScore to data score
            user.currentScore = user.getCurrentScore()
            user.currentScore += 20
            data['score'] += user.currentScore
            
            # Congratulations message
            message = '\n' + '\033[1;35m' + 'FÉLICITATIONS {0} ! VOUS MARQUEZ {1} POINTS '.format(user.name.upper(), user.currentScore)
            
            # Increment gamesPlayed
            data['gamesPlayed'] += 1
            
            # Modify bestScore if is greater than current score and print message
            if user.currentScore > data['bestScores'][maze.name]:
                data['bestScores'][maze.name] = user.currentScore
                message += 'ET VOUS BATTEZ VOTRE PRÉCÉDENT RECORD !!!'
            else:
                message += '!!!\nMalheureusement, vous ne battez pas votre précédent record : {0} points'.format(data['bestScores'][maze.name])
            
            # print message
            print(message + '\033[0m')
            
            # Save data user and reset it
            userManager.saveData(data)
            userManager.resetData()
            
            return False