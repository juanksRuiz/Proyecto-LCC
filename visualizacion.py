#-*-coding: utf-8-*-
# Miguel Castillo y Juan Camilo Ruiz, Octubre 2018

# Visualizacion de grafo con caminos a partir de una lista de literales.
#Cada literal en mayuscula representa una si decidí irme por ese lado o no.
#Cada literal en minuscula representa si hay trancon o no en ese lado.
# el literal en mayuscula es positivo sii decidi irme por ahí.
# el literal en minuscula es positivo sii hay trancon ahí.

# Formato de la entrada: - las letras proposionales seran:P,Q,R,S,T,X,A,B,C,p,q,r,s,t,x,a,b,c;
#                        - solo se aceptan literales (ej. p, ~P, q, ~R, etc.)
# Requiere tambien un numero natural, para servir de indice del grafo,
# toda vez que puede solicitarse visualizar varios tableros.

# Salida: - archivo tablero_%i.png, donde %i es un numero natural.
#         - Respuesta en consola de si la interpretacion dada,
#           es modelo para llegar del punto u al v


letrasProposicionales = list("PpQqRrSsTtXxAaBbCc")
class Tree():
    def __init__(self, l, iz ,der ):
        self.label = l
        self.left = iz
        self.right = der
def Inorder(f):
   
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"
#Creacion de formula final
#-------------------------------------------------------------
P = Tree('p',None, None )
Q = Tree('q',None,None )
R = Tree('r', None, None)
S = Tree('s', None, None)
T = Tree('t', None, None)
X = Tree('x',None, None )
A = Tree('a',None,None )
B = Tree('b', None, None)
C = Tree('c', None, None)

P2 = Tree('P',None, None )
Q2 = Tree('Q',None,None )
R2 = Tree('R', None, None)
S2 = Tree('S', None, None)
T2 = Tree('T', None, None)
X2 = Tree('X',None, None )
A2 = Tree('A',None,None )
B2 = Tree('B', None, None)
C2 = Tree('C', None, None)

pyqyr = Tree('Y', P, Tree('Y', Q, R))
sytyx = Tree('Y', S, Tree('Y', T, X))
aybyc = Tree('Y', A, Tree('Y', B, C))
R2_l1 = Tree('>', P , Tree('Y', pyqyr, Tree('-', None, Tree('O', sytyx, aybyc) )))
R2_l2 = Tree('>',S, Tree('Y', sytyx, Tree('-', None, Tree('O', pyqyr, aybyc) )))
R2_l3 = Tree('>',A, Tree('Y', aybyc, Tree('-', None, Tree('O', sytyx, pyqyr) )))

pYqopYroqYs = Tree('O', Tree('Y', P2, Q2), Tree('O', Tree('Y', P2, R2),Tree('Y', Q2, R2 ) ))
sYtosYxotYx = Tree('O', Tree('Y', S2, T2), Tree('O', Tree('Y', S2, X2),Tree('Y', T2, X2 ) ))
aYboaYcobYc = Tree('O', Tree('Y', A2, B2), Tree('O', Tree('Y', A2, C2),Tree('Y', B2, C2 ) ))

NopYNoqYNor = Tree('Y', Tree('-', None, P), Tree('Y', Tree('-', None, Q), Tree('-', None, R)))
NosYNotYNox = Tree('Y', Tree('-', None, S), Tree('Y', Tree('-', None, T), Tree('-', None, X)))
NoaYNobYNoc = Tree('Y', Tree('-', None, A), Tree('Y', Tree('-', None, B), Tree('-', None, C)))
R1_l1 = Tree('>', pYqopYroqYs, NopYNoqYNor)
R1_l2 = Tree('>', sYtosYxotYx, NosYNotYNox)
R1_l3 = Tree('>', aYboaYcobYc, NoaYNobYNoc)

O1 = Tree('Y', R1_l1, R2_l1)
O2 = Tree('Y', R1_l2, R2_l2)
O3 = Tree('Y', R1_l3, R2_l3)

formulaFinal = Tree('O', O1, Tree('O', O2, O3))
#print Inorder(formulaFinal)+"\n"+"\n"
#-------------------------------------------------------------


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


#funcion que recibe una interpretación y retorna si esa interpretación es modelo 
def Caminos(interpre):
    if(Valor_verdad(formulaFinal, interpre)):
        return "Si es modelo"
    else:
        return "No es modelo"
