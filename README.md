# Desafio de Programação

O desafio consiste em desenvolver uma simples api que calculadora que será capaz de calcular a relação entre os lados de um triângulo retângulo (mais conhecido popularmente como teorema de pitágoras).

## Backend

### Como Rodar

Primeiramente crie um virtualenv e instale as dependências:

```bash
cd Cromai-challenge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Para rodar o servidor local da API REST na porta 5000:

```bash
source .venv/bin/active  # se já não estiver ativado
python3 server.py 0.0.0.0:5000
```

### API

#### Listagem (GET /pitagoras)

Listagem de todos os triângulos retângulo.

##### Argumentos

N/A

##### Exemplo

```json
[
    {
        "id": 1,
        "cateto_a": "4",
        "cateto_b": "3",
        "hipotenusa": "5"
    },
    {
        "id": 2,
        "cateto_a": "4",
        "cateto_b": "3",
        "hipotenusa": "5"
    }
]
```

#### Adição (POST /pitagoras)

Calculando um triângulos retângulo.

##### Argumentos

Triangulo:

- cateto_a: [number]
- cateto_b: [number]

##### Formato da Resposta

##### Exemplo

Sucesso 201

```json
{
    "id": 1,
    "cateto_a": "4",
    "cateto_b": "3",
    "hipotenusa": "5"
}
```

Erro 400

```json
{
  "message": "Some error message"
}
