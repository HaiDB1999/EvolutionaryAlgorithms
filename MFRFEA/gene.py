import numpy as np

class Gene:  # gene
    #     __distances_table = {}
    def __init__(self, location):
        self.name = location[0]
        self.x_value = location[1]
        self.y_value = location[2]
        self.z_value = location[3]

    def get_distance_to(self, dest):
        x_origin, y_origin, z_origin = self.x_value, self.y_value, self.z_value
        x_dest, y_dest, z_dest = dest.x_value, dest.y_value, dest.z_value
        return ((x_dest - x_origin) ** 2 + (y_dest - y_origin) ** 2 + (z_dest - z_origin) ** 2) ** 0.5

    def get_gene(self):
        return (self.x_value, self.y_value, self.z_value)

    def get_name(self):
        return self.name

# cá thể
class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.__cost = 0
        self.name = [gene.get_name() for gene in genes]
        self.cost

    @property
    def cost(self):
        if (self.__cost == 0):
            return Energy_consumption_sensor(self)
            ######
        return self.__cost

    def get_individual(self):
        #######
        return [gene.get_gene() for gene in self.genes]

    def Energy_consumption_sensor(self):
        indiv_name = self.name
        E_max = 0
        (V_t, E_t) = decoding_network(G, relays_node, sensors_node, r, indiv_name)
        nodes_parent = [edge[0] for edge in E_t]
        nodes_child = [edge[1] for edge in E_t]
        for node in V_t[1:]:
            E_node = 0
            if (node in sensors_node):
                num = nodes_parent.count(node)
                E_node = num * e_elec + (num + 1) * e_da + E_distance(node, nodes_parent, nodes_child)
            elif (node in sensors_node):
                num = nodes_parent.count(node)
                E_node = num * (e_elec + e_da) + E_distance(node, E_t)

            E_max = max(E_node, E_max)
        return E_max


# Quần thể
class Population:
    def __init__(self, individuals):
        self.individuals = individuals
        self.__length = len(individuals)

    @property
    def length(self):
        self.__length = len(self.individuals)
        return self.__length

    def add(self, indivs):
        for indiv in indivs:
            self.individuals.append(indiv)

    def random_indivs(self, nums_indiv):
        genes = self.individuals[0].genes.copy()
        individuals = []
        for _ in range(nums_indiv):
            np.random.shuffle(genes)
            individuals.append(Individual(genes.copy()))
        self.add(individuals)

    def remove(self, indivs):
        for indiv in indivs:
            self.individuals.remove(indiv)

    def get_fittest(self):
        best_indiv = self.individuals[0]
        for indiv in self.individuals:
            if (best_indiv.cost > indiv.cost):
                best_indiv = indiv
        return best_indiv

    # Chọn lọc các thể
    def selection(self, max_len_indiv):
        if (len(self.individuals) <= max_len_indiv):
            pass
        else:
            individuals = self.individuals
            individuals.sort(key=lambda x: x.cost)
            self.remove(individuals[len(self.individuals):])