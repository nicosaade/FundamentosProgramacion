contraseña = input("Introduce una contraseña: ")

tiene_mayuscula = False
tiene_numero = False

for i in contraseña:
    if i.isupper():
        tiene_mayuscula = True
    if i.isdigit():
        tiene_numero = True
if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero:
    print("Contraseña segura")
else: 
    print("Contraseña insegura")