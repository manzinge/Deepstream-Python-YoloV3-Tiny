import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def checkFolder():
    if not os.path.exists('Plots'):
        os.makedirs('Plots')

def plotGraph(pickleArr):
    sns.set(style="darkgrid")

    fmri = pd.DataFrame(pickleArr)
    sns.lineplot(data=fmri)
    plt.savefig('Plots/fp32Plt.png')
    plt.show()
