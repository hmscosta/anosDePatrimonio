import matplotlib.pyplot as plt
import numpy as np
import csv

#labels = ['1995', '1996', '1997', '1998', '1999']
#men_means = [20, 35, 30, 35, 27]
#women_means = [25, 32, 34, 20, 25]
#men_std = [2, 3, 4, 1, 2]
#women_std = [3, 5, 2, 3, 3]
#width = 0.35       # the width of the bars: can also be len(x) sequence
#fig, ax = plt.subplots()
#ax.bar(labels, men_means, width, yerr=men_std, label='Men')
#ax.set_ylabel('Valor (R$)')
#ax.set_title('Patrimonio ao longo dos anos')
#ax.legend()
#plt.show()


f = open('dataset/bem_candidato_2018_AP.csv')
csv_f = csv.reader(f)
