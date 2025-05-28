# 🚀 Rocket DB: Sistema API para Gerenciamento de Ordens com MongoDB

---

## 📄 Descrição

Este projeto é uma **API RESTful** desenvolvida em Python para o gerenciamento de ordens (pedidos), utilizando o banco de dados **NoSQL MongoDB** e a biblioteca **PyMongo** para interação. O sistema foi estruturado para aplicar conceitos de modularidade e boas práticas, com separação de responsabilidades entre conexão, repositórios, casos de uso e validação. O objetivo principal foi consolidar o aprendizado em NoSQL, focando nas operações **CRUD (Create, Read, Update, Delete)** de ordens através de endpoints HTTP.

---

## ✨ Funcionalidades (Endpoints da API)

O sistema expõe as seguintes funcionalidades através de endpoints HTTP:

* **Criar Nova Ordem:** Permite registrar uma nova ordem no banco de dados com base em uma estrutura validada.
* **Buscar Ordens:**
    * **Buscar Ordem por ID:** Recupera os detalhes de uma ordem específica usando seu identificador único.
    * **Buscar Ordens por Critério:** Permite consultar ordens com base em filtros (por exemplo, ordens com endereço específico ou com cupons).
* **Atualizar Ordem:** Modifica informações de uma ordem existente, como seu status ou quantidade de itens.
* **Deletar Ordem:** Remove uma ordem específica ou múltiplas ordens com base em critérios.

### Exemplo de Estrutura de Ordem (JSON esperada):

A validação de ordens segue um esquema (Cerberus), que inclui campos como:

```json
{
  "data": {
    "name": "string",
    "address": "string",
    "cupom": "boolean",
    "itens": [
      {
        "name": "string",
        "quantidade": "integer"
      }
    ]
  }
}
```

### 🛠️ Tecnologias Utilizadas
- **Python 3.x**: Linguagem de programação principal.

- **MongoDB**: Banco de dados NoSQL para armazenar as ordens.

- **PyMongo**: Driver oficial do MongoDB para Python, utilizado para a comunicação.

- **Flask**: Framework web utilizado para a criação dos endpoints da API.

- **Cerberus**: Biblioteca de validação de esquemas (utilizada para validar a estrutura das ordens).



## ⚙️ Arquitetura do Projeto

O projeto segue uma arquitetura modular, com as seguintes divisões principais:

* `src/models/connection`: Lida com a conexão e configuração do MongoDB (classe `DBConnectionHandler`).
* `src/models/repository`: Contém as interfaces e a implementação concreta (`OrderRepository`) para as operações de persistência (CRUD) com o MongoDB.
* `src/use_cases`: Orquestra as operações de negócio (`RegistryFinder`, `RegistryOrder`, `RegistryUpdater`), utilizando o repositório e os validadores para implementar as funcionalidades da API.
* `src/validators`: Define e aplica as regras de validação para os dados de entrada (`registry_order_validator`, `registry_updater_validator`).
* `src/main/server`: Contém a configuração do servidor web e a definição dos endpoints da API.


## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a API em sua máquina local.

### Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

* **Python 3.x**: [Download Python](https://www.python.org/downloads/)
* **Docker**: [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/anderrosa/rocket_db.git](https://github.com/anderrosa/rocket_db.git)
    cd rocket_db
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Crie ou verifique se o arquivo `requirements.txt` na raiz do seu projeto contém as seguintes bibliotecas: `pymongo`, `flask`, `cerberus` e quaisquer outras que seu projeto utilize.)*

### Configuração e Execução do MongoDB com Docker

1.  **Inicie o contêiner do MongoDB:**
    ```bash
    docker run --name rocketdb-mongodb -p 27017:27017 -d mongo
    ```
    *Este comando irá baixar a imagem oficial do MongoDB (se ainda não tiver), criar um contêiner chamado `rocketdb-mongodb`, mapear a porta `27017` do seu host para a porta `27017` do contêiner e executá-lo em segundo plano.*

2.  **Verifique se o contêiner está rodando:**
    ```bash
    docker ps
    ```
    *Você deverá ver `rocketdb-mongodb` na lista de contêineres em execução.*

    *Se você precisar parar ou remover o contêiner:*
    ```bash
    docker stop rocketdb-mongodb
    docker rm rocketdb-mongodb
    ```

### Executando a API

Após a instalação das dependências e a configuração do MongoDB, você pode iniciar o servidor da API executando o script `run.py`:

```bash
python run.py
```

A API estará acessível em `http://localhost:3000`.

## 🧪 Testes
Você pode executar os testes do projeto usando pytest.

```Bash
￼
# Para instalar pytest (se ainda não estiver no requirements.txt)
pip install pytest

# Para rodar todos os testes
pytest

# Para rodar um teste específico (exemplo)
pytest src/models/repository/orders_repository_test.py
```

## 🤝 Contribuições
Sinta-se à vontade para sugerir melhorias, reportar problemas ou contribuir com novas funcionalidades.



## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado, como parte de um módulo de curso. Não se destina a uso comercial ou contribuições externas sem permissão explícita.


## 📧 Contato

Se você tiver alguma dúvida ou sugestão, entre em contato:

* **Anderson Rosa** - [www.linkedin.com/in/andersonrosadev](https://www.linkedin.com/in/andersonrosadev)

---

