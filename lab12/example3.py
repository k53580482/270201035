class DNA():
    def __init__(self, dna):
        self.dna = dna
    def count_nucleotides(self):
        self.a, self.t, self.g, self.c = 0, 0, 0, 0
        for i in self.dna :
            if i == "a" :
                self.a += 1
            elif i == "t":
                self.t += 1
            elif i == "g" :
                self.g += 1
            elif i == "c" :
                self.c += 1
        print("""
        Adenin : {}
        Timin : {}
        Guanin : {}
        Citozin : {}
        """.format(self.a, self.t, self.g, self.c))

    def calculate_complement(self):
        self.opposite = []
        for i in self.dna:
            if i == "a":
                self.opposite.append("t")
            elif i == "t":
                self.opposite.append("a")
            elif i == "g":
                self.opposite.append("c")
            elif i == "c":
                self.opposite.append("g")

        self.res = "".join(self.opposite)
        print(self.res)

dna1 = DNA("acgtcagta")
dna1.count_nucleotides()
dna1.calculate_complement()
