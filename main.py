
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1869873

#IIT number : 20200731

# Date: 07/12/2021

#----------------Logic------------------------------------------------------------------------------------------------------
import sys      # Built in sys module for the use of sys.exit function to exit the program without errors

#Define variables 
credPass=0
credDefer=0
credFail=0
valid_credits= [0,20,40,60,80,100,120]
option = ""
repeat = ""
verticleList=[]
outcomes=0
resultList=[]
finalList=[]


#lists to store inputs to display histogram
listProg = []
listTrail = []
listRetrv = []
listExclude = []



#-----------------------------------------------------------------------------------------------------------------------
# Function including the logic to check the progress 
def progressCheck(credPass,credDefer,credFail): #Parameters
    global resultList
    if credPass == 120:
        print ("Progress")
        listProg.append(1)              # Inserting the values to the relevant lists to keep track on how many inputs each list carry
        resultList.append("Progress")   # Inserting to a list to access later in part 3
        
    elif credPass == 100:
        print ("Progress (Module trailer)")
        listTrail.append(1)                             # Inserting the values to the relevant lists to keep track on how many inputs each list carry
        resultList.append("Progress (Module trailer)")  # Inserting to a list to access later in part 3
        
    elif ((credPass + credDefer)>= credFail):
        print ("Do not progress - Module retriever")    
        listRetrv.append(1)                             # Inserting the values to the relevant lists to keep track on how many inputs each list carry
        resultList.append("Module retriever")           # Inserting to a list to access later in part 3
        
    elif (credPass + credDefer)< credFail:
        print ("Exclude")
        listExclude.append(1)                           # Inserting the values to the relevant lists to keep track on how many inputs each list carry
        resultList.append("Exclude")                    # Inserting to a list to access later in part 3
        
    elif credPass < credDefer <= credFail:
        print ("Do not progress - Module retriever")
        listRetrv.append(1)                             # Inserting the values to the relevant lists to keep track on how many inputs each list carry
        resultList.append(" Module retriever")          # Inserting to a list to access later in part 3
    


#----------------------------------------------------------------------------------------------------------------------
#function to ask user about repeating the process to take multiple data inputs
def RepeatValidation(option):
    global repeat

    #Loop to repeat the process 
    while True:
        try:
            repeat = input("\nDo you want to continue inserting data? \nInsert 'y' for YES or 'q' to QUIT and view results : ").lower()
            if repeat == "y":
                StudentValidation(option)
                #continue
            elif repeat == "q" and option == "h":
                horizontal_histogram()
                sys.exit(0) # exit the program without errors
            elif repeat == "q" and option == "v":
                verticle_histogram()
                sys.exit(0)
            elif repeat == "q" and option == "e":
                verticle_histogram()
                ListExtension(option)
                sys.exit(0)
            elif repeat == "q" and option == "t":
                verticle_histogram()
                TextFile(option)
                sys.exit(0)
            
        except ValueError:
            print ("Invalid input, \nPlease enter 'y' or 'q' : ")

#---------------------------------------------------------------------------------------------------------------------
# function to ask students' marks and display the outputs
            # -Student validation is ending after one set of data (NO REPETITIONS)
            # -Staff version will ask to loop and display histogram at the end and both were done under one function
            
def StudentValidation(option): # Argument option was given to choose between student and staff version

    #global variables
    global credPass, credFail, credDefer, valid_credits, resultList 
    #local variables
    total=0
    
    while True: #Infinite loop to ask input until valid inputs were entered
        
        try:
            credPass = int(input("\nPlease enter your credits at pass : "))
            if credPass in valid_credits:
                
                credDefer = int(input("Please enter your credits at defer : "))
                if credDefer in valid_credits:
                    
                    credFail = int(input("Please enter your credits at fail : "))
                    if credFail in valid_credits:

                        
                        total = credPass + credFail + credDefer
                        if total != 120:
                            print ("Total Incorrect\n")
                      
                        # this is to switch between student and staff version without repeating the same code
                        else:
                            if option == "s":
                                progressCheck (credPass, credDefer, credFail)
                                sys.exit(0)
                                
                            else:

                                # inserting to a new list to access later in part 3 solution
                                resultList.append(credPass) 
                                resultList.append(credDefer)
                                resultList.append(credFail)
                                
                                progressCheck (credPass, credDefer, credFail)
                                RepeatValidation(option)
                                sys.exit(0)
                                
                    else:
                        print ("Out of range\n")
                else:
                    print ("Out of range\n")
            else:
                print ("Out of range\n")
                        
                    
        except ValueError:
            print ("Integer required\n")



