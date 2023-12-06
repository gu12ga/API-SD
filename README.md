## Controle Automático de Brilho com Integração API - README

Este script Python foi desenvolvido para automatizar o ajuste de brilho do monitor com base nos dados de presença obtidos de uma API hospedada no PythonAnywhere. O script utiliza o comando xrandr para controlar o brilho do monitor. Siga as instruções abaixo para configurar e executar o script.
Configuração:

## Certifique-se de ter as seguintes dependências instaladas no seu ambiente:

    - Python 3
    - Biblioteca requests: Instale utilizando o comando pip install requests
    - Xrandr que pode ser instalado com : sudo apt-get install x11-xserver-utils

**A variável API_URL no script representa a API hospedada no PythonAnywhere, de onde os dados de presença serão obtidos.**

## Execução:

    Abra um terminal no diretório onde o script está localizado.

    Execute o script Python:

    - luz.py

## Observações:

    O script permanecerá em execução continuamente, verificando a presença a cada 3 segundos (pode ser ajustado no script).
    Se a presença for detectada (valor 'presente' recebido da API), o brilho do monitor será ajustado para 0.9.
    Se a presença não for detectada, o brilho será ajustado para 0.2.
    Certifique-se de que o usuário que executa o script tem permissões para usar o comando xrandr.
    Se o script não conseguir encontrar o dispositivo de exibição, verifique se o comando xrandr está disponível e se o monitor está conectado corretamente.

## Exemplo de Execução:

- python3 caminho/do/arquivo luz.py

**Avisos:**

    Este script foi projetado para sistemas Linux que suportam o comando xrandr. Pode não funcionar corretamente em outros sistemas operacionais.
    Recomenda-se ajustar o intervalo de verificação da presença no script de acordo com seus requisitos específicos.

## Nota:

Este readme assume que o usuário possui conhecimentos básicos em execução de scripts Python, configuração de ambientes Linux e tem uma API funcional hospedada no PythonAnywhere. Certifique-se de revisar e adaptar o script de acordo com os requisitos específicos do seu ambiente e sistema operacional.