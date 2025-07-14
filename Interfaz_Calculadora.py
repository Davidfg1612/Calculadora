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
    explicacion.config(state="disabled")  # Solo lectura

def toggle_submenu_monedas():
    global submenu_monedas_visible
    if submenu_monedas_visible:
        submenu_monedas.place_forget()
    else:
        submenu_monedas.place(x=800, y=95)  
        submenu_monedas.lift()
    submenu_monedas_visible = not submenu_monedas_visible


raiz = tk.Tk()
ancho1 = raiz.winfo_screenwidth()
alto1 = raiz.winfo_screenheight()
ancho = ancho1 - 700
alto = alto1 - 170
raiz.title("Calculadora")
raiz.geometry(f"{ancho}x{alto}") 
raiz.config(bg="#233747")
raiz.config(bd=1, relief="flat")
raiz.resizable(False, False)


icono_ruta = os.path.join(os.path.dirname(__file__), "calculadora_icono.ico")
if os.path.exists(icono_ruta):
    raiz.iconbitmap(icono_ruta)
frame = tk.Frame(raiz, width=ancho, height=80, bg="#000000")
frame.pack_propagate(False)  
frame.pack(side="top", fill="x", expand=False)

frame2 = tk.Frame(raiz, width=ancho, height=80, bg="#000000")
frame2.pack_propagate(False)  
frame2.pack(side="top", fill="x", expand=False)
submenu = tk.Frame(frame, bg="#000000")

# Entrada del usuario (editable)
resultado = tk.Entry(frame, font=("Consolas", 30), bg="#FFFFFF", fg="#000000", insertbackground="#000000",
                bd=0, relief="flat", justify="right")
resultado.place(x=20, y=20, width=ancho - 40, height=50)
resultado.config(bd=0, relief="flat")

# Bind para permitir el uso de Enter para calcular
resultado.bind("<Return>", lambda event: op.enter(resultado, salida, event))

# Resultado (solo lectura, no editable)
salida = tk.Entry(frame2, font=("Consolas", 25), fg="#000000",
            readonlybackground="#FFFFFF", justify="right", state="readonly", relief="flat", bd=0)
salida.place(x=20, y=20, width=ancho - 40, height=45)


frame1 = tk.Frame(raiz, width=ancho, height=alto-160, bg="#000000")
frame1.pack_propagate(False) 
frame1.pack(side="bottom", fill="both", expand=True)

submenu_monedas = tk.Frame(frame1, bg="#000000", bd=2, relief="flat")
submenu_monedas.config(width=200, height=600)

tk.Button(submenu_monedas, text="COP → USD", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "COP_USD()")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="USD → COP", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "USD_COP()")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="COP → EUR", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "COP_EUR(")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="EUR → COP", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "EUR_COP(")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="USD → EUR", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "USD_EUR(")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="EUR → USD", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "EUR_USD(")).pack(side = "top", pady=5, padx=5)

tk.Button(submenu_monedas, text="kg → lb", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "kg(")).pack(side = "top", pady=5, padx=5)
tk.Button(submenu_monedas, text="g → oz", font=("Consolas", 15),bg="#000000", fg="white", relief="flat", command=lambda: resultado.insert("insert", "g(")).pack(side = "top", pady=5, padx=5)


op.crear_boton1(frame1, "Conversión", 780, 40).config(command=toggle_submenu_monedas)
op.crear_boton1(frame1, "Tutorial", 1020, 40).config(command=mostrar_tutorial)
op.crear_boton_con_offset(frame1, "(", 100, 260).config(command=lambda: resultado.insert("insert", "("))
op.crear_boton_con_offset(frame1, ")", 220, 260).config(command=lambda: resultado.insert("insert", ")"))
op.crear_boton_con_offset(frame1, "|x|", 340, 380).config(command=lambda: resultado.insert("insert", "abs("))

op.crear_boton_con_offset(frame1, "π", 340, 260).config(command=lambda: resultado.insert("insert", "π"))
op.crear_boton_con_offset(frame1, "e", 460, 260).config(command=lambda: resultado.insert("insert", "e"))
op.crear_boton_con_offset(frame1, "←", 1180, 260).config(command=lambda: op.borrar_ultimo(resultado))
op.crear_boton_con_offset(frame1, "AC", 1060, 260).config(command=lambda: op.borrar_todo(resultado))

op.crear_boton_con_offset(frame1, "0", 820, 740).config(command=lambda: resultado.insert("insert", "0"))
op.crear_boton_con_offset(frame1, ".", 940, 740).config(command=lambda: resultado.insert("insert", "."))
op.crear_boton_con_offset(frame1, "=", 1060, 740).config(command=lambda: op.calcular(resultado, salida))

