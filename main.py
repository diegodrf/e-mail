# -*- coding: utf-8 -*-
from models import Cliente
from functions import email
import shelve
import os

if os.path.exists('data.bin') is False:
    with shelve.open('data.bin', 'c') as shelve_file:
        confirmacao = None
        while confirmacao != 'Estou ciente.':
            print('O sistema ainda não possui um e-mail cadastrado para ser utilizado como o remetente das mensagens.')
            shelve_file['user'] = input('Informe o E-mail que será utilizado para enviar as mensagens (gmail): ')
            shelve_file['password'] = input('Senha: ')
            print('\nVocê tem certeza que escreveu e-mail e senha corretamente?\nVocê não poderá alterar depois.')
            print('Se SIM, digite "Estou ciente.", se não, digite qualquer coisa.\n')
            print('E-mail: {}'.format(shelve_file['user']))
            print('Senha: {}'.format(shelve_file['password']))
            confirmacao = input('\nConfirmação: ')

cliente_1 = Cliente('Renzo', 'renzo@gmail..com', 'm')
cliente_2 = Cliente('Alline', 'alline@gmail..com', 'f')
cliente_3 = Cliente('Diego', 'diego.rdfaria@gmail.com', 'm')

lista_de_clientes = [cliente_1, cliente_2, cliente_3]

with open('mensagem.txt', 'r') as f:
    msg = [line for line in f.readlines()]

msg = ''.join(msg)
with shelve.open('data.bin', 'r') as shelve_file:
    for cliente in lista_de_clientes:
        if cliente.sexo == 'M':
            pronome = 'Sr. '
        else:
            pronome = 'Sra. '

        print('Enviando para {}{}'.format(pronome, cliente.nome))

        email(shelve_file['user'], shelve_file['password'], cliente.email, 'Ola mundo', 'Bom dia ' + pronome + cliente.nome + ',\n\n' + msg)
