import random
import time

"""
print('-' * 48)

print('Aprovação de Empréstimo Bancário pra comprar uma casa')

valor_da_casa = float(input('\nQual o valor da casa?: R$'))
salário_do_comprador = float(input('Qual o salário do comprador?: R$'))
anos_a_pagar = int(input('Quantos anos a pagar?: '))

prestacao_mensal = (valor_da_casa / anos_a_pagar) / 12
porcentagem_do_salário = salário_do_comprador * 0.30

if prestacao_mensal >= porcentagem_do_salário:
    print('\nEmpréstimo negado devido a prestação mensal: R${:.2f} ser maior que 30% do salário: R${:.2f}'.format(
        prestacao_mensal, porcentagem_do_salário))
else:
    print('\nO valor da prestação mensal será: R${:.2f}'.format(prestacao_mensal))

print('-' * 48)

"""



'''print('-' * 48)

n = int(input('Digite um número (Decimal): '))
rn = int(input('\nDeseja converter esse número pra qual base?\n1 --> Binário\n2 --> Octal\n3 --> Hexadecimal\n\n'))

if rn == 1:
    print('\n{} ==> {}'.format(n, bin(n) [2:]))
elif rn == 2:
    print('\n{} ==> {}'.format(n, oct(n) [2:]))
else:
    print('\n{} ==> {}'.format(n, hex(n) [2:]))

print('-' * 48)
'''





'''print('-' * 48)
print('Qual o maior número? ou será que são iguais?...')

n1 = int(input('\nDigite o 1° Nº: '))
n2 = int(input('Digite o 2° Nº: '))

if n1 == n2:
    print('\n{} = {}'.format(n1, n2))
elif n1 > n2:
    print('\n{} => {}'.format(n1, n2))
else:
    print('\n{} <= {}'. format(n2, n1))
print('-' * 48)'''




'''print('-' * 48)

print('Vamos ver sua questão com relação ao exército...')

ano_de_nascimento = int(input('\nEm qual ano vc nasceu?: '))
idade = 2022 - ano_de_nascimento

if idade < 18:
    print('\nVc AINDA vai se alistar...\nAinda falta {} anos'.format(18 - idade))
elif idade == 18:
    print('\nJá É HORA de vc IR se alistar')
else:
    print('\nSua hora de ir alistar já PASSOU\nVc tinha que ter ido a {} anos'.format(idade - 18))

print('-' * 48)'''




"""print('-' * 48)
print('Vamos calcular a média da nota que vc tirou em alguma atividade!')

n1t = float(input('\nQual o valor TOTAL na 1° nota?: '))
n2t = float(input('Qual o valor TOTAL na 2° nota?: '))

n1 = float(input('\nQuanto vc tirou na 1° nota: '))
n2 = float(input('Quanto vc tirou na 2° nota: '))

nt = n1t + n2t

nmt1 = nt * 0.4
nmt2 = nt * 0.6
nmt3 = nt * 0.8

n = n1 + n2
pnmt = n - nmt3

print('\nA nota TOTAL é {:.1f}, a nota MÉDIA é {:.1f}, e a SUA NOTA foi: {:.1f}'.format(nt, nmt3, n))
print('Ou seja, vc tirou {:.1f} pontos a mais que a MÉDIA ({:.1f}|{:.1f})'.format(pnmt, n, nmt3))

if n >= nmt3:
    print('Sua nota foi boa, vc Passou!, PARABÉNS!!!')
elif n <= nmt1:
    print('Sua nota foi RUIM, vc REPROVOU seu BUNDA MOLE!!!')
else:
    print('Sua nota voi razoável, MARROMENO...')
    
print('-' * 48)"""






'''print('-' * 48)

print('Categoria de um atleta de acordo com sua idade')

ano = int(input('\nEm qual vc nasceu?: '))
idade = 2022 - ano

if idade <= 9:
    print('\nCom {} anos de idade é um atleta MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('\nCom {} anos de idade é um atleta INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('\nCom {} anos de idade é um atleta JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('\nCom {} anos de idade é um atleta SÊNIOR'.format(idade))
else:
    print('\nCom {} anos de idade é um atleta MASTER'.format(idade))

print('-' * 48)'''







