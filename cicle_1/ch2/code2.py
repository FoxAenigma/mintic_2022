def cliente(info:dict)-> dict:
    #input_dict
    id=info['id_cliente']
    name=info['nombre']
    age=info['edad']
    first_entry=info['primer_ingreso']

    #output_dict
    bill={}
    bill['nombre']=name
    bill['edad']=age
    bill['atraccion']=None
    bill['apto']=True
    bill['primer_ingreso']=first_entry
    bill['total_boleta']=None

    if age>18:
        sale= 0.05 if first_entry else 0
        bill['total_boleta']=20000*(1-sale)
        bill['atraccion']='X-Treme'
    elif age>=15 and age<=18:
        sale= 0.07 if first_entry else 0
        bill['total_boleta']=5000*(1-sale)
        bill['atraccion']='Carros chocones'
    elif age >=7 and age <15:
        sale= 0.05 if first_entry else 0
        bill['total_boleta']=10000*(1-sale)
        bill['atraccion']='Sillas voladoras'
    else:
        sale=None
        bill['total_boleta']='N/A'
        bill['apto']=False
        bill['atraccion']='N/A'
    
    return bill


ej1={'id_cliente':1,'nombre':'Johana Fernandez','edad':20,'primer_ingreso':True}
ej2={'id_cliente':1,'nombre':'Johana Fernandez','edad':20,'primer_ingreso':False}
ej3={'id_cliente':2,'nombre':'Gloria Suarez','edad':3,'primer_ingreso':True}
ej4={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':True}
ej5={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':False}
ej6={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':True}
ej7={'id_cliente':3,'nombre':'Tatiana Suarez','edad':8,'primer_ingreso':True}

print(cliente(ej1))
print(cliente(ej2))
print(cliente(ej3))
print(cliente(ej4))
print(cliente(ej5))
print(cliente(ej6))
print(cliente(ej7))

    

    



