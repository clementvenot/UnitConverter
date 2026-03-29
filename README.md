***

# 🚀 Unit Converter 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FFCA28?style=for-the-badge)
![API](https://img.shields.io/badge/REST%20API-4A90E2?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![No%20License](https://img.shields.io/badge/License-UNLICENSED-green?style=for-the-badge)

REST API built with **FastAPI** to convert:

- 💱 Currencies  
- 🌡️ Temperatures  
- 📏 Distances  
- ⚖️ Weights  

---

# 🛠️ Backend API

## 🔌 Endpoints

- **POST** `/convert/currency`
- **POST** `/convert/temperature`
- **POST** `/convert/distance`
- **POST** `/convert/weight`


***

## 🔄 Update Exchange Rates

A background script (update_rates.py) refreshes currency exchange rates by fetching real‑time data from an online API, ensuring all currency conversions remain up to date.

***

## 🖥️ GUI (Tkinter)

A simple Tkinter-based interface (UnitConverter.py) lets users select a category (temperature, currency, distance, weight), choose units, swap them instantly, and view conversions in real time through an intuitive and minimal UI.

<img width="505" height="339" alt="Screenshot 2026-03-30 at 00 35 26" src="https://github.com/user-attachments/assets/8d1309e3-2cdb-4fd5-808d-4b5e86cf61f4" />

***

## ⚙️ Installation

```bash
git clone https://github.com/your-username/UnitConverter.git
cd unit-converter-api
pip install fastapi uvicorn
```

---

## ▶️ Run the API 

Script : mainAPI.py
```bash
uvicorn mainAPI:app --reload
```

👉 http://127.0.0.1:8000/docs

---

## 🔌 Example Usage

### 💱 Currency Conversion

```json
{
  "value": 100,
  "unit": "EUR",
  "target": "USD"
}
```

### 🌡️ Temperature Conversion

```json
{
  "value": 25,
  "unit": "C",
  "target": "F"
}
```

### 📏 Distance Conversion

```json
{
  "value": 10,
  "unit": "km",
  "target": "m"
}
```

### ⚖️ Weight Conversion

```json
{
  "value": 5,
  "unit": "kg",
  "target": "lb"
}
```

***

## 📄 License

There is no license; you're free to use it.

***
