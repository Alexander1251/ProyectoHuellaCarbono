# **Por un futuro más limpio: Análisis global del consumo de combustibles y emisiones de carbono**

Nuestro propósito es analizar cómo han evolucionado las emisiones de carbono a nivel global desde la década de los 70's, con el objetivo de comprender el panorama actual y proyectar posibles escenarios futuros en relación a este tema.

---

## **Tabla de contenidos**
1. [Nombre](#nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#arquitectura)
4. [Proceso](#proceso)
5. [Funcionalidades](#funcionalidades)
6. [Estado del proyecto](#estado-del-proyecto)
7. [Agradecimientos](#agradecimientos)

---

## **Nombre**
**Por un futuro más limpio: Análisis global del consumo de combustibles y emisiones de carbono**

---

## **Descripción**
Este proyecto analiza datos históricos relacionados con el consumo de combustibles y las emisiones de carbono, permitiendo visualizar tendencias y estadísticas clave desde la década de 1970.

### **Imagen representativa**

![Imagen Representativa](Imagenes/IMAGEN.png)
---

## **Arquitectura**
El proyecto utiliza un diseño modular que integra tres componentes principales:

1. **Análisis de datos:** Transformación y limpieza del dataset para identificar patrones históricos de emisiones.
2. **Visualización de datos:** Generación de gráficos interactivos y dinámicos utilizando herramientas como `Matplotlib` y `Seaborn`.
3. **Despliegue web:** Desarrollo de una aplicación con el framework `Flask`, que permite a los usuarios interactuar con los datos y visualizaciones.

### **Diagrama de arquitectura**
Aqui se debe agregar un grafico que logre generar

![Diagrama de Arquitectura](image/diagrama.png)


## **Proceso**

### **1. Fuente del dataset**
El conjunto de datos se obtuvo de [Stack Overflow](#).  
*(Sustituir el enlace cuando Cristian proporcione la URL 

### **2. Limpieza de datos**
El dataset se transformó siguiendo estos pasos:
- Filtrado por **país**, **región**, **origen de emisión** y **año**.
- Conversión de datos en formatos compatibles con análisis estadístico.
- Estandarización de columnas relevantes para facilitar la visualización.

### **3. Análisis estadístico y visualizaciones**
- Estadísticas descriptivas para identificar patrones clave en las emisiones globales.
- Gráficos dinámicos que reflejan tendencias históricas y por sector.
- Uso de `Matplotlib` y `Seaborn` para visualizaciones con alta precisión, ademas de `Pandas` para el analisis de datos.

### **4. Visualización interactiva (Aplicación web)**
- **Frontend:** Interfaz desarrollada con plantillas HTML que renderizan gráficos y datos interactivos.
- **Backend:** Uso de `Flask` para procesar datos, generar gráficos y manejar rutas.
- **Gráficos dinámicos:** Las rutas permiten visualizar tendencias globales, por sector, región o país específico.

---

## **Funcionalidades**
1. **Gráficos históricos de emisiones:**
   - Tendencias globales anuales.
   - Comparaciones por región y sectores económicos.
   - Análisis específico por país.

2. **Aplicación web interactiva:**
   - Consulta y visualización de datos dinámicos.
   - Navegación intuitiva entre gráficos y opciones personalizables.

---

## **Estado del proyecto**
El proyecto se encuentra en una fase avanzada.  

**Próximos pasos:**
1. **Visualizaciones avanzadas:** Implementar gráficos interactivos utilizando librerías como `Plotly` o `Dash`.  
2. **Ampliación del dataset:** Incorporar nuevas fuentes de datos globales relacionadas con energías renovables y emisiones.
3. **Optimización del despliegue web:** Mejorar tiempos de carga y escalabilidad.

---

## **Agradecimientos**
Queremos agradecer a:
- Los autores del dataset por compartir esta valiosa información.
- La comunidad de código abierto por sus herramientas y recursos.
- El equipo de **Samsung Innovation Campus** por su formación y guía durante el proyecto.
- Cada uno de los miembros del equipo por su dedicación y esfuerzo.

---

