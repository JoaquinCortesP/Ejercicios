diccionario = {'manzana':1,
               'peras':2
               ,"sandias":4,
               }

for key, value in diccionario.items():
    valor_del_producto = diccionario.get("manzana")
    print(f"{key} : {value}")