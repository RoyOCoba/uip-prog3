## Tupla de alimentos
print("**********************")
print("Tienda La Union")
print("**********************")
print("Efectue su eleccion")
lista_tienda=[]
lista=("cereal","jugo""arroz","leche","tuna")
eleccion=1
while eleccion!='4':
   print('1-Agregar\n2-Eliminar\n3-Ver\n4-Salir')
   eleccion=input()
   if eleccion=='1':
      articulo=input()
      lista_tienda.append(articulo)
   elif eleccion=='2':
      elim=input()
      lista_tienda.remove(elim)
   elif eleccion=='3':
      print(lista_tienda)
      l=input()