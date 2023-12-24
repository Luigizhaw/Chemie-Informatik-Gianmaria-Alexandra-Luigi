
import Data

import Done2
 
from Done2 import Atom

info = Data.info
info = Done2.info
   
#Molecules
class Molecule:
    def __init__(self, atoms, edges):
        self.mol = {}
        for atom in atoms:
            self.mol[atoms.index(atom)] = (atom, {})

        for edge in edges:
            node1, node2, bond = edge
            self.mol[node1][1][node2] = bond
            self.mol[node2][1][node1] = bond

#c) The "order" of a graph is the number of nodes it has.
    def order(self):
       return len(self.mol)

#d) The "size" of a graph is the number of edges it has. Atention: Make sure you count every edge only once even though edges appear twice in a molecule's adjacency representation.
    def edge(self):
        edge_count = 0
        for node, neighbors in self.mol.items():
            edge_count += len(neighbors[1])
        return edge_count // 2  # Considering edges appear twice in adjacency representation

#e) The "degree of a node" describes the number of neighbors it has.
    def degree(self, node):
        return len(self.mol[node][1])

#f) degree 0. Implement, true if the node has no neighbors
    def isIsolate(self, node):
        return self.degree(node) == 0

#g) degree 1. Implement, true if the node has no neighbors
    def isTerminal(self, node):
        return self.degree(node) == 1
    
# #Molar mass
#     def mass(self, info):
#         total_mass = 0
#         for _, (atom, _) in self.mol.items():
#             total_mass += round(atom.mass(info), 3)  # Runde auf 3 Dezimalstellen
#         return round(total_mass, 3)  # Runde das Endergebnis der Gesamtmasse

# # Exact molar mass
#     def exactMass(self, info):
#         total_exact_mass = 0
#         for _, (atom, _) in self.mol.items():
#             total_exact_mass += round(atom.exactMass(info), 3)  # Runde auf 3 Dezimalstellen
#         return round(total_exact_mass, 3)  # Runde das Endergebnis der Gesamtmasse

#h) Molar mass
    def mass(self, info):
        total_mass = 0
        for _, (atom, _) in self.mol.items():
            total_mass += atom.mass(info)
        return total_mass

# Exact moral mass
    def exactMass(self, info):
        total_exact_mass = 0
        for _, (atom, _) in self.mol.items():
            total_exact_mass += atom.exactMass(info)
        return total_exact_mass

#i) Molecular formula
    def formula(self):
        formula_dict = {}
        for _, (atom, _) in self.mol.items():
            atom_formula = atom.formula()
            for element, count in atom_formula.items():
                if element in formula_dict:
                    formula_dict[element] += count
                else:
                    formula_dict[element] = count
        return formula_dict
    


#test = Molecule([Atom("C",3),Atom("C",2),Atom("O",1)],[(0,1,1),(1,2,1)])

tyrosineHCl = Molecule([ Atom("N",3,1),   #0
                             Atom("C",1),     #1
                             Atom("C"),       #2
                             Atom("O"),       #3
                             Atom("O",1),     #4
                             Atom("C",2),     #5
                             Atom("C"),       #6
                             Atom("C",1),     #7
                             Atom("C",1),     #8
                             Atom("C"),       #9
                             Atom("C",1),     #10
                             Atom("C",1),     #11
                             Atom("O",1),     #12
                             Atom("Cl",0,-1)],#13
                           [ (0,1,1),
                             (1,2,1),
                             (1,5,1),
                             (2,3,2),
                             (2,4,1),
                             (5,6,1),
                             (6,7,1),
                             (6,11,2),
                             (7,8,2),
                             (8,9,1),
                             (9,10,2),
                             (9,12,1),
                             (10,11,1) ]
                             )
print(tyrosineHCl.exactMass(info))

#    Its order is 14.
#    Its size is 13.
#    Its mass is 217.694.
#    Its exact mass is 217.050570924.
#    Its formula is C9H12ClNO3.
#    Its terminal nodes are nodes 0, 3, 4, and 12.
#    It hase only once isolte node: Node 13.
#    Node 13 is connected to no other node (it is isolate after all),
#    but all other nodes are connected.