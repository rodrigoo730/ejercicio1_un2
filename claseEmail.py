import re
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''

    def __init__(self, idc='', dom='', tdom='', con=''):
        self.__idCuenta = idc
        self.__dominio = dom
        self.__tipoDominio= tdom
        self.__contrasena = con
    def retornaEmail(self):
        return print('{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio))
    def getDominio(self):
        return self.__dominio

    def crearCuenta(self,per,contra):

        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', per):# ^:incion de cadena,$:finde cadena
            print('formato correcto')
            self.__idCuenta= per[:per.find("@")] # :,hasta el indice que se retorna
            self.__dominio= per[per.find("@") + 1:per.find(".")]
            self.__tipoDominio= per[per.find(".") + 1:]
            if contra == None:
                self.__contrasena = input('ingrese contraseña: ')
            print('correo creado: {}@{}.{} '.format(self.__idCuenta,self.__dominio,self.__tipoDominio))


        else: print('formato incorrecto')

    def mostrarDominio(self):
        return print(self.__tipoDominio)

    def modificarContra(self,contra):
        if(contra==self.__contrasena):
            ncontra = input('ingrese nueva contraseña: ')
            self.__contrasena = ncontra
            print('contraseña modificada')
        else:print('contraseña incorrecta')




