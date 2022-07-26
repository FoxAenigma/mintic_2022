SELECT
    p.ID_Proyecto,
    SUM(c.Cantidad * m.precio_unidad) AS "VALOR"
FROM 
    Proyecto p
INNER JOIN Compra c
	ON c.ID_proyecto = p.ID_Proyecto
INNER JOIN MaterialConstruccion m
	ON m.ID_MaterialConstruccion = c.ID_MaterialConstruccion
WHERE
    c.Pagado = "No"
GROUP BY
    p.ID_Proyecto  HAVING VALOR > 50000
ORDER BY
    VALOR DESC;
