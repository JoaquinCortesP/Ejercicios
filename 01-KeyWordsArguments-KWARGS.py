def get_product(**datos):#para trabajar keywords se usan dos asteriscos **
    print(datos["id"], datos["desc"])

get_product(id="23", name="iphone", desc="esto es un iphone")