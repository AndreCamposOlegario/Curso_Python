n = input('Digite algo: ')

print('É um número? ', n.isnumeric())

print('É uma letra? ', n.isalpha())

print('É um alfanumérico? ', n.isalnum())

print('Esta minúsculo? ', n.islower())

print('Esta maiúsculo?', n.isupper())

print(type(n))
