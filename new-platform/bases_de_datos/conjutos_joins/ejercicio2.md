# Funcionalidades de SELECT en SQL

| Funcionalidad | Para qué sirve? | Cómo funciona? | Ejemplo de uso |
|---|---|---|---|
| **ORDER BY** | Ordenar los resultados. | Organiza las filas según una o más columnas. `ASC` ordena ascendentemente y `DESC` descendentemente. Utiliza `ASC` como default. | Mostrar precios de mayor a menor. |
| **LIMIT** | Limitar la cantidad de resultados a un valor especifico. | Establece el número máximo de filas que devuelve la consulta. | Mostrar solamente los primeros 10 clientes. |
| **GROUP BY** | Agrupar registros que comparten un valor. | Combina filas que tienen el mismo valor en una o varias columnas. | Agrupar ventas por cliente y calcular el total vendido por cada uno. |
| **INNER JOIN** | Combinar registros coincidentes entre tablas. | Devuelve únicamente las filas que tienen coincidencias en ambas tablas según la condición establecida. | Mostrar vehículos junto con el nombre de sus clientes, cuando existe una relación entre ellos. |
| **LEFT JOIN** | Conserva todos los registros de la tabla izquierda. | Devuelve todas las filas de la primera tabla y agrega los datos coincidentes de la segunda. Si no hay coincidencia, las columnas de la segunda tabla contienen `NULL`. | Mostrar todos los vehículos, incluso los que no tienen un owner asociado. |
| **RIGHT JOIN** | Conservar todos los registros de la tabla derecha. | Devuelve todas las filas de la segunda tabla y agrega los datos coincidentes de la primera. Si no hay coincidencia, las columnas de la primera tabla contienen `NULL`. | Mostrar todos los clientes, incluso aquellos que no tienen vehículos asociados. |

