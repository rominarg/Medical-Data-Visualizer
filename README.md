# 🩺 Medical Data Visualizer

Este proyecto realiza **análisis y visualización de datos médicos** utilizando Python y librerías de ciencia de datos como **pandas**, **matplotlib** y **seaborn**. Forma parte del programa de certificación de **freeCodeCamp** y está diseñado para trabajar con datos reales de exámenes médicos.

---

##  Objetivo del proyecto

El objetivo principal es **explorar la relación entre enfermedades cardiovasculares y distintos factores clínicos y de estilo de vida**, mediante limpieza de datos, transformación de variables y visualizaciones claras.

Se analizan variables como:

* Presión arterial
* Colesterol y glucosa
* Peso, altura y sobrepeso (IMC)
* Hábitos como fumar, consumo de alcohol y actividad física

---

##  Dataset

**Archivo:** `medical_examination.csv`

Cada fila representa un paciente y cada columna contiene información médica recopilada durante exámenes clínicos.

### Variables principales

| Variable    | Descripción                       |
| ----------- | --------------------------------- |
| age         | Edad (en días)                    |
| height      | Altura (cm)                       |
| weight      | Peso (kg)                         |
| ap_hi       | Presión sistólica                 |
| ap_lo       | Presión diastólica                |
| cholesterol | Nivel de colesterol               |
| gluc        | Nivel de glucosa                  |
| smoke       | Fumador (binario)                 |
| alco        | Consumo de alcohol (binario)      |
| active      | Actividad física (binario)        |
| cardio      | Enfermedad cardiovascular (0 / 1) |

---

## 🛠️ Tecnologías utilizadas

* Python 3
* pandas
* numpy
* matplotlib
* seaborn
* unittest (tests automáticos)

##  Funcionalidades implementadas

### 1. Limpieza y transformación de datos

* Creación de la variable **overweight** usando el Índice de Masa Corporal (IMC)
* Normalización de variables clínicas (0 = buen estado, 1 = mal estado)
* Eliminación de datos inconsistentes y outliers

### 2. Visualización categórica

Se genera un gráfico categórico que muestra la distribución de:

* colesterol
* glucosa
* tabaquismo
* consumo de alcohol
* actividad física
* sobrepeso

Comparando pacientes con y sin enfermedad cardiovascular.

 Salida: `catplot.png`

### 3. Mapa de calor de correlaciones

Se construye un **heatmap** para analizar la correlación entre variables médicas, aplicando una máscara para el triángulo superior de la matriz.

 Salida: `heatmap.png`

---

