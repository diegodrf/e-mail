from json import dumps

class Cliente:
    def __init__(self, nome, email, sexo):
        self._nome = str(nome).title()
        self._email = str(email).lower()
        self._sexo = str(sexo).upper()

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def sexo(self):
        return self._sexo

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return dumps({'nome': self.nome, 'e-mail': self.email, 'sexo': self.email})
