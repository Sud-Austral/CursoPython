import pandas as pd
import pyodbc
import sqlalchemy
import datetime

# Variables
def ConectionString():
    return "Driver={SQL Server};Server=sud-austral.database.windows.net;Database=sudaustral;uid=sudaustral;pwd=Sud123456789"

def ConectionStringAlche():
    return "mssql+pyodbc://sudaustral:Sud123456789@sud-austral.database.windows.net/sudaustral?driver=SQL Server"

# Objetos
def Conexion():
    return pyodbc.connect(ConectionString())

def Cursor():
    conection = Conexion() 
    return conection.cursor();

def AlchemyConection():
    return sqlalchemy.create_engine(ConectionStringAlche())

# Funciones
def getDescripcion(ruta):
    return pd.read_excel(ruta, sheet_name="Descripcion_fuentes")

def getDetalle(ruta):
    return pd.read_excel(ruta, sheet_name="Detalle_fuente")

def getGeoservicio(ruta):
    return pd.read_excel(ruta, sheet_name="Geoservicios_fuentes")

def getArchivo(ruta):
    return pd.read_excel(ruta, sheet_name="Archivos_originales")

def getVariable(ruta):
    return pd.read_excel(ruta, sheet_name="Variables_originales")


def cleanDescripcion(ruta):
    data_descripcion_fuentes = getDescripcion(ruta)
    descripcion_fuentes = data_descripcion_fuentes.rename(columns={
        "ID_Fuente": "id", 
        "Entidad": "ENTIDADES_id",
        "Descripción":"entidad",
        "Metodo":"metodo",
        "Aplicaciones potenciales":"aplicaciones_potenciales"
    })
    return descripcion_fuentes

def cleanDetalle(ruta):
    data_detalle_fuentes = getDetalle(ruta)
    detalle_fuentes = data_detalle_fuentes.rename(columns={
        "ID_Fuente": "DESCRIPCION_FUENTES_id", 
        "Fuente": "fuente",
        "Nombre del set de datos":"nombre_set_datos",
        "Versión":"version_detalle",
        "Año":"anio",
        "Contacto":"nombre_contacto",
        "E-mail del contacto":"email_contacto",
        "Cobertura":"cobertura",
        "Licencia":"licencia",
        "Referencia principal":"referencia_principal",
        "Web":"web",
        "API":"api",
        "Especificaciones":"especificaciones",
        "Descarga Web":"descarga_web",
        "Descarga FTP":"descarga_ftp",
        "Descarga XML":"descarga_xml"
        })
    #descripcion_fuentes.head()
    #detalle_fuentes.head()
    detalle_fuentes["id"] = range(detalle_fuentes.shape[0]) 
    detalle_fuentes["id"] = detalle_fuentes["id"] + 1
    return detalle_fuentes

def cleanGeoservicio(ruta):
    data_geoservicios = getGeoservicio(ruta)
    geoservicios = data_geoservicios.rename(columns={
            "ID_Fuente": "DETALLE_FUENTES_id", 
            "Geoservicio": "geoservicio",
            "Tip_Geoserv":"tipo_geoservicio"
        })
    geoservicios["id"] = range(geoservicios.shape[0]) 
    geoservicios["id"] = geoservicios["id"] + 1
    return geoservicios

def cleanArchivo(ruta):
    data_archivo_original = getArchivo(ruta)
    archivo_original = data_archivo_original.rename(columns={
        "ID_Fuente": "DETALLE_FUENTES_id", 
        "ID_File": "id",
        "Colección":"coleccion",
        "Archivo":"archivo",
        "Nombre corto archivo":"nombre_corto_archivo",
        "Tipo de Dato":"tipo_dato",
        "Formato":"formato",
        "Nombre del archivo original":"nombre_archivo",
        "Nombre_CA":"nombre_ca",
        "Link de Descarga Web archivo Original":"link_descarga_web_original",
        "Link FTP archivo original":"link_ftp_original",
        "Link KML archivo original":"link_kml_original",
        "Link leyenda Imagen":"link_leyenda_imagen",
        "Link en Dropbox":"link_interno2",
        "Bloque_clip":"bloque_clip"
    })
    archivo_original["link_interno"] = ""
    archivo_original["ruta_interna"] = ""
    archivo_original["tag"] = ""
    archivo_original = archivo_original.fillna(value="")
    return archivo_original

def cleanVariable(ruta):
    data_variable_original = getVariable(ruta)
    variable_original = data_variable_original.rename(columns={
        "ID_File": "ARCHIVO_ORIGINAL_id", 
        "ID_Var": "id",
        "Variable":"variable",
        "Descripción":"descripcion",
        "Unidad":"unidad",
        "Fecha Consulta":"fecha_consulta",
        "Fecha inicio":"fecha_inicio",
        "Fecha fin":"fecha_final",
        "NombVar_estandar":"nombvar_estandar",
        "Fuente de la Variable original":"fuente_variable",
        "ID_Tema":"TEMA_id",
        "ID_SubTema":"SUBTEMAS_id",
        "TAG":"tag",
        "TAG - Ubicación":"tag_ubicacion",
        "TAG -Fecha":"tag_fecha"
    })
    variable_original["fecha_consulta"] = variable_original["fecha_consulta"].fillna(datetime.datetime(1971,1,1))
    variable_original["fecha_inicio"] = variable_original["fecha_inicio"].fillna(datetime.datetime(1971, 1, 1))
    variable_original["fecha_final"] = variable_original["fecha_final"].fillna(datetime.datetime(1771, 1, 1))
    return variable_original



