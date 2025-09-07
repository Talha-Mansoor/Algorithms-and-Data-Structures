# Name: Talha Mansoor
# NSID= kgy284
#Student number: 11346490
# Instructor's name: Ed Pakroka

import numpy as np   #importing module


election=open("election_SK_2016.csv", "r")             #opening file for reading


saskwins=0                                             #sask party wins counter
line= election.readline()                              # reading first line that is the header
tokens =line.split(",")                                #splitting each word and putting them in a list
constituency = []                                      # creating lists to hold the data
tally = []


#print(tokens)                                         #For testing purposes


for x in tokens:                                       # loop to find the column number of saskparty votes
    if(x.strip()=="saskparty"):
        break
    saskwins+=1


for line in election:                                  # for every line in file
    tokens = line.split(",")                           # split the line separated by commas
    constituency.append(tokens[0].strip())             # remove extra space and add constituency names to a list "constituency"
    for y in range(1, 7):
        tokens[y] = int(tokens[y])                     # convert data to integers
    tally.append(tokens[1:])                           #add row to tally list

#print(tally)                                          #for testing purposes

election.close()


constituency = np.array(constituency)                  #Converting lists to  arrays
tally = np.array(tally)



total = np.zeros((len(tally)), dtype='i')         #create new array of zeros with size of length of tally and datatype of integer
total[:] = np.sum(tally[:, :], axis=1)       # total number of votes in a row for every constituency


majority = []                                     #majority win list
WIN=0
for k in range(0, len(total)):
    if(tally[k, saskwins-1] > total[k]/2):        #If Sask party votes are more than half then add it to majority list
        majority.append(constituency[k])
        WIN+=1
print("The Saskatchewan Party won a vote majority in ",WIN," constituencies:")
print(*majority, sep='\n')