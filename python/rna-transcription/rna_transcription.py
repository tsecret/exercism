def to_rna(dna_strand: str):
    d = {
      'G': 'C',
      'C': 'G',
      'T': 'A',
      'A': 'U'
    }

    return "".join([d[char] for char in dna_strand ])
