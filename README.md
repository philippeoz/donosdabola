---
Como executar?
---
1. Criar e ativar um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * `mkvirtualenv bola` para criar um virtualenv chamado bola
    * `workon sfd` para ativar o virtualenv sempre que for trabalhar no projeto

2. Instalar as dependências
    * `pip install -r requirements.txt`

3. Criar um arquivo chamado `settings.ini` na pasta sfd com o seguinte conteúdo:
```

4. Depois de criado o banco de dados (manualmente), crie as tabelas
    * `python manage.py migrate`

5. Iniciar o servidor web
    * `python manage.py runserver`

5. Crie um usuário superuser, para que ele possa ativar o "is_staff" dos outros.
