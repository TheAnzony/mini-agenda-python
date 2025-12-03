def mostrar_menu():
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion


def anadir_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    while not nombre.strip():
        print("El nombre no puede estar vacío. Intente de nuevo.")
        nombre = input("Ingrese el nombre del contacto: ")
    nombre = nombre.strip()

    telefono = input("Ingrese el teléfono del contacto: ")
    while not telefono.strip():
        print("El teléfono no puede estar vacío. Intente de nuevo.")
        telefono = input("Ingrese el teléfono del contacto: ")
    telefono = telefono.strip()

    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' añadido con éxito.")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()

    if nombre in agenda:
        print(f"El teléfono de '{nombre}' es: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()

    if nombre in agenda:
        confirmar = input(
            f"¿Está seguro de que desea eliminar el contacto '{nombre}'? (s/n): "
        ).lower()
        if confirmar == "s":
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado con éxito.")
        else:
            print("Operación cancelada.")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")


def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return

    print("\nContactos en la agenda:")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre}, Teléfono: {telefono}")


def main():
    agenda = {}  # diccionario vacío

    while True:
        opcion = mostrar_menu()
        
        
        match opcion:
            case "1":
                anadir_contacto(agenda)
            case "2":
                buscar_contacto(agenda)
            case "3":
                eliminar_contacto(agenda)
            case "4":
                mostrar_agenda(agenda)
            case "5":
                print("Saliendo de la agenda. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
