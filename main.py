import matplotlib.pyplot as plt

from medical_data_visualizer import df  # importamos el DataFrame ya modificado

# Mostrar las primeras filas para verificar
print("Primeras filas del dataset:")
print(df.head())

# Verificar que se creó la columna 'overweight'
print("\nConteo de valores en 'overweight':")
print(df['overweight'].value_counts())

# Verificar que gluc y cholesterol están normalizados
print("\nConteo de valores en 'cholesterol':")
print(df['cholesterol'].value_counts())

print("\nConteo de valores en 'gluc':")
print(df['gluc'].value_counts())

