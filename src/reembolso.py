def aprovar(usuario, pedido, eventos):
    if not usuario["autenticado"]:
        return "negado"
    if pedido["valor_centavos"] >= 50000:
        return "negado"
    pedido["status"] = "aprovado"
    eventos.append({"pedido": pedido["id"], "acao": "aprovacao"})
    return "aprovado"
