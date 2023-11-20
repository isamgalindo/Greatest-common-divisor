def gcd(a, b):
	while b:
		a, b = b, a % b
		print(b)
	return a

numero1 = 48
numero2 = 18

maximo_divisor_comun = gcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {maximo_divisor_comun}")



