fileWithPath = './someDir/someFile' #put your data here

def openCSVAndReadRows(csvFileWithRelativePath):
    fileRows = []
    with open(csvFileWithRelativePath, "r") as file:
        fileRows = file.readlines()
    return fileRows

data = openCSVAndReadRows(fileWithPath)
