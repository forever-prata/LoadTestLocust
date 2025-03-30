# Load Test com Locust

Este projeto utiliza o [Locust](https://locust.io/) para realizar testes de carga em uma aplicação web.

## Pré-requisitos

Antes de executar o teste, certifique-se de ter o Python instalado e instale as dependências necessárias executando:

```bash
pip install locust
```

## Estrutura do Código

O código define uma classe `LoadTestUser` que herda de `HttpUser`, representando usuários simulados para o teste de carga.

```python
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_endpoint(self):
        self.client.get("/")
```

### Explicação do Código
- `HttpUser`: Classe base para simular usuários que fazem requisições HTTP.
- `wait_time = between(1, 3)`: Define um tempo de espera aleatório entre 1 e 3 segundos entre as requisições.
- `@task`: Define uma tarefa que será repetida pelos usuários simulados.
- `self.client.get("/")`: Faz uma requisição GET para a raiz da aplicação.

## Como Executar

Para iniciar o teste de carga, execute o seguinte comando:

```bash
locust -f nome_do_arquivo.py
```

Em seguida, abra um navegador e acesse `http://localhost:8089` para configurar o número de usuários e iniciar o teste.

## Configuração dos Testes

Na interface do Locust, você pode definir:
- **Número de usuários simultâneos**
- **Taxa de aumento de usuários por segundo**
- **URL do servidor a ser testado**

Após iniciar o teste, você poderá visualizar gráficos e estatísticas sobre o desempenho do seu endpoint.

