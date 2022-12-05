archivo = open("movimientos.txt")
movimientos = archivo.read()
movimientosarray = movimientos.split("\n")
cuantosMover = 0 
desde = 0
hasta = 0
columna1=["C","Q","B"]
columna2=["Z","W","Q","R"]
columna3=["V","L","R","M","B"]
columna4=["W","T","V","H","Z","C"]
columna5=["G","V","N","B","H","Z","D"]
columna6=["Q","V","F","J","C","P","N","H"]
columna7=["S","Z","W","R","T","G","D"]
columna8=["P","Z","W","B","N","M","G","C"]
columna9=["P","F","Q","W","M","B","J","N"]
tabla=[columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9]
intermedio=[]

for movimiento in movimientosarray:
    cuantosMover = int(movimiento.split(",")[0])
    desde = int(movimiento.split(",")[1])
    hasta = int(movimiento.split(",")[2])
    for i in range(cuantosMover):
        intermedio.insert(0,tabla[desde-1][0])
        tabla[desde-1].pop(0)
    for i in range(len(intermedio)):
        tabla[hasta-1].insert(0,intermedio[i])
    intermedio.clear()
for columna in tabla:
    print(columna[0])