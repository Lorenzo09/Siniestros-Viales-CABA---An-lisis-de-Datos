import pandas as pd
import matplotlib as mp
import seaborn as sb
import streamlit as st
import calendar

# Cargar los archivos CSV
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Definir los paths de los archivos CSV junto con sus nombres
file_paths = {
    "Datasets\df_siniestros_viales_streamlit.csv": "Siniestros Viales CABA",
    "Datasets\df_siniestros_anios.csv": "Siniestros Viales CABA por año y mes",
    "Datasets\df_siniestros_comunas.csv": "Siniestros Viales CABA por Comuna"
}

# Función para cargar y mostrar dataframes
def show_dataframes():
    st.title('Dataframes')
    # Cargar cada archivo CSV y mostrar sus datos
    for file_path, name in file_paths.items():
        st.write(f"## {name}")
        data = load_data(file_path)
        st.write(data)

# Función para generar el dashboard
def show_dashboard():
    st.title('Dashboard')
    # Definir el path del archivo CSV
    siniestros_viales = "Datasets\df_siniestros_viales_streamlit.csv"

    # Cargar los datos
    data = load_data(siniestros_viales)

    # Convertir la columna de fecha a tipo datetime
    data['FECHA'] = pd.to_datetime(data['FECHA'])

    # Extraer el año y el mes de la columna de fecha
    data['AÑO'] = data['FECHA'].dt.year
    data['MES'] = data['FECHA'].dt.month_name()

    # Ordenar los meses
    data['MES'] = pd.Categorical(data['MES'], categories=list(calendar.month_name)[1:], ordered=True)

    # Agrupar por año y mes y contar la cantidad de siniestros
    siniestros_por_mes = data.groupby(['AÑO', 'MES'])['N_VICTIMAS'].sum().reset_index()

    # Crear el gráfico interactivo    
    year_to_show = st.selectbox('Selecciona el año:', sorted(siniestros_por_mes['AÑO'].unique()))
    selected_data = siniestros_por_mes[siniestros_por_mes['AÑO'] == year_to_show]
    st.title(f"Cantidad de siniestros viales por mes en el año {year_to_show}")

    # Filtrar los datos seleccionados por año
    selected_data = selected_data.set_index('MES').loc[:, ['N_VICTIMAS']]

    # Graficar los datos como un gráfico de barras
    st.bar_chart(selected_data)

    # Agrupar por año y mes y contar la cantidad de siniestros
    siniestros_por_mes = data.groupby(['AÑO', 'MES'])['N_VICTIMAS'].sum().reset_index()

    # Convertir el nombre del mes a número
    siniestros_por_mes['MES_NUMERO'] = siniestros_por_mes['MES'].apply(lambda x: list(calendar.month_name).index(x))

    # Graficar la cantidad de siniestros viales por año y mes
    st.title("Cantidad de siniestros viales por año y mes")

    # Seleccionar los años que el usuario quiere ver
    years_to_show = st.multiselect('Selecciona los años:', sorted(siniestros_por_mes['AÑO'].unique()))

    # Filtrar los datos según los años seleccionados
    filtered_data = siniestros_por_mes[siniestros_por_mes['AÑO'].isin(years_to_show)]

    # Crear el gráfico de líneas
    chart_data = filtered_data.pivot(index='MES_NUMERO', columns='AÑO', values='N_VICTIMAS')
    st.line_chart(chart_data, use_container_width=True)

                        #Nuevo Gráfico
    import folium
    from streamlit_folium import folium_static
    from folium.plugins import MarkerCluster

    st.title("Mapa de siniestros viales en CABA")

    # Crear un mapa centrado en CABA
    mapa = folium.Map(location=[-34.6083, -58.3712], zoom_start=12)

    # Agrupar los datos por comuna
    grouped_data = data.groupby('COMUNA')

    # Crear un grupo de marcadores
    marker_cluster = folium.plugins.MarkerCluster().add_to(mapa)

    # Iterar sobre cada fila de los datos
    for index, row in data.iterrows():
        folium.Marker([row['pos y'], row['pos x']], popup=row['N_VICTIMAS']).add_to(marker_cluster)

    # Mostrar el mapa
    folium_static(mapa)



    
# Configurar la barra lateral para la navegación entre páginas
pages = {
    "Dashboard": show_dashboard,
    "Dataframes": show_dataframes
}
selection = st.sidebar.radio("Navegación", list(pages.keys()))

# Ejecutar la función correspondiente a la página seleccionada
pages[selection]()