#Función que crea una interpretacion a partir de la formula ingresada
def interpre_aux(l):
        diccionario_ayu = {}
        for j in l:
                if '~' not in j:
                        diccionario_ayu[j]= 1
                else:
                        diccionario_ayu[j[1]]= 0
        return diccionario_ayu


def pitagoras(x1, y1, x2, y2):
        y =((x2-x1)**2 + (y2+y1)**2)
        return (y)**(1./2)

def dibujar_tablero(f, n):
    # Visualiza un grafo dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
        fig, axes = plt.subplots()
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)

    # Dibujo el grafo
        step = 1./2
        tangulos = []
        angulo = 77.85
        g = 0.15
        h = 0.15
        height = (1-2*h)/6.
        width = (1-2*(g+h))/3.
         
    # Creo las líneas del grafo
        
        locacion = 1 * step
        # lineas verticales
        tangulos.append(patches.Rectangle(*[(h/2, step ), 1-h/2, 0.015],\
                facecolor='grey'))
        tangulos.append(patches.Rectangle(*[(g, 1-height ), 1-2*g, 0.015],\
                facecolor='grey'))
        tangulos.append(patches.Rectangle(*[(g, height ), 1-2*g, 0.015],\
                facecolor='grey'))
        #lineas inclinadas del punto u
        tangulos.append(patches.Rectangle(*[(2*0.5*h/2, step ), pitagoras(0.5*h, step, g, 1-height), 0.01, angulo],\
                facecolor='grey'))
        tangulos.append(patches.Rectangle(*[(2*0.5*h/2-0.007 , step ), pitagoras(0.5*h, step, g, height), 0.01, 360-(angulo+1)],\
                facecolor='grey'))
        #lineas inclinadas del punto v
        tangulos.append(patches.Rectangle(*[(1-g-0.008, 1-height ), (pitagoras(0.5*h, step, g, 1-height))-1, 0.01, -angulo-1],\
                facecolor='grey'))
        tangulos.append(patches.Rectangle(*[(1-g-0.008, height ), (pitagoras(0.5*h, step, g, 1-height))-0.99, 0.01, 360+angulo],\
                facecolor='grey'))
        
        #nodos
        tangulos.append(patches.Circle(*[(g+width+h/2, step ), 0.5*h/2],\
                facecolor='grey'))
        tangulos.append(patches.Circle(*[(2*(g+width)+h/2, step ), 0.5*h/2],\
                facecolor='grey'))

        tangulos.append(patches.Circle(*[(g+width+h/2, height ), 0.5*h/2],\
                facecolor='grey'))
        tangulos.append(patches.Circle(*[(2*(g+width)+h/2, height ), 0.5*h/2],\
                facecolor='grey'))
        
        tangulos.append(patches.Circle(*[(g+width+h/2, 1-height ), 0.5*h/2],\
                facecolor='grey'))
        tangulos.append(patches.Circle(*[(2*(g+width)+h/2, 1-height ), 0.5*h/2],\
                facecolor='grey'))
       
        #crear puntos u y v
        tangulos.append(patches.Circle(*[(3*(g+width)+h/2+0.5*h/2, step ), 0.5*h/2],\
                facecolor='black'))
        tangulos.append(patches.Circle(*[(0.5*h/2, step ), 0.5*h/2],\
                facecolor='black'))
        


        #Creamos diccionario que contiene los keys como las letras propocicionales,
        # y sus negaciones y los values los reectangulos a dibujar,
        #teniendo en cuenta que: 
        #->Si la letra está en mayuscula, el rectangulo será verde si
        #es verdadera(decicí irme por ahí) y rojo si es falsa(no decidí irme por ahí).  
        #->Si la letra está en minuscula, tenemos que:
        #       -si la letra es verdadera(hay trancon), 
        #        entonces su rectangulo será rojo.
        #       -si la letra es falsa(no hay trancon), 
        #        entonces su rectangulo será verde.
        diccionario = {'P': patches.Rectangle(*[(g , 2*h+5*height), width, height],\
        facecolor='green'), 'p':patches.Rectangle(*[(g , 2*h+4*height), width, height],\
            facecolor='green'), 'Q':patches.Rectangle(*[(g+width+h , 2*h+5*height), width, height],\
            facecolor='green'), 'q':patches.Rectangle(*[(g+width+h , 2*h+4*height), width, height],\
            facecolor='green'), 'R':patches.Rectangle(*[(g+2*(width+h) , 2*h+5*height), width, height],\
            facecolor='green'), 'r':patches.Rectangle(*[(g+2*(width+h) , 2*h+4*height), width, height],\
            facecolor='green'), 'S':patches.Rectangle(*[(g , 3*height+h), width, height],\
            facecolor='green'), 's':patches.Rectangle(*[(g , 2*height+h), width, height],\
            facecolor='green'), 'T':patches.Rectangle(*[(g+width+h , 3*height+h), width, height],\
            facecolor='green'), 't':patches.Rectangle(*[(g+width+h , 2*height+h), width, height],\
            facecolor='green'), 'X':patches.Rectangle(*[(g+2*(width+h) ,3*height+h), width, height],\
            facecolor='green'), 'x':patches.Rectangle(*[(g+2*(width+h) , 2*height+h), width, height],\
            facecolor='green'), 'A':patches.Rectangle(*[(g , height), width, height],\
            facecolor='green'), 'a':patches.Rectangle(*[(g , 0), width, height],\
            facecolor='green'), 'B':patches.Rectangle(*[(g+width+h , height), width, height],\
            facecolor='green'), 'b':patches.Rectangle(*[(g+width+h , 0), width, height],\
            facecolor='green'), 'C':patches.Rectangle(*[(g+2*(width+h) , height), width, height],\
            facecolor='green'), 'c':patches.Rectangle(*[(g+2*(width+h) , 0), width, height],\
            facecolor='green'), '~P': patches.Rectangle(*[(g , 2*h+5*height), width, height],\
            facecolor='red'), '~p':patches.Rectangle(*[(g , 2*h+4*height), width, height],\
            facecolor='red'), '~Q':patches.Rectangle(*[(g+width+h , 2*h+5*height), width, height],\
            facecolor='red'), '~q':patches.Rectangle(*[(g+width+h , 2*h+4*height), width, height],\
            facecolor='red'), '~R':patches.Rectangle(*[(g+2*(width+h) , 2*h+5*height), width, height],\
            facecolor='red'), '~r':patches.Rectangle(*[(g+2*(width+h) , 2*h+4*height), width, height],\
            facecolor='red'), '~S':patches.Rectangle(*[(g , 3*height+h), width, height],\
            facecolor='red'), '~s':patches.Rectangle(*[(g , 2*height+h), width, height],\
            facecolor='red'), '~T':patches.Rectangle(*[(g+width+h , 3*height+h), width, height],\
            facecolor='red'), '~t':patches.Rectangle(*[(g+width+h , 2*height+h), width, height],\
            facecolor='red'), '~X':patches.Rectangle(*[(g+2*(width+h) ,3*height+h), width, height],\
            facecolor='red'), '~x':patches.Rectangle(*[(g+2*(width+h) , 2*height+h), width, height],\
            facecolor='red'), '~A':patches.Rectangle(*[(g , height), width, height],\
            facecolor='red'), '~a':patches.Rectangle(*[(g , 0), width, height],\
            facecolor='red'), '~B':patches.Rectangle(*[(g+width+h , height), width, height],\
            facecolor='red'), '~b':patches.Rectangle(*[(g+width+h , 0), width, height],\
            facecolor='red'), '~C':patches.Rectangle(*[(g+2*(width+h) , height), width, height],\
            facecolor='red'), '~c':patches.Rectangle(*[(g+2*(width+h) , 0), width, height],\
            facecolor='red')  }
        #Creamos lista con rectangulos dependiendo de la formula ingresada
        ##########################################
        tangulos2 = []
        
        for l in f:
                tangulos2.append(diccionario[l])
        ##########################################

        #Dibujamos las lineas del grafo y los rectangulos
        for t in tangulos:
                axes.add_patch(t)
        for t in tangulos2:
                axes.add_patch(t)
        

        
        # plt.show()
        fig.savefig("grafo_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

script, data_archivo = argv


with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando grafo "+ str(contador)+":", l
        print Caminos(interpre_aux(l))
        print '\n'
        dibujar_tablero(l, contador)
        contador += 1

csv_file.close()