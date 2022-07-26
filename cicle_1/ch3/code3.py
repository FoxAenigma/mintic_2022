
def consultaRegistro(sales,id):
    
    def Selection(sales_dict,id):
        reg=[]
        k=0
        for s in sales_dict:
            if sales_dict[s][0]==id:
                idProducto=sales_dict[s][0]
                dProducto=sales_dict[s][1]
                pnProducto=sales_dict[s][2]
                cvProducto=sales_dict[s][3]
                sProducto=sales_dict[s][4]
                nComprador=sales_dict[s][5]
                cComprador=sales_dict[s][6]
                fVenta=sales_dict[s][7]
                flag=f'Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}'

                reg.extend([flag])
                reg.extend(['\n'])
        
        if len(reg)>1:
            reg.pop(-1)
        else:
            reg=['No hay registro de venta de ese producto']
        reg=''.join(reg)

        return reg

    inquiry=Selection(sales,id)
    print(inquiry)
    return inquiry

def AutoPartes(sales_list:list):
        return {n: sales_list[n] for n in range(len(sales_list))}

x=1

consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

