from formula_comment import Formula
import Data
info = Data.info

# Read the file and extract formulas
file_path = '/Users/derwaschbaer/Documents/GitHub/LSDPr/Chemie/Exercises/formulas.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    formulas = file.readlines()
formulas = [formula.strip() for formula in formulas]

# Create Formula instances for each formula in the file
formula_objects = [Formula(formula) for formula in formulas]

# Exercise 1: Summenformel und Molmasse des schwersten Moleküls
heaviest_molecule = max(formula_objects, key=lambda x: sum(x.numAtoms(element) for element in range(len(info))))
heaviest_formula = str(heaviest_molecule)
heaviest_mass = heaviest_molecule.mass(info)
print(f"Summenformel des schwersten Moleküls: {heaviest_formula}")
print(f"Molmasse des schwersten Moleküls: {heaviest_mass}")

# Exercise 2: Summenformel und Molmasse des leichtesten Moleküls
lightest_molecule = min(formula_objects, key=lambda x: sum(x.numAtoms(element) for element in range(len(info))))
lightest_formula = str(lightest_molecule)
lightest_mass = lightest_molecule.mass(info)
print(f"Summenformel des leichtesten Moleküls: {lightest_formula}")
print(f"Molmasse des leichtesten Moleküls: {lightest_mass}")

# Exercise 3: Summenformel und Molmasse des größten Moleküls (größte Anzahl Atome inklusive H-Atome)
max_atoms_molecule = max(formula_objects, key=lambda x: sum(x.numAtoms(element) for element in range(len(info))))
max_atoms_formula = str(max_atoms_molecule)
max_atoms_mass = max_atoms_molecule.mass(info)
print(f"Summenformel des Moleküls mit den meisten Atomen: {max_atoms_formula}")
print(f"Molmasse des Moleküls mit den meisten Atomen: {max_atoms_mass}")

# Exercise 4: Summenformel und Molmasse des kleinsten Moleküls (kleinste Anzahl Atome inklusive H-Atome)
min_atoms_molecule = min(formula_objects, key=lambda x: sum(x.numAtoms(element) for element in range(len(info))))
min_atoms_formula = str(min_atoms_molecule)
min_atoms_mass = min_atoms_molecule.mass(info)
print(f"Summenformel des Moleküls mit den wenigsten Atomen: {min_atoms_formula}")
print(f"Molmasse des Moleküls mit den wenigsten Atomen: {min_atoms_mass}")

# Exercise 5: Durchschnittliche Molmasse der Moleküle in der Datei
average_mass = sum([mol.mass(info) for mol in formula_objects]) / len(formula_objects)
print(f"Durchschnittliche Molmasse der Moleküle: {average_mass}")

# Exercise 6: Durchschnittliche Anzahl C-Atome der Moleküle in der Datei
c_atoms_count = sum([mol.numAtoms('C') for mol in formula_objects])
c_atoms_average = c_atoms_count / len(formula_objects)
print(f"Durchschnittliche Anzahl C-Atome der Moleküle: {c_atoms_average}")
