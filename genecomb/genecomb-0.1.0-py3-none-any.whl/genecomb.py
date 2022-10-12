from operator import ge
import re


class SequenceLengthMismatchException(Exception):
    """Exception for sequence lengths mismatching"""


class GeneComb:
    """Class for performing sequence analysis

    :param seq: Nucleotide sequence of the gene
    :type seq: str
    :param header: Header/ Description for the seq. Used for FASTA formatting
    :type header: str
    """

    def __init__(self, seq="", header=""):
        self.seq = seq.upper()
        self.header = header

    amino_acid_lookup = {
        "UUU": "F",
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "UAU": "Y",
        "UAC": "Y",
        "UAA": "STOP",
        "UAG": "STOP",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "UGU": "C",
        "UGC": "C",
        "UGA": "STOP",
        "UGG": "W",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGU": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }

    def base_counter(self):
        """This function returns count of all bases in a sequence as a dictionary
        Ex: ACGGGTAC -> {'A': 2, 'C': 2, 'G': 3, 'T': 1, 'X':0}

        :return: The count of all bases as a dictionary
        :rtype: dict
        """
        base_count = {"A": 0, "C": 0, "G": 0, "T": 0, "X": 0}

        for i in self.seq:
            if i == "A":
                base_count["A"] += 1
            elif i == "G":
                base_count["G"] += 1
            elif i == "C":
                base_count["C"] += 1
            elif i == "T":
                base_count["T"] += 1
            else:
                base_count["X"] += 1

        return base_count

    def gc_content(self):
        """This function returns the GC content of a sequence.
        Ex: If the sequence is 100 bases long and you have 20 C’s and 5 G’s, your GC content is 25%

        :raise ZeroDivisionError: If sequence is empty
        :return: the GC content of the GeneComb sequence
        :rtype: float
        """
        base_dict = self.base_counter()
        base_count = len(self.seq)
        gc_count = base_dict.get("C") + base_dict.get("G")
        try:
            gc_content = gc_count / base_count
        except ZeroDivisionError:
            print(
                "Tried to divide by 0: Sequence is most likely empty. Returning 0 instead"
            )
            return 0
        return round(gc_content, 2)

    def non_nucleotide_counter(self):
        """This function parses a sequence and returns a list of the location of each
        non ACGT base and the length of unknown bases if they are consecutive
        Ex: ACNGGGNNNTAC -> [[2, 2],[6, 8]]

        :return: dictionary in the form of {position: length}
        :rtype: dict
        """
        non_nucleotides = []

        match = re.finditer(r"[^ATCG]{1,}", self.seq)
        for i in match:
            non_nucleotides.append([i.start(), i.end() - 1])
        return non_nucleotides

    def find_palindromes(self, removeOverlap=False):
        """
        This function parses the sequence and returns a list of palindromic nucleotide sequences
        within the seq.

        :return: a list of all the palindromes. Each entry in the list is another with the start position at index 0
            and the end position at index 1
        :rtype: list[list[start, end]]
        """

        palindromes = []
        seq = self.seq
        # recursive function called in find_palindromes()
        def expand(low, high):
            """
            Helper function for finding palindromes
            """

            # run till `s[low.high]` is not a palindrome
            while (
                low >= 0
                and high < len(seq)
                and compare_complimentary(seq[low], seq[high])
            ):
                # update pointers
                low = low - 1
                high = high + 1

            # seq must be length of 3 or longer
            if high - low > 1:
                palindromes.append([low + 1, high - 1])

        def remove_nested_palindromes():
            """
            Helper function to remove palindromes that overlap.
            """
            current_max = palindromes[0][1]
            remove_list = []
            for i in range(len(palindromes)):
                if palindromes[i][0] <= current_max:
                    remove_list.append(palindromes[i])
                else:
                    current_max = palindromes[i][1]
            for item in remove_list:
                palindromes.remove(item)
            return palindromes

        def compare_complimentary(a, b):
            """
            Helper function to compare if two bases are complementary
            Parameters:
                a (str): first base
                b (str): second base
            Returns:
                Returns True if a and b are complimentary
            """
            if a == "A":
                return b == "T"
            elif a == "T":
                return b == "A"
            elif a == "C":
                return b == "G"
            elif a == "G":
                return b == "C"
            else:
                return False

        for i in range(len(seq)):

            # odd length strings
            expand(i, i)
            # even length strings
            expand(i, i + 1)

        # print all unique palindromic substrings
        if removeOverlap and len(palindromes) != 0:
            return remove_nested_palindromes()
        return palindromes

    def write_to_fasta_file(self, filepath, append=False, line_length=80):
        """
        Writes the sequence and header to a file in the FASTA format

        :param filepath: filepath for the file to write to
        :type filepath: str
        :param append: Option for appending to an existing file or overwriting. Defaults to false.
        :type append: bool
        :param line_length: Optional param for the length of the line when writing to file. Defaults to the FASTA standard of 80
        :type line_length: int
        """
        write_type = "w"
        if append:
            write_type = "a"
        with open(filepath, write_type) as file:
            file.write(self.header + "\n")
            for i in range(0, len(self.seq), line_length):
                file.write(self.seq[i : i + line_length] + "\n")
            file.write("\n")

    def get_rna_transcription(self):
        """Returns the transcribed sequence. Replaces all T's with U's

        :return: The corresponding RNA sequence
        :rtype: str
        """
        return self.seq.replace("T", "U")

    def get_reverse_compliment(self):
        """
        Returns the reverse complement

        :return: The reverse complement of the sequence
        :rtype: str
        """
        reverse = ""
        for c in reversed(self.seq):
            reverse += self.get_compliment(c)
        return reverse

    def translate_to_protein(self, start=0, end=-1):
        """
        Transcribes to RNA, then Translates to Protein with Amino Acid Bases. It will carry out the tranlsation from start to end;
        or until one of the bases are not a valid rna nucleotide base (A, C, G, U).

        :param start: Optional param to designate the starting point of the translation. Defaults to 0.
        :type start: int
        :param end: Option param to designate the ending point of the translation. Defaults to the end of the sequence.
        :type end: int
        :return: The protein sequence from start to end.
        :rtype: str
        """
        seq_rna = self.get_rna_transcription()
        seq_protein = ""
        if end == -1:
            end = len(seq_rna)
        for i in range(start, end, 3):
            nucleotides = seq_rna[i : i + 3]
            if len(nucleotides) == 3 and self.is_valid_rna_nucleotides(nucleotides):
                seq_protein += self.amino_acid_lookup[nucleotides]
            else:
                return seq_protein
        return seq_protein

    def get_compliment(self, character):
        """Returns the complimentary nucleotide. A and T are compliments of each other. C and G are also compliments of each other. If U is passed in as
        a character, then A will be returned.

        :param character: The nucleotide base to find a compliment for:
        :type character: str
        :return: Returns the compliment of the character base
        :rtype: str
        """
        if character == "A":
            return "T"
        elif character == "T":
            return "A"
        elif character == "C":
            return "G"
        elif character == "G":
            return "C"
        elif character == "U":
            return "A"
        else:
            return "X"

    def is_valid_rna_nucleotides(self, nucleotides):
        """Returns True if the bases in the sequence are all valid RNA bases. That is: A, C, G, U

        :return: True if the bases in the sequence are all valid RNA bases. That is: A, C, G, U
        :rtype: bool
        """
        for base in nucleotides:
            valid = base == "A" or base == "G" or base == "U" or base == "C"
            if not valid:
                return False
        return True


def count_point_mutations(gene_a, gene_b):
    """Counts the number of point mutations between two sequences of equal length

    :param gene_a: sequence A to be compared
    :type gene_a: str
    :param gene_b: sequence B to be compared
    :type gene_b: str
    :raise genecomb.SequenceLengthMismatchException: If sequences are of different length
    :return: The number of point mutations between two sequences of equal length
    :rtype: int
    """

    if len(gene_a) != len(gene_b):
        raise SequenceLengthMismatchException("Both genes must be the same length.")
    return sum(1 for a, b in zip(gene_a, gene_b) if a != b)


def read_fasta(filepath):
    """Reads a .fasta file and returns a list of GeneComb objects. Each object corresponding to each sequence in the file

    :param filepath: filepath to read from
    :type filepath: str
    :return: Either a single GeneComb object with the sequence in the file, or a list of GeneComb sequences if more than one sequence can be found in the file.
    :rtype: GeneComb or list[GeneComb]
    """
    genecomb_list = []
    current_genecomb = GeneComb()
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == ">":
                if len(genecomb_list) != 0:
                    current_genecomb = GeneComb()
                genecomb_list.append(current_genecomb)
                current_genecomb.header += line[:-1]
            else:
                current_genecomb.seq += line[:-1]
    if len(genecomb_list) == 1:
        return genecomb_list[0]
    elif len(genecomb_list) == 0:
        return GeneComb()
    else:
        return genecomb_list
