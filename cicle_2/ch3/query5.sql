SELECT
    l.Nombre || ' ' || l.Primer_Apellido || ' ' || l.Segundo_Apellido as "LIDER",
    SUM(c.Cantidad * m.Precio_Unidad) AS "VALOR"
FROM
    Proyecto p
INNER JOIN Lider l
    ON l.ID_Lider = p.ID_Lider
INNER JOIN Compra c
    ON c.ID_Proyecto = p.ID_Proyecto
INNER JOIN MaterialConstruccion m
    ON m.ID_MaterialConstruccion = c.ID_MaterialConstruccion
GROUP BY
    LIDER
ORDER BY
    VALOR DESC
LIMIT 10;
    
