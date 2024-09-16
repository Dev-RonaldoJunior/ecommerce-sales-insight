import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def load_and_process_data(file_path):
    # Carregar dados do CSV
    data = pd.read_csv(file_path, usecols=['InvoiceDate', 'Quantity', 'UnitPrice', 'Country'])

    # Converter a coluna InvoiceDate para o tipo datetime
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%m/%d/%Y %H:%M')

    # Calcular o total de vendas
    data['Total'] = data['Quantity'] * data['UnitPrice']

    # Extrair o mês da data
    data['Mes'] = data['InvoiceDate'].dt.month

    return data

def plot_vendas_por_mes(data):
    # Agrupar vendas por mês
    vendas_por_mes = data.groupby('Mes')['Total'].sum()

    # Criar gráfico de vendas por mês
    plt.figure(figsize=(12, 6))
    bars = plt.barh(vendas_por_mes.index, vendas_por_mes, color='skyblue')
    plt.xlabel('Total de Vendas (R$)')
    plt.ylabel('Mês')
    plt.title('Total de Vendas por Mês')

    # Adicionar valores dentro das barras
    for bar in bars:
        width = bar.get_width()
        plt.text(width - (width * 0.03), bar.get_y() + bar.get_height() / 2,
                 f'R$ {width:,.2f}', va='center', ha='right', color='white')

    # Formatar o eixo x
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'R$ {x:,.2f}'))

    plt.tight_layout()
    plt.show()

def plot_vendas_por_pais(data):
    # Agrupar vendas por país
    vendas_por_pais = data.groupby('Country')['Total'].sum()

    # Criar gráfico de vendas por país
    plt.figure(figsize=(12, 10))
    bars = plt.barh(vendas_por_pais.index, vendas_por_pais, color='lightgreen')
    plt.xlabel('Total de Vendas (R$)')
    plt.ylabel('País')
    plt.title('Total de Vendas por País')

    # Adicionar valores dentro das barras
    for bar in bars:
        width = bar.get_width()
        country = bar.get_label()
        if country == 'United Kingdom':
            plt.text(width / 2, bar.get_y() + bar.get_height() / 2,
                     f'R$ {width:,.2f}', va='center', ha='center', color='black')
        else:
            plt.text(width + (width * 0.02), bar.get_y() + bar.get_height() / 2,
                     f'R$ {width:,.2f}', va='center', ha='left', color='black')

    plt.tight_layout()
    plt.show()

# Caminho do arquivo CSV
file_path = 'sales_data.csv'

# Carregar e processar os dados
data = load_and_process_data(file_path)

# Criar gráficos
plot_vendas_por_mes(data)
plot_vendas_por_pais(data)
