import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)


dataFrameGroupOnlyMedicinaCourse = dataFrame.groupby("curso_busca").get_group("Medicina")

meanMonthlyPaymentPerCourseMedicina = dataFrameGroupOnlyMedicinaCourse["mensalidade"].mean()
print(meanMonthlyPaymentPerCourseMedicina)

