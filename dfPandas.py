import pandas as pd
import psycopg2
import pyodbc

df = pd.read_csv("clientes_limpio.csv", encoding="latin-1", sep=";")

print(df.loc[9999]["FECHA_NAC"])

# Paso 2: Filtra los clientes con TIPO_CLIENTE igual a 'B'
clientes_tipo_b = df[df['TIPO_CLIENTE'] == 'B']

# Paso 3: Imprime el resultado
print(clientes_tipo_b)

print("montos menores a 100000")
print(df.loc[df['MONTO'] < 100000])

print("puntaje crediticio >= 8.0")
print(df.loc[df['PUNTAJE_CREDITICIO'] >= 8.0])

# del filtro, se crea un nuevo df
df_final = df.loc[df['PUNTAJE_CREDITICIO'] >= 8.0]

# agregar una nueva columna
df['NACIONALIDAD'] = "CHILE"
#print(df)

# genera una nueva columna a partir de un calculo
df['MONTO_DOLAR'] = df['MONTO'] / 890
#print(df)

#editar columnas
#sumar 1 punto crediticio a la columna PUNTAJE_CREDITICIO
df['PUNTAJE_CREDITICIO'] = df['PUNTAJE_CREDITICIO'] + 1
#print(df)

#ELIMINAR COLUMNAS
#del df['NACIONALIDAD']
#print(df)

#para unir dos df provenientes de dos csv distintos
#df1 = pd.read_csv("archivo1.csv", encoding="latin-1", sep=";")
#df2 = pd.read_csv("archivo2.csv", encoding="latin-1", sep=";")
#df1.append(df2)

#estadisticos descriptivos
print(df.describe())

#escribir archivo csv
df.to_csv("archivo.csv", sep=';', index=False)


df_clientes = pd.read_csv("base_de_datos_de_clientes.csv", encoding="latin-1", sep=";", header=None)
encabezados = ['RUT','NOMBRE','GENERO','FECHA_NAC','EDAD','TIPO_CLIENTE','MONTO','PUNTAJE_CREDITICIO']
df_clientes.columns = encabezados
df_clientes['RUT'] = df_clientes['RUT'].str.replace("A.!--", "")
df_clientes['FECHA_NAC'] = df_clientes['FECHA_NAC'].str.replace("-", "")
df_clientes['EDAD'] = 2023 - df_clientes['FECHA_NAC'].str.split("/").str[0].astype(int)
print(df_clientes)
df_clientes.to_csv("archivo_CON_PANDAS.csv", sep=';', index=False, encoding='ISO-8859-1')
