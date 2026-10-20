
def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False) -> float:
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    if subtotal < 0: raise ValueError("Subtotal e distância não podem ser negativos")
    if distancia_km < 0: raise ValueError("Subtotal e distância não podem ser negativos")
    if subtotal == 0 and distancia_km == 0: return 0.0

    desconto = 0.1 if cliente_vip else 0.0
    subtotal_com_desconto = subtotal * (1 - desconto)

    if subtotal_com_desconto >= 100: frete = 0
    else: frete = 8 + 1.5 * distancia_km

    total = subtotal_com_desconto + frete

    print(f"Subtotal: {subtotal}, subtotal com desconto: {subtotal_com_desconto}, Frete: {frete}, Total: {total}")
    
    return round(total, 2)