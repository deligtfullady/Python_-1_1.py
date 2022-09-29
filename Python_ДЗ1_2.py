# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Ведеите x: "))
y = int(input("Ведеите y: "))
z = int(input("Ведеите z: "))
print(not (x or y or z)) == (not (x and y and z))