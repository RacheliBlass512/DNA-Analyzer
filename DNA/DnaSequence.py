NUCLEOTIDES = 'ACTGactg'


class DnaSequence:
    def __init__(self, string):
        valid_string = get_valid_string(string)
        self.string = valid_string

    def insert(self, nucleotide_val, index):
        if nucleotide_val in NUCLEOTIDES:
            try:
                self.string = self.string[:index] + nucleotide_val + self.string[index + 1:]
            except IndexError:
                print("can't do this insert")
        else:
            print("nut valid nucleotide")

    def assignment(self, dna_instance):
        if isinstance(dna_instance, str):
            self.string = get_valid_string(dna_instance)
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
        return self.string + other.string

    def set_string(self, string):
        self.string = get_valid_string(string)

    def get_string(self):
        return self.string


def get_valid_string(string):
    valid_characters = [i if i in NUCLEOTIDES else '' for i in string]
    valid_string = ''.join(valid_characters)
    if valid_string != string:
        print('the string was given is not valid, the new string is: ', valid_string)
    return valid_string
