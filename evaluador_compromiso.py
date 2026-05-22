
# ==============================================================================
# UNAD - Fundamentos de Programación
# Fase 5 – Evaluación Final POA
# Estudiante: Doris Adriana Mosquera | Código de Curso: 213022_566
# ==============================================================================

def clasificar_compromiso(duracion, clics):
    """
    Función modular que aplica la lógica de negocio (RN-01, RN-02, RN-03).
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_informe_sesiones():
    """
    Carga la matriz (RF-01) e itera los datos para la salida en consola (RI-01).
    """
    # Matriz bidimensional con los 5 registros de la prueba de escritorio
    matriz_clientes = [
        [101, 200, 12],
        [102, 45, 2],
        [103, 120, 5],
        [104, 210, 4],
        [105, 50, 15]
    ]
    
    # Diseño de la interfaz de salida en consola (RI-01)
    print("=" * 60)
    print("        INFORME DE NIVEL DE COMPROMISO DE CLIENTES")
    print("=" * 60)
    print(f"{'ID Cliente':<12} | {'Duración (s)':<13} | {'Clics':<8} | {'Clasificación':<10}")
    print("-" * 60)
    
    # Ciclo repetitivo for para recorrer las filas de la matriz
    for sesion in matriz_clientes:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamado al módulo de cálculo (RF-02)
        resultado = clasificar_compromiso(duracion, clics)
        
        print(f"{id_cliente:<12} | {duracion:<13} | {clics:<8} | {resultado:<10}")
        
    print("=" * 60)

if __name__ == "__main__":
    generar_informe_sesiones()
