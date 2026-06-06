import os
from google import genai
from dotenv import load_dotenv

# Carga de variables de entorno desde el archivo .env
load_dotenv()

clave_api = os.getenv("GEMINI_API_KEY")

# Inicializa el cliente de Gemini con la clave API
cliente = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("⛷️ Ejecutando consulta a Gemini...")

    try:
        respuesta = cliente.models.generate_content(
            model="gemini-3.5-flash",
            contents="cuanto es el resultado de 2 + 2?"
        )
        print("Respuesta de Gemini:")
        print(respuesta.text)
    except Exception as e:
        print("Error al ejecutar la consulta:", e)

if __name__ == "__main__":
    ejecutar_consulta()
    