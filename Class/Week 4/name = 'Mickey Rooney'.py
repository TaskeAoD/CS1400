name = 'Mickey Rooney'
score = 36

#Use default empty space fill character
print(f'{name:<16}{score:>6}')

#Use '0' as a fill character for score
print(f'{name:0<16}{score:0>6}')

#Use '_' as fill character for name
print(f'{name:_<16}{score:0>6}')