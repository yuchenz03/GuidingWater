from cmu_graphics import *
import random, math, copy
from PIL import Image
import os, pathlib


'''
Sources:
    Bubbles emoji: https://emojipedia.org/apple/ios-15.4/bubble
    alien emoji: https://emojipedia.org/apple/ios-14.2/alien-monster
    earth emoji: https://emojipedia.org/globe-showing-americas
    snowflake emoji: https://emojipedia.org/snowflake
    
'''
#################################
### All the character classes ###

class alien:
    def __init__(self, startX, startY, board):
        self.x = startX
        self.y = startY
        self.type = alien
    
    def getPos(self):
        return (self.x, self.y)
    
    #the alien moves freely around the board regardless of walls
    def move(self, app):
        print(self.x, self.y)
        dirs = [(-1,0),(0,-1),(0, 1),(1,0)]
        random.shuffle(dirs)
        dx, dy = dirs[0]
        self.x += dx
        self.y += dy
        
        if not isLegalPlace(self.x,self.y, app.board):
            self.x -= dx
            self.y -= dy
            # self.move(app)

def isLegalPlace(newx, newy, board):
    if newy <= 0 or newy >= len(board)-1:
        return False
    if newx <= 0 or newx >= len(board[0])-1:
        return False
    return True

class player:
    def __init__(self, startX, startY, board):
        self.color = 'orange'
        self.x = startX
        self.y = startY
        self.board = board
        self.type = alien
    
    def getPos(self):
        return (self.x, self.y)
    

class collectibles:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.taken = False
    
    def getPos(self):
        return (self.x, self.y)



#################################
### All draw helper functions ###

#drawing the menu page
def drawMainMenu(app):
    lightblue = rgb(204, 229, 255)
    drawRect(0, 0, 1500, 800, fill = lightblue)
    drawLabel(f'G u i d i n g   W a t e r', app.width/2, 100, size=50,
            font='monospace', bold=True, )
    grey = rgb(192, 192, 192)
    drawRect(150, 300, 1200, 100, fill = grey)
    drawLabel(f'LEVELS', app.width/2, 350, size=50,
            font='monospace', bold=True, )
    drawRect(150, 500, 1200, 100, fill = grey)
    drawLabel(f'HOW TO PLAY', app.width/2, 550, size=50,
            font='monospace', bold=True, )

#Drawing the game page
def drawGame(app, board):
    lightblue = rgb(204, 229, 255)
    drawRect(0, 0, 1500, 800, fill = lightblue)
    drawLabel(f'Difficulty: {app.difficulty}', app.width/2, 60, size=25,
            font='monospace', bold=True)
    drawLabel(f'Score: {app.score}', app.width/2, 80, size=25,
            font='monospace', bold=True)
    drawRect(25, 50, 100, 50, fill = 'grey')
    drawLabel('Back', 75, 75, size=30, font='monospace', bold=True)
    
    drawBoard(app)
    drawBoardBorder(app)

#Drawing how to play page
def drawHTP(app):
    lightblue = rgb(204, 229, 255)
    drawRect(0, 0, 1500, 800, fill = lightblue)
    drawRect(25, 50, 100, 50, fill = 'grey')
    drawLabel('Back', 75, 75, size=30, font='monospace', bold=True)
    drawLabel(f'How to Play:', app.width/2, 200, size=50,
            font='monospace', bold=True)
    drawLabel(f'Guide our planet through this foreign galaxy and collect the extra water',app.width/2, 400, size=30,
            font='monospace', bold=True)
    drawLabel(f'(bubbles and snowflakes) floating around to save our planet!',app.width/2, 430, size=30,
            font='monospace', bold=True)
    drawLabel(f'Snowflakes contain more water than bubbles!',app.width/2, 460, size=30,
            font='monospace', bold=True)
    drawLabel(f'Be wary of the aliens that are trying to defend their resources!',app.width/2, 490, size=30,
            font='monospace', bold=True)

