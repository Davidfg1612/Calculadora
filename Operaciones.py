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

def crear_subboton(frame, texto, x, y):
    subboton = tk.Button(
        frame,
        text=texto,
        font=("Consolas", 20),
        bg="#394757",
        fg="#FFFFFF",
        bd=1,
        relief="flat",
    )
    subboton.place(x=x, y=y)
    return subboton
def crear_boton(frame, texto, x, y):
    boton = tk.Button(
        frame,
        text=texto,
        font=("Consolas", 20),
        bg="#394757",
        fg="#FFFFFF",
        width=5,
        height=2,
        bd=1,
        relief="flat"
    )
    boton.place(x=x, y=y)
    return boton

def crear_boton1(frame, texto, x, y, **kwargs):
    boton = tk.Button(
        frame,
        text=texto,
        font=("Consolas", 20),
        bg="#394757",
        fg="#FFFFFF",
        bd=1,
        relief="flat",
        **kwargs
    )
    boton.place(x=x, y=y)
    return boton
def crear_boton_con_offset(frame, texto, x, y, **kwargs):
    return crear_boton(frame, texto, x - 80, y - 120, **kwargs)

def borrar_todo(campo):
    campo.delete(0, tk.END)

def borrar_ultimo(campo):
    pos = campo.index(tk.INSERT)
    if pos > 0:
        campo.delete(pos - 1)

def Pesos_a_dolares(pesos):
    return pesos * 0.00025

def Pesos_a_euros(pesos):
    return pesos * 0.00022

def Dolares_a_euros(dolares):
    return dolares * 0.92

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
    "√": math.sqrt,  
    "³√": raiz_cubica,    
    "ⁿ√x": raiz_enesima, 
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
    "COP": Pesos_a_dolares,
    "EUR": Pesos_a_euros,
    "USD": Dolares_a_euros,
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

