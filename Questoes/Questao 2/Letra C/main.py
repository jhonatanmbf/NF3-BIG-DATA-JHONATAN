import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameGroupMatematica = dataFrame.groupby("curso_busca").get_group("Matemática")   
print(dataFrameGroupMatematica)

dataFrameGroupMedicina= dataFrame.groupby("curso_busca").get_group("Medicina")
print(dataFrameGroupMedicina)

dataFrameGroupPedagogia= dataFrame.groupby("curso_busca").get_group("Pedagogia")
print(dataFrameGroupPedagogia)