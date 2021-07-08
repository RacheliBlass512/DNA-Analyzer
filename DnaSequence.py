NUCLEOTIDES = 'ACTGactg'


class DnaSequence:
    def __init__(self, string):
        valid_characters = [i if i in NUCLEOTIDES else '' for i in string]
        valid_string = ''.join(valid_characters)
        if valid_string != string: print('the string was given is not vaild, the new string is: ', valid_string)
        self.string = valid_string

    def insert(self, nucleotide_val, index):
        try:
            self.string = self.string[:index] + nucleotide_val + self.string[index + 1:]
        except IndexError:
            print("can't do this insert")

    def assignment(self, dna_instance):
        if isinstance(dna_instance, str):
            self.string = dna_instance
        else:
            self.string = dna_instance.string

    def __str__(self):
        return self.string

    def __eq__(self, other):
        return self.string.upper() == other.string.upper()

    def __ne__(self, other):
        return self.string.upper() != other.string.upper()

    def __getitem__(self, item):
        return self.string[item]

    def __len__(self):
        return len(self.string)

    def __add__(self, other):
        return self.string+ other.string
