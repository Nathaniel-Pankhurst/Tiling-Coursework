from graphics import *

def drawLineStartColour(win, yCoord, colour, startx, starty): #draws first line of patch
    for x in range(4):
        x1 = (startx * 100) + (x * 30)
        if x > 0:
            x1 = x1 - 5
        if x == 0 or x == 3: 
            x2 = x1 + 15
        else:
            x2 = x1 + 20
        y1 = (starty * 100) + (yCoord * 20)
        y2 = y1 + 10
        point1 = Point(x1, y1) 
        point2 = Point(x2, y2)
        rectangle = Rectangle(point1, point2)
        rectangle.setFill(colour)
        rectangle.draw(win)
    
def drawLineStartWhite(win, yCoord, colour, startx, starty): #draws second line of patch
    for x in range(3):
        x1 = (startx * 100) + (x * 30) + 10
        x2 = x1 + 20
        y1 = (starty * 100) + ((yCoord) * 20) + 10
        y2 = y1 + 10
        point1 = Point(x1, y2)
        point2 = Point(x2, y1)
        rectangle2 = Rectangle(point1, point2)
        rectangle2.setFill(colour)
        rectangle2.draw(win)
        
def patch1(win, colour, startx, starty): #draws the patch by alternating between the first and second lines of the patch as it goes down the patch.
     for y in range(5):
         drawLineStartColour(win, y, colour, startx, starty)
         drawLineStartWhite(win, y, colour, startx, starty)
        
def patch2(win, colour, startX, startY): #draws the second patch two lines at a time
    for coordinate in range(10):
        stepper = coordinate * 10
        point1A = Point((startX * 100) + stepper, (startY * 100))
        point1B = Point(((startX + 1) * 100), (startY * 100) + stepper)
        point2A = Point((startX) * 100, (startY * 100) + stepper)
        point2B = Point((startX * 100) + stepper, (startY + 1) * 100)
        line1 = Line(point1A, point1B)
        line2 = Line(point2A, point2B)
        line1.draw(win)
        line2.draw(win)
        line1.setFill(colour)
        line2.setFill(colour)
        
def colourCreation(): #Prompts the user to enter the colour patterns for the patches on the grid, then returns the value to main() so that these colours can be passed into the patch drawing functions, creating the patterns on the graphics window.
    patchColour = []
    colourStepper = 0
    while not (colourStepper >= 4):
        colourInput = input("Enter a colour: ")
        colourInput = colourInput.lower()
        if colourInput in ["red", "blue", "green", "magenta", "yellow", "cyan"]:

            patchColour.append(colourInput)
            colourStepper = colourStepper + 1
        else: 
            print("The colour you entered is invalid")
    return patchColour

def patchDraw(win, colour, x, y, gridSize):    
    if x <= 2  and y >= (gridSize - 3):
        patch2(win, colour, x, y)
    else: 
        patch1(win, colour, x, y)

def main(): # This is the main function, where every process is called, and validation checks are made.
    colourList = []
    patchList = []
    colourStepper2 = 0
    startVerify = False
    while not startVerify:
        gridSize = input("What size shall the grid be? (5, 7, or 9): ")
        if gridSize not in ["5", "7", "9"]:
            print("This is an invalid input")
        else:
            gridSize = eval(gridSize)
            startVerify = True
    colourList = colourCreation()
    winSize = gridSize * 100
    win = GraphWin("Patches, patches, patches", winSize, winSize)
    background = Rectangle(Point(0,0), Point(winSize, winSize))
    background.setFill("White")
    background.draw(win)
    for y in range(gridSize):
        for x in range(gridSize):
            patchDraw(win, colourList[colourStepper2], x, y, gridSize)
            patchList.append(colourStepper2)
            colourStepper2 = colourStepper2 + 1
            if colourStepper2 > 3:
                colourStepper2 = 0
    endRun = False
    while not endRun:
        patchCount = 0
        squarePoint = win.getMouse()
        x = squarePoint.getX()
        y = squarePoint.getY()
        pointX = x // 100
        pointY = y // 100
        for yColour in range(gridSize):
            for xColour in range(gridSize):
                if yColour == pointY and xColour == pointX:
                    print(patchCount)
                    patchList[patchCount] = patchList[patchCount] + 1
                    if patchList[patchCount] >= 4:
                        patchList[patchCount] = 0
                    patchDraw(win, colourList[patchList[patchCount]], pointX, pointY, gridSize)
                else:
                    patchCount = patchCount + 1
main()
  
        
        
    
            
                
    

