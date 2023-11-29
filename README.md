# Detecção de Movimento com OpenCV

Este código em Python utiliza a biblioteca OpenCV para detectar movimento em um ambiente capturado pela câmera do dispositivo. A detecção de movimento é realizada comparando frames consecutivos e destacando regiões com diferenças significativas. Siga as instruções abaixo para executar e entender o funcionamento do código.

## Requisitos:

- Python 3.x instalado.

- Instalação da biblioteca OpenCV. Você pode instalá-la executando o seguinte comando no terminal ou prompt de comando:

```
pip install opencv-python
```

## Executando o Código

1. Clone o repositório:

```
git clone https://github.com/gu12ga/API-SD.git
```

2. Execute o código:

```
python leitor.py
```

3. Encerrando a execução:

O programa continuará em execução até que a tecla '**q**' seja pressionada. Uma vez pressionada, o programa será encerrado e a janela de visualização será fechada.

## Funcionamento do código

O código utiliza a câmera do dispositivo para capturar frames consecutivos. A função "detecta_movimento" compara os frames consecutivos, realçando áreas com diferenças significativas. Se movimento for detectado, uma mensagem indicando "Presença detectada!" será exibida no console. A janela de visualização também mostrará o feed de vídeo, destacando áreas onde o movimento foi detectado.

## Observações

1. Certifique-se de que sua câmera esteja funcionando corretamente e é acessível pelo OpenCV.
1. Se estiver usando uma câmera embutida, você pode alterar cv2.VideoCapture(0) para cv2.VideoCapture(1) se houver problemas de detecção da câmera.
