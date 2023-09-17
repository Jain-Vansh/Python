# Program that changes the filename of particular type into desired name and organizes the folder
import os

folderPath = input("Enter the folder path: ")
fileType = input("Enter the file type: ").lower()
openFolder = os.listdir(folderPath)

count = 1
for i in openFolder:
    if (i[len(i)-3:len(i)] == fileType):
        os.rename(folderPath+"/"+i, folderPath+"/"+str(count)+".png")
        count+=1