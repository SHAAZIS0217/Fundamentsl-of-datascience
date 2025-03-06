import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Data = {
	'Smoking': [20, 15, 5, 25, 30, 10, 18, 22, 8, 12],
	'LungCancer': [5, 4, 1, 6, 8, 2, 3, 7, 1, 2]
}
df=pd.DataFrame(Data)
cor=np.corrcoef(df["Smoking"],df["LungCancer"])[0,1]
print(cor)

plt.figure(figsize=(6,6))
plt.scatter(df["Smoking"],df["LungCancer"])
plt.title('Relationship between Smoking and Lung Cancer')
plt.xlabel('Smoking')
plt.ylabel('Lung Cancer')
plt.grid(True)
plt.show()
