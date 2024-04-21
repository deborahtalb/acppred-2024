# ACPPred: Anticancer Peptide Prediction

ACPPred is a command-line tool designed for predicting the anticancer activity of peptide sequences based on their amino acid composition. It provides users with the flexibility to choose between two machine learning models for training: `Random Forest` and `Logistic Regression`.


By Déborah Trota.


## Setup

Run the following to install the ACPPred program (mamba is required).

```
$ make setup
```

## Project Structure 

- `Makefile`: centralizes the commands for the program `make`.
- `environment.yml`: defines the environment configurations and manages the dependencies.
- `requirements`: contains a list of packages or libraries needed to run the program

## Usage

### `acppred-preprocess`

Preprocesses the provided data.

* Arguments:
    * `input_directory:` Directory containing the input files.
    * `output_directory:` Directory to save the preprocessed data.

### `acppred-train`

Train the model (random forest or logistic regression).

* Arguments:
   * `input_directory:` Directory containing the preprocessed files.
   * `output:` Path to save the trained model.
* Options:
   * `-e, --estimator:` Type of estimator to be trained (options: `random_forest` or `logistic_regression`). Default is 'random_forest'.

### `acppred-predict`

Makes the prediction of the anticancer activity of a peptide provided by the user.

* Arguments:
    * `model:` Pre-trained model to be used for predictions.
    * `peptide:` Peptide sequence to be analyzed.

### `acppred-server`

Implements a server to deploy the trained model for predictions in a web application.

* Arguments:
   * `model:` Pre-trained model to be used for predictions.


## Questões 

- **O que é a ferramenta conda, e qual a sua utilidade no desenvolvimento de programas em Python?** Conda é uma ferramenta de gerenciamento de pacotes e ambientes de execução em qualquer linguagem de programação. É frequentemente utilizado com a linguagem Python, para simplificar o processo de desenvolvimento de software. Com o conda, é possível criar ambientes virtuais isolados para cada projeto, evitando conflitos de versionamento. Além disso, simplifica o processo de instalação e atualização de pacotes e bibliotecas, permitindo a sua realização com somente um comando. Dessa forma, ela garante a reprodutibilidade do ambiente de execução de um programa, através dos arquivos `environment.yml`, que especifica todas as dependências e versões necessárias para um projeto, garantindo que ele rode de forma igual em todas as máquinas.
<br>

- **Como funciona a ferramenta ACPPred? Qual a sua finalidade?** O ACPPred é uma ferramenta utilizada para a predição de atividade anticâncer em sequências de peptídeos. Esse programa possui dois modos de utilização, através do terminal, onde o usuário pode treinar os modelos com seus próprios bancos de dados de peptídeos com/sem atividade anticâncer, e através de uma aplicação web, onde o usuário pode escolher e treinar um modelo de aprendizado de máquina para prever a atividade de sequências de peptídeos. Os dois modelos utilizados para o treinamento são `Random Forest` e `Logistic Regression`.   
<br>

- **O que são aplicações CLI? Quais os comandos e opções (argumentos) criadas para a ferramenta desenvolvidas no projeto?** Aplicações CLI (command-line interface) são ferramentas desenvolvidas para serem executadas por usuários através de comandos fornecidos em um terminal ou prompt de comando.
<br>

Comandos e Argumentos do ACPPred:  
- **acppred-preprocess**: Comando para pré-processamento dos dados.
    Argumentos:
    `input_directory:` Diretório contendo os arquivos de entrada.
    `output_directory:` Diretório para salvar os dados pré-processados.
- **acppred-train**: Comando para treinamento do modelo.
    Argumentos:
    `input_directory:` Diretório contendo os arquivos pré-processados.
    `output:` Caminho para salvar o modelo treinado.
    Opções:
    `-e, --estimator:` Tipo de estimador a ser treinado (opções: 'random_forest' ou 'logistic_regression'). O padrão é 'random_forest'.
- **acppred-predict**: Comando para fazer previsões com o modelo treinado.
    Argumentos:
    `model:` Modelo pré-treinado a ser usado para previsões.
    `peptide:` Sequência de peptídeo a ser analisada.
- **acppred-server**: Comando para iniciar o servidor para a aplicação web
    Argumentos:
    `model:` Modelo pré-treinado a ser usado para previsões.
<br>

- **O que é _back-end_ e _front-end_ no contexto de aplicação web?** O _front-end_ se refere a toda a parte visual/layout de uma aplicação web com que o usuário pode ver e interagir. Normalmente, o _front-end_ é criado utilizando linguagens de marcação, como HTML e CSS, e de programação, como JavaScript. Ele também pode ser facilitado através da utilização de _frameworks_, como React.js e Bootstrap. O _back-end_ é toda a parte que é invisível aos olhos do usuário e funciona através de servidores, processando todas as requisições feitas pelo front-end, conectando com o banco de dados e executando a lógica por traz da aplicação web. O back-end de uma aplicação web pode ser construído com dezenas de linguagens de programação, sendo as mais comuns Python, Java, PHP, além de alguns _frameworks_ como Django e Node.js. 
<br>

- **O que são testes unitários? Qual a sua importância no desenvolvimento de software?** São testes automatizados presentes no código do software, que tem como finalidade verificar o funcionamento do código, através de testes em partes específicas do programa. Cada uma dessas partes é considerada uma unidade, podendo ser funções, métodos ou classes. Esses testes podem ser executados sempre que o desenvolver sentir a necessidade de verificar a presença de algum problema. Através dos testes unitários, os erros podem ser identificados de forma precoce no programa, facilitando a sua resolução. Além disso, esses testes ajudam a garantir a qualidade do código e facilitam a manutenção do software ao longo do tempo.
