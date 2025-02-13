# Monopoly Challenge

Programa que simula o famoso jogo Banco Imobiliário; sendo este um projeto pessoal e sem fins lucrativos.

## Sobre

Programa consiste em um código python que roda sobre uma API, expondo o resultado da simulação no navegador.

## Requesitos

- Python 3.12.2
- PIP 25.0.1
- FastAPI 0.115.8

## Guia de Execução

### Repositório Github
Repositório presente em link abaixo.
https://github.com/DiegoCaruba/monopoly-challenge 

### Intalação
1. Criar Ambiente Virtual
    No diretório raiz do projeto, realizar o comando:
    > python -m venv .venv

2. Ativar Ambiente Virtual
    No diretório raiz do projeto, realizar o comando:
    > . .venv/Scripts/activate (Terminal Bash)

3. Instalar Dependências
    > pip install -r requirements.txt

### Realizar simulação
4. Com Amebite Virtual ativo e sem diretório raiz do projeto, executar o comando:
    > python main.py

5. Observar em Terminal CLI que a API está em funcionamento

6. Acessar em navegador, o seguinte endereço e pressionar Enter:
    > http://localhost:8080/jogo/simular

    6.1. Observar que o resultado da simulação é retornado em navegador web e, também, logado em terminal

### Encerrar Simulação

7. Encerrar API pressionando 'Ctrl+C' no terminal

8. Encerrar Ambiente Virtual com seguinte comando:
    > deactivate