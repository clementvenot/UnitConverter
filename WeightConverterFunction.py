class Weight:
    def __init__(self):
        self.tab = {
        "t": 1_000_000,      # tonne
        "kg": 1000,          # kilogramme
        "hg": 100,           # hectogramme
        "dag": 10,           # décagramme
        "g": 1,              # gramme
        "mg": 0.001,         # milligramme
        "µg": 0.000001,      # microgramme
        "oz": 28.3495,       # once (ounce)
        "lb": 453.592,       # livre (pound)
        "st": 6350.29,       # stone
        "shortton_US": 907_185,   # tonne courte américaine (short ton US)
        "longton_UK": 1_016_050,  # tonne longue britannique (long ton UK)
        "ct": 0.2,           # carat
        "Da": 1.66054e-24,   # dalton (unité de masse atomique)
        "u": 1.66054e-24     # unité de masse atomique (unified atomic mass unit)
        }


    def convert_to_g(self, unit, value):
        return value * self.tab[unit]

    def convert_from_g(self, unit, value):
        return value / self.tab[unit]

    def convert(self, from_unit, value, to_unit):
        value_in_g = self.convert_to_g(from_unit, value)
        return self.convert_from_g(to_unit, value_in_g)