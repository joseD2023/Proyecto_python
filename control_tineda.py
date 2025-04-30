import pandas as pd 
from pandas import ExcelWriter

# Crear DataFrame de ejemplo
df = pd.DataFrame({
    'Fecha_del_pedido': ['prueba1'],
    'Producto_solicitado': ['prueba1'],
    'Empresa_del_producto': ['prueba1'],
    'Total_a_pagar': ['prueba1']
})

# Reorganizar las columnas
df = df[['Fecha_del_pedido', 'Producto_solicitado', 'Empresa_del_producto', 'Total_a_pagar']]

# Crear un objeto ExcelWriter
writer = ExcelWriter('tienda.xlsx', engine='openpyxl')

# Escribir el DataFrame en la hoja de datos
df.to_excel(writer, 'Hoja de datos', index=False)

# Guardar el archivo Excel
writer.book.save('tienda.xlsx')





