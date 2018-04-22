'''Dictionary to store the molecular weight of amino acids in Dalton. Data from
https://www.promega.com/~/media/files/resources/technical%20references/
amino%20acid%20abbreviations%20and%20molecular%20weights.pdf'''
amino_acid_weights = {
                'A':89, 'R':174, 'N':132, 'D':133, 'B':133, 'C':121, 'Q':146, 'E':147, 'Z':147, 'G':75, 'H':155,
                'I':131, 'L':131, 'K':146, 'M':149, 'F':165, 'P':115, 'S':105, 'T':119, 'W':204, 'Y':181, 'V':117}

kyte_and_doolittle = {
                'R':-4.5, 'K':-3.9, 'N':-3.5, 'D':-3.5, 'Q':-3.5, 'E':-3.5, 'H':-3.2, 'P':-1.6, 'Y':-1.3, 'W':-0.9,
                'S':-0.8, 'T':-0.7, 'G':-0.4, 'A':1.8, 'M':1.9, 'C':2.5, 'F':2.8, 'L':3.8, 'V':4.2, 'I':4.5}

eisenberg_consensus = {
                'R':-2.5, 'K':-1.5, 'N':-0.78, 'D':-0.9, 'Q':-0.85, 'E':-0.74, 'H':-0.4, 'P':0.12, 'Y':0.26, 'W':0.81,
                'S':-0.18, 'T':-0.05, 'G':0.48, 'A':0.62, 'M':0.64, 'C':0.29, 'F':1.2, 'L':1.1, 'V':1.1, 'I':1.4}
