import matplotlib.pyplot as plt

def checkIntInput(arg): # found code on https://pynative.com/python-check-user-input-is-number-or-string/#:~:text=To%20check%20if%20the%20input%20string%20is%20an%20integer%20number,using%20the%20int()%20constructor.&text=To%20check%20if%20the%20input%20is%20a%20float%20number%2C%20convert,using%20the%20float()%20constructor.
    # checks an argument if it is an integer
    try:
        an_arg = int(arg)
        return True
    except ValueError:
        return False

def checkStrInput(arg):
    # checks an argument if it is a string
    try:
        an_arg = str(arg)
        return True
    except ValueError:
        return False

def checkFloatInput(arg):
    # checks an argument if it is a float
    try:
        an_arg = float(arg)
        return True
    except ValueError:
        return False

def horizoninput(horizon):
    # turns the inputted value into an integer and adds 1 to include the last value then returns that value
    horizon = int(horizon)+1
    return horizon
    
def singularCashFlow(horizon):
    # allows a user to input each cash flow for each time increment
    cashFlow = []
    for i in range(horizon):
        cashFlag = False # error trapping, doesn't allow user to continue unless they type in an int or a float
        while cashFlag == False:
            theCash = input("Please enter the cash flow for time step " + str(i) + ": ")
            if checkFloatInput(theCash) == True or checkIntInput(theCash) == True:
                theCash = float(theCash)
                cashFlag = True
            else:
                print("Please input a number for your cash flow.")        
        cashFlow.append(theCash) # once the while loop is exited, the value is added to the cash flow
    return cashFlow

def uniformSeriesCashFlow(horizon,seriesCash):
    cashFlow = [seriesCash]*horizon # this creates a list that has the series value that is horizon values long
    return cashFlow

def gradientSeriesCashFlow(horizon,firstCash,increment):
        cashFlow = []
        for i in range(horizon):
            if i == 0:
                cashFlow.append(0)  # the first year is 0 in a gradient series
            else:
                cashFlow.append(firstCash+(i-1)*increment) # the gradient series has an intital value
        return cashFlow                                    # then changes linearly

def cashFlowDiagram(years,cashList):
    yearsList = list(range(0,years)) # this creates and manages the bar plot with given horizon and cash flow
    cfd = plt.bar(yearsList,cashList,width = .1,tick_label = yearsList)
    plt.bar_label(cfd) # learned this at https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    plt.show()

def worthOfSeries(horizon,cashFlow,percentInterest):
    # present worth formula = FV*(1+i)^(-n)
    interest = percentInterest/100 # converts percent interest into a decimal
    futureWorth = 0
    presentWorth = 0
    for i in range(horizon):
        futureWorth += cashFlow[i] # sum of each value in the series
        presentWorth += cashFlow[i]*(1+interest)**(-i) # adds the present value of each value moving forward in time
    futureWorth = round(futureWorth)
    presentWorth = round(presentWorth)
    annualWorth = round(presentWorth*((interest*(1+interest)**horizon)/(-1+(1+interest)**horizon))) # annual worth formula
    print("The future worth of the series is {}.".format(futureWorth))
    print("The present worth of the series is {}.".format(presentWorth))
    print("The annual worth of the series is {}.".format(annualWorth))

def mainProgram():
    # traps errors of horizon
    horizonFlag = False
    while horizonFlag == False:
        horizon = input("What is the length of time (horizon) you'll be looking at? ")
        if checkIntInput(horizon) == True: # requires integer input
            if int(horizon) > 0: # input cannot be zero
                horizon = int(horizon)+1
                horizonFlag = True # breaks loop
            else:
                print("Please input an integer number greater than 0. ")
        else:
            print("Please input an integer number greater than 0. ")

    numberSeriesFlag = False # similiar to the horizon error check
    while numberSeriesFlag == False:
        numberOfSeries = input("Please enter how many series you plan to include. ")
        if checkIntInput(numberOfSeries) == True:
            if int(numberOfSeries) > 0:
                numberOfSeries = int(numberOfSeries)
                numberSeriesFlag = True
            else:
                print("Please input an integer number greater than 0. ")
        else:
            print("Please input an integer number greater than 0. ")
    

    previousCashFlow = []
    for i in range(numberOfSeries):
        choiceFlag = False # checks for strings that are S,U, or H, otherwise user cannot continue
        while choiceFlag == False:
            choice = input("Please input 'S' for individual cash flows,\ninput 'U' for uniform series cash flow,\nor input 'G' for gradient series cash flow. ")
            if checkStrInput(choice) == True:
                if choice.upper() == 'S' or choice.upper() == 'U' or choice.upper() == 'G':
                    choice = choice.upper()
                    choiceFlag = True
                else:
                    print("You should input 'S','U', or 'G' to indicate what series you want to add. Please try again. ")
            else:
                print("You should input 'S','U', or 'G' to indicate what series you want to add. Please try again. ")

        if choice == 'S':
            cashFlow = singularCashFlow(horizon)
        elif choice == 'U':
            seriesFlag = False # error traps the uniform cash value until a float is given
            while seriesFlag == False:
                seriesCash = input("Please enter the cash amount for the uniform series. ")
                if checkFloatInput(seriesCash) == True:
                    seriesCash = float(seriesCash)
                    seriesFlag = True
                else:
                    print("Please input a float for your desired uniform series amount. ")
            cashFlow = uniformSeriesCashFlow(horizon,seriesCash) # calls function to calculate cash flow
        elif choice == 'G':
            firstCashFlag = False   # two error traps for each input for the gradient series
            while firstCashFlag == False:
                firstCash = input("Please enter the initial amount for the gradient series. ")
                if checkFloatInput(firstCash) == True:
                    firstCash = float(firstCash)
                    firstCashFlag = True
                else:
                    print("Please input a float for your desired gradient series starting value. ")
            incrementFlag = False
            while incrementFlag == False:
                increment = input("Please enter the change per year for the gradient series. ")
                if checkFloatInput(increment) == True:
                    increment = float(increment)
                    incrementFlag = True
                else:
                    print("Please input a float for your desired change in each year of the series. ")
            cashFlow = gradientSeriesCashFlow(horizon,firstCash,increment)
                
        if i == 0:
            previousCashFlow = cashFlow # only useful if there's more than one series
        else: # code found on https://www.geeksforgeeks.org/python-adding-two-list-elements/
            cashFlow = [sum(j) for j in zip(cashFlow,previousCashFlow)] #sums a tuple to get a list again
            previousCashFlow = cashFlow 

    percentFlag = False # interest error trapping
    while percentFlag == False:
            percentInterest = input("What is the interest rate of the series? ")
            if checkFloatInput(percentInterest) == True:
                if float(percentInterest) != 0: # requires a value greater than 0 because there's a singularity there
                    percentInterest = float(percentInterest)
                    percentFlag = True
                else:
                    print("Please input a valid float that is not 0. ")
            else:
                print("Please input a valid float that is not 0. ")

    worthOfSeries(horizon,cashFlow,percentInterest) # calculates present, future, and annual worth
    
    cashFlowDiagram(horizon,cashFlow) # creates the cash flow diagram

    return

mainProgram()