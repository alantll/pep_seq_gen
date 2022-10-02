from itertools import product
from molwts import molwts
from molwt_calculator import calc_molwt

def string_to_list(input):
    """
    Convert input string to list of peptide fragments.
    :params input (str): string of peptide fragments (comma-separated).
    :return: list of fragments and invalid inputs.
    """
    fragment_lst = []
    invalid_lst = []
    for fragment in input.upper().split(','):
        for residue in fragment:
            if residue not in molwts.keys():
                invalid_lst.append(residue)
            else:
                if fragment not in fragment_lst:
                    fragment_lst.append(fragment.strip())
                else:
                    pass

    fragment_lst.sort()
    invalid_lst.sort()

    return fragment_lst, invalid_lst

def generate_sequences(fragment_lst, max_connections, to_csv='n'):
    """
    Generate all possible peptide sequences from a list of fragments.
    :param fragment_lst (list): List of amino acid or peptide fragments to combine.
    :param max_connections (int): Maximum number of connections formed.
    :param to_csv (str): Save data to file. Default is 'n'
    :return: summary string and sequence string containing all possible sequences and the molecular weights.
    """
    summary = ""
    output = "Sequence, MW\n"
    total = 0
    for i in range(1, max_connections + 1):
        count = 0
        for fragments in product(fragment_lst, repeat=i+1):
            conjugate = ''.join(fragments)
            output += f'{conjugate}, {calc_molwt(conjugate):.4f}\n'
            count += 1
            total += 1
        summary += f'>{count} possible products with {i} connections(s)\n'
    summary = f'--Total number of possible products: {total}\n' + summary

    if to_csv == 'y':
        with open('data.csv', 'w') as out:
            out.write(output)

    return summary, output

def main():
    fragment_str = input('Amino acid/peptide fragments: ')
    fragments, invalids = string_to_list(fragment_str)
    if len(invalids) != 0:
        print("Invalid amino acids: '{}'.".format("', '".join(invalids)))

        return

    try:
        max_connections = int(input('Maximum number of connections: '))
    except ValueError:
        print('Max connections requires a number.')

        return

    save_yn = input('Save to file? (y/n): ')
    if save_yn not in 'yn':
        print("Must provide 'y' or 'n' for save to file")

        return

    summary, results = generate_sequences(fragments, max_connections, to_csv=save_yn)
    print("\nInput fragments: '{}'".format("', '".join(fragments)))
    print(f'Maximum connections: {max_connections}')
    print(summary)
    print(results)

    return

if __name__ == "__main__":
    main()
