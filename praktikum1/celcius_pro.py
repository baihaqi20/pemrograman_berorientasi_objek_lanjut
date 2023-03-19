class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        fahrenheit = (9/5) * celcius + 32
        print("konversi ", celcius, "derajat celcius adalah ", fahrenheit, "derajat Fahrenheit")

    @staticmethod
    def celcius_to_reamur(celcius):
        reamur = 4/5 * celcius
        print("konversi ", celcius, "derajat celcius adalah ", reamur, "derajat Reamur")

    @staticmethod
    def celcius_to_kelvin(celcius):
        kelvin = celcius + 273
        print("konversi ", celcius, "derajat celcius adalah ", kelvin, "derajat Kelvin")
suhu = Suhu()

suhu.celcius_to_fahrenheit(75)
suhu.celcius_to_reamur(60)
suhu.celcius_to_kelvin(90)
