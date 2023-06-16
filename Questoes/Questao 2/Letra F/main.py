import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameWithoutCidadeFiltro = dataFrame.drop('cidade_filtro', axis=1)
print(dataFrameWithoutCidadeFiltro)