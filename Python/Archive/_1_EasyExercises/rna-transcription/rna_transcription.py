translation_table = str.maketrans("GCTA", "CGAU")

def to_rna(dna_strand):    
    return dna_strand.translate(translation_table)
