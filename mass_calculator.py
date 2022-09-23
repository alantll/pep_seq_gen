from aa_mass import aa_masses as aa

def calc_mass(seq):
    """
    Calculate mass of peptide.
    :param seq: Peptide sequence.
    :return: molecular weight of peptide.
    """
    # Add 19 amu for C-terminal -OH, N-terminal -H, and H+
    mass = 19.01784116688
    # Iterate though residues and sum masses
    for residue in seq:
        mass = mass + aa[residue]

    return mass

def main():
    sequence = input('Peptide sequence: ').upper()
    mass = calc_mass(sequence)
    print(sequence, mass)

if __name__ == "__main__":
    main()