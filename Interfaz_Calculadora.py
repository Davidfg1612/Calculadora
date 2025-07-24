#Calculadora con interfaz gráfica en Python usando tkinter versión 3.0.
from tkinter import *
import tkinter as tk
import os
import Operaciones as op

submenu_monedas_visible = False

def mostrar_tutorial():
    ventana = tk.Toplevel(raiz)
    ventana.title("Tutorial de funciones")
    ventana.geometry("1100x700")
    explicacion = tk.Text(ventana, wrap="word", bg="#2C2C2C", fg="#E5E5E5", font=("Consolas", 12), bd=0, relief="flat")
    explicacion.pack(expand=True, fill="both")

    texto = """
Bienvenido al tutorial de la calculadora.

Esta calculadora permite realizar operaciones matemáticas avanzadas y conversiones de unidades.
Puedes ingresar expresiones matemáticas directamente en la entrada de texto y presionar Enter o el botón "=" para calcular el resultado.
También puedes usar los botones para insertar números y operaciones de manera más rápida.
Para ingresar números mediante el teclado, asegúrate de que la entrada esté activa (haz clic en ella (esta en la parte superior del todo, la que esta en el medio de las funciones y la parte superior es donde se mostrara el resultado, la de arriba es donde se mostrara la operación a realizar)o usa Tab para seleccionarla).
Funciones disponibles:

• (): Paréntesis para agrupar operaciones.
• =: Calcula el resultado de la expresión.
• AC: Borra todo el contenido de la entrada.
• ←: Borra el último carácter de la entrada.
• ,: Coma para separar números.
• fibo(n): Devuelve el n-ésimo número de Fibonacci.
• MCD(a, b): Máximo común divisor.
• MCM(a, b): Mínimo común múltiplo.
• porc(x): Convierte porcentaje (ej: porc(25, 200) devuelve 50.0).
• grad(x): Convierte radianes a grados.
• round+(x): Redondea hacia arriba.
• round-(x): Redondea hacia abajo.
• round(x): Redondea al entero más cercano.
• ³√(x): Raíz cúbica.
• ⁿ√x(n, x): Raíz enésima de x.
• √(x): Raíz cuadrada.
• log(x): Logaritmo natural.
• log₁₀(x): Logaritmo en base 10.
• log₂(x): Logaritmo en base 2.
• sin(x): Seno.
• cos(x): Coseno.
• tan(x): Tangente.
• int(x): Convierte a entero.
• abs(x): Valor absoluto.
• e: Constante de Euler.
• π: Número pi.
• x!: Factorial de x.
• hypot(x, y): Hipotenusa de un triángulo rectángulo. (Ingresa los dos catetos)
• exp(x): Exponencial de x.

• EXTRAS:

• COP(x): Convierte pesos colombianos a dólares.
• USD(x): Convierte dólares a euros.
• EUR(x): Convierte euros a pesos colombianos.
• kg(x): Convierte kilogramos a libras.
• g(x): Convierte gramos a onzas.

• ERRORES:

• ValueError: Si se ingresa un valor númerico no válido (ej: letras)\n.
• ZeroDivisionError: Si se intenta dividir por cero (Puede presentarse en otras operaciones)\n.
• SyntaxError: Si la expresión a operar ingresada no es válida (ej: paréntesis sin cerrar)\n.
• TypeError: Si se intenta realizar una operación con tipos de datos incompatibles (ej: sumar un número y una cadena de texto)\n.
• NameError: Si se usa una variable no definida en la expresión del diccionario\n.
• AttributeError: Si se intenta acceder a un método que no existe en un objeto (ej: numero = 10 \n numero.append(5) los enteros no poseen método append)\n.
• IndexError: Si se intenta acceder a un índice fuera del rango de una lista o cadena (ej: lista = [1, 2, 3] \n lista[5])\n.
• KeyError: Si se intenta acceder a una clave que no existe en un diccionario (ej: diccionario = {'a': 1, 'b': 2} \n diccionario['c'])\n.
• OverflowError: Si se intenta realizar una operación que excede el límite de tamaño de un número (ej: 10**1000)\n.
• MemoryError: Si se intenta usar más memoria de la disponible (puede ocurrir con listas muy grandes o recursiones profundas)\n.
• RecursionError: Si se excede el límite de recursión al llamar a una función recursiva demasiadas veces (ej: fibo(1000) si no se usa memorización)\n.
• ImportError: Si se intenta importar un módulo que no existe o no está instalado (ej: import modulo_inexistente)\n.

    """
    explicacion.insert("0.2", texto)
    explicacion.config(state="disabled")

