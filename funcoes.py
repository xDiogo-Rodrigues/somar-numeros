def is_int(param):
        if not isinstance(param, int):
            raise TypeError('Os dados precisam ser números inteiros')
      
def somar(*args):
    return sum(args)


