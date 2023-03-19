class Reamur:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        celsius = self.temperature * 5/4
        return celsius

    def to_fahrenheit(self):
        fahrenheit = (self.temperature * 9/4) + 32
        return fahrenheit

    def to_kelvin(self):
        kelvin = (self.temperature * 5/4) + 273.15
        return kelvin

# Membuat objek Reamur dengan nilai awal 25 derajat Reamur
reamur = Reamur(25)

# Mengkonversi suhu Reamur menjadi Celsius
celsius = reamur.to_celsius()
print("25 derajat Reamur = ", celsius, "derajat Celsius")

# Mengkonversi suhu Reamur menjadi Fahrenheit
fahrenheit = reamur.to_fahrenheit()
print("25 derajat Reamur = ", fahrenheit, "derajat Fahrenheit")

# Mengkonversi suhu Reamur menjadi Kelvin
kelvin = reamur.to_kelvin()
print("25 derajat Reamur = ", kelvin, "derajat Kelvin")