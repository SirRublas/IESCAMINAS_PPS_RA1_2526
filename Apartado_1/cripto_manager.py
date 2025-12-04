import string

class CriptoManager:
    def __init__(self):
        self.alfabeto = string.ascii_lowercase
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Cifra un texto usando el cifrado César.
        Mueve cada letra 'desplazamiento' posiciones a la derecha.
        """
        resultado = []
        for char in texto:
            if char.lower() in self.alfabeto:
                # Determinar si es mayúscula para mantener el formato
                es_mayuscula = char.isupper()
                char_idx = self.alfabeto.index(char.lower())
                
                # Calcular nueva posición con módulo 26 para dar la vuelta (z->a)
                nuevo_idx = (char_idx + desplazamiento) % 26
                nueva_letra = self.alfabeto[nuevo_idx]
                
                if es_mayuscula:
                    nueva_letra = nueva_letra.upper()
                resultado.append(nueva_letra)
            else:
                # Si no es letra (espacio, número, signo), se deja igual
                resultado.append(char)
        
        return "".join(resultado)

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra un texto cifrado con César.
        Simplemente invierte el desplazamiento.
        """
        return self.cifrar_cesar(texto, -desplazamiento)

# Bloque principal para ejecutar la app en consola
if __name__ == "__main__":
    app = CriptoManager()
    print("=== APP DE CRIPTOGRAFÍA SENCILLA ===")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    opcion = input("Selecciona una opción (1/2): ")
    
    msg = input("Introduce el mensaje: ")
    try:
        shift = int(input("Introduce el desplazamiento (número entero): "))
        
        if opcion == "1":
            print(f"Resultado: {app.cifrar_cesar(msg, shift)}")
        elif opcion == "2":
            print(f"Resultado: {app.descifrar_cesar(msg, shift)}")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: El desplazamiento debe ser un número.")