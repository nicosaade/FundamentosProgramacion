NombreCompleto = str(input("Ingrese su nombre completo: "))
partes = NombreCompleto.strip().split()
PrimerNombre = partes[0].lower()
PrimerApellido = partes[2].lower()
Correo = PrimerNombre + "." + PrimerApellido + "@keyinstitute.edu.sv"
print("El correo que se debe asignar al usuario ingresado es:",Correo)
