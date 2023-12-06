## Controle Automático de Brilho com Integração API - README

Este script Python foi desenvolvido para automatizar o ajuste de brilho do monitor com base nos dados de presença obtidos de uma API hospedada no PythonAnywhere. Diferentemente da branch cliente2, este utiliza o comando light para controlar o brilho do monitor. Siga as instruções abaixo para configurar e executar o script.
Configuração:

## Certifique-se de ter as seguintes dependências instaladas no seu ambiente:

    - Python 3
    - Biblioteca requests: Instale utilizando o comando pip install requests
    Utilitário light: Este utilitário é utilizado para ajustar o brilho. Instale-o usando o gerenciador de pacotes do seu sistema operacional.

    Para sistemas  Ubuntu:

    -  sudo apt-get install light

## Execução:

    Abra um terminal no diretório onde o script está localizado.
    Execute o script Python:

    -  luz.py

## Observações:

    O script permanecerá em execução continuamente, verificando a presença a cada 3 segundos (pode ser ajustado no script).

    Se a presença for detectada (valor 'presente' recebido da API), o brilho do monitor será ajustado para 80%.

    Se a presença não for detectada, o brilho será ajustado para 20%.

    Certifique-se de que o usuário que executa o script tem permissões para usar o comando light.

    Se o script não conseguir ajustar o brilho, verifique se o comando light está disponível no seu sistema e se a instalação foi concluída com êxito.

## Exemplo de Execução:

    - python3 caminho/do/arquivo luz.py

## Avisos:

    Recomenda-se ajustar o intervalo de verificação da presença no script de acordo com seus requisitos específicos.

    Este script foi projetado para sistemas Linux que suportam o comando light. Pode não funcionar corretamente em outros sistemas operacionais.

## Nota:

Este readme assume que o usuário possui conhecimentos básicos em execução de scripts Python, configuração de ambientes Linux e tem uma API funcional hospedada no PythonAnywhere. Certifique-se de revisar e adaptar o script de acordo com os requisitos específicos do seu ambiente e sistema operacional.