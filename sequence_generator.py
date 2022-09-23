from itertools import product
from aa_mass import aa_masses as aa
from mass_calculator import calc_mass

def conjugates_to_list(conjugates):
    """
    Add peptide conjugates to list.
    :params conjugates: string of peptide conjugates.
    :return: list of conjugates.
    """
    #conj = [conj.strip() for conj in peptide.upper().split(',')]
    conjugates_list = []
    for conjugate in conjugates.upper().split(','):
        conjugates_list.append(conjugate.strip())
    conjugates_list.sort()

    return conjugates_list

def generate_sequences(conjugates_list, num_connects):
    """
    Generate all possible peptide sequences from fragments
    :param conjugates_list: List of conjugates to combine.
    :param num_connects: number of connections.
    :return: None
    """
    total = 0
    for i in range(2, int(num_connects) + 2):
        count = 0
        for conjugates in product(conjugates_list, repeat=i):
            sequences = ''.join(conjugates)
            print(sequences, format(calc_mass(sequences), '.4f'))
            count += 1
            total += 1
        print(f'{count} fragments with {i - 1} bond(s) formed')
    print('Total number of possible fragments: ', total)

    return

def main():
    peptides = input('Enter peptide conjugates: ')
    num_connect = input('Maximum number of bonds formed: ')

    conjugates = conjugates_to_list(peptides)
    generate_sequences(conjugates, num_connect)

if __name__ == "__main__":
    main()
