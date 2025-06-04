import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1️⃣ Importar datos
df = pd.read_csv('medical_examination.csv')

# 2️⃣ Agregar columna overweight usando BMI
# BMI = peso / (altura en metros)^2
df['overweight'] = ((df['weight'] / ((df['height']/100)**2)) > 25).astype(int)

# 3️⃣ Normalizar datos: 0 = bueno, 1 = malo
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
