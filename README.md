# Documentação do Projeto de Sistema de Irrigação

! Projeto com fins academicos para a disciplina de IoT, industria 4.0, Cloud, python

## Integrantes do Grupo

- Luis Mario

- Nycolas Dias

### Introdução

- Utilizando Arduino, Sensores de umidade e bomba d'agua o sistema tem como objetivo verificar dados do solo e automatizar irrigação para que o mesmo não fique desidratado e improprio para atividades botanicas

### Componentes fisicos ultilizados para o projeto

- Arduino Uno (ou Algum outro modelo compativel)
- Sensor de Umidade do solo
- Bomba D'agua (5V ou 12V)
- Modulo Relé (Para controlar a bomba)
- Fonte de 12V (caso necessario)
- Jumpers e Protoboards
- Mangueira e Reservatorio de Água

### Componentes de Software utilizados para o projeto

- Python
    - Versão 3.7 ou superiores
    - biblioteca PySerial

- C
    - Arduino IDE

## Funcionamento do Sistema

1. O sensor de umidade verificará a umidade do solo
2. O Arduino recebe dados do sensor e verifica se a umidade está abaixo do nivel definido
3. Se o nivel esttiver abaixo o Arduino acionará o Relé para umidecer o solo
4. A bomba vai irrigar o solo ate que o sensor detecte a umidade definida como ideal 
5. Após isso o sistema entrará em modo de monitoramento


# Data da Entrega Final

- 06/2025

# Como executar o projeto

+ Adicinar