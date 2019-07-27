# n_queens.py

queenCount = 12

def checkConflict(nextY):
    for posY in range(nextY):
        if abs(queenList[posY]-queenList[nextY])==abs(posY-nextY) or queenList[posY] == queenList[nextY]:
            return True
    return False

count = 0
def putQueen(nextY):
    for queenList[nextY] in range(queenCount):
        if checkConflict(nextY)==False:
            nextY+=1

            if nextY < queenCount:
                putQueen(nextY)
            else:
                global count
                count+=1
                print(str(count)+": " + ", ".join(str(pos) for pos in queenList))

            nextY-=1

# call the method
queenList = [0] * queenCount
putQueen(0)
