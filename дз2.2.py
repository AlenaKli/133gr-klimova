import math

def calculate_gravitational_force(mass2, distance):
    mass1 = 5.972e24 # Масса Земли в кг
    G = 6.67430e-11 # Гравитационная постоянная
    force = (G * mass1 * mass2) / math.pow(distance, 2)
    return force

mass_planet = float(input("Введите массу планеты (в кг): "))
distance = float(input("Введите расстояние между Землей и планетой (в метрах): "))

gravitational_force = calculate_gravitational_force(mass_planet, distance)
print("Сила гравитации между Землей и планетой:", gravitational_force, "Н")
