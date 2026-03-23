from fastapi import FastAPI
from pydantic import BaseModel

from CurrencyConverterFunction import Currency
from TemperatureConverterFunction import Temperature
from DistanceConverterFunction import Distance
from WeightConverterFunction import Weight

app = FastAPI(
    title="Conversion API",
    description="API permettant la conversion de devises, températures, distances et poids.",
    version="2.0.0"
)

# -----------------------------
#  SCHEMAS API (entrées JSON)
# -----------------------------

class CurrencyRequest(BaseModel):
    value: float
    unit: str
    target: str

class TemperatureRequest(BaseModel):
    value: float
    unit: str
    target: str

class DistanceRequest(BaseModel):
    value: float
    unit: str
    target: str

class WeightRequest(BaseModel):
    value: float
    unit: str
    target: str


# -----------------------------
#  ROUTES
# -----------------------------

@app.post("/convert/currency")
def convert_currency(data: CurrencyRequest):
    try:
        c = Currency(data.value, data.unit)
        result = c.convert_to(data.target)
        return {
            "input": f"{data.value} {data.unit}",
            "converted_to": data.target,
            "result": result
        }
    except ValueError as e:
        return {"error": str(e)}


@app.post("/convert/temperature")
def convert_temperature(data: TemperatureRequest):
    try:
        t = Temperature(data.value, data.unit)
        result = t.convert_to(data.target)
        return {
            "input": f"{data.value} {data.unit}",
            "converted_to": data.target,
            "result": result
        }
    except ValueError as e:
        return {"error": str(e)}


@app.post("/convert/distance")
def convert_distance(data: DistanceRequest):
    try:
        d = Distance()
        result = d.convert(data.unit, data.value, data.target)
        return {
            "input": f"{data.value} {data.unit}",
            "converted_to": data.target,
            "result": result
        }
    except KeyError:
        return {"error": "Unité inconnue."}


@app.post("/convert/weight")
def convert_weight(data: WeightRequest):
    try:
        w = Weight()
        result = w.convert(data.unit, data.value, data.target)
        return {
            "input": f"{data.value} {data.unit}",
            "converted_to": data.target,
            "result": result
        }
    except KeyError:
        return {"error": "Unité inconnue."}


# Pour lancer l’API : 
# uvicorn mainAPI:app --reload
