import os
import shutil
import sys

sFileTypes = open("ShortExtensionList.txt").read().splitlines()
sUserDestination = input(r"Where do you want to put the located files? For Example, 'C:\Users\YourUsername\Desktop\NewFolder' without quotes: ")
sUserInput = input("Enter the drive you want to scan. For example, 'C:' without quotes: ")
sUserNamedLog = input("Name your log, so you know what it's called. For example, 'MyLog.txt' without quotes. It will be located in the same folder as this program. You'll need this to reference the original file paths: ")

#sUserLogDestination = input(r"Make a .txt file and provide its location for the log. For example, 'C:\Users\YourUsername\Desktop\NewFolder\Log.txt': ")

sFileToStartScan = r"" + sUserInput 
for root, dirs, files in os.walk(sFileToStartScan):
    for file in files:
        for x in sFileTypes:
            if file.endswith(x):
                
                #sys.stdout = open(r"" + sUserLogDestination, "a") #this works really well, but needs to have ouputlog
                
                print(os.path.join(root, file))
                #with open("Crap.txt", "a") as text_file:
                with open(f"" + sUserNamedLog, "a") as text_file:
                    print(f"" + os.path.join(root, file), file=text_file)
                #with open(r"" + sUserLogDestination, "w") as text_file:
                    #print(f"" + os.path.join(root, file), file=text_file)
                #shutil.copy(os.path.abspath(root + '/' + file), r'H:\PythonProjects\Dump')
                shutil.copy(os.path.abspath(root + '/' + file), r"" + sUserDestination)

