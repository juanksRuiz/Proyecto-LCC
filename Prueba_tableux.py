#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

letrasProposicionales = list('PpQqRrSsTtXxAaBbCc')

# Creamos:
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

#Creamos fórmula final
Formula_final = Regla_3+Regla_2+'Y'+Regla_1+'Y'
Formula_final = Formula_final+Regla_4+'Y'


A = T.StringtoTree(Formula_final,letrasProposicionales)

print T.Inorder(A)


# Las hojas son conjuntos de formulas o marcas 'x' o 'o'

lista_hojas = [[A]]

OK = '' # El tableau regresa Satisfacible o Insatisfacible


OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'modelos.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas en " + archivo

        import visualizacion as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"

