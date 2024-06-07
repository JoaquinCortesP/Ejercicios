def suma(*numeros):#los * lo transforman en iterables para empaquetar
    resultado=0
    for numero in numeros:
        resultado += numero
    print(resultado)

entrada = input("Ingrese los números separados por \"+\": ")
numeros = [float(num) for num in entrada.split("+")]

suma(*numeros)