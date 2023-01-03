def Calc(n1,op,n2):
    if op == '+':
        return soma(n1,n2)
    elif op == '-':
        return sub(n1,n2)
    elif op == '*':
        return mult(n1,n2)
    elif op == '/':
        return div(n1,n2)
    else:
        return 'Operador invalido'
def soma( n1,n2):
    return n1+n2
def sub( n1,n2):
    return n1-n2
def mult( n1,n2):
    return n1*n2
def div( n1,n2):
    return n1/n2
def procentage(n1):
    return n1*.01