
from pedido import calcular_total_pedido

print("total esperado: 103.00")
calcular_total_pedido(80.00, 10, False)
# Retorno esperado: 103.00

print("total esperado: 120.00")
calcular_total_pedido(120.00, 10, False)
# Retorno esperado: 120.00

print("total esperado: 113.00")
calcular_total_pedido(100.00, 10, True)
# Retorno esperado: 113.00