#Drawing the levels page
def drawLevels(app):
    lightblue = rgb(204, 229, 255)
    drawRect(0, 0, 1500, 800, fill = lightblue)
    drawRect(25, 50, 100, 50, fill = 'grey')
    drawLabel('Back', 75, 75, size=30, font='monospace', bold=True)
    grey = rgb(192, 192, 192)
    drawRect(150, 150, 1200, 100, fill = grey)
    drawLabel(f'EASY', app.width/2, 200, size=50,
            font='monospace', bold=True, )
    drawRect(150, 350, 1200, 100, fill = grey)
    drawLabel(f'MEDIUM', app.width/2, 400, size=50,
            font='monospace', bold=True)
    drawRect(150, 550, 1200, 100, fill = grey)
    drawLabel(f'HARD', app.width/2, 600, size=50,
            font='monospace', bold=True)
    
def drawAliens(app):
    for alien in app.aliens:
        row, col = alien.getPos()
        cellLeft, cellTop = getCellLeftTop(app, row, col)
        cellWidth, cellHeight = getCellSize(app)
        newWidth, newHeight = (cellWidth,cellHeight)
        drawImage(app.alien,cellLeft,cellTop,width=newWidth,height=newHeight)
    
def drawCollectibles(app):
    for bubble in app.bubbles:
        row, col = bubble.getPos()
        cellLeft, cellTop = getCellLeftTop(app, row, col)
        cellWidth, cellHeight = getCellSize(app)
        newWidth, newHeight = (cellWidth,cellHeight)
        drawImage(app.bubble,cellLeft,cellTop,width=newWidth,height=newHeight)
    for snow in app.snows:
        row, col = snow.getPos()
        cellLeft, cellTop = getCellLeftTop(app, row, col)
        cellWidth, cellHeight = getCellSize(app)
        newWidth, newHeight = (cellWidth,cellHeight)
        drawImage(app.snowflake,cellLeft,cellTop,width=newWidth,height=newHeight)
    

def drawPlayer(app):
    row, col = app.player.getPos()
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    newWidth, newHeight = (cellWidth,cellHeight)
    drawImage(app.earth,cellLeft,cellTop,width=newWidth,height=newHeight)

def displayWinMessage(app):
    drawRect(150, 150, 1200, 200, fill = 'green')
    drawLabel(f'Congratulations! You have saved our planet!', app.width/2, 200, size=30,
            font='monospace', bold=True, )
    drawLabel(f'Water collected: {app.score} gallons', app.width/2, 250, size=30,
            font='monospace', bold=True, )
    drawLabel(f'Press back to return to the main menu', app.width/2, 300, size=30,
            font='monospace', bold=True, )
    
def displayLoseMessage(app):
    drawRect(150, 150, 1200, 200, fill = 'red')
    drawLabel(f'You have not collected enough water for our planet!', app.width/2, 200, size=30,
            font='monospace', bold=True, )
    drawLabel(f'Water collected: {app.score} gallons', app.width/2, 250, size=30,
            font='monospace', bold=True, )
    drawLabel(f'Press back to return to the main menu', app.width/2, 300, size=30,
            font='monospace', bold=True, )

#################################
### All mouse helper functions ###
# Mouse helper for main menu
def mouseMainMenu(app, mouseX, mouseY):
    #If the player wants to play the game:
    if 150 <= mouseX <=  1350 and 300 <= mouseY <= 400:
        app.prevPage = app.page
        app.page = 'levels'
    #If the player wants to see how to play
    if 150 <= mouseX <=  1350 and 500 <= mouseY <= 600:
        app.prevPage = app.page
        app.page = 'HTP'

#Mouse helper for levels page
def mouseLevels(app, mouseX, mouseY):
    #If the player wants to play the game:
    if 150 <= mouseX <=  1350 and 150 <= mouseY <= 250:
        app.difficulty = 'Easy'
        app.prevPage = 'levels'
        app.page = 'game'
    #If the player wants to see how to play
    if 150 <= mouseX <=  1350 and 350 <= mouseY <= 450:
        app.difficulty = 'Medium'
        app.prevPage = 'levels'
        app.page = 'game'
    if 150 <= mouseX <=  1350 and 550 <= mouseY <= 650:
        app.difficulty = 'Hard'
        app.prevPage = 'levels'
        app.page = 'game'




#################################
### Drawing the board functions ###
# create an initial board with all borders drawn in
def initialBoard(height, width):
    board = [['w' if row%2 == 0 else 'c' for row in range(width)] if col%2 == 1 else ['w' for row in range(width)] for col in range(height)]
    return board

