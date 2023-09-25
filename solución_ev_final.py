#Alumno: Rodrigo Jeldres Carrasco

import pandas as pd
import numpy as np

detalle_boletas = pd.read_csv("detalle_boletas.csv", encoding="utf-8", sep=",")
del detalle_boletas["Precio_prod"]
detalle_boletas["Pais_Venta"] = "Chile"
detalle_boletas = detalle_boletas.rename(columns={"NXXX": "Num Boleta"})
#detalle_boletas = detalle_boletas.loc[~detalle_boletas["ID"].str.contains("4XXXXX")]
#detalle_boletas = detalle_boletas.loc[~detalle_boletas["Num Boleta"].str.contains("55417XXXXXXX")]
detalle_boletas = detalle_boletas.loc[~(detalle_boletas["ID"].str.contains("4XXXXX") | detalle_boletas["Num Boleta"].str.contains("55417XXXXXXX"))]
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("!", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("{", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace(".", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("_", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("-", "")
estadisticas = detalle_boletas.pivot_table(values="Cantidad",index="ID", aggfunc={np.mean, np.min, np.max, np.std})
print(f"Estadisticos descriptivos para columna Cantidad\n{estadisticas}")
df_fecha_aux = detalle_boletas["Fecha"].str.split("/", expand=True)
df_fecha_aux.columns = ["Anho", "Mes", "Dia"]
detalle_boletas = detalle_boletas.join(df_fecha_aux)
del detalle_boletas["Fecha"]

lista_productos = pd.read_csv("Lista productos.csv", encoding="utf-8", sep=",")
detalle_boletas["ID"] = detalle_boletas["ID"].astype("int64")
lista_productos["ID"] = lista_productos["ID"].astype("int64")
detalle_boletas2 = detalle_boletas.merge(lista_productos, on="ID", how="left")
print(detalle_boletas2.head())
print(detalle_boletas2.shape)
detalle_boletas2["Ingreso total"] = detalle_boletas2["Precio Unitario"] * detalle_boletas2["Cantidad"]
print(detalle_boletas2.head())
print(detalle_boletas2["Ingreso total"].head())
estadisticas = detalle_boletas2.pivot_table(index="Nombre", values ="Ingreso total", aggfunc={np.mean, np.min, np.max, np.std})
print(f"Estadisticos descriptivos para columna Ingreso total\n{estadisticas}")
#detalle_boletas2.to_csv("archivo final.csv", index=False, encoding="utf-8", sep=";")
