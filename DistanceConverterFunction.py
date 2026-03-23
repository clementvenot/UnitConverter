class Distance:
    def __init__(self):
        tab = {
            "nm": 0.000000001,
            "µm": 0.000001,
            "mm": 0.001,
            "cm": 0.01,
            "dm": 0.1,
            "m": 1,
            "dam": 10,
            "hm": 100,
            "km": 1000,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.344,
            "nmi": 1852,
            "ftm": 1.8288,
            "UA": 149597870700,
            "ly": 9.4607 * 10**15,
            "pc": 3.0857 * 10**16
        }


    def convert_to_m(self, unit, value):
        return value * self.tab[unit]

    def convert_from_m(self, unit, value):
        return value / self.tab[unit]

    def convert(self, from_unit, value, to_unit):
        value_in_m = self.convert_to_m(from_unit, value)
        return self.convert_from_m(to_unit, value_in_m)