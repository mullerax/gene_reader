from Bio import SeqIO
import data

class FoundGeneClass():
    def __init__(self):
        self.name = 0
        self.mass = 0
        self.hyd_kd = 0
        self.hyd_ec = 0


def gene_find_func(path, mass_low, mass_high):
    gb_file = "sequence N9.gb"
    found_gene_array = []
    for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    # now do something with the record

        min_amino_acid_weight = mass_low
        max_amino_acid_weight = mass_high

        for feature in gb_record.features:
            if feature.type == "CDS":

                #print(feature.location.end - feature.location.start)
                gene_weight = 0
                hydrophob_kyte_doolitle = 0
                hydrophob_eisenberg_consensus = 0
                try:
                    for amino_acid in feature.qualifiers["translation"][0]:
                        gene_weight += data.amino_acid_weights[amino_acid]
                        hydrophob_kyte_doolitle += data.kyte_and_doolittle[amino_acid]
                        hydrophob_eisenberg_consensus += data.eisenberg_consensus[amino_acid]
                except:
                    pass
                if int(min_amino_acid_weight) < gene_weight < int(max_amino_acid_weight):
                    matching_gene = FoundGeneClass()
                    matching_gene.name = feature.qualifiers["locus_tag"][0]
                    matching_gene.mass = gene_weight
                    matching_gene.hyd_kd = hydrophob_kyte_doolitle
                    matching_gene.hyd_ec = hydrophob_eisenberg_consensus
                    # print(feature.qualifiers["locus_tag"][0])
                    # print("Gene weight: %f" % gene_weight)
                    # print("Hydrophobicity from kyte and doolittle scale: %f" % hydrophob_kyte_doolitle)
                    # print("Hydrophobicity from eisenberg consensus scale %f" %hydrophob_eisenberg_consensus)
                    found_gene_array.append(matching_gene)
    return found_gene_array



def write_results(result_array):
    result_string = ""
    for gene in result_array:
        result_string += "Name: "
        result_string += gene.name
        result_string += '\n'

        result_string += "Mass: "
        result_string += str(gene.mass)
        result_string += '\n'

        result_string += "Hydrophobicity (Kyte and Doolittle) "
        result_string += '\n'
        result_string += str(gene.hyd_kd)
        result_string += '\n'

        result_string += "Hydrophobicity (Eisenberg Consensus) "
        result_string += '\n'
        result_string += str(gene.hyd_ec)
        result_string += '\n'

        result_string += "----------------------------------------"
        result_string += '\n'
        result_string += '\n'

    return result_string


