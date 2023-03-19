class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        fahrenheit = (9/5) * self.celsius + 32
        return fahrenheit
    
    def to_reamur(self):
        reamur = 4/5 * self.celsius
        return reamur
    
    def to_kelvin(self):
        kelvin = self.celsius + 273
        return kelvin
    
c = 75
converter = TemperatureConverter(c)
print("Konversi", c, "derajat Celsius ke Fahrenheit adalah", converter.to_fahrenheit(), "derajat Fahrenheit")
print("Konversi", c, "derajat Celsius ke Reamur adalah", converter.to_reamur(), "derajat Reamur")
print("Konversi", c, "derajat Celsius ke Kelvin adalah", converter.to_kelvin(), "derajat Kelvin")
