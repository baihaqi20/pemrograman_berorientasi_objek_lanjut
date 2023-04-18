class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Aldo", 25)

try:
    alamat = person.alamat
    print("Alamat:", alamat)
except AttributeError:
    print("AttributeError terjadi! Mohon periksa kembali atribut yang diminta.")
