# Modulo 2, actividad 1, largo de una palabra.
# Mostrar el mensaje con el largo de la palabra ingresada.
mensaje = "Ingrese una palabra de 4 a 8 letras: "
palabra = input(mensaje).strip()  # Elimina espacios al inicio/final

#Muestra el numero de carácteres de la palabra ingresada, y valida que tenga entre 4 y 8 letras.
# Muestra que sean letras y no digitos.
while True:
     # Validar que solo contenga letras
    if not palabra.isalpha():
        print("Error: Solo se permiten letras (sin números ni caracteres especiales).")
        palabra = input(mensaje).strip()
        continue
    if len(palabra) < 4: #aqui valida que tenga minimo 4 letras con el len de la palabra
        print("Hacen falta letras, tiene", len(palabra), "letras")
        palabra = input(mensaje)
    elif len(palabra) > 8: #aqui valida que tenga maximo 8 letras con el len de la palabra
        print("Sobran letras, tiene", len(palabra), "letras" )        
        palabra = input(mensaje)
    else: #si la palabra tiene entre 4 y 8 letras, muestra que es correcta
        print(palabra, "Es correcta.")
        break

# Verificación de la palabra con while
verificacion = input("Ingrese su palabra nuevamente: ")
while verificacion != palabra:
    print("Palabra incorrecta, intente de nuevo.")
    verificacion = input("Ingrese su palabra nuevamente: ")

print("Palabra correcta.")
print("Fin del programa.")