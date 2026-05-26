import pandas as pd

# Lectura obligatoria con ruta relativa
df = pd.read_csv('datos/sales_sample_2024.csv')

print("--- ¡DATOS CARGADOS CON ÉXITO POR PACO! ---")
print(df.head()) # Muestra las primeras filas de tus datos reales

# Resumen estadístico simple guardado en la carpeta resultados
resumen = df.describe()
resumen.to_csv('resultados/resumen_ventas.csv')
print("\n¡Reporte generado con exito en resultados/resumen_ventas.csv!")
