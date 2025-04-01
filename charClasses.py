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
    def move(self, board):
        dirs = [(-1,0),(0,-1),(0, 1),(1,0)]
        random.shuffle(dirs)
        dx, dy = dirs[0]
        self.x += dx
        self.y += dy
        
        if not isLegalPlace(self.x,self.y, board):
            self.x -= dx
            self.y -= dy

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
