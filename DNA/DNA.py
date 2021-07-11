from DNA.DnaSequence import DnaSequence


class DNA:
    id_counter = 0

    def __init__(self, sequence, name):
        self.sequence = DnaSequence(sequence)
        self.id = DNA.id_counter
        self.name = name
        DNA.id_counter += 1

    def __str__(self):
        return 'sequence: ' + str(self.sequence) + '\tid: ' + str(self.id) + '\tname: ' + self.name

    def get_sequence(self):
        return self.sequence

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_sequence(self, new_sequence):
        self.sequence.set_string(new_sequence)
