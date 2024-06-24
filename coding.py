from colorama import init, Fore
init(autoreset=True)

def codificar(texto):
    texto_codificado = texto.encode('utf-8').hex()
    return texto_codificado

def decodificar(codigo):
    texto_decodificado = bytearray.fromhex(codigo).decode('utf-8')
    return texto_decodificado

def main():
    continuar = True
    while continuar:
        print(Fore.GREEN + "¿Que deseas hacer?")
        print("1.Codificar texto")
        print("2.Decodificar codigo")
        opcion = input("Selecciona una opcion(1/2):")

        if opcion == '1':
            texto = input("Introduce el texto a codificar:")
            texto_codificado = codificar(texto)
            print(Fore.CYAN + f"Texto codificado:{texto_codificado}")
        elif opcion == '2':
            codigo = input("Introduce el codigo a decodificar:")
            texto_decodificado = decodificar(codigo)
            print(Fore.CYAN + f"Texto decodificado:{texto_decodificado}")
        else:
            print(Fore.RED + "Opcion no valida")

        seguir = input(Fore.YELLOW + "¿Quieres continuar? (s/n): ")
        if seguir.lower() != 's':
            continuar = False

if __name__ == "__main__":
    main()

