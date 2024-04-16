import itertools

# Fonction booléenne
def f(a, b, c):
    return a and b or b and not c or a and not c

# Mode interactif
def interactive_mode():
    print("Mode interactif :")
    a = bool(input("Entrez la valeur de a (True/False) : "))
    b = bool(input("Entrez la valeur de b (True/False) : "))
    c = bool(input("Entrez la valeur de c (True/False) : "))
    result = f(a, b, c)
    print("Résultat de f(a, b, c) :", int(result))

# Table de vérité
def truth_table():
    print("\nTable de vérité de f(a, b, c):")
    print("a | b | c | f(a, b, c)")
    print("-" * 19)
    for combo in itertools.product([True, False], repeat=3):
        a, b, c = combo
        result = f(a, b, c)
        print(f"{int(a)} | {int(b)} | {int(c)} | {int(result)}")

# Tableau de Karnaugh
def karnaugh_map():
    print("\nTableau de Karnaugh :")
    print("      b'c'  bc  bc'  b'c")
    print("   +----------------------")
    for a in [True, False]:
        for b in [True, False]:
            print(f"a={int(a)} |", end=" ")
            for c in [True, False]:
                result = f(a, b, c)
                print(f" {int(result)}  ", end=" ")
            print()
        print()

# Exécution du code interactif
if __name__ == "__main__":
    interactive_mode()
    truth_table()
    karnaugh_map()