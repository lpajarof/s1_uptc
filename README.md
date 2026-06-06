# Gemini API v2

Proyecto de ejemplo para ejecutar una consulta básica contra la API de Gemini utilizando el cliente `google-genai`.

## Descripción

- `app_gemini.py`: script principal que carga la clave API desde un archivo `.env` y consulta el modelo `gemini-3.5-flash` con una pregunta simple.
- `prueba_entorno.py`: script de verificación de entorno que comprueba si se está usando un entorno virtual y si hay conectividad a Internet.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Requisitos

- Python 3.11 o superior
- Una clave de API válida de Gemini configurada en un archivo `.env`

## Configuración

1. Crear un entorno virtual (opcional pero recomendado):

```powershell
python -m venv .venv
``` 

2. Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

4. Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
GEMINI_API_KEY=tu_clave_api_aqui
```

## Uso

Ejecutar el script principal:

```powershell
python app_gemini.py
```

Esto imprimirá la respuesta del modelo Gemini para la consulta de ejemplo.

## Verificar el entorno

Para comprobar la configuración del entorno y la conexión a Internet, ejecuta:

```powershell
python prueba_entorno.py
```

## Notas

- Asegúrate de no subir el archivo `.env` a repositorios públicos.
- Si usas Windows PowerShell y tienes políticas de ejecución restrictivas, ejecuta `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` antes de activar el entorno virtual.


## Evidencias
Ejecución del script
![Salida consola](/imagenes/img1.png)