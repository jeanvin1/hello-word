import calendar
import random
import cmath

    #Hello World

print('Hello World!')
x = input('Digite alguma coisa que deseja: ')
print(x)

    #Calculadora de Soma

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
s = n1 + n2 
print('A soma de {} + {} é igual a = {}'.format(n1, n2, s))

    #Identificador

v1 = input('Digite alguma coisa: ')

print('Qual tipo/classe?', type(v1))

print('É alunm?', v1.isalnum())
print('É alpha?', v1.isalpha())
print('É ascii?', v1.isascii())
print('É decimal?', v1.isdecimal())
print('É digit?', v1.isdigit())
print('É identifier?', v1.isidentifier())
print('É lower?', v1.islower())
print('É numeric?', v1.isnumeric())
print('É printable?', v1.isprintable())
print('É space?', v1.isspace())
print('É title?', v1.istitle())

    #Calculadora Geral

n1 = float(input('D1: '))
n2 = float(input('D2: '))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A resultado é: Soma = {:.3f} | Subtração = {:.3f} | Multiplicação = {:.3f} | Divisão = {:.3f}'.format(s, sb, m, d))
print('Divisão Inteira = {:.3f} | Exponenciação = {:.3f}'.format(di, e))

    #Calculadora Geral [OTIMIZADO]

n1 = float(input('D1: '))
n2 = float(input('D2: '))

print('A resultado é: Soma = {:.3f} | Subtração = {:.3f} | Multiplicação = {:.3f} | Divisão = {:.3f}'.format(
    (n1 + n2), (n1 - n2), (n1 * n2), (n1 / n2)))