op.crear_boton_con_offset(frame1, "1", 820, 620).config(command=lambda: resultado.insert("insert", "1"))
op.crear_boton_con_offset(frame1, "2", 940, 620).config(command=lambda: resultado.insert("insert", "2"))
op.crear_boton_con_offset(frame1, "3", 1060, 620).config(command=lambda: resultado.insert("insert", "3"))

op.crear_boton_con_offset(frame1, "4", 820, 500).config(command=lambda: resultado.insert("insert", "4"))
op.crear_boton_con_offset(frame1, "5", 940, 500).config(command=lambda: resultado.insert("insert", "5"))
op.crear_boton_con_offset(frame1, "6", 1060, 500).config(command=lambda: resultado.insert("insert", "6"))

op.crear_boton_con_offset(frame1, "7", 820, 380).config(command=lambda: resultado.insert("insert", "7"))
op.crear_boton_con_offset(frame1, "8", 940, 380).config(command=lambda: resultado.insert("insert", "8"))
op.crear_boton_con_offset(frame1, "9", 1060, 380).config(command=lambda: resultado.insert("insert", "9"))

op.crear_boton_con_offset(frame1, "+", 1180, 380).config(command=lambda: resultado.insert("insert", "+"))
op.crear_boton_con_offset(frame1, "-", 1180, 500).config(command=lambda: resultado.insert("insert", "-"))
op.crear_boton_con_offset(frame1, "*", 1180, 620).config(command=lambda: resultado.insert("insert", "*"))
op.crear_boton_con_offset(frame1, "/", 1180, 740).config(command=lambda: resultado.insert("insert", "/"))

op.crear_boton_con_offset(frame1, "^", 580, 260).config(command=lambda: resultado.insert("insert", "**"))
op.crear_boton_con_offset(frame1, ",", 700, 740).config(command=lambda: resultado.insert("insert", ","))
op.crear_boton_con_offset(frame1, "log₂", 700, 620).config(command=lambda: resultado.insert("insert", "log2("))
op.crear_boton_con_offset(frame1, "log₁₀", 700, 500).config(command=lambda: resultado.insert("insert", "log10("))
op.crear_boton_con_offset(frame1, "log", 700, 380).config(command=lambda: resultado.insert("insert", "log("))

op.crear_boton_con_offset(frame1, "√", 580, 740).config(command=lambda: resultado.insert("insert", "raiz2("))
op.crear_boton_con_offset(frame1, "³√", 580, 620).config(command=lambda: resultado.insert("insert", "raiz3("))
op.crear_boton_con_offset(frame1, "ⁿ√x", 580, 500).config(command=lambda: resultado.insert("insert", "raizn("))
op.crear_boton_con_offset(frame1, "MCD", 580, 380).config(command=lambda: resultado.insert("insert", "MCD("))

op.crear_boton_con_offset(frame1, "fibo", 460, 740).config(command=lambda: resultado.insert("insert", "fibo("))
op.crear_boton_con_offset(frame1, "int", 460, 620).config(command=lambda: resultado.insert("insert", "int("))
op.crear_boton_con_offset(frame1, "e^x", 460, 500).config(command=lambda: resultado.insert("insert", "exp("))
op.crear_boton_con_offset(frame1, "MCM", 460, 380).config(command=lambda: resultado.insert("insert", "MCM("))

op.crear_boton_con_offset(frame1, "sin", 340, 740).config(command=lambda: resultado.insert("insert", "sin("))
op.crear_boton_con_offset(frame1, "cos", 340, 620).config(command=lambda: resultado.insert("insert", "cos("))
op.crear_boton_con_offset(frame1, "tan", 340, 500).config(command=lambda: resultado.insert("insert", "tan("))

op.crear_boton_con_offset(frame1, "grad", 220, 740).config(command=lambda: resultado.insert("insert", "grad("))
op.crear_boton_con_offset(frame1, "round-", 220, 620).config(command=lambda: resultado.insert("insert", "round-("))
op.crear_boton_con_offset(frame1, "round", 220, 500).config(command=lambda: resultado.insert("insert", "round("))
op.crear_boton_con_offset(frame1, "round+", 220, 380).config(command=lambda: resultado.insert("insert", "round+("))
op.crear_boton_con_offset(frame1, "grad", 100, 740).config(command=lambda: resultado.insert("insert", "grad("))
op.crear_boton_con_offset(frame1, "hypot", 100, 620).config(command=lambda: resultado.insert("insert", "hypot("))
op.crear_boton_con_offset(frame1, "porc", 100, 500).config(command=lambda: resultado.insert("insert", "porc("))
op.crear_boton_con_offset(frame1, "x!", 100, 380).config(command=lambda: resultado.insert("insert", "factorial("))


op.crear_boton(frame1, "Off", 20, 20).config(command=raiz.quit)



raiz.mainloop()
