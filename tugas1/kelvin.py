class Kelvin:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        celsius = self.temperature - 273.15
        return celsius

    def to_fahrenheit(self):
        fahrenheit = (self.temperature * 9/5) - 459.67
        return fahrenheit

    def to_reamur(self):
        reamur = (self.temperature - 273.15) * 4/5
        return reamur

# Membuat objek Kelvin dengan nilai awal 100 Kelvin
kelvin = Kelvin(100)

# Mengkonversi suhu Kelvin menjadi Celsius
celsius = kelvin.to_celsius()
print("100 derajat Kelvin = ", celsius, "derajat Celsius")

# Mengkonversi suhu Kelvin menjadi Fahrenheit
fahrenheit = kelvin.to_fahrenheit()
print("100 derajat Kelvin = ", fahrenheit, "derajat Fahrenheit")

# Mengkonversi suhu Kelvin menjadi Reamur
reamur = kelvin.to_reamur()
print("100 derajat Kelvin = ", reamur, "derajat reamur")