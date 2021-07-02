class Operacao:

    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        if(b == 0):
            return 'A operação não pode ser efetuada'
        else:
            return a / b
    
    def potencia(a, b):
        if(b == 0):
            return 1
        else:
            return a**b
    
    def radiciacao(a):
        return a**0.5