def toggle_submenu_monedas():
    global submenu_monedas_visible
    if submenu_monedas_visible:
        submenu_monedas.place_forget()
    else:
        submenu_monedas.place(x=500, y=25)
        submenu_monedas.lift()
    submenu_monedas_visible = not submenu_monedas_visible


raiz = tk.Tk()
ancho_total = raiz.winfo_screenwidth()
alto_total = raiz.winfo_screenheight()
raiz.geometry(f"{int(ancho_total * 0.8)}x{int(alto_total * 0.8)}")
raiz.title("Calculadora")
raiz.config(bg="#233747")
raiz.config(bd=1, relief="flat")



icono_ruta = os.path.join(os.path.dirname(__file__), "calculadora_icono.ico")
if os.path.exists(icono_ruta):
    raiz.iconbitmap(icono_ruta)

frame = tk.Frame(raiz, bg="#DDDDDD")
frame.pack(side="top", expand=False, fill="x")

frame2 = tk.Frame(raiz, bg="#DDDDDD")
frame2.pack(side="top",expand=False, fill="x")


# Entrada del usuario (editable)
resultado = tk.Entry(frame, font=("Consolas", 30), bg="#FFFFFF", fg="#000000", insertbackground="#000000",
                justify="right")
resultado.pack(padx=20, pady=20, expand=True, fill="x")

# Resultado (solo lectura, no editable)
salida = tk.Entry(frame2, font=("Consolas", 25), fg="#000000",
            readonlybackground="#FFFFFF", justify="right", state="readonly")
salida.pack(padx=20, pady=20, expand=True, fill="x")


frame1 = tk.Frame(raiz, width=ancho_total * 0.8 - 800, bg="#DDDDDD")
frame1.pack(side="top", expand=True, fill="both")

for fila in range(7):
    frame1.rowconfigure(fila, weight=1)

for col in range(9):
    frame1.columnconfigure(col, weight=1, uniform="col")

# Bind para permitir el uso de Enter para calcular
resultado.bind("<Return>", lambda event: op.enter(resultado, salida, event))

submenu_monedas = tk.Frame(frame1, bg="#FFFFFF", bd=2, relief="raised")

tk.Button(submenu_monedas, text="COP → USD", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "COP_USD()")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="USD → COP", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "USD_COP()")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="COP → EUR", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "COP_EUR(")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="EUR → COP", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "EUR_COP(")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="USD → EUR", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "USD_EUR(")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="EUR → USD", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "EUR_USD(")).pack(pady=5, padx=5)
tk.Button(submenu_monedas, text="kg → lb", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "kg(")).pack(pady=5, padx=5, fill="x")
tk.Button(submenu_monedas, text="g → oz", font=("Consolas", 15),bg="#FFFFFF", fg="#000000", command=lambda: resultado.insert("insert", "g(")).pack(pady=5, padx=5, fill="x")



op.crear_boton_estilo(frame1, "Off", 0, 0, estilo="rojo", comando=raiz.quit)
op.crear_boton_estilo(frame1, "Extras", 0, 1, estilo="verde", comando=toggle_submenu_monedas)
op.crear_boton_estilo(frame1, "Tutorial", 0, 2, comando=mostrar_tutorial)
op.crear_boton_estilo(frame1, "AC", 1, 7, estilo="rojo", comando=lambda: op.borrar_todo(resultado))
op.crear_boton_estilo(frame1, "←", 1, 8, estilo="rojo", comando=lambda: op.borrar_ultimo(resultado))

op.crear_boton_estilo(frame1, "(", 1, 0, comando=lambda: resultado.insert("insert", "("))
op.crear_boton_estilo(frame1, ")", 1, 1, comando=lambda: resultado.insert("insert", ")"))
op.crear_boton_estilo(frame1, "π", 1, 2, comando=lambda: resultado.insert("insert", "π"))
op.crear_boton_estilo(frame1, "e", 1, 3, comando=lambda: resultado.insert("insert", "e"))
op.crear_boton_estilo(frame1, "^", 5, 3, comando=lambda: resultado.insert("insert", "**"))

