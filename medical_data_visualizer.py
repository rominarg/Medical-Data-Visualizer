import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1️ Importar datos
df = pd.read_csv('medical_examination.csv')

# 2️ Agregar columna overweight usando BMI
# BMI = peso / (altura en metros)^2
df['overweight'] = ((df['weight'] / ((df['height']/100)**2)) > 25).astype(int)

# 3️ Normalizar datos: 0 = bueno, 1 = malo
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():

    # 5 Convertir a formato largo (melt)
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6 Contar valores por categoría
    df_cat = (
        df_cat
        .value_counts()
        .reset_index(name='total')
    )

    # Renombrar columnas para que catplot funcione
    df_cat.columns = ['cardio', 'variable', 'value', 'total']

    # 7 Crear el gráfico categórico
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 9 NO MODIFICAR ESTAS DOS LÍNEAS
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map

def draw_heat_map():

    # 11 Limpiar datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12 Calcular matriz de correlación
    corr = df_heat.corr()

# 13 Generar máscara para el triángulo superior
mask = np.triu(np.ones_like(corr, dtype=bool))

# 14 Configurar la figura
fig, ax = plt.subplots(figsize=(12, 8))


