import win32com.client
import pythoncom

import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv(override=True)

# Leer variables de entorno
provider = os.getenv("PROVIDER")
data_source = os.getenv("DATA_SOURCE")
exclusive = os.getenv("EXCLUSIVE")

# Construir la cadena de conexión
CONNECTION_STRING = (
    fr"Provider={provider};"
    fr"Data Source={data_source};"
    fr"Exclusive={exclusive};"
)


def open_connection():
    try:
        pythoncom.CoInitialize()
        connection = win32com.client.Dispatch('ADODB.Connection')
        connection.Open(CONNECTION_STRING)
        return connection
    except Exception as e:
        raise Exception(f"Error al abrir la conexión: {e}")


def execute_query(query):
    connection = None
    recordset = None
    try:
        connection = open_connection()
        recordset = win32com.client.Dispatch('ADODB.Recordset')
        recordset.Open(query, connection)

        data = []
        while not recordset.EOF:
            row = {recordset.Fields.Item(i).Name: recordset.Fields.Item(
                i).Value for i in range(recordset.Fields.Count)}
            data.append(row)
            recordset.MoveNext()
        return data
    except Exception as e:
        raise Exception(f"Error al ejecutar la consulta: {e}")
    finally:
        if recordset:
            recordset.Close()
        if connection:
            connection.Close()
        pythoncom.CoUninitialize()


def close_resources(recordset, connection):
    try:
        if recordset:
            recordset.Close()
        if connection:
            connection.Close()
    except Exception as e:
        print(f"Error al cerrar los recursos: {e}")
    finally:
        pythoncom.CoUninitialize()
