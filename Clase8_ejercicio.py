import datetime

class Indices:
    def __init__(self):
        self.__pot_d = 0
        self.__pot_t = 0
        self.__pot_a1 = 0
        self.__pot_a2 = 0
        self.__pot_b = 0
        self.__pot_g = 0

    def verPot_D(self):
        return self.__pot_d

    def asignarPot_D(self, p):
        self.__pot_d = p

    def verPot_T(self):
        return self.__pot_t

    def asignarPot_T(self, p):
        self.__pot_t = p

    def verPot_A1(self):
        return self.__pot_a1

    def asignarPot_A1(self, p):
        self.__pot_a1 = p

    def verPot_A2(self):
        return self.__pot_a2

    def asignarPot_A2(self, p):
        self.__pot_a2 = p

    def verPot_B(self):
        return self.__pot_b

    def asignarPot_B(self, p):
        self.__pot_b = p

    def verPot_G(self):
        return self.__pot_g

    def asignarPot_G(self, p):
        self.__pot_g = p


class Visita:
    def __init__(self):
        self.__fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__registro = ''
        self.__notas = ''
        self.__indice = Indices()

    def verFecha(self):
        return self.__fecha

    def asignarFecha(self, f):
        self.__fecha = f

    def verRegistro(self):
        return self.__registro

    def asignarRegistro(self, r):
        self.__registro = r

    def verNotas(self):
        return self.__notas

    def asignarNotas(self, n):
        self.__notas = n

    def verIndice(self):
        return self.__indice

    def asignarIndice(self, i):
        self.__indice = i


class Paciente:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''
        self.__visitas = {}  

    def verNombre(self):
        return self.__nombre

    def asignarNombre(self, n):
        self.__nombre = n

    def verCedula(self):
        return self.__cedula

    def asignarCedula(self, c):
        self.__cedula = c

    def verGenero(self):
        return self.__genero

    def asignarGenero(self, g):
        self.__genero = g

    def verVisitas(self):
        return self.__visitas

    def asignarVisita(self, v):
        self.__visitas[v.verFecha()] = v


class Sistema:
    def __init__(self):
        self.__pacientes = {}  

    def verificarExiste(self, c):
        return c in self.__pacientes

    def ingresarPac(self, p):
        self.__pacientes[p.verCedula()] = p

    def eliminarPac(self, c):
        del self.__pacientes[c]
        return True

    def recuperarPac(self, c):
        return self.__pacientes[c]

    def cargarGuardar(self):
        pass


def validar(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingrese un número válido.")


def main():
    sis = Sistema()
    while True:
        print("\nIngrese:\n 1 Nuevo paciente\n 2 Editar paciente\n 3 Eliminar un paciente\n 4 Cargar\n 0 Salir")
        valor = validar("Seleccione una opcion: ")

        if valor == 0:
            print("Chao")
            break

        elif valor == 1:
            cedula = validar("Ingrese la cedula: ")
            if sis.verificarExiste(cedula):
                print(f"Ya esta en el sistema...verifique la cedula ingresada {cedula}")
                continue
            p = Paciente()
            p.asignarCedula(cedula)
            nombre = input("Ingrese el nombre: ")
            p.asignarNombre(nombre)
            genero = input("Ingrese el genero (M/F): ")
            p.asignarGenero(genero)
            sis.ingresarPac(p)
            print(f"Paciente {nombre} ingresado correctamente.")

        elif valor == 2:
            cedula = validar("Ingrese la cedula del paciente a editar: ")
            if not sis.verificarExiste(cedula):
                print("Paciente no encontrado.")
                continue
            p = sis.recuperarPac(cedula)
            print(f"Editando paciente: {p.verNombre()}")
            nombre = input("Nuevo nombre (Enter para conservar): ")
            if nombre:
                p.asignarNombre(nombre)
            genero = input("Nuevo genero (Enter para conservar): ")
            if genero:
                p.asignarGenero(genero)
            print("Paciente actualizado.")

        elif valor == 3:
            cedula = validar("Ingrese la cedula del paciente a eliminar: ")
            if not sis.verificarExiste(cedula):
                print("Paciente no encontrado.")
                continue
            sis.eliminarPac(cedula)
            print("Paciente eliminado correctamente.")

        elif valor == 4:
            print("Funcion cargar/guardar en construccion.")

        else:
            print("Opcion no valida.")


if __name__ == '__main__':
    main()