#-*- coding: utf-8 -*-
conectivos_Binarios = ['Y','O','>']
letrasProposicionales = ['p','q','r']


#CLASES Y FUNCIONES
#####################################################################


class Tree():
    def __init__(self, l, iz ,der ):
        self.label = l
        self.left = iz
        self.right = der


def In_order(Arb):
    if Arb.label in letrasProposicionales:
        return Arb.label
    elif Arb.label =='-':
        return Arb.label + In_order(Arb.right)
    elif Arb.label in conectivos_Binarios:
        return "("+ In_order(Arb.left)+ Arb.label + In_order(Arb.right)+")"

#Función que determina el valor de verdad de un árbol depediendo de cierta interpretación

def Valor_verdad(Arb, Inte):
    if Arb.right == None:
        return Inte[Arb.label]
    elif Arb.label == '-':
        if Valor_verdad(Arb.right, Inte) == 1:
            return 0
        else:
            return 1
    elif Arb.label == 'Y':
        if Valor_verdad(Arb.left, Inte) == 1 and Valor_verdad(Arb.right,Inte) == 1 :
            return 1
        else:
            return 0
    elif Arb.label == 'O':
        if Valor_verdad(Arb.left,Inte) == 1 or Valor_verdad(Arb.right,Inte) == 1 :
            return 1
        else:
            return 0
    elif Arb.label == '>':
        if Valor_verdad(Arb.left,Inte) ==0 or Valor_verdad(Arb.right,Inte) == 1 :
            return 1
        else:
            return 0

#Teniendo en cuenta los valores de verdad de dos árboles en todas las interpretaciones posibles, esta función determina si los árboles son equivaletes o no
def Equivalencia(Arb1, Arb2):
    print "=> "+In_order(Arb1)+" es equivalente a "+In_order(Arb2)+"? "

    for i in interp:
        y = Valor_verdad(Arb1, i)
        x = Valor_verdad(Arb2, i)
        if x != y:
            return " No, no son equivalentes"

    return " Si, son equivalentes"

#############################################################################################################################################################################
#Creamos todas las interpretaciones posibles para tres letras proposicionales(p,q,r)

interp = []
prim_inter  = {}

for i in letrasProposicionales:
    prim_inter[i] = 1

interp.append(prim_inter)

for a in letrasProposicionales:
    interp_auxiliar= [i for i in interp]
    for i  in interp_auxiliar:
        segun_interp = {}
        for b in letrasProposicionales:
            if a ==b:
                segun_interp[b] = 1- i[b]
            else:
                segun_interp[b] = i[b]
        interp.append(segun_interp)




P = Tree('p',None, None )
Q = Tree('q',None,None )
R = Tree('r', None, None)
noP = Tree('-', None, P)
noQ = Tree('-', None, Q)

#Ejercicio 5
A1 = Tree('Y', P, Tree('O', Q, R))
A2 = Tree('O', Tree('Y',P, Q), Tree('Y', P, R))
A3 = Tree ('O', P, Q)
A4 = Tree('-', None, Tree('Y', noP, noQ))
A5 = Tree('Y', P , Q)
A6 = Tree('-',  None, Tree('O', noP, noQ))
A7 = Tree('>', P,Q)
A8 = Tree('O', noP, Q)

#*****************************
print  Equivalencia(P, noP)+"\n"
print  Equivalencia(A3, A4)+"\n"
print  Equivalencia(A5, A6)+"\n"
print  Equivalencia(A7, A8)+"\n"
