
num1 = int(input("Digite o primeiro número:\n "))
num2 = int(input("Digite o segundo número:\n "))


sum = num1 + num2
print(f"A soma de {num1} e {num2} é {sum}")     
sub = num1 - num2
print(f"A subtração de {num1} e {num2} é {sub}")
div = num1 / num2
print(f"A divisão de {num1} e {num2} é {div}")
mult = num1 * num2
print(f"A multiplicação de {num1} e {num2} é {mult}")
mod = num1 % num2
print(f"O módulo de {num1} e {num2} é {mod}")   
expo = num1 ** num2 
print(f"O exponencial de {num1} e {num2} é {expo}")


# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}?  {bigger_equal}")

# Atribuição
num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1
