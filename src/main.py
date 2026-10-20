
from pedido import calcular_total_pedido

print("\ntotal esperado: 103.00")
calcular_total_pedido(80.00, 10, False)
# Retorno esperado: 103.00

print("\ntotal esperado: 120.00")
calcular_total_pedido(120.00, 10, False)
# Retorno esperado: 120.00

print("\ntotal esperado: 113.00")
calcular_total_pedido(100.00, 10, True)
# Retorno esperado: 113.00

print("\ntotal esperado: 0.00")
try: 
    calcular_total_pedido(-10.00, 5, False)
except ValueError as e:
    print(f"Erro esperado: {e}")
# Deve lançar ValueError
