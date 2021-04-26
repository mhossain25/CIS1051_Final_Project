import matplotlib.pyplot as plt

def horizoninput():
    horizon = input("Please enter the planning horizon of your investment: ")
    horizon = int(horizon)+1
    return horizon

def uniformSeriesCashFlow():
    seriesCash = input("Please enter the value of the uniform series: ")
    seriesCash = int(seriesCash)
    return seriesCash

def uniformCashFlowDiagram(years,cashes):
    yearsList = list(range(0,years))
    cashFlow = [cashes]*horizon
    plt.bar(yearsList,cashes,width=.1,tick_label=yearsList)
    plt.show()
    return cashFlow

def gradientSeriesCashFlow()
        firstCash = input("Please enter the first value of the gradient series: ")
        firstCash = int(firstCash)
        increment = input("Please enter how much the series will change per year: ")
        increment = int(increment)
        return [firstCash,increment]

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
    return cashList