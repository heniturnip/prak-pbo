username = 'informatika'
password = '12345678'
i=0

while i < 3:
    user = str(input('Username Anda = '))
    passw =str(input('Password Anda = '))
    if user == username and passw == password:
        print('Berhasil login!')
        i=4
    else:
        print('Username atau password salah, coba lagi')
        i=i+1

