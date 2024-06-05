<h1 align='center'>
 <b>Siniestros viales en la Ciudad de Buenos Aires 2016 - 2021</b>
</h1>

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme1.jpg)

<h2 align='center'>
 <b> Segundo Proyecto Individual Henry</b>
</h2>

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme2.jpg)

La Ciudad Autónoma de Buenos Aires (CABA), capital de la República Argentina, es una metrópoli vibrante y llena de historia, considerada uno de los principales centros culturales y económicos de América Latina. Con una población de aproximadamente 3 millones de habitantes, Buenos Aires es un núcleo cosmopolita donde se fusionan la tradición y la modernidad, atrayendo a millones de turistas cada año. La ciudad se destaca por su arquitectura europea, sus teatros, y su vida nocturna, además de ser la cuna del tango, un género musical y baile reconocido internacionalmente.

Históricamente, Buenos Aires ha sido el escenario de numerosos eventos significativos para la nación argentina. Fundada en 1580 por Juan de Garay, la ciudad ha crecido y evolucionado, desde sus raíces coloniales hasta convertirse en un centro urbano de relevancia global. Entre sus monumentos más emblemáticos se encuentran el Obelisco, el Teatro Colón y la Casa Rosada, sede del Poder Ejecutivo Nacional. Además, sus barrios como San Telmo, La Boca, y Recoleta ofrecen un vistazo a la rica herencia cultural y artística de la ciudad.

Sin embargo, detrás de esta fachada vibrante y culturalmente rica, Buenos Aires enfrenta serios desafíos, uno de los más graves es la seguridad vial. Los siniestros viales representan un problema enorme para la ciudad, afectando tanto a los residentes como a los visitantes. Según datos recientes, los accidentes de tránsito en la ciudad han causado un alarmante número de víctimas y heridos, lo que subraya la necesidad de medidas urgentes y eficaces para mejorar la seguridad vial.

Entre 2016 y 2021, Buenos Aires ha registrado una preocupante cantidad de siniestros viales, muchos de los cuales han resultado en fatalidades. Estos incidentes no solo causan un dolor inmenso a las familias afectadas, sino que también generan un impacto negativo en el sistema de salud pública y en la economía local. La gran cantidad de accidentes involucra a diversos tipos de vehículos, incluidos automóviles, motocicletas y peatones, lo que destaca la urgencia de implementar estrategias de prevención y educación vial.

La situación de los siniestros viales en Buenos Aires requiere atención inmediata y la colaboración de todos los sectores de la sociedad. Las autoridades municipales están trabajando en diversas iniciativas para reducir estos números alarmantes, como la mejora de la infraestructura vial, la implementación de campañas de concientización y la promoción de normas de tránsito más estrictas. Solo con un esfuerzo conjunto será posible hacer de Buenos Aires una ciudad más segura para todos sus habitantes y visitantes.


## Desarrollo del proyecto

El primer paso fue desmenuzar los datos. Para ello, me centré en realizar un proceso de ETL (Extracción, Transformación y Carga) con el cual definí los valores necesarios para entender los datos de la problemática. Así, analicé la composición y el tamaño de los datasets disponible, con el propósito de observar similitudes, diferencias, datos atipicos.

Para continuar, comencé un proceso de EDA (Análisis de Datos Exploratorio), para empezar a graficar ya con los datos correctamente cargados y entender el desafío al que se enfrenta la Ciudad Autónoma de Buenos Aires.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme3.jpg.png)


Todo el proceso se puede constatar en el link del repositorio (EDA.ipynb):

Con estos primeros datos, podemos observar que existe un fuerte disminución en la cantidad de siniestros viales en el año 2020. Por lo tanto, decidí verificar que no se tratase de datos erróneos.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/Casospordia.jpeg)

La variación en el año 2020 puede ser constatada gracias a los datos oficiales del organismo de salud en la Ciudad Autónoma de Buenos Aires. Allí, se vivió una de las cuarentenas más estrictas del país, por lo cual se vió afectado el número de siniestros viales. Sin embargo, esto significa que los datos no son erróneos y podemos continuar.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme4.jpg.png)

## Primer KPI 

Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses en la Ciudad Autónoma de Buenos Aires (CABA), en comparación con la tasa del semestre anterior.teniendo en cuenta que el Sistema Nacional de Información Criminal (SNIC) define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000.

Con el siguiente gráfico, buscaba darle solución al primer KPI, el cual buscaba la diferencia entre los últimos semestres del año. En el cual podemos confirmar que hubo una reducción de siniestros viales. Para ello, podemos mirar el Dashboard interactivo.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme5.jpeg)

Para continuar, comencé a graficar los distintos siniestros por comuna y tipo de vehículo. Allí, se puede ver con claridad que las víctimas fatales más comunes son los que se encuentran manejando una moto.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme6.png)

## Segundo KPI 

Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año en la Ciudad Autónoma de Buenos Aires (CABA), en comparación con el año anterior.

Para el siguiente KPI, habría que comparar ambos gráficos realizados. En los cuales podemos ver la cantidad de víctimas y la cantidad de víctimas motociclistas. Para ello, podemos también acceder al Dashboard.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme7.jpeg)

Con este KPI, podemos ver que la cantidad de víctimas lamentablemente no sólo ni disminuyó. Si no que aumentó considerablemente.

## Tercer KPI 

Para finalizar, en el tercer y último KPI, muestro cómo a pesar de la pandemia, el año 2021 tuvo una reducción en su cantidad de siniestros viales sobre autopistas frente al año 2020.

![image](https://github.com/Lorenzo09/Siniestros-Viales-CABA---An-lisis-de-Datos/blob/master/Imagenes/readme8.png)


## Creacion del Dashboard

Para finalizar el proyecto, decidí hacer un pequeño Dashboard con STREAMLIT. En él, utilicé los gráficos de manera eficiente para que cualquiera pueda visualizar los siniestros viales en CABA durante los años 2016 y 2021. Además de graficar los KPIs presentados en este documento.


## Datos utilizados

- [INDEC Instituto Nacional de Estadística de la República Argentina](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165) <br>
- [Buenos Aires Data](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165)

## Tecnologías utilizadas

- [pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)

## Contacto 
- Correo electrónico: lorenzolacava1@gmail.com
