import pandas as pd

try:
	#poner ruta
	ruta_secretaria_movilidad = "/Users/juand/OneDrive/Escritorio/APRENDIZAJE_SUPERVISADO/MUERTO.csv"
	ruta_siniestros_usa ="/Users/juand/OneDrive/Escritorio/APRENDIZAJE_SUPERVISADO/Siniestros_usa.csv"
	# Cargar el dataset
	d_secretaria = pd.read_csv(ruta_secretaria_movilidad)
	d_siniestros = pd.read_csv(ruta_siniestros_usa)

	#Informacion del dataset

	with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', None,
                       'display.max_colwidth', None):

		print("\nInformacion del dataset de la secretaria de movilidad")
		print(d_secretaria.info())

		print("\nInformacion del dataset de siniestros en USA")
		print(d_siniestros.info())

except FileNotFoundError:
	    print("Error: No se encontró el archivo. Verifica la ruta.")
except pd.errors.EmptyDataError:
	    print("Error: El archivo está vacío.")
except pd.errors.ParserError:
	    print("Error: El archivo tiene un formato inválido.")
except Exception as e:
	    print(f"Ocurrió un error inesperado: {e}")