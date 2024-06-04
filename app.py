import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import calendar
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Configuración inicial para seaborn
sb.set(style="whitegrid")

# Colores para los gráficos
COLOR_PALETTE = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f1c40f', '#34495e']

# Cargar los archivos CSV
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Definir los paths de los archivos CSV junto con sus nombres
file_paths = {
    "Datasets/df_siniestros_viales_streamlit.csv": "Siniestros Viales CABA",
    "Datasets/df_siniestros_anios.csv": "Siniestros Viales CABA por Año y Mes",
    "Datasets/df_siniestros_comunas.csv": "Siniestros Viales CABA por Comuna"
}

# Función para cargar y mostrar dataframes
def show_dataframes():
    st.title('📊 Datos utilizados para el Dashboard')
    # Cargar cada archivo CSV y mostrar sus datos
    for file_path, name in file_paths.items():
        st.write(f"## {name}")
        data = load_data(file_path)
        st.write(data)

# Función para mostrar los KPIs
def show_kpis():
    st.title('📈 Indicadores Clave de Desempeño (KPIs)')

    # KPI 1: Tasa de homicidios
    st.subheader('🔴 Tasa de Homicidios - Primer y Segundo Semestre 2021')
    tasa_primer_semestre_2021 = 1.761857
    tasa_segundo_semestre_2021 = 1.345418
    reduccion_10 = tasa_primer_semestre_2021 * 0.9

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['Primer Semestre 2021', 'Segundo Semestre 2021'], [tasa_primer_semestre_2021, tasa_segundo_semestre_2021], color=COLOR_PALETTE[:2])
    ax.axhline(reduccion_10, color='red', linestyle='--', label='10% de reducción')
    ax.set_xlabel('Semestre')
    ax.set_ylabel('Tasa de homicidios')
    ax.set_title('Comparación de tasas de homicidios - Primer y Segundo Semestre 2021')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # KPI 2: Accidentes de motos
    st.subheader('🛵 Cantidad de accidentes mortales de motociclistas - 2020 y 2021')
    siniestros_moto = load_data("Datasets/df_siniestros_viales_streamlit.csv")
    siniestros_moto = siniestros_moto[siniestros_moto['VICTIMA'] == 'MOTO']

    # Convertir la columna de fecha a tipo datetime
    siniestros_moto['FECHA'] = pd.to_datetime(siniestros_moto['FECHA'])

    # Extraer el año de la columna de fecha
    siniestros_moto['AÑO'] = siniestros_moto['FECHA'].dt.year

    accidentes_2020 = siniestros_moto[siniestros_moto['AÑO'] == 2020]['N_VICTIMAS'].sum()
    accidentes_2021 = siniestros_moto[siniestros_moto['AÑO'] == 2021]['N_VICTIMAS'].sum()
    porcentaje_reduccion = ((accidentes_2020 - accidentes_2021) / accidentes_2020) * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['2020', '2021'], [accidentes_2020, accidentes_2021], color=COLOR_PALETTE[2:4])
    ax.set_title('Cantidad de accidentes mortales de motociclistas')
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de accidentes mortales')
    ax.text(0, accidentes_2020 + 10, f'{accidentes_2020}', ha='center', color='blue')
    ax.text(1, accidentes_2021 + 10, f'{accidentes_2021}', ha='center', color='orange')
    ax.set_ylim(0, max(accidentes_2020, accidentes_2021) * 1.2)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.text(0.5, (accidentes_2020 + accidentes_2021) / 2, f'Reducción del {porcentaje_reduccion:.2f}%', ha='center', va='center', fontsize=12, color='red')
    st.pyplot(fig)

