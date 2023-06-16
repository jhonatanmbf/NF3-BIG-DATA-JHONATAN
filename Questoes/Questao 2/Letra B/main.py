import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameGroupBacharelado = dataFrame.groupby("grau").get_group("Bacharelado")
dataFrameGroupLicenciatura= dataFrame.groupby("grau").get_group("Licenciatura")
dataFrameGroupTecnologico= dataFrame.groupby("grau").get_group("Tecnológico")

print(dataFrameGroupBacharelado)
print(dataFrameGroupLicenciatura)
print(dataFrameGroupTecnologico)