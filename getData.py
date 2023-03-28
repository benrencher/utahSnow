import urllib.request, json

url = "https://www.nrcs.usda.gov/Internet/WCIS/AWS_PLOTS/basinCharts/POR/WTEQ/assocHUCut3/state_of_utah.json"
response = urllib.request.urlopen(url)
status = response.status
if status != 200:
  print(f"An error occured; status: {status}")
  raise SystemExit(-1)

dataByDay = json.loads(response.read())

dataByYear = {}
for key, value in dataByDay[0].items():
  if key.isdigit():
    dataByYear[key] = {}

for day in dataByDay:
  date = day['date']
  for year in dataByYear:
    dataByYear[year][date] = day[year]