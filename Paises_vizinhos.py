# -*- coding: cp1252 -*-
class Pais:
    def __init__(self,nome,capital,dimensao,lista_fronteira):
        self.__nome=nome
        self.__capital=capital
        self.__fronteira=lista_fronteira
        self.__dimensao=dimensao
    def getpais(self):
        return(self.__nome,self.__capital,self.__fronteira)
    def setpais(self,novacapital):
        self.__capital=novacapital
        print(' a nova capital deste pais e: ',self.__capital)
    def paisigual(self,nome1,capital1):
        if(nome1==self.__nome and capital1==self.__capital):
            print('os paises ', nome1 ,' e ',self.__nome,' sao iguais.')
        else:
            print('esses países nao sao iguais')
    def maisfronteira(self,novafronteira):
        self.__fronteira.append(novafronteira)
        if(novafronteira==self.__nome):
            print('um pais não pode fazer fronteira com ele mesmo')
        else:
            print('as fronteiras com esse pais sao : ', self.__fronteira)
    def outropais(self,novopais):
        fronteira1=set(self.__fronteira)
        fronteira2=set(novopais.__fronteira)
        comum=fronteira1.intersection(fronteira2)
        print(' as fronteiras comuns nestes paises sao: ',comum)
        
