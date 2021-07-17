from turtle import *
import time
#####GLOBAL VARIABLES#####
squareSize = 50
arrSize = 12


mazeArr = [[0 for j in range(arrSize* 3)] for i in range(arrSize * 3)]
pathArr = mazeArr
speed(0)
count = 1
endNum = (arrSize * 3) - 1
startMid = int(arrSize / 2 - 1) * 3
mid1 = startMid + 1
mid2 = startMid + 4

start = [1,1]
end = [1,10]

#####ARRAY METHODS#####

def setStart(y,x):
    global start
    start[0] = (1 + y*3)
    start[1] = (1+ x*3)

def setEnd(y,x):
    global end
    end[0] = (1 + y*3)
    end[1] = (1 + x*3)

def setupArr(arr):
    endNum = (arrSize * 3) - 1
    startMid = int(arrSize / 2 - 1) * 3
    for arrY in range(len(arr)):
        for arrX in range(len(arr[0])):
            if (arr[arrY][arrX] != -9 and arr[arrY][arrX] != -8):
                #MIDDLE
                if ((arrY >= startMid and arrY <= startMid + 5 or arrY >= startMid and arrY <= startMid + 5)
                    and (arrX >= startMid and arrX <= startMid + 5 or arrX >= startMid and arrX <= startMid + 5)):
                    arr[arrY][arrX] = -1
                #GREEN OF MAZE
                else:
                    arr[arrY][arrX] = 0    
                #ROWS & COLUMNS
                if (arrX % 3 == 1 or arrY % 3 == 1):
                    if (arrX % 3 == 1 and arrY % 3 == 1):
                        arr[arrY][arrX] = -3
                    else:
                        arr[arrY][arrX] = -2
                #EDGES OF MAP
                if ((arrX == 0 or arrX == endNum and arrY >= 0 and arrY <= endNum) or
                    (arrY == 0 or arrY == endNum and arrX >= 0 and arrX <= endNum)):
                    arr[arrY][arrX] = 0
                #CORNER
                arr[endNum][0] = -1
                arr[endNum][1] = -1
                arr[endNum][2] = -1
                arr[endNum - 1][0] = -1
                arr[endNum - 2][0] = -1
                arr[endNum - 2][2] = -1
                #START AND END POINTS
                arr[start[0]][start[1]] = 1
                arr[mid1][mid1] = -5
                arr[mid2][mid1] = -5
                arr[mid2][mid2] = -5
                arr[mid1][mid2] = -5
                if (end[0] != -1 and end[1] != -1):
                    arr[end[0]][end[1]] = -5

def printArr(arr):
    row = ""
    for arrY in range(len(mazeArr)):
        for arrX in range(len(mazeArr[0])):
            if (mazeArr[arrY][arrX] == 0):
                row = row + "   "
            elif (mazeArr[arrY][arrX] >= 0 and mazeArr[arrY][arrX] <= 9):
                row = row + "  " + str(mazeArr[arrY][arrX])
            else:
                row = row + " " + str(mazeArr[arrY][arrX])

        print(row)
        print()
        row = ""

def testArrRows(arr):
    for arrY in range(len(mazeArr)):
        for arrX in range(len(mazeArr[0])):
            arr[arrY][arrX] = arrX

def setVWall(y,x, arr):
    arr[y * 3 - 2][x * 3 - 1] = -8
    arr[y * 3 - 2][x * 3] = -8

def setHWall(y,x, arr):
    arr[y * 3 - 1][x * 3 - 2] = -8
    arr[y * 3][x * 3 - 2] = -8

