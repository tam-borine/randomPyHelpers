import csv
import zipfile

fileWithPath = './someDir/someFile' #put your data here
somelist = []

def openCSVAndReadRows(csvFileWithRelativePath):
    fileRows = []
    with open(csvFileWithRelativePath, "r") as file:
        fileRows = file.readlines()
    return fileRows

def writeToTxtFile(somelist): #more lists can be added, ie. a matrix of data
    with open('somefile.txt', "w") as f: #auto migrates
        wtr = csv.writer(f, delimiter=',')
        wtr.writerows([somelist])
    return

def unzip(zipped_dir, dest_dir):
    with zipfile.ZipFile(zipped_dir) as zf:
        zf.extractall(dest_dir)
