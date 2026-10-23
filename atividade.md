# Caso prático para participantes

## Missão de inspeção
Vocês são a equipe que examina um recorte de um fluxo de reembolso. Leiam os critérios C1 a C5, o código E1 e a execução E2. Em oito minutos, registrem até três achados e pelo menos uma limitação da conclusão. Não é necessário executar Python para participar.

## Como trabalhar
Distribuam leitura dos critérios, análise de código, conferência da execução e registro. Antes de responder, discutam: qual regra se aplica, onde está a evidência e o que ela permite concluir? Um representante acessa o Kahoot com o nome da squad e envia a resposta acordada.

Não presumam controles que não aparecem no recorte. Também não estendam um resultado local a toda a organização. Informações insuficientes podem exigir coleta adicional.

## Critérios de avaliação


Contexto fictício: aprovação de solicitações de reembolso em memória. A função aprovar é o ponto de entrada completo da decisão neste recorte; não há uma validação externa de perfil ou estado a pressupor. Usuários e pedidos de entrada são válidos, com os campos apresentados; valores são inteiros positivos em centavos. Não há pagamento real, banco de dados, interface web ou integração externa.

- C1 — Apenas usuário autenticado com perfil exatamente "aprovador" pode aprovar.
- C2 — Valores de até R$ 500,00, inclusive, podem ser aprovados; acima disso devem ser negados.
- C3 — Somente pedido com status "pendente" pode ser aprovado. Nova tentativa em pedido aprovado deve ser negada, sem gerar novo evento de aprovação.
- C4 — Toda aprovação deve gerar evento com identificador do pedido, ação e identificador do usuário responsável.
- C5 — Em ambiente de produção, eventos devem ser retidos por 180 dias.

E1 é o código numerado; E2 contém execuções locais determinísticas dos cenários S1 a S4. As execuções não demonstram armazenamento ou retenção em produção. O código foi criado com desvios intencionais para a aula.

## E1 Código numerado
```python
01  def aprovar(usuario, pedido, eventos):
02      if not usuario["autenticado"]:
03          return "negado"
04      if pedido["valor_centavos"] >= 50000:
05          return "negado"
06      pedido["status"] = "aprovado"
07      eventos.append({"pedido": pedido["id"], "acao": "aprovacao"})
08      return "aprovado"
```

## E2 Resumo das execuções
S1 — Usuário U-S1 autenticado, perfil leitor; pedido pendente de R$ 100,00. Resultado: aprovado; um evento com pedido e ação.
S2 — Usuário U-S2 autenticado, perfil aprovador; pedido pendente de R$ 500,00. Resultado: negado; nenhum evento.
S3 — Usuário U-S3 autenticado, perfil aprovador; pedido inicialmente pendente de R$ 100,00; duas chamadas sucessivas para o mesmo objeto. Resultados: aprovado e aprovado; dois eventos de aprovação.
S4 — Usuário U-S4 não autenticado, perfil aprovador; pedido pendente de R$ 100,00. Resultado: negado; nenhum evento.
O arquivo E2_execucao.json contém os registros completos, reproduzíveis pelo script executar_cenarios.py.

## Ficha de achados
Squad: __________________  Representante: __________________
Para cada achado, preencher: identificador; critério; arquivo, linha ou cenário; descrição do desvio; impacto possível; recomendação; verificação posterior.
Achado 1: __________________________________________________
Achado 2: __________________________________________________
Achado 3: __________________________________________________
Limitação ou evidência adicional necessária: __________________

## Resultado esperado da participação
Uma resposta por squad em cada questão e a justificativa de pelo menos um achado no encerramento. A classificação do jogo não representa, sozinha, uma avaliação de aprendizagem individual.
