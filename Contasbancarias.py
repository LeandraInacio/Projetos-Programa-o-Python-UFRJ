# -*- coding: cp1252 -*-
class Banco:
    ContasCriadas=0
    def __init__(self,saldo,tipo_cliente,saldo_especial):
        self.__saldo=saldo
        if(tipo_cliente != 'c'and tipo_cliente != 'e'):
            self.__tipo_cliente= 'c'
        else:
            self.__tipo_cliente=tipo_cliente
        if(self.__tipo_cliente=='e'):
            self.__saldo_especial=500
        else:
            self.__saldo_especial=saldo_especial
        Banco.ContasCriadas +=1
    def creditar(self,valor):
        if(valor>=1000):
            print('favor solicitar na agencia bancaria')
        else:
            self.__saldo=int (self.__saldo)+ int(valor)
    def debitar(self,valor):
        if(valor>=1000):
            print('favor solicitar na agencia bancaria')
        else:
            if(self.__tipo_cliente=='e'):
                self.__saldo=self.__saldo+self.__saldo_especial
            if(self.__saldo>= valor):
                self.__saldo=int (self.__saldo)- int(valor)
            else:
                print('valor nao existe na conta')
    def mostrarsaldo(self):
        print('saldo total : ', self.__saldo)
    def totalcontas():        
        print('o numero de contas criadas e : ', Banco.ContasCriadas)
    def saldocliente(self):
        print(' saldo do cliente : ', self.__saldo)
        print('tipo do cliente: ', self.__tipo_cliente)
        print('saldo especial do cliente: ',self.__saldo_especial)
        
        
