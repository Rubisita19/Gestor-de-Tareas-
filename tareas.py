import csv
import os

ARCHIVO_TAREAS = 'tareas.csv'

# Cargar tareas desde el archivo CSV
def cargar_tareas():
    tareas = []
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                tareas.append(fila)
    return tareas

# Guardar tareas en el archivo CSV
def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'prioridad', 'estado']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(tareas)

# Agregar una nueva tarea
def agregar_tarea(tareas):
    nombre = input("Nombre de la tarea: ")
    prioridad = input("Prioridad (Alta, Media, Baja): ")
    tarea = {'nombre': nombre, 'prioridad': prioridad, 'estado': 'Pendiente'}
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada exitosamente.\n")

# Ver tareas (todas, completadas o pendientes)
def ver_tareas(tareas, estado_filtro=None):
    if estado_filtro:
        tareas_filtradas = [t for t in tareas if t['estado'] == estado_filtro]
    else:
        tareas_filtradas = tareas

    if not tareas_filtradas:
        print("No hay tareas para mostrar.\n")
        return

    for i, tarea in enumerate(tareas_filtradas):
        print(f"{i + 1}. {tarea['nombre']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}")
    print()

# Marcar una tarea como completada
def completar_tarea(tareas):
    ver_tareas(tareas, estado_filtro='Pendiente')
    try:
        indice = int(input("Número de la tarea a completar: ")) - 1
        pendientes = [t for t in tareas if t['estado'] == 'Pendiente']
        tarea = pendientes[indice]
        tarea['estado'] = 'Completada'
        guardar_tareas(tareas)
        print("✅ Tarea completada.\n")
    except (ValueError, IndexError):
        print("❌ Selección inválida.\n")

# Eliminar una tarea
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Número de la tarea a eliminar: ")) - 1
        tarea = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f"🗑️ Tarea '{tarea['nombre']}' eliminada.\n")
    except (ValueError, IndexError):
        print("❌ Selección inválida.\n")

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("📋 GESTOR DE TAREAS CON PRIORIDADES")
        print("1. Agregar tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tareas pendientes")
        print("4. Ver tareas completadas")
        print("5. Marcar tarea como completada")
        print("6. Eliminar tarea")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            ver_tareas(tareas, estado_filtro='Pendiente')
        elif opcion == '4':
            ver_tareas(tareas, estado_filtro='Completada')
        elif opcion == '5':
            completar_tarea(tareas)
        elif opcion == '6':
            eliminar_tarea(tareas)
        elif opcion == '7':
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida.\n")

if __name__ == '__main__':
    menu()
