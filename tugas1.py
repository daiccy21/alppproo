def cek_angka(a, b, c):
    return a != b and a != c and b != c and (a + b == c or a + c == b or b + c == a)

print(cek_angka(1, 2, 3))  
print(cek_angka(1, 1, 2))  
print(cek_angka(2, 3, 5))  
print(cek_angka(1, 2, 4))  