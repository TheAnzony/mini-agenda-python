import json
import os

def mostrar_menu():
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion


def añadir_contacto():
        
    nombre = input("Introduce tu nombre: ").strip()
    tel = input("Introduce tu numero de telefono: ").strip()

    # Agregar o actualizar el contacto en el diccionario
    agenda[nombre] = tel
    
    with open("agenda.json","w") as archivo:
        json.dump(agenda,archivo, indent=4)
        
def mostrar_contactos():
    
    print("\nContactos en la agenda:")
    
    try:
        with open("agenda.json", "r") as archivo:
            agenda = json.load(archivo)
        if agenda:
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("No hay datos en la agenda.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay datos en la agenda.")
        
    print("\n")
    
    
def buscar_contacto():
    if not agenda:
        print("La agenda está vacía. No hay contactos para buscar.")
        return
    nombre_buscar = input("Introduce el nombre del contacto a buscar: ").strip()
    
    if nombre_buscar in agenda:
        print(f"Contacto encontrado: Nombre: {nombre_buscar}, Teléfono: {agenda[nombre_buscar]}")
    else:
        print("Contacto no encontrado.")
        
def eliminar_contacto():
    nombre_eliminar = input("Introduce el nombre del contacto a eliminar: ").strip()
    
    if nombre_eliminar in agenda:
        del agenda[nombre_eliminar]
        with open("agenda.json","w") as archivo:
            json.dump(agenda,archivo, indent=4)
        print(f"Contacto {nombre_eliminar} eliminado.")
    else:
        print("Contacto no encontrado.")
    


if __name__ == "__main__":


    try:
        with open("agenda.json","r") as archivo:
           agenda = json.load(archivo)

    except (FileNotFoundError, json.JSONDecodeError):
        agenda = {}
        
        
    while True:
        opcion = mostrar_menu()
    
        match opcion:
            case "1":
                añadir_contacto()
            case "2":
                buscar_contacto()
            case "3":
                eliminar_contacto()
            case "4":
                mostrar_contactos()
            case "5":
                print("Saliendo del programa")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                

    
    
        
        
    

    
    
    
    





