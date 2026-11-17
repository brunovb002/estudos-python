
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

contador = 0
vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Digite uma palavra: ')
palavra = palavra.lower()

for i in palavra:
    if i in vogais:
        contador += 1
print('Sua palavra tem ', contador, 'vogais')   


# %% Exercício 5 - Validador de ticker
# Um ticker válido tem 4 letras seguidas de 1 ou 2 dígitos.
# Testes: PETR4 e BOVA11 -> válidos; ABC, PETRA e PETR123 -> inválidos

ticker = input('Digite seu ticker: ')
ticker = ticker.upper()

literal = ticker[:4]
numerico = ticker[4:]
tamanho = len(numerico)

if literal.isalpha(): 
    if (tamanho == 1 or tamanho == 2) and numerico.isdigit():
        print(ticker, 'é um ticker válido!')

    else:
        print(ticker, 'não é um ticker valido.')
else:
    print(ticker, 'não é um ticker valido.')




# %% Exercício 6 - Palíndromo
# Verifique se um texto é igual de trás para frente, ignorando espaços e sem usar [::-1].
# Testes: arara e ame a ema -> sim; python -> não

texto = input('Digite um texto: ')
texto = texto.lower().replace(' ', '')

# Modo 1 
palindromo = True
for i in range(len(texto) // 2):
    if texto[i] != texto[len(texto) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print('Forma 1: é palíndromo')
else:
    print('Forma 1: não é palíndromo')

# Alternativa
invertido = ''
for letra in texto:
    invertido = letra + invertido

if invertido == texto:
    print('Forma 2: é palíndromo')
else:
    print('Forma 2: não é palíndromo')




# %% Exercício 7 - FizzBuzz
# Mostre os números de 1 a 30, trocando múltiplos de 3 por Fizz, de 5 por Buzz e de ambos por FizzBuzz.
# Teste: 15 -> FizzBuzz

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    


# %% Exercício 8 - Tempo para dobrar
# Usando while, descubra quantos meses um valor leva para dobrar a uma taxa mensal fixa.
# Teste: 1% ao mês -> 70 meses

taxa = float(input('Qual a taxa mensal (em %)? '))
taxa = taxa / 100
valor = 100
contador = 0
valor_corrigido = 0
valord = 100

while valor_corrigido < (valord * 2):
    valor_corrigido = valor * (1 + taxa)
    valor = valor_corrigido
    contador += 1 

print('Serão necessários ', contador, ' meses para duplicar seu valor')



# V2 

taxa = float(input('Qual a taxa mensal (em %)? '))
taxa = taxa / 100

valor = 100
alvo = valor * 2
meses = 0

while valor < alvo:
    valor = valor * (1 + taxa)
    meses += 1

print(f'Serão necessários {meses} meses para dobrar seu valor')





# %% Exercício 9 - Adivinhação
# Defina um número secreto de 1 a 100 e dê 7 tentativas.
# A cada erro, diga se o número é maior ou menor e, no fim, mostre se a pessoa ganhou ou perdeu.
# Teste: a última tentativa certa ainda deve contar como vitória

import random

secreto = random.randint(1,100)
numero = 0
contador = 0 

print('Tente advinhar o número secreto, ele está entre 1 e 100!')

while contador < 7:
    numero = int(input('Digite um número: '))
    contador += 1

    if numero < secreto:
        print ('o número é maior que ', numero)
    elif numero > secreto:
        print ('o número é menor que ', numero)
    else:
        print('Parabens, voce acertou!!')
        break

if numero != secreto:
    print('Voce esgotou as 7 tentativas, tente novamente. O número secreto era ', secreto )   
    



# %% Exercício 10 - Taxas diárias
# Sem usar min, max ou sum, ache a menor taxa, a maior e a média, ignorando os None.
# Teste: [10.5, None, 11.2, 9.8, None, 12.0] -> 9.8, 12.0 e 10.875

taxas = [10.5, None, 11.2, 9.8, None, 12.0]

menor = None
maior = None
soma = 0
quantidade = 0

for taxa in taxas:
    if taxa is None:
        continue  
    
    if menor is None or taxa < menor:
        menor = taxa
    if maior is None or taxa > maior:
        maior = taxa

    soma += taxa
    quantidade += 1

media = soma / quantidade

print('Menor taxa:', menor)
print('Maior taxa:', maior)
print('Média:', media)



# %% Exercício 11 - Segundo maior
# Ache o segundo maior valor distinto, sem usar sort, sorted ou max.
# Testes: [5, 8, 8, 3, 7] -> 7; [4, 4] -> não existe

numeros = [5, 8, 8, 3, 7]

maior = None
segundo = None

for n in numeros:
    if maior is None or n > maior:        
        segundo = maior
        maior = n
    elif n != maior and (segundo is None or n > segundo):
                segundo = n

if segundo is None:
    print('Não existe segundo maior')
else:
    print('Segundo maior:', segundo)





# %% Exercício 12 - Extrato
# Começando com saldo zero, percorra as movimentações e mostre o saldo final,
# o menor saldo e a posição da primeira que deixou o saldo negativo.
# Teste: [1000, -200, -900, 500, -100] -> final 300, menor -100, posição 2 (contando do zero)

movimentacoes = [1000, -200, -900, 500, -100]

saldo = 0
menor_saldo = 0
primeira_negativa = None

for i in range(len(movimentacoes)):
    saldo += movimentacoes[i]

    if saldo < menor_saldo:
        menor_saldo = saldo

    
    if saldo < 0 and primeira_negativa is None:
        primeira_negativa = i

print('Saldo final:', saldo)
print('Menor saldo:', menor_saldo)

if primeira_negativa is None:
    print('O saldo nunca ficou negativo')
else:
    print('Primeira movimentação que deixou o saldo negativo: posição', primeira_negativa)



# %%
