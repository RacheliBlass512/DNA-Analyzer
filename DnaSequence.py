NUCLEOTIDES = 'ACTGactg'


class DnaSequence:
    def __init__(self, string):
        valid_charachtrs = [i if i in NUCLEOTIDES else '' for i in string]
        valid_string = ''.join(valid_charachtrs)
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
        return "DnaSequence. dna_string: " + self.string

    def __eq__(self, other):
        return self.string == other.string

    def __ne__(self, other):
        return self.string != other.string

    def __getitem__(self, item):
        return self.string[item]

    def __len__(self):
        return len(self.string)