print('Divisão Inteira = {:.3f} | Exponenciação = {:.3f}'.format((n1 // n2), (n1 ** n2)))

    #Reconhecimento de antecessor e sucessor

n = int(input('Digite um número: '))
n1 = (n) - 1
n2 = (n) + 1
print('Antecessor = {} | Sucessor = {}'.format(n1, n2))

    #Reconhecimento de antecessor e sucessor [OTIMIZADO]

n = int(input('Digite um número: '))
print('Antecessor = {} | Sucessor = {}'.format(((n) - 1), ((n) + 1)))

    #Calculadora de dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5
print('O dobro é: {} | O triplo é: {} | A raiz quadrada é: {:.3f}'.format(d, t, r))

    #Calculadora de dobro, triplo e raiz quadrada [OTIMIZADO]

n = int(input('Digite um número: '))
print('O dobro é: {} | O triplo é: {} | A raiz quadrada é: {:.3f}'.format((n*2), (n*3), (n**0.5)))

    #Calculadora de média

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A média é: {:.1f}'.format(m))

    #Calculadora de média [OTIMIZADO]

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('A média é: {:.1f}'.format((n1 + n2) / 2))

    #Calculadora (Multiplicação/Divisão) /Gerador de tabuada (Multiplicação/Divisão)

n = float(input('Digite um número: '))

m0 = n * 0
m1 = n * 1
m2 = n * 2
m3 = n * 3
m4 = n * 4
m5 = n * 5
m6 = n * 6
m7 = n * 7
m8 = n * 8
m9 = n * 9
m10 = n * 10

print('Tabuada de Multiplicação \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(
    m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10))

d1 = n / 1
d2 = n / 2
d3 = n / 3
d4 = n / 4
d5 = n / 5
d6 = n / 6
d7 = n / 7
d8 = n / 8
d9 = n / 9
d10 = n / 10

print('Tabuada de Divisão \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f} \n {:.3f}'.format(
    0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10))

    #Calculadora (Multiplicação/Divisão) /Gerador de tabuada (Multiplicação/Divisão) [OTIMIZADO]

n = float(input('Digite um número: '))
print('_' * 16)
print('Tabuada de Multiplicação')

print('{:.0f} x {:2} = {:.0f}'.format(n, 0, n*0))
print('{:.0f} x {:2} = {:.0f}'.format(n, 1, n*1))
print('{:.0f} x {:2} = {:.0f}'.format(n, 2, n*2))
print('{:.0f} x {:2} = {:.0f}'.format(n, 3, n*3))
print('{:.0f} x {:2} = {:.0f}'.format(n, 4, n*4))
print('{:.0f} x {:2} = {:.0f}'.format(n, 5, n*5))
print('{:.0f} x {:2} = {:.0f}'.format(n, 6, n*6))
print('{:.0f} x {:2} = {:.0f}'.format(n, 7, n*7))
print('{:.0f} x {:2} = {:.0f}'.format(n, 8, n*8))
print('{:.0f} x {:2} = {:.0f}'.format(n, 9, n*9))
print('{:.0f} x {:2} = {:.0f}'.format(n, 10, n*10))

print('_' * 16)
print('Tabuada de Divisão')

print('{:.0f} x {:2} = {:.3f}'.format(n, 0, 0))
print('{:.0f} x {:2} = {:.3f}'.format(n, 1, n/1))
print('{:.0f} x {:2} = {:.3f}'.format(n, 2, n/2))
print('{:.0f} x {:2} = {:.3f}'.format(n, 3, n/3))
print('{:.0f} x {:2} = {:.3f}'.format(n, 4, n/4))
print('{:.0f} x {:2} = {:.3f}'.format(n, 5, n/5))
print('{:.0f} x {:2} = {:.3f}'.format(n, 6, n/6))
print('{:.0f} x {:2} = {:.3f}'.format(n, 7, n/7))
print('{:.0f} x {:2} = {:.3f}'.format(n, 8, n/8))
print('{:.0f} x {:2} = {:.3f}'.format(n, 9, n/9))
print('{:.0f} x {:2} = {:.3f}'.format(n, 10, n/10))

    #Conversor de metros para centímetros e milímetro

n = float(input('Digite um número(metros): '))
c = n * 100
m = n * 1000
print('Centímetros: {:.0f} | Milímetros: {:.0f}'.format(c, m))

    #Conversor de metros para centímetros e milímetro [OTIMIZADO]

n = float(input('Digite um número(metros): '))
print('Centímetros: {:.0f} | Milímetros: {:.0f}'.format((n * 100), (n * 1000)))

    #Conversor de Dólar

n = float(input('Quanto reais vc tem?: '))
d = n / 5.16
print('Vc tem {:.2f} doralis'.format(d))

    #Conversor de Dólar [OTIMIZADO]

n = float(input('Quanto reais vc tem?: '))
print('Vc tem {:.2f} doralis'.format(n / 5.16))

    #Calculadora de área e quantidade de tinta por metro quadrado

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = l * a
qtl = ar / 2
print('A área da parede é: {:.3f} metros ao quadrado | E a quantidade de tinta necessária é: {:.3f} litros'.format(l * a, qtl))

#Calculadora de área e quantidade de tinta por metro quadrado [OTIMIZADO]

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

print('A área da parede é: {:.3f} metros ao quadrado | E a quantidade de tinta necessária é: {:.3f} litros'.format(
    (l * a), (l * a) / 2))

    #Calculadora de desconto (5%)

p = float(input('Digite o preço do produto: '))
pp = p * 0.05
pd = p - pp
print('O preço com 5% de desconto é: {:.2f}'.format(pd))

    #Calculadora de desconto (5%) [OTIMIZADO]

p = float(input('Digite o preço do produto: '))
print('O preço com 5% de desconto é: {:.2f}'.format(p - (p * 0.05)))

    #Calculadora de aumento de salário em % (15%)

si = float(input('Digite o salário: '))
sp = si * 0.15
sf = si + sp
print('O salário com 15% de aumento é: {:.2f}'.format(sf))

    #Calculadora de aumento de salário em % (15%) [OTIMIZADO]

si =float(input('Digite o salário: '))
print('O salário com 15% de aumento é: {:.2f}'.format(si + (si * 0.15)))

    #Conversor de centigrados para fahrenheit

v = float(input('Digite uma tempertura: °C '))
f = (v * 9/5) + 32
print('Convertido pra °F temos: °F {}'.format(f))

    #Conversor de centigrados para fahrenheit [OTIMIZADO]

v = float(input('Digite uma tempertura: °C '))
print('Convertido pra °F temos: °F {}'.format((v * 9 / 5) + 32))

    #Calculadora de """estadia"""

kmp = float(input('Quantos Km vc rodou com o carro?: '))
dal = float(input('Quantos dias esse carro está alugado?: '))
pa = (dal * 60) + (kmp * 0.15)
print('O preço a pagar é de: R${:.2f}'.format(pa))

    #Calculadora de """estadia""" [OTIMIZADO]

kmp = float(input('Quantos Km vc rodou com o carro?: '))
dal = float(input('Quantos dias esse carro está alugado?: '))
print('O preço a pagar é de: R${:.2f}'.format((dal * 60) + (kmp * 0.15)))

    #Arredondador pra interos

import math
n = float(input('Digite um número: '))
print('Porção inteira é: {}'.format(math.trunc(n)))

    #Calculadora de Hipotenusa

co = float(input('Qual o comprimento do cateto oposto?: '))
ca = float(input('Qual o comprimento do cateto adjacente?: '))

print('O comprimento da hipotenusa é: {:.3f}'.format(math.sqrt(math.pow(co, 2) + math.pow(ca, 2))))
print('O comprimento da hipotenusa é: {:.3f}'.format(math.hypot(co, ca)))

    #Calculadora de Seno, Cosseno e Tangente

import cmath
a = float(input('Digite um ângulo: '))
print('Seno: {:.3f} | Cosseno: {:.3f} | Tangente: {:.3f}'.format((cmath.sin(a)), (cmath.cos(a)), (cmath.tan(a))))

    #Sorteador de nomes

lt = input('Primeira aluno: '), \
    input('Segunda aluno: '),  \
    input('Terceira aluno: '), \
    input('Quarta aluno: ')

print('\nO escolhido foi: {}'.format(random.choice(lt)))

    #Sorteador de nomes em ordem

p1 = str(input('Primeira aluno: '))
p2 = str(input('Segunda aluno: '))
p3 = str(input('Terceira aluno: '))
p4 = str(input('Quarta aluno: '))

lt = [p1, p2, p3, p4]
random.shuffle(lt)

print('\nO escolhido foi: {}'.format(lt))

    #Reprodutor de Áudio

'''pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('Python/Áudios/teste.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()'''

    #Identificador de UDCM

n = float(input('Digite um número: '))

#print('unidade: {3} \ndezenas: {2} \ncentenas: {1} \nmilhar: {0}'.format((n[0]), (n[1]), (n[2]), (n[3])))
print('unidade: {:.0f} \ndezenas: {:.0f} \ncentenas: {:.0f} \nmilhar: {:.0f}'.format(
    (n // 1 % 10), (n // 10 % 10), (n // 100 % 10), (n // 1000 % 10)))

    #Reconhecedor do nome "Santo"

c = str(input('Digite um nome de uma cidade: '))

print('Essa cidade começa com santo?: {}'.format('SANTO' in (((c.upper()).split())[0])))

    #Reconhecedor do nome "Silva"

n = str(input('Digite um nome: '))

print('Esse nome tem SILVA?: {}'.format('SILVA' in(n.upper())))

    #Reconhecimento 'geral' da letra A

fr = str(input('Digite uma frase: ')).strip()

print('A letra A aparece: {} vezes'.format(((fr.upper()).count('A'))))
print('A letra A aparece primeiro em: {}'.format((fr.upper()).find(('A') + 1)))
print('A letra A aparece por último em: {}'.format((fr.upper()).rfind('A')))

    #Identificador do primeiro e último nomes

n = input('Digite um nome: ')

print('Primeiro nome: {}'.format((n.split())[0]))
print('Ultimo nome: {}'.format((n.split())[(len(n.split())) - 1]))

    #Editor de nome 'geral'

n = str(input('Digite o um nome: '))
print(n.upper())
print(n.lower())
print(len(''.join(n.split())))
print(len((n.split())[0]))

    #Calculadora de Média de 2 notas (Versão avançada 1)

print('_' * 48)
print('\nVamos calcular a média da nota que vc tirou em alguma atividade!')

n1t = float(input('\nQual o valor TOTAL na 1° nota?: '))
n2t = float(input('Qual o valor TOTAL na 2° nota?: '))

n1 = float(input('\nQuanto vc tirou na 1° nota: '))
n2 = float(input('Quanto vc tirou na 2° nota: '))

nt = (n1t + n2t)
nmt = (n1t + n2t) * 0.6
n = (n1 + n2)
pnmt = n - nmt

print('\nA nota TOTAL é {:.1f}, a nota MÉDIA é {:.1f}, e a SUA NOTA foi: {:.1f}'.format(nt, nmt, n))
print('Ou seja, vc tirou {:.1f} pontos a mais que a MÉDIA ({:.1f}|{:.1f})'.format(pnmt, n, nmt))

if n >= nmt:
    print('Sua nota foi boa PARABÉNS!!!')
else:
    print('Sua nota foi RUIM, seu BUNDA MOLE!!!')
print('_' * 48)
print(' ')

    #Adivinhe o número

print('-' * 48)
n = int(input('\nTente adivinhar um número de 0 a 5: '))
nr = random.randint(0, 5)

if n == nr:
    print('\nPARABÉNS vc ACERTOU!!!')
else:
    print('\nDeu RUIM vc ERROU!!!\nO número certo é {}'.format(nr))
print('_' * 48)
print(' ')

    #Par ou Ímpar?

print('-' * 48)
n = int(input('Digite um número: '))

if (n % 2) == 0:
    print('\nEsse número {}, é PAR'.format(n))
else:
    print('\nEsse número {}, é ÍMPAR'.format(n))
print('-' * 48)

    #Se passar de 200km é mais barato

print('-' * 48)
km = float(input('Digite a quantidade de Km da sua viajem: '))

if km <= 200:
    print('\nO preço a pagar por {}km é: R${:.2f}'.format((km), (km * 0.50)))
else:
    print('\nO preço a pagar por {}km é: R${:.2f}'.format((km), (km * 0.45)))
print('-' * 48)

    #Será que é Bissesto?

print('-' * 48)
a = int(input('Digite um ANO: '))

if calendar.isleap(a):
    print('\n{} é um ano BISSESTO!'.format(a))
else:
    print('\n{} NÃO é um ano BISSESTO!'.format(a))
print('-' * 48)

    #Qual o maior número?

print('-' * 48)
print('Digite 3 números')

n1 = float(input('\n1°: '))
n2 = float(input('2°: '))
n3 = float(input('3°: '))

n = [n1, n2, n3]

print('\nO maior número é: {}'.format(max(n)))
print('O menor número é: {}'.format(min(n)))
print('-' * 48)

    #Quanto maior o salário melhor

print('-' * 48)
s = float(input('Digite a quantidade de um salário: R$'))

if s >= 1250:
    print('\nSeu salário tera um aumento de 10%: R${:.2f}'.format(
        (s * 0.10) + s))
else:
    print('\nSeu salário tera um aumento de 15%: R${:.2f}'.format(
        (s * 0.15) + s))
print('-' * 48)

    #Dá pra fazer um triângulo?

print('-' * 48)

r1 = float(input('Digite o valor do 1° segmento: '))
r2 = float(input('Digite o valor do 2° segmento: '))
r3 = float(input('Digite o valor do 3° segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\nEsses segmentos PODEM formar um TRIÂNGULO!')
else:
    print('\nEsses segmentos NÃO podem formar um TRIÂNGULO')

print('-' * 48)

    #Vai dar multa?

print('_' * 48)
v1 = float(input('\nA qual velocidade vc está Km/h: '))

if v1 < 80:
    print('\nTudo OK')
else:
    print('\nVocê deve reduzir a velocidade!\nE tmb vai receber uma multa no valor de: R${:.2f}'.format(
        (v1 - 80) * 7))
print('_' * 48)
print(' ')

