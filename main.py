import pandas as pd

# Datos
datos = [
    {"estudiante": "Ana", "materia": "Mate",     "periodo": "2024-1", "nota": 4.5},
    {"estudiante": "Ana", "materia": "Historia", "periodo": "2024-1", "nota": 3.8},
    {"estudiante": "Ana", "materia": "Mate",     "periodo": "2024-2", "nota": 4.2},
    {"estudiante": "Luis","materia": "Mate",     "periodo": "2024-1", "nota": 3.5},
    {"estudiante": "Luis","materia": "Historia", "periodo": "2024-2", "nota": 4.0},
    {"estudiante": "sergio","materia": "Mate",    "periodo": "2024-1", "nota": 4.8},
    {"estudiante": "sergio","materia": "Historia","periodo": "2024-2", "nota": 4.9}
]

df = pd.DataFrame(datos)


# 1. Procesamiento de información
print("\n Notas por estudiante:")
for estudiante, grupo in df.groupby('estudiante'):
    print(f"\nEstudiante: {estudiante}")
    print(grupo[['materia', 'periodo', 'nota']])

# 2. Cálculo de promedio
promedio = df['nota'].mean()
print(f"\n Promedio general del curso: {promedio:.2f}")

# 3. Tendencia por período
print("\n Tendencia de rendimiento por estudiante:")
tendencia = df.groupby(['estudiante', 'periodo'])['nota'].mean().unstack()
print(tendencia)

# 4. Transformación básica (1.1)
df['nota_ajustada'] = df['nota'] * 1.1  # Ajuste del 10%
print("\n4. Notas con ajuste del 10%:")
print(df[['estudiante', 'materia', 'nota', 'nota_ajustada']].to_string(index=False))

# 5. Almacenamiento (2.2)
df.to_csv('notas_estudiantes.csv', index=False)
print("\n5. Datos guardados en 'notas_estudiantes.csv'")