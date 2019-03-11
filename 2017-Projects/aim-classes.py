import xlrd


#This module allows you to read excel documents. I have never used it before but it came up in possible solutions
#   to the problem with multiple sheets in an excel document preventing it from correctly turning into a .csv
#   This module allows you to parse through, sheet by sheet, and cell by cell for data.


workbook = xlrd.open_workbook('/Users/jameskitchens/Downloads/AIMcourses.xlsx', 'r')


classes = []


#open each sheet individually
for i in range(2,18):
   worksheet = workbook.sheet_by_index(i)
   timeToPrint = False #only want it to print the data that I want
   column = 0  #the first column of the sheet is always full for classes
   for row in range(worksheet.nrows):  #"worksheet.nrows" is the number of rows in the excel document
       if worksheet.cell(row, column).value != xlrd.empty_cell.value:
           if worksheet.cell(row, column).value == "Department":   #"Department" is the key word across all sheets that tells me when to start printing
               timeToPrint = True  #so I set timeToPrint to True
               startPrintRow = row + 1
           if timeToPrint and row >= startPrintRow:
               classes.append(str(worksheet.cell(row, column).value) + str(worksheet.cell(row, column+1).value) + '\t' + str(worksheet.cell(row, column+2).value) + '\t' + str(worksheet.name))    #contains the important data and appends to list


classes.sort()  #sorts, so that all of the same class are right next to one another




outfile = open('/Users/jameskitchens/Downloads/AIMcourses_sorted.txt', 'w')


fullCourse = []


#needed because some courses fulfill multiple AIMs
for i in range(len(classes)):
   course = classes[i].split('\t')
   number = course[0]
   title = course[1]
   aim = course[2]
   objectives = number + '\t' + title + '\t' + aim
   for j in range(1,6):    #assuming that one class fulfills no more than 5 AIMs
       try:
           if number == classes[i+j].split('\t')[0]:   #if class number is the same as the class number in the next line
               objectives += '\t' + classes[i+j].split('\t')[2]    #append the other AIMs fulfilled to end of objectives
           else:
               break
       except:
           break
   outfile.write(objectives + '\n')    #writes everything to outfile


"""

This is the script that I worked on for most of class time. This was my first experience with the model “xlrd” and found its way of parsing through the data to be clunky, though once I discovered the worksheet.nrows and worksheet.ncols values, it made life simpler. xlrd only allows you to parse cell by cell, rather than line by line. Maybe I just wasn’t able to find a better solution, but I had to work with what I found. nrows is the number of rows in the sheet, and ncols is the number of columns. This is much more optimal than saying “always check the first 10 columns and 100 rows” (which results in an error anyways, because of how xlrd reads the file.


Objective of the Script:
----Open a file containing all of the AIMs and classes that fulfill the AIM requirements
----Tell me what AIM(s) the class fulfills


Though this sounds relatively simply, I was unable to find a sheet similar to this on the Warren Wilson website, and there were too many classes to do by hand in a timely manner. So that’s why Python is so nice!


The script creates and writes to a file the class number, the title of the class, and finally the AIMs that it fulfills.
"""
