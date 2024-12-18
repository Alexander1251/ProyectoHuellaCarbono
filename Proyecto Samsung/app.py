from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os
import matplotlib

# Configuración para evitar problemas de hilos con Matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Cargar el dataset
data_path = os.path.join("data", "datos_limpios.csv")
data = pd.read_csv(data_path)

# Transformar el dataset de formato ancho a formato largo
data = pd.melt(
    data, 
    id_vars=['pais_nombre', 'codigo_pais', 'region', 'origen_emision'], 
    var_name='year', 
    value_name='emissions'
)
data['year'] = pd.to_numeric(data['year'], errors='coerce')

def plot_to_base64(fig):
    """Convierte una gráfica de Matplotlib a una imagen en base64."""
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')

@app.route('/')
def home():
    # Gráfica de emisiones globales totales
    yearly_emissions = data.groupby('year')['emissions'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    yearly_emissions.plot(ax=ax, color='green', title="Emisiones Globales Totales", ylabel="Emisiones Totales (toneladas)", xlabel="Año")
    global_emissions_img = plot_to_base64(fig)
    plt.close(fig)

    return render_template('index.html', global_emissions_img=global_emissions_img)

@app.route('/sector')
def sector():
    # Gráfica de emisiones por sector detallado en el tiempo
    sector_yearly = data.groupby(['year', 'origen_emision'])['emissions'].sum().reset_index()
    pivot_sector = sector_yearly.pivot(index='year', columns='origen_emision', values='emissions')

    fig, ax = plt.subplots(figsize=(12, 8))
    pivot_sector.plot(ax=ax, linewidth=2)
    ax.set_title("Evolución de las Emisiones por Origen de emisión")
    ax.set_ylabel("Emisiones Totales (toneladas)")
    ax.set_xlabel("Año")
    legend = plt.legend(title="Categorías", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.setp(legend.get_texts(), fontsize='small')  # Hacer la etiqueta de categorías más pequeña
    plt.tight_layout()
    sector_img = plot_to_base64(fig)
    plt.close(fig)

    return render_template('sector.html', sector_img=sector_img)

@app.route('/region')
def region():
    # Gráfica de emisiones por región a lo largo del tiempo
    region_yearly = data.groupby(['year', 'region'])['emissions'].sum().reset_index()
    pivot_region = region_yearly.pivot(index='year', columns='region', values='emissions')

    fig, ax = plt.subplots(figsize=(12, 8))
    pivot_region.plot(ax=ax, linewidth=2)
    ax.set_title("Evolución de las Emisiones por Región")
    ax.set_ylabel("Emisiones Totales (toneladas)")
    ax.set_xlabel("Año")
    legend = plt.legend(title="Regiones", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.setp(legend.get_texts(), fontsize='small')  # Hacer la leyenda más pequeña
    plt.tight_layout()
    
    region_img = plot_to_base64(fig)
    plt.close(fig)

    return render_template('region.html', region_img=region_img)


@app.route('/country', methods=['GET', 'POST'])
def country():
    # Visor interactivo para emisiones por país
    countries = data['pais_nombre'].unique()
    selected_country = request.form.get('country', countries[0])

    country_emissions = data[data['pais_nombre'] == selected_country].groupby('year')['emissions'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    country_emissions.plot(ax=ax, color='forestgreen', title=f"Emisiones de {selected_country}", ylabel="Emisiones Totales (toneladas)", xlabel="Año")
    country_img = plot_to_base64(fig)
    plt.close(fig)

    return render_template('country.html', countries=countries, selected_country=selected_country, country_img=country_img)

if __name__ == '__main__':
    app.run(debug=True)