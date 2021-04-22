import matplotlib.pyplot as plt

def singularCashFlowDiagram(years,cashes):
    yearsList = list(range(0,years))
    plt.bar(yearsList,cashes,width=.1,tick_label=yearsList)
    plt.show()

horizon = input("Please enter the planning horizon of your investment: ")
horizon = int(horizon)+1
cashFlow = []
for i in range(horizon):
    theCash = input("Please enter the cash flow for time step " + str(i) + ": ")
    theCash = int(theCash)
    cashFlow.append(theCash)

singularCashFlowDiagram(horizon,cashFlow)