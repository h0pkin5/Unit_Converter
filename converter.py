
class Converter(object):

    def __init__(self, base, conversion_dictionary):
        self.base_unit = base
        self.converter_dictionary = conversion_dictionary
        self.unit_list = [k for k, _ in self.converter_dictionary.items()]

    def convertFromBase(self, value, unit):
        return float(value)/self.converter_dictionary[unit]

    def convertNoneBase(self, value, value_unit, unit):
        return (value*self.converter_dictionary[value_unit])/self.converter_dictionary[unit]

    def convertToBase(self, value, value_unit):
        return value*self.converter_dictionary[value_unit]


MASS_UNITS = {
            'grain': 0.06479891,
            'ounce': 28.349523125,
            'dram': 1.7718451953125,
            'stone': 6350.29318,
            'pennyweight': 1.55517384,
            'pfund': 453.59237,
            'troy pfund': 373.2417216,
            'feinunze': 31.1034768,
            'gramm': 1
            }

LENGTH_UNITS = {
            'inch': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'kilometer': 1000,
            'meilen': 1609.34,
            'dezimeter': 0.1,
            'nautische länge': 5556,
            'meter': 1
            }

SQUARED_UNITS = {
            'square inch':  0.00064516,
            'square foot': 0.09290304,
            'square yard': 0.83612736,
            'square mile': 2589988.110336,
            'hektar': 10000,
            'ar': 100,
            'square kilometer': 1000000,
            'square meter': 1,
            'square decimeter': 0.01,
            'square centimeter': 0.0001,
            'square millimeter': 0.000001
            }
