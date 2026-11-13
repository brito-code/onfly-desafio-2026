# Declaração de Uso de IA

**Ferramenta:** Cursor  
**Modelo:** Grok 4.7  

## Como utilizei a IA no projeto
Utilizei o Cursor como um assistente de contexto (para discutir a arquitetura do projeto), como facilitador de digitação e formatação, e para sanar duvidas.

**O que eu (Humano) fiz:**
- Configurei o ambiente virtual isolado (`.venv`).
- Li o `README.md` original e explorei os arquivos para compreender a estrutura do projeto.
- Executei a suíte de testes original (`pytest -q`) e li os erros no terminal para mapear onde estavam os problemas.
- Discuti minhas hipóteses com a IA para validar o meu entendimento sobre a regra de negócio do repositório (ex: as regras de no-show, cálculos de data e precisão monetária).
- Pensei e defini a lógica/abordagem de correção para cada um dos 5 defeitos (como trocar `float` por `Decimal`, tirar o `break`, usar *allow-list* no status).
- Avaliei criticamente as sugestões sintáticas da IA, garantindo que atendessem à minha abordagem de forma eficaz.
- Validei cada alteração rodando o `pytest` e realizei os *commits* atômicos um por um.
- Revisei e aprovei os textos de formatação final dos relatórios gerados a partir do meu contexto.

**O que a IA (Cursor) fez:**
- Explicou detalhes do contexto do repositório durante minha investigação inicial, auxiliando no meu entendimento do domínio do problema.
- A partir do meu raciocínio e abordagem, analisou o planejamento que criei e aplicou a mudança na sintaxe mecânica do arquivo específico.
- Ajudou a esclarecer comportamentos nativos do Python que eu precisava para a minha solução (como a ordenação de tuplas com sinal negativo).
- Baseando-se nas minhas instruções e validações, ajudou a formatar a documentação final.
- Não alterou o código base de regras, a pasta de testes e os dados, e não tomou nenhuma decisão de arquitetura de forma autônoma.