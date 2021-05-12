from claseEmail import Email
import csv


def test():

    idcuenta = 'juan' ; dominio = 'gmail' ; tdominio= 'com' ; contrasena = '123'  # 1er correo
    print('1er correo: {}@{}.{} '.format(idcuenta,dominio,tdominio,contrasena))
    email = Email()
    cadena_email = idcuenta + '@' + dominio + '.' + tdominio
    email.crearCuenta(cadena_email,contrasena)
    idcuenta = 'pablo.'; dominio = 'gmail@'; tdominio = 'com'; contrasena = '123'   # 2do correo
    print('2do correo: {}@{}.{} '.format(idcuenta, dominio, tdominio, contrasena))
    email = Email()
    cadena_email = idcuenta + '@' + dominio + '.' + tdominio
    email.crearCuenta(cadena_email,contrasena)


if __name__ == '__main__':

    p = input('Desea ejecutar test 1:si  cualquier otro caracter:no  ::')
    if p == '1':
        test()
    #p1
    print('Ingreso de nombre de una persona y direccion de e-mail')
    persona= input(' nombre: ')
    idcuenta = input(' id de la cuenta: ')
    dominio = input(' dominio: ')
    tdominio = input('tipo de dominio: ')
    contra = input('contraseña: ')
    email = Email(idcuenta,dominio,tdominio,contra)
    cadena_email = idcuenta + '@' + dominio + '.'+ tdominio
    email.crearCuenta(cadena_email,contra)
    print('Estimado <{}> te enviaremos tus mensajes a la direccion <{}@{}.{}>'.format(persona,idcuenta,dominio,tdominio))

    #p2
    print('Cambio de contraseña ')
    contrasena = input('Ingrese contraseña a modificar: ')
    email.modificarContra(contrasena)

    #p3
    print('Crear email a partir de un correo')
    emaill = input('ingrese email: ')
    email = Email()
    contrasenia = None
    email.crearCuenta(emaill,contrasenia)

    #p4
    print('Lectura del archivo')
    dominio = input('ingrese dominio a buscar: ')
    archivo = open('ArchiCorreo.csv')
    reader= csv.reader(archivo,delimiter=';')
    cont=0
    for fila in reader:
        email= Email(fila[0],fila[1],fila[2],fila[3])
        if(email.getDominio()==dominio):
            cont=cont+1
    archivo.close()
    print('la cantidad de dominios iguales a {} es {}'.format(dominio,cont))





