import pandas as pd

def listaPeliculas(ruta:str)->str:

    if ruta.find('.csv') != -1:
        try:
            d=pd.read_csv(ruta)
            sub_d=d[['Country','Language','Gross Earnings']]
            table=pd.pivot_table(sub_d,values='Gross Earnings',index=['Country','Language'])
            return table.head(10)
        except: 
            return 'Error al leer el archivo de datos.'
    else:
        return 'Extensión inválida.'

def listaPeliculas2(ruta:str)->str:

    if ruta.find('.csv') != -1:
        try:
            d=pd.read_csv(ruta)
            sub_d=d[['Country','Language','Gross Earnings']]
            table=pd.pivot_table(sub_d,values="Gross Earnings",index=["Country",'Language'])
            return table.head(10)
        except: 
            return 'Error al leer el archivo de datos.'
    else:
        return 'Extensión inválida.'

def ListaPeliculas3(rutaFileCsv: str) -> str:
    if rutaFileCsv.find('.csv') != -1:
        try:
            csv = pd.read_csv(rutaFileCsv)
            subGrupoPeliculas = csv[["Country", "Language", "Gross Earnings"]]
            gananciaPaisLenguaje = pd.pivot_table(subGrupoPeliculas, index=["Country", "Language"],values='Gross Earnings')
            print(gananciaPaisLenguaje.head(10))
        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')

rutaFileCsv='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'
print(listaPeliculas(rutaFileCsv)==listaPeliculas3(rutaFileCsv))