import matplotlib.pyplot as plt

def horizoninput():
    horizon = input("Please enter the planning horizon of your investment: ")
    horizon = int(horizon)+1
    return horizon
    
def singularCashFlow(horizon):
    cashFlow = []
    for i in range(horizon):
        theCash = input("Please enter the cash flow for time step " + str(i) + ": ")
        theCash = int(theCash)
        cashFlow.append(theCash)
    return cashFlow

def singularCashFlowDiagram(years,cashes):
    yearsList = list(range(0,years))
    plt.bar(yearsList,cashes,width=.1,tick_label=yearsList)
    plt.show()

#singularCashFlowDiagram(horizon,cashFlow)