class Query:

    def get_encrypted_weight(self, graph, v1, v2):
        mapped_v1 = self.retrieve_vertice(graph, v1)
        mapped_v2 = self.retrieve_vertice(graph, v2)
        edge_list = graph.get_edge_list()
        for edge in edge_list:
            if (mapped_v1 == edge[0] and mapped_v2 == edge[1]) or \
                    (mapped_v1 == edge[1] and mapped_v2 == edge[0]):
                return edge[2]
        return 0

    def get_weight(self, graph, v1, v2):
        keys = graph.get_keys()
        encrypted_weight = self.get_encrypted_weight(graph, v1, v2)
        for key in keys:
            if (key[0] == v1 and key[1] == v2) or (key[0] == v2 and key[1] == v1):
                if key[3] == 1:
                    encrypted_weight /= key[2]
                else:
                    encrypted_weight -= key[2]
        real_weight = encrypted_weight
        if real_weight < 2:
            return 0
        else:
            return real_weight

    def get_path_weight(self, graph, list_of_vertices):
        total_weight = 0
        for i in range(len(list_of_vertices) - 1):
            total_weight += self.get_weight(graph, list_of_vertices[i], list_of_vertices[i + 1])
        return total_weight

    def get_hamiltonian_weight(self, graph, list_of_vertices):
        total_weight = self.get_path_weight(graph, list_of_vertices)
        total_weight += self.get_weight(graph, list_of_vertices[-1], list_of_vertices[0])
        return total_weight

    def retrieve_vertice(self, graph, vertex):
        keys = graph.get_keys()
        for mapping in keys[-1]:
            if vertex == mapping[0]:
                return mapping[1]
        return 0
