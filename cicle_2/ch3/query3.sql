SELECT
    Proyecto.Ciudad,
    Proyecto.Clasificacion,
    COUNT(Proyecto.ID_Proyecto) AS "TOTAL",
    MIN(Fecha_Inicio) AS "VIEJO",
    MAX(Fecha_Inicio) AS "RECIENTE"
FROM
    Proyecto
WHERE NOT
    (
    Proyecto.Clasificacion = "Casa Campestre"
    OR Proyecto.Clasificacion = "Condominio"
    )
GROUP BY 
    Proyecto.Ciudad, Proyecto.Clasificacion
ORDER BY
    Proyecto.Ciudad ASC,
    Proyecto.Clasificacion ASC;
