a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print(type(soma))
soma = str(soma)
# print(type(soma))
resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
      '\nMultiplicacao: {multiplicacao}'
      '\nDivisao: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                resto=resto,
                                divisao=divisao))
print(resultado)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)