class Mascota:
    def __init__(self):
        self.nombre = ""
        self.historia = 0
        self.tipo = ""
        self.peso = 0.0
        self.fecha = ""
        self.medicamento = ""

    def asignarNombre(self, nombre):
        self.nombre = nombre
    def asignarHistoria(self, historia):
        self.historia = historia
    def asignarTipo(self, tipo):
        self.tipo = tipo
    def asignarPeso(self, peso):
        self.peso = peso
    def asignarFecha(self, fecha):
        self.fecha = fecha
    def asignarMedicamento(self, medicamento):
        self.medicamento = medicamento
    def verHistoria(self):
        return self.historia
    def verFecha(self):
        return self.fecha
    def verMedicamento(self):
        return self.medicamento

class Sistema:

    def __init__(self):
        self.listaMascotas = []
    def existeMascota(self, historia):
        for m in self.listaMascotas:
            if m.verHistoria() == historia:
                return True
        return False

    def ingresarMascota(self, mascota):
        if len(self.listaMascotas) >= 10:
            return "No hay capacidad"
        if self.existeMascota(mascota.verHistoria()):
            return "Mascota ya existe"
        self.listaMascotas.append(mascota)
        return "Mascota ingresada"

    def buscarMascota(self, historia):
        for m in self.listaMascotas:
            if m.verHistoria() == historia:
                return m
        return None

    def verFecha(self, historia):
        m = self.buscarMascota(historia)
        if m != None:
            return m.verFecha()
        else:
            return "Mascota no existe"
    def verMedicamento(self, historia):
        m = self.buscarMascota(historia)

        if m != None:
            return m.verMedicamento()
        else:
            return "Mascota no existe"
    def contarMascotas(self):
        return len(self.listaMascotas)
    def eliminarMascota(self, historia):
        for m in self.listaMascotas:
            if m.verHistoria() == historia:
                self.listaMascotas.remove(m)
                return "Mascota eliminada"
        return "No existe"

def main():
    sis = Sistema()
    while True:
        print("\n1. Ingresar mascota")
        print("2. Ver fecha ingreso")
        print("3. Ver numero mascotas")
        print("4. Ver medicamento")
        print("5. Eliminar mascota")
        print("6. Salir")

        op = int(input("Opcion: "))

        if op == 1:
            historia = int(input("Historia clinica: "))
            if sis.existeMascota(historia):
                print("Ya existe")
                continue
            if sis.contarMascotas() >= 10:
                print("No hay cupo")
                continue

            nombre = input("Nombre: ")
            tipo = input("Tipo (canino/felino): ")
            peso = float(input("Peso: "))
            fecha = input("Fecha: ")
            medicamento = input("Medicamento: ")

            m = Mascota()
            m.asignarHistoria(historia)
            m.asignarNombre(nombre)
            m.asignarTipo(tipo)
            m.asignarPeso(peso)
            m.asignarFecha(fecha)
            m.asignarMedicamento(medicamento)

            print(sis.ingresarMascota(m))

        elif op == 2:
            h = int(input("Historia: "))
            print(sis.verFecha(h))
        elif op == 3:
            print("Total:", sis.contarMascotas())
        elif op == 4:
            h = int(input("Historia: "))
            print(sis.verMedicamento(h))
        elif op == 5:
            h = int(input("Historia: "))
            print(sis.eliminarMascota(h))
        elif op == 6:
            print("Adios")
            break

main()