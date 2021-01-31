# Princípios SOLID na Prática utilizando Python
### Adaptado de [Wagner Nogueira - Princípios SOLID na Prática - .NET C# ](https://medium.com/@engnogueirawgn/princ%C3%ADpios-solid-na-pr%C3%A1tica-e932608406d6)

### Para executar o projeto:

#### 1- instale as dependências com pip ou pipenv

``` shell script
> pipenv install
```

ou

``` shell script
> pip install -r requirements.txt
```

#### 2- Estando dentro do diretório raiz do projeto, configure o arquivo `.env` seguindo o modelo do arquivo `.env.exemple`, com o seguinte comando:

``` shell script
> cp .env.exemple .env
```

> #### Atribua valores as variáveis de credenciais AUTH_USER e AUTH_PASSWORD conforme as orientações no arquivo `.env`. Utilizar variáveis de ambiente é uma forma segura de informar credenciais já que você as informa no seu arquivo local `.env` e não diretamente no código.  
