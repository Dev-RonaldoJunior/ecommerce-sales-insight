
# Análise de Vendas

Este projeto realiza a análise de dados de vendas com base em um arquivo CSV. O objetivo é gerar visualizações que ajudam a entender melhor o desempenho das vendas ao longo do tempo e por país.

## Descrição do Projeto

O projeto contém um script Python que processa dados de vendas e gera dois tipos de gráficos:

- **Gráfico de Vendas por Mês**: Mostra o total de vendas acumuladas para cada mês em um gráfico de barras horizontais.
- **Gráfico de Vendas por País**: Exibe o total de vendas por país, com destaque especial para o Reino Unido, onde os valores são exibidos dentro das barras.

## Estrutura do Projeto

- `analyze_sales.py`: Script Python que realiza a leitura, processamento e visualização dos dados.
- `sales_data.csv`: Arquivo CSV de exemplo contendo dados de vendas.
- `.gitignore`: Arquivo para excluir arquivos e pastas indesejadas do controle de versão.
- `requirements.txt`: Lista de dependências necessárias para executar o script.

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <URL-do-repositório>
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd <nome-do-repositório>
   ```

3. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Coloque o arquivo `sales_data.csv` na mesma pasta que o script `analyze_sales.py`.**

2. **Execute o script para gerar os gráficos:**
   ```bash
   python analyze_sales.py
   ```

   O script criará e exibirá dois gráficos: um para vendas por mês e outro para vendas por país.

## Dependências

O projeto usa as seguintes bibliotecas Python:

- `pandas`
- `matplotlib`

Estas dependências estão listadas no arquivo `requirements.txt`.

## Observações

- Certifique-se de que o arquivo `sales_data.csv` está no formato correto e contém as colunas necessárias: `InvoiceDate`, `Quantity`, `UnitPrice`, e `Country`.
- O script pode demorar um pouco para carregar e gerar os gráficos, dependendo do tamanho do arquivo de dados.

## Contribuição

Contribuições são bem-vindas. Para sugestões ou melhorias, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