# function to create the maze
def createBoard(rows, cols, board):
    initial = initialBoard(rows, cols)
    numOfCells = rows*cols
    #first, let us define a starting point on the left wall
    startcol = 0
    startrow = 2*random.randint(1, (rows-2)//2)+1
    board[startrow][startcol] = 'c'
    
    #Then, let us create the board recursively using backtracking.
    backtracker((startrow, startcol+1), set(), numOfCells, board)
    
    #then, let us define an ending point on the right wall
    potentialEndRow = []
    for i in range(len(board)):
        if board[i][len(board[0])-2] == 'c':
            potentialEndRow.append(i)
    
    random.shuffle(potentialEndRow)
            
    endcol = len(board[0])-1
    endrow = potentialEndRow[0]
    board[endrow][endcol] = 'c'
    return (startrow, startcol, endrow, endcol)

# scrambles all the possible directions
def scrambleDirs():
    dirs = [(-1,0),(0,-1),(0, 1),(1,0)]
    random.shuffle(dirs)
    return dirs

#mutating function that mutates board
def backtracker(location, visited, numOfCells, board):
    if len(visited) == numOfCells:
        return None
    row, col = location
    visited.add(location)
    dirs = scrambleDirs()
    for (dx, dy) in dirs:
        newrow = row + 2*dx
        newcol = col + 2*dy
        if isLegal(newrow, newcol, visited, board):
            wallToCell(row, col, newrow, newcol, board)
            backtracker((newrow, newcol), visited, numOfCells, board)    
    return None

def wallToCell(x, y, x1, y1, board):
    row = (x+x1)//2
    col = (y+y1)//2
    board[row][col] = 'c'

#checks if a location is legal
def isLegal(row, col, visited, board):
    if row <= 0 or row >= len(board)-1:
        return False
    if col <= 0 or col >= len(board[0])-1:
        return False
    if (row, col) in visited:
        return False
    return True

def drawBoard(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col] == 'w':
                color = 'black'
            elif app.board[row][col] == 'c':
                color = 'lightblue'
            drawCell(app, row, col, color)

def drawBoardBorder(app):
# draw the board outline (with double-thickness):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
        fill=None, border='black',
        borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
            fill=color, border='black',
            borderWidth=app.cellBorderWidth)

def getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
        return (row, col)
    else:
        return None

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def getDifficulty(app):
    if app.difficulty == 'Hard':
        app.rows = 31
        app.cols = 59
        app.bubblesNum = 10
        app.snowNum = 4
        app.alienNum = 6
    elif app.difficulty == 'Medium':
        app.rows = 21
        app.cols = 41
        app.bubblesNum = 7
        app.snowNum = 3
        app.alienNum = 4
    elif app.difficulty == 'Easy':
        app.rows = 17
        app.cols = 29
        app.bubblesNum = 4
        app.snowNum = 2
        app.alienNum = 3
        
        
#################################
### Default functions for cmu graphics ###

def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def resetApp(app):
    app.width = 1500
    app.height = 800
    app.difficulty = None
    app.prevPage = 'mainMenu'
    app.page = 'mainMenu'
    app.board = None
    app.bubblesNum = 0
    app.snowNum = 0
    app.alienNum = 0
    app.rows = None
    app.cols = None
    app.count = 0
    app.countSteps = 0
    app.playing = False
    app.score = 0
    app.won = None
    app.lost = None
    
    #player details
    app.playerRow = None
    app.playerCol = None
    
    
    #opening each of the images. Sources cited at top of file.
    app.earth = openImage("images/earth.png")
    app.snowflake = openImage("images/snowflake.png")
    app.alien = openImage("images/alien.png")
    app.bubble = openImage("images/bubbles.png")
    app.bubble = CMUImage(app.bubble)
    app.earth = CMUImage(app.earth)
    app.snowflake = CMUImage(app.snowflake)
    app.alien = CMUImage(app.alien)
    
def onAppStart(app):
    resetApp(app)

