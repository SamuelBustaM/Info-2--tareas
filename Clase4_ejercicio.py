class Paciente:
    def __init__(self):
        self.nombre = ""
        self.cedula = 0
        self.genero = ""
        self.servicio = ""
    def asignarNombre(self, nombre):
        self.nombre = nombre
    def asignarCedula(self, cedula):
        self.cedula = cedula
    def asignarGenero(self, genero):
        self.genero = genero
    def asignarServicio(self, servicio):
        self.servicio = servicio
    def verNombre(self):
        return self.nombre
    def verCedula(self):
        return self.cedula
    def verGenero(self):
        return self.genero
    def verServicio(self):
        return self.servicio

class Sistema:
    def __init__(self):
        self.listaPacientes = []
    def ingresarPaciente(self, paciente):
        self.listaPacientes.append(paciente)
        print("Paciente ingresado correctamente.")
    def verPaciente(self, cedula):
        for p in self.listaPacientes:
            if p.verCedula() == cedula:
                return p
        return None
    
    def verNumeroPacientes(self):
        return len(self.listaPacientes)

def main():
    sis = Sistema()
    while True:
        print("\n===== SISTEMA DE PACIENTES =====")
        print("1. Ingresar paciente")
        print("2. Ver paciente")
        print("3. Número de pacientes")
        print("4. Salir")
        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            print("\n--- Ingreso de nuevo paciente ---")
            nombre = input("Ingrese nombre: ")
            cedula = int(input("Ingrese cédula: "))
            genero = input("Ingrese género: ")
            servicio = input("Ingrese servicio: ")

            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            sis.ingresarPaciente(pac)

        elif opcion == 2:
            cedula = int(input("Ingrese cédula a buscar: "))
            paciente = sis.verPaciente(cedula)
            if paciente != None:
                print("\n--- Datos del paciente ---")
                print("Nombre:", paciente.verNombre())
                print("Cédula:", paciente.verCedula())
                print("Género:", paciente.verGenero())
                print("Servicio:", paciente.verServicio())
            else:
                print("Paciente no encontrado.")
        elif opcion == 3:
            total = sis.verNumeroPacientes()
            print("Total pacientes registrados:", total)
        elif opcion == 4:
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")
main()