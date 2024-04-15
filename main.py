
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro: Não é possivel fazer essa operação com 0'
    
num1 = float(input('Digite o primeiro numero:\n'))
print(f'Você digitou {num1}\n')

num2 = float(input('Digite o segundo numero:\n'))
print(f'Você digitou {num2}\n')

print('Operadores:')
print('+ -> Adição')
print('- -> Subtração')
print('X -> Multiplicação')
print('/ -> Divisão')

operador = input('Digite o operador da conta ( + | - | X | / ) ')

if operador == '+':
    print('Resultado:', adicao(num1, num2))
elif operador == '-':
    print('Resultado:', subtracao(num1,num2))
elif operador == 'x':
    print('Resultado:', multiplicacao(num1, num2))
elif operador == '/':
    print('Resutaldo:', divisao(num1, num2))




    
