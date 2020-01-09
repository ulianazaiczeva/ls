class LSystem:
    def __init__(self, definition):
        self.definition = definition
        self.name, p, self.axiom, *theorems = definition.strip().split('\n')
        self.p = int(angles)
        self.theorems = dict(map(lambda s: s.split(), theorems))
        self.evolution = 0
        self.lstring = ''

    def k(self):
        return 360 / self.p

    def start(self):
        self.evolution = 1
        self.lstring = self.axiom

    def evolve(self):
        r = []
        for ch in self.lstring:
            r.append(self.theorems.get(ch, ch))
        self.lstring = ''.join(r)
        self.evolution += 1

    def evolve_to(self, steps):
        for g in range(steps):
            self.evolve()

    def reset(self):
        self.start()
