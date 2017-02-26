class Thermometer(object):

    KELVIN_FORMAT = "%.1fK"
    CELCIUS_FORMAT = "%.1fC"
    FAHRENHEIT_FORMAT = "%.1fF"

    def __init__(self):
        self.temperature_in_kelvin = -1.0

    def driver_value(self, value):
        self.temperature_in_kelvin = value/100.0

    def get_temperature(self):
        return self.KELVIN_FORMAT % self.temperature_in_kelvin

    def get_temperature_in_celcius(self):
        return self.CELCIUS_FORMAT % (self.temperature_in_kelvin - 273.15)

    def get_temperature_in_fahrenheit(self):
        return self.FAHRENHEIT_FORMAT % ((self.temperature_in_kelvin - 273.15) * 1.8 + 32 )


