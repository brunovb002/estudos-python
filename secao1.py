
# %% Exercício 1 - Juros compostos
# Peça valor inicial, taxa mensal e número de meses, e mostre o valor final com 2 casas.
# Teste: 1000, 1% e 12 meses -> 1126.83

capital = float(input('Qual valor você deseja investir? '))
tempo = int(input('Por quantos meses? '))
juros = float(input('Qual a taxa de juro (em %) '))

juros = juros/100


montante = capital *(1 +juros)**tempo 

print(f'Esse será seu montante: {montante:.2f}')



# %% Exercício 2 - Par ou ímpar
# Peça um número inteiro e diga se é par ou ímpar.
# Se a pessoa digitar algo que não é número, mostre uma mensagem de erro sem o programa quebrar.
# Teste: 7 -> ímpar; abc -> mensagem de erro

valor = input('digite seu número: ')

try:
    valor = int(valor)
    resto = valor%2
    if resto == 0:
        print(valor, 'é um número par')
    else:
        print(valor,'é um número impar')
except ValueError:
    print('Digite um número inteiro válido')

# %% Exercício 3 - Alíquota por prazo
# Peça o número de dias e mostre a alíquota:
# até 180 dias, 22,5%; até 360, 20%; até 720, 17,5%; acima disso, 15%.
# A tabela é só para o exercício.
# Testes: 180 -> 22,5%; 181 -> 20%; 721 -> 15%; 0 ou negativo -> inválido

dias = input('Quantos dias? ')

try:
    dias = int(dias)
    if 0 < dias <= 180:
        print('A aliquota será de 22,5%')
    elif 180 < dias <= 360:
        print('A aliquota será de 20%')
    elif 360 <= dias <= 720:
        print('A aliquota será de 17,5%')
    elif 720 < dias:
        print('A aliquota será de 15%')
    else:
        print('número negativo e zero nao pode')

except ValueError:
    print('Digite um valor válido')

# %% Exercício 4 - Contador de vogais
# Peça uma palavra e conte as vogais, aceitando maiúsculas e minúsculas.
# Teste: Programacao -> 5


# %% Exercício 5 - Validador de ticker
# Um ticker válido tem 4 letras seguidas de 1 ou 2 dígitos.
# Testes: PETR4 e BOVA11 -> válidos; ABC, PETRA e PETR123 -> inválidos


# %% Exercício 6 - Palíndromo
# Verifique se um texto é igual de trás para frente, ignorando espaços e sem usar [::-1].
# Testes: arara e ame a ema -> sim; python -> não


# %% Exercício 7 - FizzBuzz
# Mostre os números de 1 a 30, trocando múltiplos de 3 por Fizz, de 5 por Buzz e de ambos por FizzBuzz.
# Teste: 15 -> FizzBuzz


# %% Exercício 8 - Tempo para dobrar
# Usando while, descubra quantos meses um valor leva para dobrar a uma taxa mensal fixa.
# Teste: 1% ao mês -> 70 meses


# %% Exercício 9 - Adivinhação
# Defina um número secreto de 1 a 100 e dê 7 tentativas.
# A cada erro, diga se o número é maior ou menor e, no fim, mostre se a pessoa ganhou ou perdeu.
# Teste: a última tentativa certa ainda deve contar como vitória


# %% Exercício 10 - Taxas diárias
# Sem usar min, max ou sum, ache a menor taxa, a maior e a média, ignorando os None.
# Teste: [10.5, None, 11.2, 9.8, None, 12.0] -> 9.8, 12.0 e 10.875


# %% Exercício 11 - Segundo maior
# Ache o segundo maior valor distinto, sem usar sort, sorted ou max.
# Testes: [5, 8, 8, 3, 7] -> 7; [4, 4] -> não existe


# %% Exercício 12 - Extrato
# Começando com saldo zero, percorra as movimentações e mostre o saldo final,
# o menor saldo e a posição da primeira que deixou o saldo negativo.
# Teste: [1000, -200, -900, 500, -100] -> final 300, menor -100, posição 2 (contando do zero)