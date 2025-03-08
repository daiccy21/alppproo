celcius_ke_fahrenheit = lambda c: (9/5) * c + 32
celcius_ke_reamur = lambda c: 0.8 * c

print(f"C = 100, F = {int(celcius_ke_fahrenheit(100))}") 
print(f"C = 80, R = {(int(celcius_ke_reamur(80)))}") 
print(f"C = 0, F = {(int(celcius_ke_fahrenheit(0)))}")