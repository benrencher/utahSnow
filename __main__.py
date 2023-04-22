from fastapi import FastAPI

app = FastAPI()

@app.get("/dataByDay")
async def dataByDay():
    return open("../dataByDay.json").read()

@app.get("/dataByYear")
async def dataByYear():
    return open("../dataByYear.json").read()

@app.get("/waterYear/{year}")
async def waterYear(year: int):
    return year

@app.get("/waterYears/{startYear}/{endYear}")
async def waterYears(startYear: int, endYear: int):
    return f"{startYear} {endYear}"