def onStep(app):
    app.countSteps += 1
    if app.page == 'game' and app.count == 0:
        app.count += 1
        getDifficulty(app)
        #app functions
        app.width = 1500
        app.height = 800
        
        app.boardLeft = 120
        app.boardTop = 120
        app.boardWidth = 1260
        app.boardHeight = 630
        
        #cell dimensions
        app.cellBorderWidth = 0.05
        app.mazeBorderWidth = 1
        
        board = initialBoard(app.rows, app.cols)
        (startrow, startcol, endrow, endcol) = createBoard(app.rows, app.cols, board)
        app.board = board
        app.endrow, app.endcol = endrow, endcol
        
        app.player = player(startrow, startcol, board)
        app.bubbles = []
        while len(app.bubbles) <= app.bubblesNum:
            row = random.randint(1, len(board)-1)
            col = random.randint(1, len(board[0])-1)
            if board[row][col] == 'c':
                app.bubbles.append(collectibles(row, col, 'bubble'))
        
        app.snows = []
        while len(app.snows) <= app.snowNum:
            row = random.randint(1, len(board)-1)
            col = random.randint(1, len(board[0])-1)
            if board[row][col] == 'c':
                app.snows.append(collectibles(row, col, 'snow'))

        app.aliens = []
        while len(app.aliens) < app.alienNum:
            row = random.randint(1, len(board)-1)
            col = random.randint(1, len(board[0])-1)
            if board[row][col] == 'c':
                app.aliens.append(alien(row, col, app.board))

        app.playing = True
    
    if app.playing == True:
        if app.countSteps % 30 == 0:
            for a in app.aliens:
                print("not me")
                a.move(app)
        playGame(app)

def playGame(app):
    playerx, playery = app.player.getPos()
    #If the player reaches the end of the maze, they win
    if (playerx, playery) == (app.endrow, app.endcol):
        app.won = True
        app.playing = False
    #if the collectibles are passed through, they disappear
    for bubble in app.bubbles:
        row, col = bubble.getPos()
        if (playerx, playery) == (row,col):
            app.bubbles.remove(bubble)
            app.score += 10
    for snow in app.snows:
        row, col = snow.getPos()
        if (playerx, playery) == (row,col):
            app.snows.remove(snow)
            app.score += 20
    #If the player is touched by an alien, their score decreases.
    for alien in app.aliens:
        row, col = alien.getPos()
        if (playerx, playery) == (row,col):
            app.score -= 10 #however, simply doing this will cause the score
            #to decrease multiple times if the alien touches the player
            #Decreasing app.stepsPerSecond will cause the collectibles to 
            #disappear a lot later than it should
            #SO what do I doooooo
    

        

def redrawAll(app):
    if app.page == 'mainMenu':
        drawMainMenu(app)
    elif app.page == 'levels':
        drawLevels(app)
    elif app.page == 'game' and app.board != None:
        drawGame(app, app.board)
        drawCollectibles(app)
        drawAliens(app)
        drawPlayer(app)
        if app.playing == False and app.won == True and app.score > 0:
            displayWinMessage(app)
        elif app.lost == True:
            displayLoseMessage(app)
        elif app.playing == False and app.won == True and app.score < 0:
            displayLoseMessage(app)
    elif app.page == 'HTP':
        drawHTP(app)

def onMousePress(app, mouseX, mouseY):
    if app.page == 'mainMenu':
        mouseMainMenu(app, mouseX, mouseY)
    elif app.page == 'levels':
        mouseLevels(app, mouseX, mouseY)
    elif app.page == 'game':
        if 25 <= mouseX <= 125 and 50 <= mouseY <= 100:
            resetApp(app)

    if 25 <= mouseX <= 125 and 50 <= mouseY <= 100:
        app.page = app.prevPage
        app.prevPage = 'mainMenu'

def legalPlayerMove(app, newy, newx):
    if app.board[newy][newx] == 'c':
        return True
    if newy <= 0 or newy >= len(app.board)-1:
        return False
    if newx <= 0 or newx >= len(app.board[0])-1:
        return False
    if app.board[newy][newx] != 'c':
        return False
    return True

#Moving the player
def onKeyPress(app, key):
    if app.playing == True:
        origx, origy = app.player.getPos()
        if key == "left": app.player.y -= 1
        if key == "right": app.player.y += 1
        if key == "down": app.player.x += 1
        if key == "up": app.player.x -= 1
        x,y = app.player.getPos()
        if not legalPlayerMove(app,x,y):
            app.player.x = origx
            app.player.y = origy

def main():
    runApp()

main()

