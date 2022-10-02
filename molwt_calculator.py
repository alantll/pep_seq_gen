from molwts import molwts

def calc_molwt(sequence):
    """
    Calculate mass of peptide.
    :param sequence (str): Peptide sequence.
    :return: molecular weight of peptide.
    """
    # Add 19 amu for C-terminal -OH, N-terminal -H, and H+
    mwt = 19.01784116688
    # Iterate though residues and sum masses
    for residue in sequence:
        mwt += molwts[residue]

    return mwt

def main():
    sequence = input('Peptide sequence: ').upper()
    mwt = calc_molwt(sequence)
    print(sequence, mwt)

if __name__ == "__main__":
    main()