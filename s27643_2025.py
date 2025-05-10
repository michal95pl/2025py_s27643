import random

# program generuje losową sekwencję DNA o zadanej długości, wstawia do niej imię użytkownika i zapisuje wynik w formacie FASTA

# funkcja do generowania sekwencji DNA
def generate_dna_sequence(length):
    # dodaje do pustej sekwencji losowe nukleotydy A, C, G, T o zadanej długości
    return ''.join(random.choices('ACGT', k=length))

def insert_name(sequence, name):
    # losuje pozycję wstawienia imienia w sekwencji
    pos = random.randint(0, len(sequence))
    # wstawia imię wylosowanej pozycji
    return sequence[:pos] + name + sequence[pos:]

def calculate_statistics(sequence):
    # oryginal
    #sequence = ''.join([base for base in sequence if base in 'ACGT'])
    # modified (niepotrzebne filtrowanie gdy do funkcji nie przekazyjemy sekwencji z imieniem)

    # oblicza długość sekwencji
    length = len(sequence)
    # zlicza ilość wystąpień każdego nukleotydu, nastepnie dzieli przez długość sekwencji i mnoży przez 100
    # zapisuje wyniki w słowniku
    stats = {nuc: (sequence.count(nuc) / length) * 100 for nuc in 'ACGT'}
    cg = stats['C'] + stats['G']
    at = stats['A'] + stats['T']
    #oryginal
    #cg_at_ratio = cg / at if at != 0 else 0
    # modified (niepotrzebne obliczanie stosunku CG/AT)
    return stats, cg

def save_to_fasta(file_name, header, sequence):
    # tworzy plik z podaną nazwą
    with open(file_name, 'w') as f:
        # zapisuje nagłówek i sekwencję w formacie FASTA
        f.write(f">{header}\n")
        # zapisuje sekwencję w formacie FASTA
        f.write(sequence + "\n")

def main():
    # Dane wejściowe od użytkownika
    length = int(input("Podaj długość sekwencji: "))
    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

    # Generowanie sekwencji DNA
    dna_seq = generate_dna_sequence(length)

    # Wstawianie imienia do sekwencji
    seq_with_name = insert_name(dna_seq, name)

    # Obliczanie statystyk
    # oryginal
    #stats, cg_percent = calculate_statistics(seq_with_name)
    # modified (tworzenie statystyk sekwencji bez imienia)
    stats, cg_percent = calculate_statistics(dna_seq)

    # tworzenie nazwy pliku z ID sekwencji oraz rozszerzeniem .fasta
    file_name = f"{seq_id}.fasta"
    # tworzenie headeru z ID sekwencji oraz opisu
    header = f"{seq_id} {description}"
    save_to_fasta(file_name, header, seq_with_name)

    # Wyświetlanie wyników
    print(f"\nSekwencja została zapisana do pliku {file_name}")
    print("Statystyki sekwencji:")
    # dla każdego nukleotydu A, C, G, T wyświetla jego procentowy udział w sekwencji
    for nuc in 'ACGT':
        print(f"{nuc}: {stats[nuc]:.1f}%")
    print(f"%CG: {cg_percent:.1f}")

# funkcja uruchamiająca program
if __name__ == "__main__":
    main()