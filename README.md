# Projeto: Controle de Brilho Distribuído

## Alunos
- Gustavo Gabriel Martins
- Ronald De Souza Galdino
- Luis Felipe Costa Teixeira

## Índice
# Índice
- [Descrição da Arquitetura no GitHub](#descrição-da-arquitetura-no-github)
  - [Criação do Django](#0-Criação do DJango)
  - [Visão Geral do Sistema Distribuído](#1-visão-geral-do-sistema-distribuído)
  - [Arquitetura de Microserviços](#2-arquitetura-de-microserviços)
  - [Integração com Django](#3-integração-com-django)
  - [Sensor de Presença e Controle de Luz](#4-sensor-de-presença-e-controle-de-luz)
  - [Referências e Base Teórica](#5-referências-e-base-teórica)
- [Qualidade do Tutorial no README](#qualidade-do-tutorial-no-readme)
  - [Instalação](#1-instalação)
  - [Configuração](#2-configuração) 
  - [Execução do Sistema](#3-execução-do-sistema)
    - [Para leitor.py (Sensor)](#para-leitorpy-sensor)
    - [Para luz.py (Recebedor de Solicitações)](#para-luzpy-recebedor-de-solicitações-e-controlador-de-brilho)
  - [Uso do Sensor de Presença](#4-uso-do-sensor-de-presença)
  - [Exemplos de Requisições à API](#5-exemplos-de-requisições-à-api)
  - [Resolução de Problemas Comuns](#6-resolução-de-problemas-comuns)

### 0. Criação do DJango
Requisitos: Ter o python instalado.

Primeiro é preciso baixar o DJango, rode o comando no terminal: pip install django
Teste se ocorreu corretamente: django-admin --version

Para criar o projeto Django rode o comando em um diretório específico: django-admin startproject nome_do_projeto
Caso haja migrações para o BD: python manage.py migrate

Criando um novo aplicativo: python manage.py startapp nome_do_app

Altere a configuração do arquivo settings.py para adcionar o app e poder acessar ele:
INSTALLED_APPS = [
    # ...
    'nome_do_app',
]

Para adicionar as URLs, crie um arquivo url.py no app para exportar as urls para o arquivo url padrão da API.
urls.py padrão da API:
urlpatterns = [
    path('', include('app.urls'))
]

Adicone o localhost no arquivo settings.py:
ALLOWED_HOSTS = ['127.0.0.1']

Para executar, basta rodar o comando no terminal: python manage.py runserver

## Descrição da Arquitetura no GitHub

### 1. Visão Geral do Sistema Distribuído

O projeto visa criar um sistema distribuído utilizando Django, destacando a necessidade de distribuição para suportar a complexidade da aplicação. Os principais componentes incluem microserviços, uma REST API, e integração com um sensor de presença baseado em câmera para controle de luz do computador.

### 2. Arquitetura de Microserviços

O sistema é estruturado em microserviços independentes, cada um responsável por funcionalidades específicas. Os microserviços são modularizados para facilitar manutenção, escalabilidade e implementação ágil de novos recursos.

### 3. Integração com Django

Cliente-Servidor em Sistemas Distribuídos

O paradigma cliente-servidor é fundamental em sistemas distribuídos, onde as funções do sistema são divididas entre clientes, que solicitam serviços, e servidores, que fornecem esses serviços. No contexto do projeto, o sensor de presença e o atuador de luz agem como clientes, fazendo requisições para a REST API no servidor PythonAnywhere, que por sua vez processa esses dados e os responde.

**Características do Modelo Cliente-Servidor:**

  - Centralização de Lógica de Negócios: O servidor centraliza a lógica de negócios e fornece serviços para os clientes. Neste projeto, o servidor Django gerencia a lógica de controle de luz e recebe dados do sensor.

  - Descentralização de Recursos: Os clientes (sensores e atuadores de luz) e o servidor podem estar distribuídos em diferentes locais geográficos, permitindo uma arquitetura distribuída eficiente.

  - Comunicação Assíncrona: O modelo cliente-servidor permite a comunicação assíncrona, onde os clientes podem enviar solicitações e continuar a operar enquanto aguardam a resposta do servidor. Isso é crucial em sistemas distribuídos para otimizar o desempenho e a escalabilidade.

  - Escalabilidade: A arquitetura cliente-servidor facilita a escalabilidade, permitindo a adição de novos clientes e servidores conforme necessário.

Arquitetura Baseada em Eventos

Dentro do contexto do trabalho, foi utilizada a arquitetura cliente-servidor como base para a implementação do estilo arquitetônico de marramento de eventos. No caso, o barremnto seria a API, e os componentes seriam o sensor de luz baseado em câmera e o atuador de luz.

### 4. Sensor de Presença e Controle de Luz

Um componente crucial do sistema é o sensor de presença baseado na câmera. Ele detecta a presença e altera dinamicamente a intensidade da luz do computador. A integração com Django ocorre por meio de APIs dedicadas que recebem informações do sensor e respondem as requisições dos clientes quando eles solicitam, os quais ajustam as configurações de luz correspondentes.

### 5. Referências e Base Teórica

A arquitetura reflete conceitos fundamentais discutidos na disciplina GCC129 - Sistemas Distribuídos, conforme abordados no livro base. Referências adicionais incluem pesquisas em sites.

## Qualidade do Tutorial no README
### 1. Instalação

Clone o repositório:

git clone https://github.com/gu12ga/API-SD/tree/main

### 2. Configuração

Após clonar o repositório, a configuração varia dependendo do papel que a sua máquina desempenhará no sistema: se será o leitor.py (sensor) ou o luz.py (recebedor de solicitações e controlador de brilho). Abaixo estão as instruções para cada cenário:

Se a sua máquina é responsável pelo sensor, você deve apenas rodar o código.

Se sua máquina é responsável pelo controle de brilho (luz.py), é importante observar a branch em que você está trabalhando:

Para a branch cliente2, é necessário instalar o xrandr. Execute:

    sudo apt-get install x11-xserver-utils

Para a branch cliente2.1, é necessário instalar o light. Execute:

    sudo apt-get install light

Certifique-se de instalar as dependências corretas de acordo com a branch que você está utilizando.


### 3. Execução do Sistema

#### Para leitor.py (Sensor):

1. Abra o terminal e navegue até o diretório do projeto.
2. Execute o seguinte comando para rodar o código:
 
   python3 leitor.py ou execute direto do VS Code

#### Para luz.py (Recebedor de Solicitações e Controlador de Brilho):

1. Abra o terminal e navegue até o diretório do projeto.
2. Execute o seguinte comando para rodar o código:

   python3 luz.py no terminal do diretório

### 4. Uso do Sensor de Presença

Ao executar o sensor, a câmera do seu notebook ou computador será ativada, iniciando a detecção de presença. Em caso de movimento detectado, o sensor enviará a informação para o servidor PythonAnywhere que hospeda a API Django. Isso acionará a alteração dinâmica do brilho em outro computador que estiver executando o código responsável pelo controle de luz.

### 5. Exemplos de Requisições à API
A API possui endpoints específicos para o sensor de presença e o controle de luz. Abaixo estão exemplos de como realizar requisições para interagir com esses endpoints:

- **Enviar Dados do Sensor (Detectar Presença):**
  - **Método:** POST
  - **Endpoint:** `/api/leitor/`
  - **Descrição:** Envia dados do sensor para o servidor indicando a detecção de presença.

- **Ajustar Brilho com Base na Detecção de Movimento:**

  - **Método:** GET
  - **Endpoint:** `/api/ilumina/`
  - **Descrição:** Recebe informações do sensor e ajusta dinamicamente o brilho.

### 6. Resolução de Problemas Comuns

Caso seu computador ou notebook não possua uma câmera integrada ou não seja possível acessá-la, você pode encontrar o seguinte erro ao tentar executar o sensor de presença (leitor.py):

   - **Sem o sensor ligado na camera nunca vai ser identificada a presença e não vai mandar nenhuma requisição**

1. Verifique se sua máquina possui uma câmera integrada. Caso não tenha, considere usar um dispositivo externo ou adaptadores de câmera compatíveis.

2. Certifique-se de que a câmera esteja corretamente configurada e conectada ao computador.

3. Se você estiver utilizando um ambiente de desenvolvimento, como o VS Code, confirme se as permissões para acessar a câmera foram concedidas.

4. Caso o problema persista, consulte a documentação da biblioteca que está sendo utilizada para a captura de imagens (por exemplo, OpenCV) para obter informações específicas sobre configuração e detecção de câmeras.

Lembre-se de que a presença de uma câmera é fundamental para o funcionamento adequado do sensor de presença. Caso ainda encontre dificuldades, busque suporte técnico ou consulte fóruns relacionados à biblioteca específica que está sendo utilizada.

