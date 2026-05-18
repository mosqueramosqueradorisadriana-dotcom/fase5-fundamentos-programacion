Programa: evaluador_compromiso.py
Descripción: Herramienta informática para evaluar el nivel de compromiso 
de las sesiones de clientes basándose en su duración y clics.

def clasificar_sesion(duracion: int, clics: int) -> str:
  """
   Módulo encargado de aplicar la lógica de negocio para clasificar 
    el nivel de compromiso de una sesión individual.

     # Lógica de negocio: Compromiso Alto (RN-01)
    if duracion > 180 and clics > 8:
        return "Alto"  """ 
  
    # Lógica de negocio: Compromiso Bajo (RN-02)
    elif duracion < 60 or clics < 3:
        return "Bajo"

# Lógica de negocio: Compromiso Medio (RN-03)
    else:
        return "Medio"

def evaluar_matriz_sesiones(matriz_datos: list) -> None:
    """
    Módulo principal que recorre la matriz de datos, invoca al clasificador 
    y genera la salida en consola formateada para el usuario.
     """
  
    print("-" * 65)
    print(f"{'ID CLIENTE':<12} | {'DURACIÓN':<12} | {'EVENTOS CLICS':<15} | {'COMPROMISO':<10}")
    print("-" * 65)
  
   for sesion in matriz_datos:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        # Invocación del módulo de clasificación
        nivel_compromiso = clasificar_sesion(duracion, clics)  


     # Presentación de resultados formateados
        print(f"{id_cliente:<12} | {str(duracion)+'s':<12} | {clics:<15} | {nivel_compromiso:<10}")
    print("-" * 65)

   # --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # Matriz de datos iniciales con las 5 filas requeridas
    # Formato de cada fila: [ID Cliente, Duración (segundos), Eventos Clics]

   datos_clientes = [
        [101, 200, 12],  # Caso: Alto (Duración > 180 y Clics > 8)
        [102, 45, 2],    # Caso: Bajo (Duración < 60 o Clics < 3)
        [103, 120, 5],   # Caso: Medio (Ninguno de los extremos)
        [104, 210, 4],   # Caso: Medio (Cumple duración, pero no clics)
        [105, 50, 15]    # Caso: Bajo (Cumple clics, pero duración < 60)
    ]
       # Ejecución de la herramienta
    evaluar_matriz_sesiones(datos_clientes)
    