#--------------------------------------------------------------------------------------------------
#Function to display Horizontal histogram
def horizontal_histogram():
    global outcomes
    print ("\n","-_"*40)
    print ("\nHorizontal Histogram\n")
    print ("Progress  - ", len(listProg), " : ", "*" * len(listProg))
    print ("Trailer   - ", len(listTrail), " : ", "*" * len(listTrail))
    print ("Retriever - ", len(listRetrv), " : ", "*" * len(listRetrv))
    print ("Excluded  - ", len(listExclude), " : ", "*" * len(listExclude))
    # to display the total outcomes
    outcomes = len(listProg) + len(listTrail) + len(listRetrv) + len(listExclude) 
    print ("\n",outcomes, "outcomes in total")
    print ("\n","-_"*40)

#--------------------------------------------------------------------------------------------------
# Part 2 - verticle histogram as a function and added to the options menu
def verticle_histogram():
    global outcomes

    outcomes = len(listProg) + len(listTrail) + len(listRetrv) + len(listExclude)
    verticleList = [listProg,listTrail,listRetrv,listExclude]

    print ("\n","-_"*40)
    print("\n\t Progress",len(listProg)," \t Trailer",len(listTrail), "\t Retriever",len(listRetrv),"\t Exclude",len(listExclude))
    for x in range (outcomes):
        for y in verticleList:
            if len(y)>0:
                print("\t ", "*", "\t ", end =" ")
                y.pop() # .pop() will remove the last value from list and return it
            else:
                print("\t ", " ", "\t ", end =" ")
        print() 
    print("\n",outcomes,"outcomes in total " )

#--------------------------------------------------------------------------------------------------
# Part 3 - List

def ListExtension(option):
    global resultList, outcomes, finalList, textList


    # outcomes represents final results, and outcomes*4 = total inputs + results
    contents=(int(outcomes))*4


    # to create a new list with the content of resultList's from the last to the begining
    # because .pop() will will give last value from the list,
    #i've created a new list called finalList with the content from end to begining of resultList
    while contents >0:

        finalList.append(resultList.pop())
        contents-=1
            
    print ("\n","-"*40)

    
    count=int(outcomes)
    # While sets of 4 in the resultList pop, until the outcomes count end
    while (count >= 1):

        
        print (finalList)
        print ("\t",finalList.pop(-4),"-",finalList.pop(),",",finalList.pop(),",",finalList.pop())
        count-=1
    print ("\n","-"*40)


#--------------------------------------------------------------------------------------------------
# Part 4 - Text file

def TextFile(option):

    text= sys.stdout # system specified parameter to write output on a text file  
    sys.stdout = open ("results.txt","w")
    ListExtension(option)

    
    sys.stdout.close()
    sys.stdout = text

    print("\nDisplaying outputs from results.txt\n")
    file =  open ("results.txt","r") 
    lines = file.readlines()
    for line in lines: # this will read the created txt file line by line
        print(line,end="")
    file.close()
    

    

#--------------------------------------------------------------------------------------------------           

# give options for user to choose between parts of the coursework
def options():
    option=""
    while True:
        option = input( "\nInsert  's' for PART 1 - student version (ONE SET OF DATA/No Loops),"
                        "\nInsert  'h' for PART 1 - staff version (horizontal histogram),"
                        "\nInsert  'v' for PART 2 - staff version (verticle histogram),"
                        "\nInsert  'e' for PART 3 - staff version (verticle histogram + List extension "
                        "\nInsert  't' for PART 4 - staff version (Text file extension) \n:").lower()

        if option == "s":
            StudentValidation(option) # Arguments were given
        elif option == "h":
            StudentValidation(option)
        elif option == "v":
            StudentValidation(option)
        elif option == "e":
            StudentValidation(option)
        elif option == "t":
            StudentValidation(option)

            
            break

#-----------------------Main Body----------------------------------------------------------------------------------

print("-"*14,"Welcome!","-"*14,'\n', 
      "\nInsert an letter based on your selection from below"
      "\n(Student version only takes 1 input and staff versions can take multiple inputs)\n",
      "\n","-"*15,"Menu","-"*15)

# call the main function to run the program

for i in range (1 , 101):
    print (i)

#---------------------------------------------------------------------------------------------------------------

#References    
# https://docs.python.org/3/library/sys.html

















