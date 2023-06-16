import pandas as pd

data = pd.read_csv('Data/cursos-prouni.csv', encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)
dataFrame = dataFrame.head(16)

graphicInBar = dataFrame.plot(x='grau', y='nota_integral_ampla', kind='bar')

print(graphicInBar)
