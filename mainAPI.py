from fastapi import FastAPI
from pydantic import BaseModel
from CurrencyConverterFunction import Currency
from TemperatureConverterFunction import Temperature

app = FastAPI(
    title="Conversion API",
    description="API permettant la conversion de devises et de températures.",
    version="1.0.0"
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

# Pour lancer l’API : uvicorn mainAPI:app --reload