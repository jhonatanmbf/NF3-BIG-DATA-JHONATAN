import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)

dataFrameOnlyCourseTecnologi = dataFrame[dataFrame['grau'] == 'Tecnológico']
dataFrameGroupPerCourse = dataFrameOnlyCourseTecnologi.groupby("curso_busca")

dataFrameGroupPerCourse.first()