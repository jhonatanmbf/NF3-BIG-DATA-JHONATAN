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

dataFrameLocYear = dataFrame.loc[dataFrame["year"] == 1985]

print(dataFrameLocYear)