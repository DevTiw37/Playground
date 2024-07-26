import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = [1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, 0.14285714285714285, 0.125, 0.1111111111111111, 0.1, 0.09090909090909091, 0.08333333333333333, 0.07692307692307693, 0.07142857142857142, 0.06666666666666667, 0.0625, 0.058823529411764705, 0.05555555555555555, 0.05263157894736842]
series = pd.Series(data, index=range(1, 20))
plt.figure(figsize=(10, 6))
plt.plot(series.index, series.values, marker='o', linestyle='-', color='blue')
plt.title('Division Values')
plt.xlabel('Division Number')
plt.ylabel('Value')
plt.grid(True)
plt.show()

