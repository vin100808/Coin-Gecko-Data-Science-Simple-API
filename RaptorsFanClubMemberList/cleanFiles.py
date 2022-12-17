'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    
# --------------------------------------------------------------------------------------------- #
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem,'r+') as activeFile: # r+ such that can remove and edit
        #TODO: Open the exMem file in a+ mode
        with open(exMem,'a+') as exFile: # a+ because we only need to append inactive members
            #TODO: Read each member in the currentMem (1 member per row) file into a list.
            header = activeFile.readline() # filter out the first line which is the header
            currentMemberLines = activeFile.readlines()
            activeFile.seek(0,0) # set the pointer back to beginning for overwrite
            activeFile.write(header)
            
            #TODO: iterate through the members and create a new list of the innactive members
            for line in currentMemberLines:
                if line.find('no') != -1: # meaning its inactive
                    exFile.write(line) # if inactive, just append
                else:
                    activeFile.write(line)
            activeFile.truncate()
# --------------------------------------------------------------------------------------------- #


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