op.crear_boton_estilo(frame1, "x!", 2, 0, comando=lambda: resultado.insert("insert", "factorial("))
op.crear_boton_estilo(frame1, "|x|", 2, 1, comando=lambda: resultado.insert("insert", "abs("))
op.crear_boton_estilo(frame1, "MCM", 3, 2, comando=lambda: resultado.insert("insert", "MCM("))
op.crear_boton_estilo(frame1, "MCD", 2, 2, comando=lambda: resultado.insert("insert", "MCD("))
op.crear_boton_estilo(frame1, "porc", 3, 0, comando=lambda: resultado.insert("insert", "porc("))
op.crear_boton_estilo(frame1, "7", 2, 5, comando=lambda: resultado.insert("insert", "7"))
op.crear_boton_estilo(frame1, "8", 2, 6, comando=lambda: resultado.insert("insert", "8"))
op.crear_boton_estilo(frame1, "9", 2, 7, comando=lambda: resultado.insert("insert", "9"))
op.crear_boton_estilo(frame1, "ⁿ√x", 2, 3, comando=lambda: resultado.insert("insert", "raizn("))

op.crear_boton_estilo(frame1, "hypot", 5, 0, comando=lambda: resultado.insert("insert", "hypot("))
op.crear_boton_estilo(frame1, "cos", 3, 1, comando=lambda: resultado.insert("insert", "cos("))
op.crear_boton_estilo(frame1, "int", 4, 2, comando=lambda: resultado.insert("insert", "int("))
op.crear_boton_estilo(frame1, "³√", 3, 3, comando=lambda: resultado.insert("insert", "raiz3("))
op.crear_boton_estilo(frame1, "4", 3, 5, comando=lambda: resultado.insert("insert", "4"))
op.crear_boton_estilo(frame1, "5",  3, 6, comando=lambda: resultado.insert("insert", "5"))
op.crear_boton_estilo(frame1, "6", 3, 7, comando=lambda: resultado.insert("insert", "6"))
op.crear_boton_estilo(frame1, "√", 4, 3, comando=lambda: resultado.insert("insert", "raiz2("))

op.crear_boton_estilo(frame1, "log", 3, 4, comando=lambda: resultado.insert("insert", "log("))
op.crear_boton_estilo(frame1, "tan", 4, 1, comando=lambda: resultado.insert("insert", "tan("))
op.crear_boton_estilo(frame1, "e^x", 5, 2, comando=lambda: resultado.insert("insert", "exp("))
op.crear_boton_estilo(frame1, "+", 2, 8, comando=lambda: resultado.insert("insert", "+"))
op.crear_boton_estilo(frame1, "log₁₀",  2, 4, comando=lambda: resultado.insert("insert", "log10("))
op.crear_boton_estilo(frame1, "1", 4, 5, comando=lambda: resultado.insert("insert", "1"))
op.crear_boton_estilo(frame1, "2", 4, 6, comando=lambda: resultado.insert("insert", "2"))
op.crear_boton_estilo(frame1, "3", 4, 7, comando=lambda: resultado.insert("insert", "3"))
op.crear_boton_estilo(frame1, "-", 3, 8, comando=lambda: resultado.insert("insert", "-"))

op.crear_boton_estilo(frame1, "log₂", 4, 4, comando=lambda: resultado.insert("insert", "log2("))
op.crear_boton_estilo(frame1, "sin", 5, 1, comando=lambda: resultado.insert("insert", "sin("))
op.crear_boton_estilo(frame1, "fibo", 4, 0, comando=lambda: resultado.insert("insert", "fibo("))
op.crear_boton_estilo(frame1, "*", 4, 8, comando=lambda: resultado.insert("insert", "*"))
op.crear_boton_estilo(frame1, ",", 5, 4, comando=lambda: resultado.insert("insert", ","))
op.crear_boton_estilo(frame1, "0", 5, 5, comando=lambda: resultado.insert("insert", "0"))
op.crear_boton_estilo(frame1, ".", 5, 6, comando=lambda: resultado.insert("insert", "."))
op.crear_boton_estilo(frame1, "=", 5, 7, estilo="azul", comando=lambda: op.calcular(resultado, salida))
op.crear_boton_estilo(frame1, "/", 5, 8, comando=lambda: resultado.insert("insert", "/"))

raiz.mainloop()
