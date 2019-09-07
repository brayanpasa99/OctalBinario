CONVERSION = {"0": "000", "1": "001", "2": "010", "3": "011", "4": "100", "5": "101", "6": "110", "7": "111"}


def main():
    ejecutar = True
    while (ejecutar):
        print("1. Decimal - Binario")
        print("2. Decimal - Quinario")
        print("3. Decimal - Octal")
        print("4. Decimal - Hexadecimal")
        print("5. Salir")

        opc = int(input("Ingrese la opcion: "))

        if opc < 5:

            num_dec = int(input("Ingrese el numero a convertir: "))

        if opc == 1:
            print(dec_ds(num_dec, 2))
            print(dec_ex(num_dec))
        elif opc == 2:
            print(dec_ds(num_dec, 5))
        elif opc == 3:
            print(dec_ds(num_dec, 8))
        elif opc == 4:
            print(dec_ds(num_dec, 16))
        elif opc == 5:
            ejecutar = False
        else:
            print("No es una opcion valida")


def dec_ds(num, base):
    num_conv = ""
    while num >= base:
        num_conv = num_conv + LETRAS[str(num % base)];
        num = int(num / base);

    num_conv = num_conv + LETRAS[str(num)];
    num_conv = num_conv[::-1]
    return "Método de divisiones sucesivas: "+num_conv

def dec_ex(n):
    i=0
    while(2**i<=n):
        exponente = i
        i = i+1

    suma = 0
    resultado = ""

    while (exponente>=0):
        if (suma + (2**exponente)<=n):
            resultado = resultado + "1"
            suma = suma + 2**exponente
            exponente = exponente - 1
        else:
            resultado = resultado + "0"
            exponente = exponente - 1

    return "Metodo de exponenciacion: "+resultado


if __name__ == "__main__":
    main()