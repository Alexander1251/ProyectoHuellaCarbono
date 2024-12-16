# Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargar el conjunto de datos
file_path = '/data/notebook_files/datos_limpios.csv'  
data = pd.read_csv(file_path)

# Inspeccionar columnas del conjunto de datos
print("Columnas disponibles en el conjunto de datos:")
print(data.columns)

# Reformatear el conjunto de datos para análisis
# Convertir los años (1970-2023) de columnas a filas
melted_data = data.melt(id_vars=['pais_nombre', 'codigo_pais', 'region', 'origen_emision'], 
                        var_name='Año', value_name='Emisiones')

# Convertir la columna 'Año' a tipo numérico
melted_data['Año'] = pd.to_numeric(melted_data['Año'], errors='coerce')

# Eliminar filas con valores nulos en 'Emisiones' o 'Año'
melted_data = melted_data.dropna(subset=['Emisiones', 'Año'])

# Convertir 'Emisiones' a tipo numérico
melted_data['Emisiones'] = pd.to_numeric(melted_data['Emisiones'], errors='coerce')

# Preparar el conjunto de datos para análisis
valid_data_filtered_cleaned = melted_data.copy()

# Análisis 1: Top 10 países emisores 
# Este análisis busca identificar los principales países responsables de las emisiones totales.
top_countries = valid_data_filtered_cleaned.groupby('pais_nombre')['Emisiones'].sum().sort_values(ascending=False).head(10)

# Visualización del top 10 países emisores
plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar')
plt.title("Top 10 países emisores de carbono")
plt.xlabel("País")
plt.ylabel("Emisiones Totales")
plt.grid(axis='y')
plt.show()

# Conclusión: Los mayores emisores incluyen grandes economías industrializadas y emergentes como China, Estados Unidos e India.

# Análisis 2: Contribución de sectores emisores por región 
# Este análisis examina qué sectores dominan las emisiones en cada región.
sector_region_emissions = valid_data_filtered_cleaned.groupby(['region', 'origen_emision'])['Emisiones'].sum().unstack().fillna(0)
top_sectors_per_region = sector_region_emissions.div(sector_region_emissions.sum(axis=1), axis=0).sort_values(by='Main Activity Electricity and Heat Production', ascending=False)

# Visualización de la contribución de sectores por región
top_sectors_per_region.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab20')
plt.title("Contribución de sectores emisores por región")
plt.xlabel("Región")
plt.ylabel("Proporción de Emisiones")
plt.grid(axis='y')
plt.legend(title="Sector", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Conclusión: La producción de electricidad y calor domina en la mayoría de las regiones, mientras que el transporte es clave en Norteamérica.

# Análisis 3: Impacto del COVID-19 en emisiones globales 
# Evaluar cómo la pandemia afectó las emisiones durante 2019-2021.
covid_years = valid_data_filtered_cleaned[valid_data_filtered_cleaned['Año'].isin([2019, 2020, 2021])]
covid_impact = covid_years.groupby(['Año'])['Emisiones'].sum()

# Visualización del impacto del COVID-19
plt.figure(figsize=(12, 6))
covid_impact.plot(kind='bar')
plt.title("Impacto del COVID-19 en emisiones globales (2019-2021)")
plt.xlabel("Año")
plt.ylabel("Emisiones Totales")
plt.grid(axis='y')
plt.show()

# Conclusión: Las emisiones disminuyeron notablemente en 2020 debido a la pandemia, pero se recuperaron en 2021.

# Análisis 4: Promedio de emisiones per cápita por región 

population_estimates = {
    "Asia-Stan": 100_000_000,
    "Brazil": 210_000_000,
    "Canada": 38_000_000,
    "Central Europe": 300_000_000,
    "China +": 1_400_000_000,
    "North America": 370_000_000,
    "Rest Central America": 180_000_000,
    "South Africa": 60_000_000
}

valid_data_filtered_cleaned['poblacion'] = valid_data_filtered_cleaned['region'].map(population_estimates)
valid_data_filtered_cleaned['emisiones_per_capita'] = (
    valid_data_filtered_cleaned['Emisiones'] / valid_data_filtered_cleaned['poblacion']
)

emisiones_per_capita_avg = valid_data_filtered_cleaned.groupby('region')['emisiones_per_capita'].mean().sort_values(ascending=False)

# Visualización de emisiones per cápita por región
plt.figure(figsize=(12, 6))
emisiones_per_capita_avg.plot(kind='bar')
plt.title("Promedio de emisiones per cápita por región")
plt.xlabel("Región")
plt.ylabel("Emisiones per cápita (toneladas)")
plt.grid(axis='y')
plt.show()

# Conclusión: Norteamérica y Canadá tienen las emisiones per cápita más altas debido a sus niveles de consumo energético.

# Análisis 5: Crecimiento relativo de emisiones por región 
# Comparar el crecimiento desde 1970 hasta el presente.
region_growth = valid_data_filtered_cleaned.groupby(['region', 'Año'])['Emisiones'].sum().unstack()
region_growth_relative = (region_growth.loc[:, region_growth.columns[-1]] / region_growth.loc[:, region_growth.columns[0]] - 1) * 100

# Visualización de crecimiento relativo por región
plt.figure(figsize=(12, 6))
region_growth_relative.sort_values(ascending=False).plot(kind='bar')
plt.title("Crecimiento relativo de emisiones por región (1970 a último año)")
plt.xlabel("Región")
plt.ylabel("Crecimiento Relativo (%)")
plt.grid(axis='y')
plt.show()

# Conclusión: Regiones emergentes como China han experimentado el mayor crecimiento relativo en emisiones.

# Análisis 6: Tendencia general de emisiones promedio con regresión lineal 
# Evaluar y predecir tendencias generales de las emisiones promedio.
emisiones_tendencia = valid_data_filtered_cleaned.groupby('Año')['Emisiones'].mean()
X = emisiones_tendencia.index.values.reshape(-1, 1)
y = emisiones_tendencia.values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(12, 6))
plt.plot(X, y, label="Emisiones promedio reales", color="blue")
plt.plot(X, y_pred, label="Línea de tendencia (Regresión Lineal)", color="red", linestyle="--")
plt.title("Tendencia de emisiones promedio con regresión lineal")
plt.xlabel("Año")
plt.ylabel("Emisiones promedio")
plt.legend()
plt.grid(True)
plt.show()

# Conclusión: Las emisiones promedio muestran un crecimiento constante, con un aumento anual promedio estimado de 126.37 unidades según el modelo de regresión.
