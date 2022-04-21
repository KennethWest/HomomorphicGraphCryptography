from Graph import Graph
from Query import Query


def main():
    q = Query()
    g = Graph(5)
    g.visualize()
    g.encrypt_g2()
    g.visualize()
    g.visualize_without_labels()
    g.encrypt_g3()
    g.visualize()
    print(q.get_weight(g, 1, 2))
    print(q.get_path_weight(g, [0, 1, 2, 3]))
    print(q.get_hamiltonian_weight(g, [0, 1, 2, 3]))
    g.decrypt()
    g.visualize()


if __name__ == '__main__':
    main()
