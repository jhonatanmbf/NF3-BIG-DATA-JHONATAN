import pandas as pd
import requests

urlCsv = 'https://www.w3resource.com/python-exercises/pandas/filter/world_alcohol.csv'
response = requests.get(urlCsv)

with open("dadoPerAnalitcs.csv", "wb") as file:
  file.write(response.content)

data = pd.read_csv("dadoPerAnalitcs.csv", encoding = 'utf-8', sep = ',')
dataFrame = pd.DataFrame(data);
dataFrame = dataFrame.fillna(0.0)
dataFrame = dataFrame.rename(columns={"Year":"year", "WHO region":"who_region", "Country":"country", "Beverage Types":"beverage_types", "Display Value":"display_value"})

describeWithDisplayValue = dataFrame["display_value"].describe()
print(describeWithDisplayValue)

meanWithDisplayValue = dataFrame["display_value"].mean()
print(meanWithDisplayValue)

medianWithDisplayValue = dataFrame["display_value"].median()
print(medianWithDisplayValue)

modeWithDisplayValue = dataFrame["display_value"].mode()
print(modeWithDisplayValue)

dataFrameGroupBeverageTypes = dataFrame.groupby("beverage_types")
graphicInBar = dataFrameGroupBeverageTypes.plot(x='beverage_types', y='display_value', kind='bar')

print(graphicInBar)

