
def red(var):
    return '\033[0;31m' + str(var) + '\033[m'
    
def grisoscuro(var):
    return '\033[0;30m' + str(var) + '\033[m'

def blanco_bold(var):
    return '\033[0;1m' + str(var) + '\033[m'
    
def gris(var):
    return '\033[0;2m' + str(var) + '\033[m'
    
def blanco(var):
    return '\033[0;3m' + str(var) + '\033[m'
    
def subrayado(var):
    return '\033[0;4m' + str(var) + '\033[m'
    
def inverso(var):
    return '\033[0;7m' + str(var) + '\033[m'
    
def rojo_subrayado_negrita(var):
    return '\033[31;4;1m' + str(var) + '\033[m'
    
def red_bold(var):
    return '\033[31;1m' + str(var) + '\033[m'

def verde(var):
    return '\033[0;32m' + str(var) + '\033[m'

def amarillo(var):
    return '\033[0;33m' + str(var) + '\033[m'

def azul(var):
    return '\033[0;34m' + str(var) + '\033[m'
    
def color(var):
    return '\033[0;35m' + str(var) + '\033[m'
    
def morado(var):
    return '\033[2;35m' + str(var) + '\033[m'
def morado2(var):
    return '\033[1;35m' + str(var) + '\033[m'
    
def bonito(var):
    var= var.replace('[', verde('[')).replace(']', verde(']')).replace('\'', azul('\'')).replace(',', amarillo(','))
    var= var.replace('<', morado('<')).replace('>', morado('>')).replace(morado('<')+'type',morado('<')+morado2('type'))
    return var
