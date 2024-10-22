import pandas as pd
from pyproj import Transformer
import time

# Converter de SIRGAS 2000 (EPSG:4674) para UTM (exemplo para Zona 22S - EPSG:32722)
transformer = Transformer.from_crs("EPSG:4674", "EPSG:32722", always_xy=True)

def converter_para_utm(lon, lat):
    easting, northing = transformer.transform(lon, lat)
    return easting, northing

df = pd.read_csv('entrada.csv', sep=';')

df[['Easting', 'Northing']] = df.apply(
    lambda row: converter_para_utm(row['Longitude'], row['Latitude']), axis=1, result_type='expand'
)

df.to_csv('saida.csv', sep=',', index=False)

print("Conversão concluída e salva no arquivo 'saida.csv'.")
time.sleep(3)
