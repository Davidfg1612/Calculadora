import math
import tkinter as tk

def división(numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir por 0"
    else:
        return numero1 / numero2

def modulo(numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir por 0"
    else:
        return numero1 % numero2

def raiz_enesima(numero1, numero2):
    if numero2==0:
        raise ValueError("No se puede calcular la raíz con índice cero")
    elif numero1<0 and numero2% 2 == 0:
        raise ValueError("No se puede calcular la raíz par de un numero menor a 0")
    else:
        return numero1**(1/numero2)

def raiz_cubica(numero):
    return numero**(1/3)

def insertar_valor_absoluto(resultado):
    resultado.insert("insert", "||")
    resultado.icursor(resultado.index("insert") - 1)


def insertar_factorial(numero):
    return numero.insert("insert", "!")

def factorial(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, int(numero) + 1):
            resultado *= i
        return resultado

def MCM (numero1, numero2):
    return math.lcm (int(numero1), int(numero2))

def MCD (numero1, numero2):
    return math.gcd (int(numero1), int(numero2))

def fibonacci(numero):
    if numero < 0:
        raise ValueError("n debe ser un entero no negativo")
    elif numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, int(numero) + 1):
            a, b = b, a + b
        return b
    
def porcentaje(porcentaje, total):
    return (porcentaje / 100) * total

def entero(numero):
    return int(numero)

    boton.lace(x=x, y=y)
def borrar_todo(campo):
    campo.delete(0, tk.END)

def borrar_ultimo(campo):
    pos = campo.index(tk.INSERT)
    if pos > 0:
        campo.delete(pos - 1)

def COP_a_USD(x):
    return x / 4000  # Ejemplo de tasa

def USD_a_COP(x):
    return x * 4000

def COP_a_EUR(x):
    return x / 4400

def EUR_a_COP(x):
    return x * 4400

def USD_a_EUR(x):
    return x * 0.91

def EUR_a_USD(x):
    return x / 0.91

def kg_a_lb(kg):
    return kg * 2.20462

def g_a_oz(g):
    return g * 0.035274

contexto_eval = {
    # Constantes
    "π": math.pi,
    "e": math.e,
    # Aritmética
    "abs": abs,
    "int": int,
    "pow": pow,
    # Funciones trigonométricas
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    # Logaritmos
    "log": math.log,         
    "log10": math.log10,
    "log2": math.log2,
    # Raíces y potencias
    "raiz2": math.sqrt,  
    "raiz3": raiz_cubica,    
    "raizn": raiz_enesima, 
    "exp": math.exp,
    # Operaciones avanzadas
    "MCD": math.gcd,
    "MCM": math.lcm,
    "fibo": fibonacci,
    "factorial": factorial,
    "hypot": math.hypot,
    "porc": porcentaje,
    "exp": math.exp,      
    # Conversión
    "grad": math.degrees, 
    "rad": math.radians, 
    "round+": math.ceil,  
    "round-": math.floor,
    "round": round,
    "COP_USD": COP_a_USD,
    "EUR_COP": EUR_a_COP,
    "USD_EUR": USD_a_EUR,
    "COP_EUR": COP_a_EUR,
    "USD_COP": USD_a_COP,
    "EUR_USD": EUR_a_USD,
    "kg": kg_a_lb,
    "g": g_a_oz,
}

def evaluar(entrada, salida):
    try:
        expresion = entrada.get()
        resultado_valor = eval(expresion, {"__builtins__": None}, contexto_eval)

        # Actualiza el Entry de salida de forma segura

        salida.config(state="normal")          # Permite escribir temporalmente
        salida.delete(0, tk.END)               # Limpia el contenido anterior
        salida.insert(0, str(resultado_valor)) # Inserta el nuevo resultado
        salida.config(state="readonly")        # Lo bloquea 

    except Exception as e:
        salida.config(state="normal")
        salida.delete(0, tk.END)
        salida.insert(0, f"Error: {str(e)}")
        salida.config(state="readonly")

def calcular(resultado, salida):
    evaluar(resultado, salida)

def enter(entrada, salida, event=None):
    evaluar(entrada, salida)


def crear_boton_estilo(parent, texto, fila, columna, comando=None,
                    colspan=1, rowspan=1, estilo="normal"):
    estilos = {
        "normal": {"bg": "#FFFFFF", "fg": "#000000"},
        "azul":   {"bg": "#007BFF", "fg": "#FFFFFF"},
        "rojo":   {"bg": "#FF4136", "fg": "#FFFFFF"},
        "verde":   {"bg": "#2FB618", "fg": "#FFFFFF"}, 
    }

    colores = estilos.get(estilo, estilos["normal"])

    boton = tk.Button(
        parent,
        text=texto,
        font=("Consolas", 20),
        width=8, height=4,
        bg=colores["bg"],
        fg=colores["fg"],
        command=comando
    )
    boton.grid(
        row=fila,
        column=columna,
        columnspan=colspan,
        rowspan=rowspan,
        padx=10,
        pady=10
    )
    return boton