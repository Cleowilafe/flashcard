import random
import json
import os

ARQUIVO = "flashcards.json"

# Se não existir arquivo, cria um com exemplos
if not os.path.exists(ARQUIVO):
    flashcards_iniciais = [
        {
            "jp": "久しぶり！元気にしてた？",
            "pt": "Quanto tempo! Você tem estado bem?",
            "nivel": 1
        },
        {
            "jp": "最近どう？",
            "pt": "E aí, como você anda ultimamente?",
            "nivel": 1
        },
        {
            "jp": "どのくらいここに住んでるの？",
            "pt": "Há quanto tempo você mora aqui?",
            "nivel": 1
        }
    ]
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(flashcards_iniciais, f, ensure_ascii=False, indent=4)

# Carregar flashcards
with open(ARQUIVO, "r", encoding="utf-8") as f:
    flashcards = json.load(f)

def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=4)

def estudar():
    print("\n=== Modo Estudo ===\n")

    while True:
        card = random.choices(
            flashcards,
            weights=[c["nivel"] for c in flashcards],
            k=1
        )[0]

        print("\nJaponês:")
        print(card["jp"])
        input("\nPressione Enter para ver a tradução...")

        print("\nPortuguês:")
        print(card["pt"])

        acerto = input("\nVocê acertou? (s/n/q): ").lower()

        if acerto == "s":
            card["nivel"] += 1
        elif acerto == "n":
            card["nivel"] = max(1, card["nivel"] - 1)
        elif acerto == "q":
            salvar()
            break

def adicionar():
    print("\n=== Adicionar Flashcard ===\n")
    jp = input("Frase em japonês: ")
    pt = input("Tradução em português: ")

    flashcards.append({
        "jp": jp,
        "pt": pt,
        "nivel": 1
    })

    salvar()
    print("Flashcard adicionado!")

while True:
    print("\n==== MINI ANKI ====")
    print("1 - Estudar")
    print("2 - Adicionar frase")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        estudar()
    elif opcao == "2":
        adicionar()
    elif opcao == "3":
        salvar()
        break
