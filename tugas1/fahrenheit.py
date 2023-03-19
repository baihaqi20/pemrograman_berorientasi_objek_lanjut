class Fahrenheit:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        celsius = (self.temperature - 32) * 5/9
        return celsius

    def to_reamur(self):
        reamur = (self.temperature - 32) * 4/9
        return reamur

    def to_kelvin(self):
        kelvin = (self.temperature + 459.67) * 5/9
        return kelvin

# Membuat objek Fahrenheit dengan nilai awal 32 derajat Fahrenheit
fahrenheit = Fahrenheit(32)

# Mengkonversi suhu Fahrenheit menjadi Celsius
celsius = fahrenheit.to_celsius()
print("32 derajat Fahrenheit = ", celsius, "derajat Celsius")

# Mengkonversi suhu Fahrenheit menjadi Reamur
reamur = fahrenheit.to_reamur()
print("32 derajat Fahrenheit = ", reamur, "derajat Reamur")

# Mengkonversi suhu Fahrenheit menjadi Kelvin
kelvin = fahrenheit.to_kelvin()
print("32 derajat Fahrenheit = ", kelvin, "derajat Kelvin")