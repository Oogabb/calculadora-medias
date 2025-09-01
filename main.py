# 📘 Calculadora de Médias - ADS
# Autor: Gabriel Boscovich da Silva
# Objetivo: Calcular a média de um aluno e indicar se está aprovado, em recuperação ou reprovado.

def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"

def main():
    print("=== Calculadora de Médias ===\n")
    while True:
        try:
            qtd_notas = int(input("Quantas notas deseja inserir? "))
            if qtd_notas <= 0:
                print("Por favor, informe um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    notas = []
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Digite a {i+1}ª nota: "))
                if nota < 0 or nota > 10:
                    print("A nota deve estar entre 0 e 10.")
                    continue
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Digite um número (ex: 7.5).")

    media = calcular_media(notas)
    print("\n--- Resultado ---")
    print(f"Média Final: {media:.2f}")
    print(f"Status: {situacao(media)}")

if __name__ == "__main__":
    main()
