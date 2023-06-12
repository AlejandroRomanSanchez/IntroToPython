numeros = list(range(0, 6))
cuadrado = 0
cubo = 0

print(f'number square cube')

for numero in numeros:
    cuadrado = numero *numero
    cubo = cuadrado * numero
    print(f'{numero :> 5}{cuadrado :> 8}{cubo :> 5}')


    

