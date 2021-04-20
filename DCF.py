import matplotlib.pyplot as plt

def cashflowdiagram(years,amounts):
    plt.bar(years,amounts,width=.1,tick_label=years)
    plt.show()

# specify the planning horizon
horizon = input("Please enter the planning horizon of your investment: ")
horizon = int(horizon)+1
horizonList = list(range(0,horizon))

# introduce cash flows for each interval of the horizon
cashFlow = []
for i in range(horizon):
    theCash = input("Please enter the cash flow for time step " + str(i) + ": ")
    theCash = int(theCash)
    cashFlow.append(theCash)

print(horizonList)
print(cashFlow)

cashflowdiagram(horizonList,cashFlow)