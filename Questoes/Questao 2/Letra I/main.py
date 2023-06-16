import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameGroupGrau= dataFrame.groupby("grau").get_group("Bacharelado")
descPerNotaIntegralAmpla = dataFrameGroupGrau["nota_integral_ampla"].describe()

print(descPerNotaIntegralAmpla)

