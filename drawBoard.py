#################################
### Drawing the board functions ###
'''
The sources that I used when doing this problem are:
https://www.cs.cmu.edu/~112/notes/student-tp-guides/Mazes.pdf
https://en.wikipedia.org/wiki/Maze_generation_algorithm
https://www.youtube.com/watch?v=sVcB8vUFlmU
https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking

'''
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
    elif app.difficulty == 'Medium':
        app.rows = 21
        app.cols = 41
        app.bubblesNum = 7
        app.snowNum = 3
    elif app.difficulty == 'Easy':
        app.rows = 17
        app.cols = 29
        app.bubblesNum = 4
        app.snowNum = 2
        
        
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
    app.rows = None
    app.cols = None
    app.count = 0
    app.countSteps = 0
    app.playing = False
    # app.stepsPerSecond = 2
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
        while len(app.aliens) < 3:
            row = random.randint(1, len(board)-1)
            col = random.randint(1, len(board[0])-1)
            if board[row][col] == 'c':
                app.aliens.append(alien(row, col, app.board))

        app.playing = True
    
    if app.playing == True:
        if app.countSteps % 30 == 0:
            for a in app.aliens:
                a.move(app.board)
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
            app.score -= 10
    

        

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