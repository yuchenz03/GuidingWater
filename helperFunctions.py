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
    drawLabel(f'You have not collected enough water for our planet!', app.width/2, 200, size=50,
            font='monospace', bold=True, )
    drawLabel(f'Water collected: {app.score} gallons', app.width/2, 200, size=50,
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