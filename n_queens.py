# n_queens.py

queenCount = 12

def checkConflict(queenList, nextY):
    for posY in range(nextY):
        if abs(queenList[posY]-queenList[nextY])==abs(posY-nextY) or queenList[posY] == queenList[nextY]:
            return True
    return False

count = 0
def putQueen(queenCount, queenList, nextY):
    for queenList[nextY] in range(queenCount):
        if checkConflict(queenList, nextY)==False:
            nextY+=1

            if nextY < queenCount:
                putQueen(queenCount, queenList, nextY)
            else:
                global count
                count+=1
                print(str(count)+": " + ", ".join(str(pos) for pos in queenList))

            nextY-=1

# call the method
queenList = [0] * queenCount
putQueen(queenCount, queenList, 0)
