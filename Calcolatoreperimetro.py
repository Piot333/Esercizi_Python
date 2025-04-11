import math  # Importiamo la libreria math per usare pi

# Funzione per calcolare il perimetro del quadrato
def perimetro_quadrato(lato):
    return lato * 4

# Funzione per calcolare la circonferenza del cerchio
def perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

# Funzione per calcolare il perimetro del rettangolo
def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

# Benvenuto al programma
print("Benvenuto nel calcolatore di Issac! Il calcolatore dei perimetri!")

# Chiediamo all'utente che tipo di figura vuole calcolare
print("\nScegli una figura geometrica:")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = input("Inserisci il numero della figura (1, 2, 3): ")

# Chiediamo l'unità di misura
unita = input("Quale unità di misura vuoi usare? (es. cm, m): ")

# Iniziamo il calcolo in base alla scelta dell'utente
if scelta == "1":  # Se l'utente sceglie il quadrato
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro = perimetro_quadrato(lato)
    print(f"Il perimetro del quadrato è: {perimetro} {unita}")

elif scelta == "2":  # Se l'utente sceglie il cerchio
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = perimetro_cerchio(raggio)
    print(f"La circonferenza del cerchio è: {perimetro} {unita}")

elif scelta == "3":  # Se l'utente sceglie il rettangolo
    base = float(input("Inserisci la lunghezza della base del rettangolo: "))
    altezza = float(input("Inserisci la lunghezza dell'altezza del rettangolo: "))
    perimetro = perimetro_rettangolo(base, altezza)
    print(f"Il perimetro del rettangolo è: {perimetro} {unita}")

else:
    print("Scelta non valida. Per favore inserisci 1, 2 o 3.")
