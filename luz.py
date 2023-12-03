import subprocess
import requests
import time
API_URL = "http://luisteixeira13.pythonanywhere.com/ilumina/"  # Substitua pelo URL real da sua API
def set_brightness(brightness):
    # Valores típicos para brightness: 0.1 (mínimo) a 1.0 (máximo)
    brightness = min(1.0, max(0.1, brightness))

    # Obtém a lista de dispositivos de exibição
    display_list = subprocess.check_output(["xrandr"]).decode("utf-8").splitlines()

    # Procura o nome do dispositivo de exibição (normalmente eDP-1, VGA-1, etc.)
    display_name = None
    for line in display_list:
        if " connected" in line:
            display_name = line.split()[0]
            break

    if display_name:
        # Ajusta o brilho usando xrandr
        subprocess.run(["xrandr", "--output", display_name, "--brightness", str(brightness)])
    else:
        print("Não foi possível encontrar o dispositivo de exibição.")

while True:
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            print(response.json())
            data = response.json()  # Aqui você acessa os dados JSON
            presenca = data['presença']
            if presenca == 'presente':
                set_brightness(0.9)
                print("Presente!!!")
            else:
                set_brightness(0.2)
            print("Dados enviados com sucesso para a API!")
        else:
            print(f"Falha ao enviar dados para a API. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar dados para a API: {e}")
    time.sleep(3)