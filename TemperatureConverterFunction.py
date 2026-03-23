class Temperature:
    
    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.lower()

    # --- Conversions en Celsius ---
    def to_celsius(self):
        if self.unit in ["c", "celsius"]:
            return self.value
        elif self.unit in ["f", "fahrenheit"]:
            return (self.value - 32) * 5/9
        elif self.unit in ["k", "kelvin"]:
            return self.value - 273.15
        else:
            raise ValueError("Unité source inconnue")

    # --- Conversions depuis Celsius ---
    @staticmethod # staticmethod car cette fonction n’a pas besoin d’accéder à l’instance (self)
    def from_celsius(celsius_value, target_unit):
        target_unit = target_unit.lower()

        if target_unit in ["c", "celsius"]:
            return celsius_value
        elif target_unit in ["f", "fahrenheit"]:
            return celsius_value * 9/5 + 32
        elif target_unit in ["k", "kelvin"]:
            return celsius_value + 273.15
        else:
            raise ValueError("Unité cible inconnue")

    # --- Fonction principale de conversion ---
    def convert_to(self, target_unit):
        celsius = self.to_celsius()
        return Temperature.from_celsius(celsius, target_unit)