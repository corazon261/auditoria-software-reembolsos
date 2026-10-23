from src.reembolso import aprovar
import json

def executar():
    casos = [
        ("S1", "leitor", True, 10000, "pendente", 1),
        ("S2", "aprovador", True, 50000, "pendente", 1),
        ("S3", "aprovador", True, 10000, "pendente", 2),
        ("S4", "aprovador", False, 10000, "pendente", 1),
    ]
    saida = []
    for sid, perfil, autenticado, valor, status, vezes in casos:
        usuario = {"id": "U-" + sid, "perfil": perfil, "autenticado": autenticado}
        pedido = {"id": "P-" + sid, "valor_centavos": valor, "status": status}
        eventos = []
        respostas = [aprovar(usuario, pedido, eventos) for _ in range(vezes)]
        saida.append({"cenario": sid, "usuario": usuario, "valor_centavos": valor,
                      "status_inicial": status, "chamadas": vezes, "respostas": respostas,
                      "status_final": pedido["status"], "eventos": eventos})
    return saida

if __name__ == "__main__":
    print(json.dumps(executar(), ensure_ascii=False, indent=2))
