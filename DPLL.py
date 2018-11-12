#-*-coding: utf-8-*-
import cnf as cn



letrasProposicionales = list('PpQqRrSsTtXxAaBbCc')
def DPLL(S,I):
    #S: comjunto de clausulas
    #I: diccionario de interpretaciones sobre el cual se hace recursion
    #I comienza vacio
    #Eliminando clausulas unitarias
    

    
    while((len(x) != 0 for x in S) and len(S)>0):
        print "S antes: ",S
        S,lit = UnitPropagation(S)
        print "S despues: ",S
        if lit == None:
            return ("Insatisfacible", {})
        #Si el literal es positivo
        if len(lit) == 1:
            I[lit] = 1
        #Si el literal es negativo
        elif len(lit) == 2:
            I[lit[1]] = 0
    
    if(len(S)==0):
        for c in Sprincipal:
            for i in c:
                if len(i)==2:
                    if i[1] not in I.keys():
                        S.append([i])
                        DPLL(S, I)
                elif len(i)==1:
                    if i not in I.keys():
                        S.append([i])
                        DPLL(S, I)


                
        return ("Satifacible", I)
    DPLL(S, I)



def Max(S):
    dic = {}
    for c in S:
        for i in c:
            if i not in dic:
                dic[i]= 0
            else:
                dic[i] +=1
    max = 0
    for c in dic.values():
        if c>max:
            max = c
    for i in dic.keys():
        if dic[i] == max:
            return i



def buscarCU(S):
    if(len(S)!=0):
        for c in S:
            if len(c) == 1:
                return True
    return False

def UnitPropagation(S):
    #print "S: ",S
    #Asumiendo que no hay clausulas vacias
    lit = ''
    for c in S:
        if len(c) == 1:
            if len(c[0]) == 1 or len(c[0]) == 2:
                lit = c[0]
            
            S.remove(c)
            print "literal unitario encontrado: ",lit
            break

   
    #Caso en el que hay una clausula unitaria
    if len(lit) == 1 or len(lit) == 2:
        S = removeLit(lit,S)

    
    else:
        #No hay clausulas unitarias
        lit = Max(S)
        print "literal unitario encontrado: ",lit
        S = removeLit(lit,S)
    return S, lit
        
def removeLit(lit,S):
    S2 = []
    for c in S:
        #Caso que literal sea positivo
        if len(lit) == 1 and ('-' + lit) in c:
            print '-' + str(lit) + " esta en la clausula " + str(c)
            print "Clausula antes: ",c
            c.remove('-'+lit)
            S2.append(c)
            print "Clausula despues: ",c
        elif len(lit) == 2 and lit[1] in c:
            print  str(lit) + " esta en la clausula " + str(c)
            #Caso de literal negativo
            lit = lit[1]
            print "Clausula antes: ",c
            c.remove(lit)
            S2.append(c)
            print "Clausula despues: ",c
        elif lit not in c:
            S2.append(c)
            
    return S2
#No funciona el codigo con esta formula:
#----------------------------------------------------------------------------------------#
# Regla_1
R1_cam1 = 'R-Q-YP-YrqYrpYOqpYO>'
R1_cam2 = 'X-T-YS-YxtYxsYOtsYO>'
R1_cam3 = 'C-B-YA-YcbYcaYObaYO>'
Regla_1 = R1_cam3+R1_cam2+'Y'+R1_cam1+'Y'

# Regla_2
Regla_2 = 'CBYAYXTYSYORQYPYO'

# Regla_3
R3_cam1 = 'CBYAYXTYSYO-RQYPYYP>'
R3_cam2 = 'CBYAYRQYPYO-XTYSYYS>'
R3_cam3 = 'RQYPYXTYSYO-CBYAYYA>'
Regla_3 = R3_cam3+R3_cam2+'Y'+R3_cam1+'Y'

# Regla_4
R4_cam1 = 'R-Q-YP-YR-Q-OP-O>'
R4_cam2 = 'X-T-YS-YX-T-OS-O>'
R4_cam3 = 'C-B-YA-YC-B-OA-O>'
Regla_4 =  R4_cam3+R4_cam2+'Y'+R4_cam1+'Y'
 
#Regla_5
Regla_5 = 'b-a-YtsYYqp-YY'

#Creamos fórmula final
Formula_final = Regla_3+Regla_2+'Y'+Regla_1+'Y'
Formula_final = Formula_final+Regla_4+'Y'+Regla_5+'Y'

A = cn.StringtoTree(Formula_final, letrasProposicionales)

#print("Trabajando con la fórmula: ", cn.Inorder(A))

A = cn.quitarDobleNegacion(A)

#print(u"La fórmula sin dobles negaciones es:\n ", cn.Inorder(A))

A = cn.reemplazarImplicacion(A)

#print(u"La fórmula reemplazando implicaciones es:\n ", cn.Inorder(A))

A = cn.quitarDobleNegacion(A)

#print(u"La fórmula sin dobles negaciones es:\n ", cn.Inorder(A))


OK = True
while OK:
	aux1 = cn.Inorder(A)
	print("Se analiza: ", aux1)
	B = cn.deMorgan(A)
	B = cn.quitarDobleNegacion(B)
	aux2 = cn.Inorder(B)
	print("Se obtuvo : ", aux2)
	if  aux1 != aux2:
		print(u"Se aplicó deMorgan")
		OK = True
		A = B
	else:
		print(u"No se aplicó deMorgan")
		OK = False

OK = True
while OK:
	OK, A = cn.aplicaDistributiva(A)

conjuntoClausulas = cn.formaClausal(A)
ccPrincipal = conjuntoClausulas
#----------------------------------------------------------------------------------------#

#El código corre con esta formula:
S = [['p'],['-p','q','-r'],['q','r']]
Sprincipal = S
#----------------------------------------------------------#

I= {}
print DPLL(S, I)

