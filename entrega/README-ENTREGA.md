# Relatório de Correções - Desafio Onfly

## Como comecei (Metodologia)
Antes de alterar qualquer código, criei um ambiente virtual (`.venv`) e rodei a ferramenta Ruff para garantir que a sintaxe estava correta. Depois, rodei os testes automatizados que já vieram no projeto com o comando `pytest -q`. 

O resultado inicial foi **`5 failed in 2.59s`**. Olhando o que o terminal imprimiu (os *tracebacks*), consegui entender o que o sistema esperava e o que ele estava devolvendo de errado. A partir daí, foquei em corrigir um erro por vez, rodando o teste novamente a cada alteração para garantir que funcionava.

## Mapa de Defeitos Corrigidos

**1. Noites negativas (`stay_calculator.py`)**
- **O erro:** O código subtraía apenas o dia do mês (`.day`). Se o check-in fosse dia 30 e o check-out dia 02, o resultado dava -28 noites.
- **A correção:** Mudei a conta para subtrair as datas inteiras usando `(checkout - checkin).days`. Assim o Python já resolve sozinho a virada do mês usando `timedelta`.

**2. Erro de precisão nos valores (`currency_converter.py`)**
- **O erro:** O código usava `float` para converter as moedas e fazia uma divisão. Pesquisando sobre isso, vi que usar `float` para dinheiro gera pequenos erros nos centavos por causa da forma como o computador faz a conta, além de a divisão estar invertendo o valor.
- **A correção:** Troquei o `float` por `Decimal` (que é o ideal para dinheiro em Python) e passei a multiplicar o valor pela taxa de câmbio (`amount * rates[currency]`).

**3. Cobrança de NO_SHOW (`status_policy.py`)**
- **O erro:** A função aceitava qualquer status que fosse diferente de "CANCELLED". Com isso, as reservas marcadas como "NO_SHOW" estavam entrando na conta do faturamento incorretamente.
- **A correção:** Mudei a lógica para ser bem restrita: agora o código só soma no faturamento se o status for exatamente `"CONFIRMED"`.

**4. Ranking invertido (`report_builder.py`)**
- **O erro:** A lista dos top hotéis ordenava a chave `amount` do menor para o maior.
- **A correção:** Ajustei a chave de ordenação para usar o valor numérico `total_brl` com um sinal de menos na frente `(-h["total_brl"])`. Isso inverte a ordem nativa do Python, colocando os maiores faturamentos no topo. Em caso de empate, o `hotel_id` desempata por ordem alfabética.

**5. Leitura incompleta do CSV (`csv_reservation_repository.py`)**
- **O erro:** Tinha um `break` no meio do loop fazendo o código parar de ler o arquivo na linha 200. O arquivo original tem 300 reservas, então 100 ficavam de fora sem dar nenhum aviso de erro.
- **A correção:** Simplesmente removi o limite e o `break`, deixando o iterador do arquivo ler todas as linhas até o final.

## Como Validar

Para testar as correções no ambiente virtual, basta rodar:

```powershell
ruff check .
pytest -q
```

## Resultado dos Testes

Depois das cinco correções, a suíte completa passou:

```text
5 passed in 2.78s
```