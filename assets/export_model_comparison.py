from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

folder=Path(__file__).resolve().parent
with (folder/'model_comparison.csv').open(encoding='utf-8') as stream:
    data=list(csv.DictReader(stream))
x=[int(row['period']) for row in data]
observed=[float(row['observed']) for row in data]
predicted=[float(row['predicted']) for row in data]
fig,ax=plt.subplots(figsize=(6.6,3.5),layout='constrained')
ax.plot(x,observed,'o-',color='#19364A',label='Observed',lw=1.7,ms=5)
ax.plot(x,predicted,'s--',color='#227C81',label='Model',lw=1.7,ms=4)
ax.set(xlabel='Period',ylabel='Demand (units)',xticks=x)
ax.grid(alpha=.18)
ax.legend(frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.savefig(folder/'model_comparison.png',dpi=220)
plt.close(fig)
