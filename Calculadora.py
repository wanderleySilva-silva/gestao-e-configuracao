from Operacao import Operacao

class Calculadora:

    flag = True

    opr = Operacao

    while flag:

        print('Calculadora Python\n' + 
            '1. Soma\n' +
            '2. Subtracao\n' +
            '3. Multiplicacao\n' +
            '4. Divisao\n' +
            '5. Potencia\n' +
            '6. Sair')

        opcao = input('Escolha uma das opções listadas: ')

        if(opcao == '1'):
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
            print()

            print(opr.soma(a, b))
        
        elif(opcao == '2'):
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
            print()

            print(opr.subtracao(a, b))

        elif(opcao == '3'):
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
            print()

            print(opr.multiplicacao(a, b))
        
        elif(opcao == '4'):
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
            print()

            print(opr.divisao(a, b))
        
        elif(opcao == '5'):
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
            print()

            print(opr.potencia(a, b))
        
        elif(opcao == '6'):
            a = int(input('Digite um número e veja sua raiz quadrada: '))
            print()
            
            print(opr.radiciacao(a))
            
        elif(opcao == '7'):
            flag = False

        

    