'''print('-' * 48)

print('Calculadora de IMC')

peso = float(input('\nQual o seu peso? (kg/m²): '))
altura = float(input('Qual a sua altura? (m): '))

imc = peso / (altura * altura)

print('\nSeu imc é: {:.1f} kg/m²'.format(imc))

if imc <= 18.5:
    print('\nVc está ABAIXO do peso ideal')
elif imc > 18.5 and imc <= 25:
    print('\nVc está com o peso IDEAL')
elif imc > 25 and imc <= 30:
    print('\nVc está com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('\nVc está com SOBREPESO')
else:
    print('\nVc está com OBESIDADE MÓRBIDA')

print('-' * 48)'''







'''print('-' * 48)

print('Valor a ser pago')

pn = float(input('\nQual o valor original do produto?: R$'))

op = int(input('\nQual meio de pagamento vc quer?\n\n1 --> A vista em DINHEIRO/CHEQUE com 10% de desconto\n2 --> A vista no CARTÃO com 5% de desconto\n3 --> 2x no CARTÃO sem juros\n4 --> 3x ou mais no CARTÃO com 20% de JUROS\n\n'))

if op == 1:
    print('\nO preço total a pagar é: R${:.2f}'.format(pn - (pn * 0.10)))
elif op == 2:
    print('\nO preço total a pagar é: R${:.2f}'.format(pn - (pn * 0.05)))
elif op == 3:
    print('\nO preço total a pagar é: 2 x R${:.2f}'.format(pn / 2))
elif op == 4:
    j = float(input('Em quantas parcelas deseja pagar?: '))
    print('\nO preço total a pagar é: {:.0f} x R${:.2f}'.format(j, (pn + (j * (0.2 * pn))) / j))
else:
    print('\nNão inventa moda de não selecionar um dos números da opções acima')

print('-' * 48)'''


"""print('-' * 48)

print('Vamos jogar JOKENPÔ!!!')

ppt = int(input('\nPedra Papel Tesoura?\nSuas opções são:\n\n0 --> Pedra\n1 --> Papel\n2 --> Tesoura\n\nEu escolho: '))

nr = random.randint(0, 2)

if nr == 0 and 0 == ppt:
    print('O computador escolheu: 0 - Pedra!\n\nEMPATE')
elif nr == 0 and 1 == ppt:
    print('O computador escolheu: 0 - Pedra!\n\nVc GANHOU!!!')
elif nr == 0 and 2 == ppt:
    print('O computador escolheu: 0 - Pedra!\n\nVc PERDEU! As maquinas vão DOMINAR o Mundo!')

elif nr == 1 and 0 == ppt:
    print('O computador escolheu: 1 - Papel!\n\nVc PERDEU! As maquinas vão DOMINAR o Mundo!')
elif nr == 1 and 1 == ppt:
    print('O computador escolheu: 1 - Papel!\n\nEMPATE')
elif nr == 1 and 2 == ppt:
    print('O computador escolheu: 1 - Papel!\n\nVc GANHOU!!!')

elif nr == 2 and 0 == ppt:
    print('O computador escolheu: 2 - Tesoura!\n\nVc GANHOU!!!')
elif nr == 2 and 1 == ppt:
    print('O computador escolheu: 2 - Tesoura!\n\nVc PERDEU! As maquinas vão DOMINAR o Mundo!')
elif nr == 2 and 2 == ppt:
    print('O computador escolheu: 2 - Tesoura!\n\nEMPATE')

else:
    print('\nNão inventa moda de não selecionar uma das opções acima!\nSeu BUNDA MOLE!!!')

print('-' * 48)"""



'''

print('-' * 48)
print('Contagem regressiva pra explosão de fogos!\n')

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print('\nBOOOOOMMMM!!!')

print('-' * 48)'''




print('-' * 48)
n = int(input('Quais o números PAR dentro no número: '))
print(' -' * 24)

for c in range(0, n, 2):
    print(c)

print('-' * 48)




print('-' * 48)
n = int(input(''))