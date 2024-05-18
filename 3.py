def num_primo(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
def main():
    while True:
        try:
            número = int(input("Introduce un número entero mayor que 2: "))
            if número > 2:
                break
            else:
                print("El número no es mayor que 2.Ingrese un nuevo número.")
        except ValueError:
            print("El número no es entero. Ingrese un nuevo número")
            
    if num_primo(número):
        print(número,"es un número primo")
    else:
        print(número,"no es un número primo")
if __name__ == "__main__":
    main()