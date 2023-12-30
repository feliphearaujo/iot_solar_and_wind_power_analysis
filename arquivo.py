import pandas as pd
from influxdb import InfluxDBClient

# Configurações do InfluxDB
host = 'localhost'  # Endereço do InfluxDB
port = 8086         # Porta do InfluxDB
database = 'wind_power'   # Nome do banco de dados
measurement = 'wind_power'  # Nome da medição (tabela)

# Conectando ao InfluxDB
client = InfluxDBClient(host=host, port=port)
client.create_database(database)
client.switch_database(database)

# Lendo o arquivo CSV
csv_file = 'dados.csv'
df = pd.read_csv(csv_file)

# Convertendo os dados para o formato InfluxDB
data_points = []
for index, row in df.iterrows():
    data_point = {
        "measurement": measurement,
        "time": pd.to_datetime(row["time"]),
        "fields": {
            "wind_speed_mph": row["wind_speed_mph"],
            "wind_power_watt": row["wind_power_watt"],
        }
    }
    data_points.append(data_point)

# Escrevendo os dados no InfluxDB
client.write_points(data_points)

# Fechando a conexão com o InfluxDB
client.close()
