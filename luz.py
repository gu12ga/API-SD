import subprocess
import requests
import time

API_URL = "http://luisteixeira13.pythonanywhere.com/ilumina/"

def set_brightness(brightness):
    try:
        brightness = min(100, max(10, int(brightness * 100)))  # Converte para o formato aceito pelo 'light'

        subprocess.run(["light", "-S", str(brightness)])

        print(f"Brilho ajustado para {brightness}%")

    except subprocess.CalledProcessError as e:
        print(f"Falha ao ajustar o brilho: {e}")
    except Exception as e:
        print(f"Erro inesperado ao ajustar o brilho: {e}")

while True:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()
        presenca = data.get('presença', 'ausente')

        if presenca == 'presente':
            set_brightness(0.2)
            print("Presente!!!")
        else:
            set_brightness(0.2)

        print("Dados enviados com sucesso para a API!")

    except requests.RequestException as e:
        print(f"Falha ao enviar dados para a API: {e}")
    except Exception as e:
        print(f"Erro inesperado ao enviar dados para a API: {e}")

    time.sleep(3)

