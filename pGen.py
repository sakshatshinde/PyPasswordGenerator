#Password generator by Sakshat Shinde

import random

#declaring the password variable
password = ""

#Msgs for the user
print("Choose parameters, atleast 2 for safety, we recommend 3\n")
print("For example if you want to choose 1,3 and 4")
print("Type \'134' \n")
print("1: Pet name, 2: Spouse name, 3: Fav Movie, 4: Your favourite number, 5: Significant Date")
parametersChosen = input("Type in the parameters: ")

def runGen():
    parArray = []
    funcArray = []

    #Making an array of the chosen options
    for i in parametersChosen:
        parArray.append(int(i))

    #Checking which options the user has chosen
    for j in parArray:
        if(j == 1):
            petName = input("What was your first pet's name? ")
            funcArray.append(petName.lower())
        elif(j == 2):
            spouseName = input("What was your spouse's first name? ")
            funcArray.append(spouseName.upper())
        elif(j == 3):
            favMovie = input("What was your fav movie? ")
            funcArray.append(favMovie.lower())
        elif(j == 4):
            firstCar = input("Enter your favourite number? ")
            funcArray.append(firstCar.lower())
        elif(j == 5):
            sigDate = input("Enter the significant date without \'/' ")
            funcArray.append(sigDate)

        else:
            "Something went wrong, please check the options you enetered and retry!"


    
    #special character set so we can wrap the password in characters
    specialCh = ['!', '.', '&', '/', '?']

    #Password Generation function

    def passGen():
        random.shuffle(funcArray)
        #print(funcArray)
        password = ''
        for i in funcArray:
            password = password + i
        password = random.choice(specialCh) + password + random.choice(specialCh)
        return password
        
    print(passGen())


#Running the main function

runGen()

