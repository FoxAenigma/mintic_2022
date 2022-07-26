select
    ID_Proyecto as "ID",
    Constructora,
    Ciudad, 
    Proyecto.Clasificacion,
    Estrato,
    Nombre || ' ' || Primer_Apellido || ' ' || Segundo_Apellido as "LIDER"
from
    Proyecto
inner join Tipo on Tipo.ID_Tipo = Proyecto.ID_Tipo
inner join Lider on Lider.ID_Lider = Proyecto.ID_Lider
where
    Banco_Vinculado = "Conavi"
order by
    Fecha_Inicio desc,
    Ciudad asc,
    Constructora asc;
    
