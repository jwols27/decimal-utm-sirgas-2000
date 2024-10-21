import pandas as pd
from pyproj import Transformer

# Configuração do transformer para converter de SIRGAS 2000 (EPSG:4674) para UTM (exemplo para Zona 22S - EPSG:32722)
transformer = Transformer.from_crs("EPSG:4674", "EPSG:32722", always_xy=True)

# Função para converter longitude e latitude para UTM
def converter_para_utm(lon, lat):
    easting, northing = transformer.transform(lon, lat)
    return easting, northing

# Ler o arquivo CSV com separador ',' e com colunas na ordem 'Longitude;Latitude'
df = pd.read_csv('conversor.csv', sep=',')

# Aplicar a conversão para cada linha do DataFrame e armazenar em novas colunas
df[['Easting', 'Northing']] = df.apply(
    lambda row: converter_para_utm(row['Longitude'], row['Latitude']), axis=1, result_type='expand'
)

# Salvar o resultado em um novo arquivo CSV com ';' como separador
df.to_csv('saida.csv', sep=',', index=False)

print("Conversão concluída e salva no arquivo 'saida.csv'.")
