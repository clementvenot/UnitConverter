import requests
import json

url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

rates = data["rates"] # reponse JSON

# Écrire dans le fichier JSON avec formatage propre
with open("exchangeRates.json", 'w') as f:
    json.dump(rates, f, indent=4) # indent=4 plus lisible

print("Fichier exchangeRates.json mis à jour avec succès")
print(f"{len(rates)} devises chargées")
