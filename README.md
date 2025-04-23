# 🧑‍💻Freitas Codes🚀

Este projeto fornece uma API que retorna os meus projetos previamente cadastrados neste sistema, assim como certificados.
## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework web utilizado para construir a API.
- **PostgreSQL**: Banco de dados utilizado para armazenar os projetos e certificados.
- **Django REST Framework**: Ferramenta para criação de APIs RESTful.

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/devdinho/freitascodes.git
    ```
2. Acesse o diretório do projeto:
    ```bash
    cd freitascodes
    ```
3. Suba e inicie o Container Docker
    ```bash
    docker compose up --build
    ```

## Endpoints Principais

- **GET /api/projetos/**: Retorna a lista de projetos cadastrados.
- **GET /api/certificados/**: Retorna a lista de certificados cadastrados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
