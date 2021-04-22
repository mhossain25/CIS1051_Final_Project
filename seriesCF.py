import matplotlib.pyplot as plt

def uniformCashFlowDiagram(years,cashes):
    yearsList = list(range(0,years))
    cashFlow = [cashes]*horizon
    plt.bar(yearsList,cashes,width=.1,tick_label=yearsList)
    plt.show()

def gradientCashFlowDiagram(years,initialcash,incremental):
    yearsList = list(range(0,years))
    cashList = []
    for i in range(years):
        if i == 0:
            cashList.append(0)
        else:
            cashList.append(initialcash+i*incremental)
    plt.bar(yearsList,cashList,width = .1,tick_label = yearsList)
    plt.show()

# declare the planning horizon
horizon = input("Please enter the planning horizon of your investment: ")
horizon = int(horizon)+1

# giving user choices for uniform or gradient series
choice = input("Please enter 'u' for a uniform series or 'g' for a gradient series: ")
choice = choice.lower()
if choice == 'u':
    seriesCash = input("Please enter the value of the uniform series: ")
    seriesCash = int(seriesCash)
    uniformCashFlowDiagram(horizon,seriesCash)
elif choice == 'g':
    firstCash = input("Please enter the first value of the gradient series: ")
    firstCash = int(firstCash)
    increment = input("Please enter how much the series will increase per year: ")
    increment = int(increment)
    gradientCashFlowDiagram(horizon,firstCash,increment)    
else:
    print("You didn't select an option.")

