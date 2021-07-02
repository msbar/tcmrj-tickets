# tcmrj-tickets

Sistema de Chamados do TCMRJ

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9
3. Ative o virtualenv.
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
https://github.com/msbar/tcmrj-tickets.git
cd tcmrj-tickets
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envia as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Envie o código para o heroku.

```console
heroku create minhainstancia

heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com

git push heroku master --force