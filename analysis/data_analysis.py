import polars as pl
import matplotlib.pyplot as plt

# Carregar os dados
df_weather = pl.read_parquet('../data/processed/weather_data_transformed.parquet')

# Extrair as colunas relevantes
temperatures = df_weather['temperature_celsius'].to_numpy()
cities = df_weather['city'].to_numpy()
humidities = df_weather['humidity'].to_numpy()

# Gerar o relatório em Markdown
with open('report.md', 'w') as report:
    report.write("# Relatorio de Analise Climatica\n")
    
    # Distribuição das Temperaturas
    plt.figure(figsize=(10, 6))
    plt.hist(temperatures, bins=20, alpha=0.7, label='Temperatura')
    plt.title('Distribuicao das Temperaturas em Celsius')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frequencia')
    plt.savefig('temperature_distribution.png')
    plt.close()
    report.write("## Distribuicao das Temperaturas em Celsius\n")
    report.write("![Distribuicao das Temperaturas](temperature_distribution.png)\n")
    
    # Temperatura por Cidade
    plt.figure(figsize=(10, 6))
    plt.bar(cities, temperatures, alpha=0.7)
    plt.title('Temperatura por Cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(rotation=45)
    plt.savefig('temperature_by_city.png')
    plt.close()
    report.write("## Temperatura por Cidade\n")
    report.write("![Temperatura por Cidade](temperature_by_city.png)\n")
    
    # Correlação entre Temperatura e Umidade
    plt.figure(figsize=(10, 6))
    plt.scatter(temperatures, humidities, alpha=0.7)
    plt.title('Correlacao entre Temperatura e Umidade')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Umidade (%)')
    plt.savefig('temperature_vs_humidity.png')
    plt.close()
    report.write("## Correlacao entre Temperatura e Umidade\n")
    report.write("![Correlacao entre Temperatura e Umidade](temperature_vs_humidity.png)\n")

print("Relatório gerado com sucesso: report.md")