def setMaze1(arr):
    setVWall(1,11, pathArr)
    setVWall(2,1,pathArr)
    setVWall(2,2,pathArr)
    setVWall(2,3,pathArr)
    setVWall(2,11,pathArr)
    setVWall(3,2,pathArr)
    setVWall(3,10,pathArr)
    setVWall(3,11,pathArr)
    setVWall(4,2,pathArr)
    setVWall(4,3,pathArr)
    setVWall(4,6,pathArr)
    setVWall(4,9,pathArr)
    setVWall(4,10,pathArr)
    setVWall(5,1,pathArr)
    setVWall(5,3,pathArr)
    setVWall(5,4,pathArr)
    setVWall(5,6,pathArr)
    setVWall(5,10,pathArr)
    setVWall(5,1,pathArr)
    setVWall(6,4,pathArr)
    setVWall(6,7,pathArr)
    setVWall(6,8,pathArr)
    setVWall(7,1,pathArr)
    setVWall(7,3,pathArr)
    setVWall(7,5,pathArr)
    setVWall(7,7,pathArr)
    setVWall(7,8,pathArr)
    setVWall(7,9,pathArr)
    setVWall(7,10,pathArr)
    setVWall(8,4,pathArr)
    setVWall(8,8,pathArr)
    setVWall(8,9,pathArr)
    setVWall(8,10,pathArr)
    setVWall(8,11,pathArr)
    setVWall(9,1,pathArr)
    setVWall(9,7,pathArr)
    setVWall(9,8,pathArr)
    setVWall(9,11,pathArr)
    setVWall(10,7,pathArr)
    setVWall(10,11,pathArr)
    setVWall(11,2,pathArr)
    setVWall(11,3,pathArr)
    setVWall(11,11,pathArr)
    setVWall(12,1,pathArr)
    setHWall(2,1, pathArr)
    setHWall(2,4, pathArr)
    setHWall(2,5, pathArr)
    setHWall(2,6, pathArr)
    setHWall(2,7, pathArr)
    setHWall(2,8, pathArr)
    setHWall(2,9, pathArr)
    setHWall(2,10, pathArr)
    setHWall(3,1, pathArr)
    setHWall(3,3, pathArr)
    setHWall(3,4, pathArr)
    setHWall(3,5, pathArr)
    setHWall(3,6, pathArr)
    setHWall(3,7, pathArr)
    setHWall(3,8, pathArr)
    setHWall(3,9, pathArr)
    setHWall(3,11, pathArr)
    setHWall(4,2, pathArr)
    setHWall(4,5, pathArr)
    setHWall(4,8, pathArr)
    setHWall(5,3, pathArr)
    setHWall(5,6, pathArr)
    setHWall(5,7, pathArr)
    setHWall(5,11, pathArr)
    setHWall(6,3, pathArr)
    setHWall(6,4, pathArr)
    setHWall(6,10, pathArr)
    setHWall(6,11, pathArr)
    setHWall(6,12, pathArr)
    setHWall(7,2, pathArr)
    setHWall(7,4, pathArr)
    setHWall(7,6, pathArr)
    setHWall(7,7, pathArr)
    setHWall(8,2, pathArr)
    setHWall(8,3, pathArr)
    setHWall(8,5, pathArr)
    setHWall(8,6, pathArr)
    setHWall(8,7, pathArr)
    setHWall(9,1, pathArr)
    setHWall(9,3, pathArr)
    setHWall(9,4, pathArr)
    setHWall(9,5, pathArr)
    setHWall(9,6, pathArr)
    setHWall(9,7, pathArr)
    setHWall(9,9, pathArr)
    setHWall(9,10, pathArr)
    setHWall(9,11, pathArr)
    setHWall(10,1, pathArr)
    setHWall(10,2, pathArr)
    setHWall(10,4, pathArr)
    setHWall(10,5, pathArr)
    setHWall(10,6, pathArr)
    setHWall(10,8, pathArr)
    setHWall(10,9, pathArr)
    setHWall(10,10, pathArr)
    #
    #setHWall(11,3, pathArr)
    setHWall(11,5, pathArr)
    setHWall(11,6, pathArr)
    setHWall(11,7, pathArr)
    setHWall(11,8, pathArr)
    setHWall(11,9, pathArr)
    setHWall(11,10, pathArr)
    setHWall(11,11, pathArr)
    #
    #setHWall(11,4, pathArr)
    

    
#####PATHFINDING METHODS#####

def findPath(arr):
    count = 1
    #WHILE END POINTS ARE NOT FOUND
    while ( arr[mid1][mid1] == -5 and arr[startMid + 4][mid1] == -5 and
            arr[startMid + 4][startMid + 4] == -5 and arr[mid1][startMid + 4] == -5):

        #LOOK IN ARRAY FOR PLACES THAT NEED TO POPULATE
        for r in range (0, len(arr) - 1):
            for c in range (0, len(arr[0]) - 1):
                if(arr[r][c] == count):
                    
                    #print("FOUND" + str(count))
                    #LOOK FOR PATH TO POPULATE 
                    if (arr[r][c + 1] == -2 or arr[r][c + 1] == -3 or arr[r][c + 1] == -5):
                        arr[r][c + 1] = (count + 1)
                            
                    if (arr[r][c - 1] == -2 or arr[r][c - 1] == -3 or arr[r][c - 1] == -5):
                        arr[r][c - 1] = (count + 1)
                                            
                    if (arr[r - 1][c] == -2 or arr[r - 1][c] == -3 or arr[r - 1][c] == -5):
                        arr[r - 1][c] = (count + 1)
                                  
                    if (arr[r + 1][c] == -2 or arr[r + 1][c] == -3 or arr[r + 1][c] == -5):
                        arr[r + 1][c] = (count + 1)
   
                    if ( arr[mid1][mid1] != -5 or arr[mid2][mid1] != -5 or
                        arr[mid2][mid2] != -5 or arr[mid1][mid2] != -5):
                        printArr(arr)
                        count = count + 1
                        arr = traceBack(arr, count)
                        return(arr)
                        break
                    
        if (count % 8 == 0):
            drawGrid(arr)
            update()
        count = count + 1
    return(arr) 


