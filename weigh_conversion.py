class weighConverter:
    def __init__(self):
        tab = {
        "t": 1000000,
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "mg": 0.001,
        "µg": 0.000001,
        "oz": 28.3495,
        "lb": 453.592,
        "st": 6350.29,
        "shortton_US": 907_185,
        "longton_UK": 1_016_050,
        "ct": 0.2,
        "Da": 1.66054e-24,
        "u": 1.66054e-24
        }


    def convert_to_g(self, unit, value):
        return value * self.tab[unit]

    def convert_from_g(self, unit, value):
        return value / self.tab[unit]

    def convert(self, from_unit, value, to_unit):
        value_in_m = self.convert_to_m(from_unit, value)
        return self.convert_from_m(to_unit, value_in_m)


# Exemple d'utilisation
converter = weightConverter()

print(converter.convert_to_g("ft", 40))
print(converter.convert_from_g("ft", 40))
print(converter.convert("dm", 400, "ft"))


