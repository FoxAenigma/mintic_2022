print('------------------------ Inicio Registro diario ---------------------------------')
def pack_off(tiquet): 
    nominal=sum(list(map(lambda t: t[-1]*t[-2],tiquet)))
    return f'{nominal:,.2f}' if nominal>6e5 else f'{(nominal+25e3):,.2f}'
def ordenes(rutinaContable):
    if not rutinaContable: 
        return print('-------------------------- Fin Registro diario ----------------------------------')
    else: 
        print(f'La factura {rutinaContable[0][0]} tiene un total en pesos de {pack_off(rutinaContable[0][1:])}')
        rutinaContable.pop(0); ordenes(rutinaContable)  