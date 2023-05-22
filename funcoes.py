def is_int(param):
        if not isinstance(param, int):
            raise TypeError('Os dados precisam ser números inteiros')
      
def somar(*args):
    return sum(args)

def criar_funcao(func,*args):
    def interna():
        for arg in args:
            is_int(arg)
        resultado = func(*args)
        return resultado
    return interna