# Función para generar el dashboard
def show_dashboard():
    st.title('🚦 Siniestros Viales en CABA durante 2016 y 2021')
    # Definir el path del archivo CSV
    siniestros_viales = "Datasets/df_siniestros_viales_streamlit.csv"

    # Cargar los datos
    data = load_data(siniestros_viales)
    data_comunas = load_data("Datasets/df_siniestros_comunas.csv")

    # Convertir la columna de fecha a tipo datetime
    data['FECHA'] = pd.to_datetime(data['FECHA'])

    # Extraer el año y el mes de la columna de fecha
    data['AÑO'] = data['FECHA'].dt.year
    data['MES'] = data['FECHA'].dt.month_name()

    # Ordenar los meses
    data['MES'] = pd.Categorical(data['MES'], categories=list(calendar.month_name)[1:], ordered=True)

    # Agrupar por año y mes y contar la cantidad de siniestros
    siniestros_por_mes = data.groupby(['AÑO', 'MES'])['N_VICTIMAS'].sum().reset_index()

    # Inicializar selected_view en st.session_state si no está definido
    if 'selected_view' not in st.session_state:
        st.session_state.selected_view = 'mes'

    selected_view = st.session_state.selected_view

    # Gráficos
    if selected_view == "mes":
        col1, col2 = st.columns(2)

        # Columna 1: Gráfico de barras por mes
        with col1:
            # Gráfico de siniestros por mes
            year_to_show = st.selectbox('Selecciona el año:', sorted(siniestros_por_mes['AÑO'].unique()))
            selected_data = siniestros_por_mes[siniestros_por_mes['AÑO'] == year_to_show]
            st.title("")
            selected_data = selected_data.set_index('MES').loc[:, ['N_VICTIMAS']]
            st.bar_chart(selected_data)

        # Columna 2: Gráfico de torta por comuna
        with col2:
            st.title("Porcentaje de Víctimas por Comuna")
            # Filtrar los datos por el año seleccionado
            comunas_data = data_comunas[data_comunas['Año'] == year_to_show]

            # Agrupar por comuna y sumar las víctimas
            comunas_data = comunas_data.groupby('COMUNA')['N_VICTIMAS'].sum().reset_index()

            # Ordenar por número de víctimas y seleccionar las 3 comunas con más víctimas
            comunas_data = comunas_data.sort_values(by='N_VICTIMAS', ascending=False)
            top_3_comunas = comunas_data[:3]
            other_comunas = pd.DataFrame([{
                'COMUNA': 'Otras',
                'N_VICTIMAS': comunas_data[3:]['N_VICTIMAS'].sum()
            }])

            # Concatenar las 3 comunas principales con la categoría "Otras"
            final_comunas_data = pd.concat([top_3_comunas, other_comunas])

            # Crear el gráfico de torta
            fig, ax = plt.subplots()
            ax.pie(final_comunas_data['N_VICTIMAS'], labels=final_comunas_data['COMUNA'], autopct='%1.1f%%', startangle=90, colors=COLOR_PALETTE)
            ax.axis('equal')  # Para asegurar que el gráfico sea un círculo.
            st.pyplot(fig)

    elif selected_view == "año_mes":
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de siniestros por año y mes
            st.title("📅 Cantidad de siniestros viales por año y mes")
            years_to_show = st.multiselect('Selecciona los años:', sorted(siniestros_por_mes['AÑO'].unique()), default=[2016], key='multiselect_years')
            siniestros_por_mes['MES_NUMERO'] = siniestros_por_mes['MES'].apply(lambda x: list(calendar.month_name).index(x))
            filtered_data = siniestros_por_mes[siniestros_por_mes['AÑO'].isin(years_to_show)]
            chart_data = filtered_data.pivot(index='MES_NUMERO', columns='AÑO', values='N_VICTIMAS')
            chart_data.index = [calendar.month_name[i] for i in chart_data.index]  # Convertir los números de los meses a nombres de meses
            st.line_chart(chart_data)

        with col2:
            # Gráfico de siniestros por tipo de víctima y mes
            st.title("🚶‍♂️🚗 Siniestros por Tipo de Víctima y Mes")

            # Agregar selección de año y mes
            selected_year = st.selectbox('Selecciona el año:', sorted(data['AÑO'].unique()), key='select_year_victims')
            selected_month = st.selectbox('Selecciona el mes:', list(calendar.month_name)[1:], key='select_month_victims')

            # Filtrar los datos según el año y mes seleccionados
            filtered_data = data[(data['AÑO'] == selected_year) & (data['MES'] == selected_month)]

            # Agrupar los datos filtrados por tipo de víctima
            victim_data = filtered_data.groupby('VICTIMA')['N_VICTIMAS'].sum().reset_index()

            fig, ax = plt.subplots(figsize=(10, 6))
            sb.barplot(data=victim_data, x='VICTIMA', y='N_VICTIMAS', ax=ax)
            ax.set_xlabel('Tipo de Víctima')
            ax.set_ylabel('Cantidad de Siniestros')
            ax.set_title(f'Siniestros por Tipo de Víctima en {selected_month} {selected_year}')
            st.pyplot(fig)


    elif selected_view == "mapa":
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Mapa de siniestros
            st.title("🗺️ Mapa de siniestros viales en CABA")
            mapa = folium.Map(location=[-34.6083, -58.3712], zoom_start=12)
            marker_cluster = MarkerCluster().add_to(mapa)
            for index, row in data.iterrows():
                folium.Marker([row['pos y'], row['pos x']], popup=row['N_VICTIMAS']).add_to(marker_cluster)
            folium_static(mapa)
        
        with col2:
            st.title("Mapa de Comunas")
            st.image("Imagenes/comunas.jpg", use_column_width=True)

# Configurar la barra lateral para la navegación entre páginas y gráficos
st.sidebar.title("🗂️ Navegación")

pages = {
    "Dashboard": show_dashboard,
    "Dataframes": show_dataframes,
    "KPIs": show_kpis
}
selection = st.sidebar.radio("Elige una página:", list(pages.keys()))

if selection == "Dashboard":
    st.sidebar.title("📊 Menú de Gráficos")
    if st.sidebar.button("Siniestros por Mes"):
        st.session_state.selected_view = "mes"
    if st.sidebar.button("Siniestros por Año y Mes"):
        st.session_state.selected_view = "año_mes"
    if st.sidebar.button("Mapa de Siniestros"):
        st.session_state.selected_view = "mapa"

# Ejecutar la función correspondiente a la página seleccionada
pages[selection]()
