def traceBack(arr, count):
    endX = 0
    endY = 0
    if (arr[mid1][mid1] == count):
        endY = mid1; endX = mid1
    elif (arr[mid2][mid1] == count):
        endY = mid2; endX = mid1
    elif (arr[mid2][mid2] == count):
        endY = mid2; endX = mid2
    elif (arr[mid1][mid2] == count):
        endY = mid1; endX = mid2

    
    while (arr[endNum - 1][1] == 1 and count >= -1):
        count = count - 1
        if (count % 8 == 0):
            drawGrid(arr)
            update()
        if (arr[endY][endX + 1] == count ):
            arr[endY][endX + 1] = -9
            endX = endX + 1
            
        elif (arr[endY][endX - 1] == count ):
            arr[endY][endX - 1] = -9
            endX = endX - 1
            
        elif (arr[endY - 1][endX] == count ):
            arr[endY - 1][endX] = -9
            endY = endY - 1
            
        elif (arr[endY + 1][endX] == count ):
            arr[endY + 1][endX] = -9
            endY = endY + 1
    setupArr(arr)
    
    return(arr)


#####DRAW METHODS#####
def drawGrid(gridSize, size, thickness, fill):
    width(thickness)
    penup()
    xPos = -squareSize * 5
    yPos = -squareSize * 5
    setx(xPos)
    sety(yPos)
    pendown()
    for y in range (0,gridSize):
        for x in range (0,gridSize):
            drawSquare(x, y, size, fill)

def drawLargeGrid():
    width(5)
    penup()
    pendown()
    for y in range (0, int(arrSize)):
        for x in range (0, int(arrSize)):
            drawLargeSquare(x, y)

def drawSmallGrid(arr):
    width(1)
    penup()
    pendown()
    for y in range (0, arrSize * 3):
        for x in range (0, arrSize * 3):
            drawSmallSquare(x, y, arr)
 
def drawLargeSquare(x,y):
    penup()
    setx(-(arrSize / 2) * squareSize + (x * squareSize))
    sety(((arrSize / 2) * squareSize) - (y * squareSize))
    pendown()
    for loop in range (0,4):
        forward(squareSize)
        right(90)

def drawSmallSquare(x,y, arr):
    penup()
    setx((-(arrSize / 2 * 3) * squareSize / 3) + (x * squareSize / 3))
    sety(((arrSize / 2 * 3 -1) * squareSize / 3) - (y * squareSize / 3))
    pendown()
    #color("black","blue")
    setColor(x,y, arr)
    begin_fill()
    for loop in range (0,4):
        forward(squareSize / 3)
        left(90)
    end_fill()        


def setColor(arrX,arrY,arr):
    sqColor = arr[arrY][arrX]
    if (sqColor == -1):
       color("black", "yellow")
    elif (sqColor == -2):
        color("black","orange")
    elif (sqColor == -3):
        color("black","orange")
    elif (sqColor == -5 or sqColor == 1 or sqColor > 1):
        color("black","blue")
    elif (sqColor == -8 ):
        color("black","black")
    elif (sqColor == -9 ):
        color("black","red")
    else:
        color("black", "green")

def drawGrid(arr):
    drawSmallGrid(arr)
    drawLargeGrid()
    
#####ROBOT METHODS#####
        
#def drawRobot(x,y, rot):
    #Will eventually draw robot



#####MAIN######
def main():
    tracer(0, 0)
    #SETUP ARRAYS
    setupArr(mazeArr)
    pathArr = mazeArr
    
    setStart(0,11)

    setMaze1(pathArr)
    drawGrid(pathArr)
    #time.sleep(3)
    #printArr(arr)
    pathArr = findPath(pathArr)
    drawGrid(pathArr)
    
    #RESET TURTLE AND UPDATE
    setx(0)
    sety(0)
    update()
    #TEST ARRAY TO SEE NUMBERS
    #printArr(pathArr)
    

#RUNS MAIN
main()
