# Alunos: Gustavo Gabriel Martins
# Ronald
# Luis Felipe Costa Teixeira

# Índice
- [Descrição da Arquitetura no GitHub](#descrição-da-arquitetura-no-github)
  - [Visão Geral do Sistema Distribuído](#1-visão-geral-do-sistema-distribuído)
  - [Arquitetura de Microserviços](#2-arquitetura-de-microserviços)
  - [Integração com Django](#3-integração-com-django)
  - [Sensor de Presença e Controle de Luz](#4-sensor-de-presença-e-controle-de-luz)
  - [Referências e Base Teórica](#5-referências-e-base-teórica)
- [Qualidade do Tutorial no README](#qualidade-do-tutorial-no-readme)
  - [Instalação](#1-instalação)
  - [Configuração](#2-configuração)
  - [Execução do Sistema](#3-execução-do-sistema)
  - [Uso do Sensor de Presença](#4-uso-do-sensor-de-presença)
  - [Exemplos de Requisições à API](#5-exemplos-de-requisições-à-api)
  - [Resolução de Problemas Comuns](#6-resolução-de-problemas-comuns)
- [Arquiteturas Utilizadas](#arquiteturas-utilizadas)
  - [Arquitetura de Microserviços](#1-arquitetura-de-microserviços)
  - [Padrão REST para a API](#2-padrão-rest-para-a-api)
  - [Arquitetura em Camadas](#3-arquitetura-em-camadas)
  - [Arquitetura de Eventos (opcional)](#4-arquitetura-de-eventos-opcional)

## Descrição da Arquitetura no GitHub:
## 1. Visão Geral do Sistema Distribuído:

O projeto visa criar um sistema distribuído utilizando Django, destacando a necessidade de distribuição para suportar a complexidade da aplicação. Os principais componentes incluem microserviços, uma REST API, e integração com um sensor de presença baseado em câmera para controle de luz do computador.
## 2. Arquitetura de Microserviços:

O sistema é estruturado em microserviços independentes, cada um responsável por funcionalidades específicas. Os microserviços são modularizados para facilitar manutenção, escalabilidade e implementação ágil de novos recursos.
## 3. Integração com Django:

O Django é fundamental na construção da REST API, gerenciando a lógica de negócios e a comunicação entre os microserviços. Sua estrutura MVC (Model-View-Controller) é aproveitada para uma organização eficiente do código.
## 4. Sensor de Presença e Controle de Luz:

Um componente crucial do sistema é o sensor de presença baseado na câmera. Ele detecta a presença e altera dinamicamente a intensidade da luz do computador. A integração com Django ocorre por meio de APIs dedicadas que recebem informações do sensor e ajustam as configurações de luz correspondentes.
## 5. Referências e Base Teórica:

A arquitetura reflete conceitos fundamentais discutidos na disciplina GCC129 - Sistemas Distribuídos, conforme abordados no livro base. Referências adicionais incluem [inserir referências específicas utilizadas].
Qualidade do Tutorial no README:
## 1. Instalação:

    Clone o repositório: git clone https://github.com/seugrupo/nome-do-repositorio.git
    Instale as dependências: pip install -r requirements.txt

## 2. Configuração:

    Configure as variáveis de ambiente no arquivo .env com as informações necessárias.

## 3. Execução do Sistema:

    Execute o servidor Django: python manage.py runserver

## 4. Uso do Sensor de Presença:

    Siga as instruções no diretório sensor-de-presenca para configurar e executar o sensor.

## 5. Exemplos de Requisições à API:

    Consulte a documentação da API em /api/docs para exemplos de requisições.

## 6. Resolução de Problemas Comuns:

    Consulte a seção de Perguntas Frequentes (FAQ) para solucionar problemas comuns.

## Arquiteturas Utilizadas:
## 1. Arquitetura de Microserviços:

Os microserviços incluem:

    auth-service: Serviço de autenticação.
    light-control-service: Serviço de controle de luz.

## 2. Padrão REST para a API:

A API segue os princípios RESTful, proporcionando comunicação eficiente entre os microserviços.
## 3. Arquitetura em Camadas:

A aplicação é dividida em camadas distintas, separando apresentação, lógica de negócios e acesso a dados.
## 4. Arquitetura de Eventos (opcional):

A arquitetura incorpora eventos assíncronos para comunicação eficiente entre os microserviços, permitindo uma resposta rápida a eventos do sensor.