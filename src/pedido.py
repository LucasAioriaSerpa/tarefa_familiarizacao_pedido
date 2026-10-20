
def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False) -> float:
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    print(f"Calculando total do pedido com subtotal: {subtotal}, distância: {distancia_km}, cliente VIP: {cliente_vip}")

    if subtotal < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")
    if distancia_km < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")

    desconto = 0.1 if cliente_vip else 0
    subtotal_com_desconto = desconto * subtotal if desconto > 0 else subtotal

    if subtotal_com_desconto > 100: frete = 0
    else: frete = 8 + 1.5 * distancia_km

    total = subtotal + frete

    print(f"Subtotal: {subtotal}, Desconto: {subtotal_com_desconto}, Frete: {frete}, Total: {total}")
    
    return round(total)
