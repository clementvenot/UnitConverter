from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    value: float = Field(..., description="Valeur à convertir")
    unit: str = Field(..., description="Devise source (ex : EUR, USD, GBP)")
    target: str = Field(..., description="Devise cible (ex : EUR, USD, GBP)")

class TemperatureRequest(BaseModel):
    value: float = Field(..., description="Valeur à convertir")
    unit: str = Field(..., description="Unité source (C, F, K)")
    target: str = Field(..., description="Unité cible (C, F, K)")

class DistanceRequest(BaseModel):
    value: float = Field(..., description="Valeur à convertir")
    unit: str = Field(..., description="Unité source (m, km, cm, etc.)")
    target: str = Field(..., description="Unité cible (m, km, cm, etc.)")

class WeightRequest(BaseModel):
    value: float = Field(..., description="Valeur à convertir")
    unit: str = Field(..., description="Unité source (kg, g, lb, oz)")
    target: str = Field(..., description="Unité cible (kg, g, lb, oz)")


# -----------------------------
#  ROUTES
# -----------------------------

@app.post(
    "/convert/currency",
    summary="Convertir une devise",
    description="Convertit un montant d'une devise vers une autre (ex : EUR → USD)."
)
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


@app.post(
    "/convert/temperature",
    summary="Convertir une température",
    description="Convertit une température entre Celsius, Fahrenheit et Kelvin."
)
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


@app.post(
    "/convert/distance",
    summary="Convertir une distance",
    description="Convertit des distances entre différentes unités : m, km, cm, mm, mi, ft, etc."
)
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


@app.post(
    "/convert/weight",
    summary="Convertir un poids",
    description="Convertit des poids entre kg, g, livres (lb), onces (oz), etc."
)
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