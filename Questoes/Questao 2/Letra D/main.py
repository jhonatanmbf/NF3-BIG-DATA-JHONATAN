import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameGroupUf = dataFrame.groupby("uf_busca")
meanPerState = dataFrameGroupUf["nota_integral_ampla"].mean()
print(meanPerState)