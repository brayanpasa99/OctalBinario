CONVERSION = {"0": "000", "1": "001", "2": "010", "3": "011", "4": "100", "5": "101", "6": "110", "7": "111"}

def main():
    ejecutar = True
    while (ejecutar):

        print("1. Convertir de Octal a Binario")
        print("2. Salir")

        opc = int(input("Ingrese la opcion: "))

        if opc == 1:
            num_dec = int(input("Ingrese el numero a convertir: "))
            print(oct_dec(num_dec))
            print("")

        elif opc == 2:
            ejecutar = False

        else:
            print("No es una opcion valida")
            print("")

def oct_dec(num):
    i = 0
    num_conv = ""
    num_str = str(num)
    while(i<len(num_str)):
        num_conv = num_conv + CONVERSION[num_str[i]]
        i = i + 1
    return "Numero en binario: " + num_conv

if __name__ == "__main__":
    main()