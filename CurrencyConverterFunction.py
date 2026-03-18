class Currency:
    # Taux par rapport à 1 USD
    rates = {
        "USD": 1.0,
        "EUR": 1.09,
        "JPY": 0.0061,
        "GBP": 1.27,
        "CHF": 1.11,
        # Ajouter les 160 monnaies
    }

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.upper()

        if self.unit not in Currency.rates:
            raise ValueError("Monnaie inconnue : " + self.unit)

    # Convertit vers USD (la base)
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