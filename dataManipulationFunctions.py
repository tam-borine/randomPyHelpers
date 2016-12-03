
def createMatrix(data):
    matrix = []
    for row in data:
        row = row.split(",")
        matrix.append(row)
    return matrix


def buildDict(matrixOfData, colNames):
    aDict = {}
    zippedMatrix = transposeMatrix(matrixOfData) #returns a list of rows
    zippedMatrix.pop(0)
    zippedTable = attachColNamesToColData(zippedMatrix, colNames) #returns a list of cols
    for colData, colName in zippedTable:
        aDict[colName] = colData
    return aDict

def attachColNamesToColData(zippedMatrix, colNames):
    return zip(zippedMatrix, colNames)

def transposeMatrix(matrix):
    return list(zip(*matrixOfData)) #list is necessary for version compatibility issue from 2-3 with this use of zip taking *args

indexOfColNames = 0 #replace this number so it works for your dataset
matrixOfData = createMatrix(data)
colNames = data[indexOfColNames].split(",")
aDict = buildDict(matrixOfData,colNames)
print(aDict)
