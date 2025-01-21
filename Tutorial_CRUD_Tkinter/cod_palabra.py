from itertools import permutations


def get_combinations(letters):
    all_combinations = []
    for i in range(cant_letras, len(letters) + 1):
         
        all_combinations.extend([''.join(p) for p in permutations(letters, i)])
    return all_combinations


def main():
    user_input = input("Ingrese letras sin espacios: ")
    # print(f"Cantidad de letras ingresadas: {len(user_input)}")
    combinations = get_combinations(user_input)
    print("Las combinaciones posibles son:")
    for i in range(cant_letras, len(combinations), 20):
        for combo in combinations[i:i+20]:
            print(combo)
        print("--------------")
        continua = input("´S´ para continuar...")
        if continua.upper() != "S":
            break
        print("--------------")


if __name__ == "__main__":
    cant_letras = 0
    cant_letras = int(input("Ingrese tamaño de la combinacion o cero 0: "))
    if cant_letras == 0:
        cant_letras = 3
    main()
