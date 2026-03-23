class Distance:
    def __init__(self):
        
        self.tab = {
            "nm": 0.000000001,        # nanomètre
            "µm": 0.000001,           # micromètre
            "mm": 0.001,              # millimètre
            "cm": 0.01,               # centimètre
            "dm": 0.1,                # décimètre
            "m": 1,                   # mètre
            "dam": 10,                # décamètre
            "hm": 100,                # hectomètre
            "km": 1000,               # kilomètre

            "in": 0.0254,             # inch / pouce
            "ft": 0.3048,             # pied (foot)
            "yd": 0.9144,             # yard
            "mi": 1609.344,           # mile
            "nmi": 1852,              # mile nautique
            "ftm": 1.8288,            # fathom (brasse)

            "UA": 149_597_870_700,    # unité astronomique
            "ly": 9.4607 * 10**15,    # année-lumière
            "pc": 3.0857 * 10**16     # parsec
        }

    def convert_to_m(self, unit, value):
        return value * self.tab[unit]

    def convert_from_m(self, unit, value):
        return value / self.tab[unit]

    def convert(self, from_unit, value, to_unit):
        value_in_m = self.convert_to_m(from_unit, value)
        return round(self.convert_from_m(to_unit, value_in_m), 4)