from Bio.SeqUtils import ProtParam
from argparse import ArgumentParser
import pandas as pd

def compute_aa_composition(peptide:str) -> dict: #Defines the type of return (-> dict)
    """
        Compute the amino acid composition for a peptide sequence 
        and returns a dictionary containing the percent of each 
        amino acid.

        Args:

        - peptide (str): sequence of the peptide (one letter code). 

        Returns: 

        - aa_composition (dict): dictionary of amino acid composition. 

        """
    protein_analysis = ProtParam.ProteinAnalysis(peptide)
    return protein_analysis.get_amino_acids_percent()

def preprocess_datasets(positive_peptide_file:str, negative_peptide_file:str, output_file='data/processed/train.csv') -> None:
    """
    Preprocess the raw peptide files and produces a CSV file containing
    the amino acid compositions. 

    Args:

    - positive_peptide_file (str): file containing peptides that have anticancer activity.
    - negative_peptide_file (str): file containing peptides that have no anticancer activity. 

    Kwargs:

    - output_file (str): output CSV file.

    Returns: 

    - None.

    """
    rows = []
    for line in open(positive_peptide_file):
        peptide = line.strip('\n')
        aa_composition = compute_aa_composition(peptide)
        aa_composition['activity'] = 1
        rows.append(aa_composition)
    
    for line in open(negative_peptide_file):
        peptide = line.strip('\n')
        aa_composition = compute_aa_composition(peptide)
        aa_composition['activity'] = 0
        rows.append(aa_composition)

    df_processed = pd.DataFrame(rows)
    df_processed.to_csv(output_file, index=False)


def main():

    argument_parser = ArgumentParser()
    argument_parser.add_argument('input_directory', help='directory containing the input files')
    argument_parser.add_argument('output_directory', help='directory to save the preprocessed peptide data')
    arguments = argument_parser.parse_args()

    preprocess_datasets(f'{arguments.input_directory}/train_positive.txt', 
                        f'{arguments.input_directory}/train_negative.txt',
                        output_file=f'{arguments.output_directory}/train.csv'
                        )

    preprocess_datasets(f'{arguments.input_directory}/test_positive.txt', 
                        f'{arguments.input_directory}/test_negative.txt', 
                        output_file=f'{arguments.output_directory}/test.csv'
                        )


if __name__ == '__main__':
    main()