import cv2
import time
import json

import requests
API_URL = "http://luisteixeira13.pythonanywhere.com/leitor/"  # Substitua pelo URL real da sua API
# Função para detectar movimento
def detecta_movimento(frame_antigo, frame_atual, threshold=25):
    # Converte os frames para escala de cinza
    frame_antigo_cinza = cv2.cvtColor(frame_antigo, cv2.COLOR_BGR2GRAY)
    frame_atual_cinza = cv2.cvtColor(frame_atual, cv2.COLOR_BGR2GRAY)

    # Calcula a diferença absoluta entre os frames
    diferenca = cv2.absdiff(frame_antigo_cinza, frame_atual_cinza)

    # Aplica um limiar para destacar as regiões com diferença significativa
    _, threshold_dif = cv2.threshold(diferenca, threshold, 255, cv2.THRESH_BINARY)

    # Encontra contornos na imagem
    contornos, _ = cv2.findContours(threshold_dif, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verifica se há contornos significativos
    return len(contornos) > 0

captura = cv2.VideoCapture(0)
_, frame_antigo = captura.read()

cv2.namedWindow("Detecção de Presença", cv2.WINDOW_NORMAL)

teste = False
teste2 = 0

while True:
    _, frame_atual = captura.read()
    movimento = detecta_movimento(frame_antigo, frame_atual, threshold=100)
    frame_antigo = frame_atual.copy()

    if teste:
        teste2 += 1
        if teste2 >= 3:
            try:
                data = {"presença": "presente"}
                headers = {"Content-Type": "application/json"}
                response = requests.post(API_URL, data=json.dumps(data), headers=headers)
                if response.status_code == 200:
                    print("Dados enviados com sucesso para a API!")
                else:
                    print(f"Falha ao enviar dados para a API. Código de status: {response.status_code}")
            except Exception as e:
                print(f"Erro ao enviar dados para a API: {e}")
            
    
    if movimento:
        print("Presença detectada!")

        teste2 = 0
        teste = True

        # Aqui você pode adicionar a lógica para enviar dados para a API
        # Exemplo de envio de dados usando requests.post com JSON
        try:
            data = {"presença": "presente"}
            headers = {"Content-Type": "application/json"}
            response = requests.post(API_URL, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("Dados enviados com sucesso para a API!")
            else:
                print(f"Falha ao enviar dados para a API. Código de status: {response.status_code}")
        except Exception as e:
            print(f"Erro ao enviar dados para a API: {e}")

    cv2.imshow("Detecção de Presença", frame_atual)
    key = cv2.waitKey(1) & 0xFF
    
    if key in (ord('q'), 27):
        break

captura.release()
cv2.destroyAllWindows()