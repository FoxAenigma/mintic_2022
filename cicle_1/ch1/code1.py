def CDT(usuario:str, monto:int, tiempo:int):

    if tiempo>=0 and tiempo<=2:
        k=monto*0.98
    elif tiempo>2:
        k=(monto*0.03*tiempo)/12

    return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {monto} para un tiempo de {tiempo} meses es: {k}'

