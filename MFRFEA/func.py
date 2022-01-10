from gene import *
from random import sample

def crossover_mutate(parent1, parent2, pc=0.7, pm=0.2):
    result = []

    # lai ghép
    rc = np.random.random()
    if (rc < pc):
        t = sample(range(len(parent1.genes)), 2)
        t.sort()
        [t1, t2] = t
        child1 = parent1.genes.copy()
        child2 = parent2.genes.copy()

        child1[t1:t2] = parent2.genes[t1:t2]
        child2[t1:t2] = parent1.genes[t1:t2]
        len_gene = len(parent1.genes)

        for i in range(t1):
            while (child1[i] in child1[t1:t2]):
                child1[i] = parent1.genes[parent2.genes.index(child1[i])]

            while (child2[i] in child2[t1:t2]):
                child2[i] = parent2.genes[parent1.genes.index(child2[i])]

        for i in range(t2, len_gene):
            while (child1[i] in child1[t1:t2]):
                child1[i] = parent1.genes[parent2.genes.index(child1[i])]

            while (child2[i] in child2[t1:t2]):
                child2[i] = parent2.genes[parent1.genes.index(child2[i])]

        result += [Individual(child1), Individual(child2)]

    # Đột biến
    rm = np.random.random()
    if (rm < pm):
        child1 = mutate(parent1)
        child2 = mutate(parent2)
        result += [child1, child2]
    return result

def mutate(indiv):
    genes = indiv.genes
    a, b = sample(list(range(len(genes))), 2)

    # swap
    temp = genes[a]
    genes[a] = genes[b]
    genes[b] = temp
    return Individual(genes)

def evolution(pop, pc=0.7, pm=0.2, MAX_LEN=100):
    indivs_child = []
    while (len(indivs_child) < MAX_LEN / 2):
        try:
            parent1, parent2 = sample(pop.individuals, 2)
            indivs_child += crossover_mutate(parent1, parent2, pc, pm)
        except:
            print("individuals in population < 2")

    pop.add(indivs_child)
    pop.selection(MAX_LEN)