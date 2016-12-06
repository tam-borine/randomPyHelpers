
def getNumberOfFilesWhoseNamesContain(substr):
   count = 0
   for file in listOfFiles:
       if substr in file:
           count += 1
   return count


def getNumberOfFilesContainingForEachIn(listOfDates)
   dict = {}
   for date in listOfDates:
       dict[date] = getNumberOfFilesWhoseNamesContain(date) #defined above
   return dict
