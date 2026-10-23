# Critérios do caso

Contexto fictício: aprovação de solicitações de reembolso em memória. A função aprovar é o ponto de entrada completo da decisão neste recorte; não há uma validação externa de perfil ou estado a pressupor. Usuários e pedidos de entrada são válidos, com os campos apresentados; valores são inteiros positivos em centavos. Não há pagamento real, banco de dados, interface web ou integração externa.

- C1 — Apenas usuário autenticado com perfil exatamente "aprovador" pode aprovar.
- C2 — Valores de até R$ 500,00, inclusive, podem ser aprovados; acima disso devem ser negados.
- C3 — Somente pedido com status "pendente" pode ser aprovado. Nova tentativa em pedido aprovado deve ser negada, sem gerar novo evento de aprovação.
- C4 — Toda aprovação deve gerar evento com identificador do pedido, ação e identificador do usuário responsável.
- C5 — Em ambiente de produção, eventos devem ser retidos por 180 dias.

E1 é o código numerado; E2 contém execuções locais determinísticas dos cenários S1 a S4. As execuções não demonstram armazenamento ou retenção em produção. O código foi criado com desvios intencionais para a aula.
