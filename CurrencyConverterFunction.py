import json

class Currency:
    
    # Charger les taux depuis le fichier JSON
    with open("exchangeRates.json", 'r') as f:
        rates = json.load(f)

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.upper()

        # Vérifier que la monnaie est connue
        if self.unit not in Currency.rates:
            raise ValueError("Monnaie inconnue : " + self.unit)

    # Convertit vers USD 
    def to_usd(self):
        return self.value * Currency.rates[self.unit]

    # Convertit depuis USD vers une monnaie cible
    @staticmethod 
    def from_usd(usd_value, target_unit):
        target_unit = target_unit.upper()

        if target_unit not in Currency.rates:
            raise ValueError("Monnaie inconnue : " + target_unit)

        return usd_value / Currency.rates[target_unit]

    # Conversion principale
    def convert_to(self, target_unit):
        usd_value = self.to_usd()
        return round(Currency.from_usd(usd_value, target_unit), 2)