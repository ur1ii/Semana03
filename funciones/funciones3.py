#Registrar las edades de n cantidad de personas y mostrar la edad mas alta y mas baja y la cantidad de personas registradas
#
ages = []

def addAge(age):
    ages.append(age)
    return 0

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        maxAge = age
    return maxAge

def getMinAge():
    minAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
        return minAge
def showSize():
    return len(ages)

def showAges():
    return ages

while True:
    try:
        age = int(input("Ingresa tu edad: "))
        if age > 0:
            addAge(age)
        else:
            print("Debe ser un numero positivo")
        answer = input("Ingresar otro [S - N]: ")
        if answer.upper() != "S":
            break
    except ValueError:
        print("Debe ingresar un numero entero.")

print("Mostrar edades")
print(f"La cantidad de edades registradas es: {showSize()}")
print(showAges())
print(f"La edad mayor es: {getMaxAge()}")
print(f"La edad menor es: {getMinAge()}")


