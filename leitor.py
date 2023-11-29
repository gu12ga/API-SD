# Faz a instalação:
#
#pip install opencv-python
#
#
import cv2
import time 

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

# Inicializa a câmera
captura = cv2.VideoCapture(0)

# Lê o primeiro frame
_, frame_antigo = captura.read()

while True:
    # Lê o próximo frame
    _, frame_atual = captura.read()

    # Detecta movimento
    movimento = detecta_movimento(frame_antigo, frame_atual)

    # Atualiza o frame antigo
    frame_antigo = frame_atual.copy()

    # Exibe o resultado
    if movimento:
        print("Presença detectada!")

    # Exibe o frame (opcional)
    cv2.imshow("Detecção de Presença", frame_atual)
    
    # timer para capturar o próximo frame.
    time.sleep(1)

    # Sai do loop quando a tecla 'q' é pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
captura.release()
cv2.destroyAllWindows()
