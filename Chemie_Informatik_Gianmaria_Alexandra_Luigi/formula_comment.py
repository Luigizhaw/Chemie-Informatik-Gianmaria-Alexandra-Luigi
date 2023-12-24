import Data
info = Data.info
for index, element in enumerate(info):
    element['atomic_number'] = index

class Formula:
    """
    Represents a chemical formula and provides various operations on it.

    Attributes:
    - __formula (dict): Dictionary representation of the chemical formula.

    Methods:
    - symbol(element): Returns the symbol of the given element.
    - atomicNumber(element): Returns the atomic number of the given element.
    - addElement(formula, element, count): Adds an element with a count to the formula.
    - formulaFromList(pair_list): Generates a formula from a list of element-count pairs.
    - parseFormula(formula_string): Parses a formula string and returns a formula dictionary.
    - numAtoms(element): Returns the count of a specific element in the formula.
    - printPair(element, count): Returns a formatted string for a pair of element and count.
    - printFormula(formula): Returns a formatted string for the entire formula.
    - __str__(): Returns a formatted string representation of the formula.
    - hasElement(element): Checks if the formula contains a specific element.
    - mass(info): Returns the mass of the formula.
    - exactMass(info): Returns the exact mass of the formula.
    - containsFormula(other_formula): Checks if the formula contains another formula.
    - addFormula(other_formula): Adds another formula to the current formula.
    """
    
    def __init__(self, data):
        """
        Initializes a Formula instance.

        Parameters:
        - data (str/list/dict): Input data to initialize the formula.

        Raises:
        - ValueError: If an invalid input type is provided.
        """
        self.info = data

        if isinstance(data, str):
            self.__formula = self.parseFormula(data)
        elif isinstance(data, list):
            self.__formula = self.formulaFromList(data)
        elif isinstance(data, dict):
            self.__formula = data
        else:
            raise ValueError("Invalid input type")
    
    # Excercise a)
    def symbol(self, element):
        if isinstance(element, int):
            fromSymbol = {element['atomic_number']: element['symbol'] for element in Data.info}
            return fromSymbol.get(element, None)
        else:
            return str(element)
    
    # Excercise b)
    def atomicNumber(self, element):
        """
        Adds an element with a count to the formula.

        Parameters:
        - formula (dict): Current formula.
        - element (str/int): Element symbol or atomic number.
        - count (int): Number of atoms.

        Returns:
        - dict: Updated formula.
        """
        
        if isinstance(element, str):
            element = element.capitalize()
            fromSymbol = {element['symbol']: element['atomic_number'] for element in Data.info}
            return fromSymbol.get(element, None)
        else:
            return element

    # Excercise c)
    def addElement(self, formula, element, count):
        atomic_number = self.atomicNumber(element)
        if count >= 0:
            if atomic_number in formula:
                formula[atomic_number] += count
            else:
                formula[atomic_number] = count
        return formula

    # Excercise d)
    def formulaFromList(self, pair_list):
        formula = {}
        for element, count in pair_list:
            formula = self.addElement(formula, element, count)
        return formula

    # Excercise e)
    def parseFormula(self, formula_string):
        """
        Parses a formula string and returns a formula dictionary.

        Parameters:
        - formula_string (str): Chemical formula string.

        Returns:
        - dict: Formula generated from the string.
        """
        
        formula = {}
        i = 0
        while i < len(formula_string):
            element = formula_string[i]
            i += 1
            if i < len(formula_string) and formula_string[i].islower():
                element += formula_string[i]
                i += 1
            count = ''
            while i < len(formula_string) and formula_string[i].isdigit():
                count += formula_string[i]
                i += 1
            count = int(count) if count else 1
            formula = self.addElement(formula, element, count)
        return formula

    # Excercise g)
    def numAtoms(self, element):
        """
        Returns the count of a specific element in the formula.

        Parameters:
        - element (int/str): Element (atomic number or symbol).

        Returns:
        - int: The count of the element in the formula.
        """
        
        atomic_number = self.atomicNumber(element)
        return self.__formula.get(atomic_number, 0)
    
    # Excercise h)
    def printPair(self, element, count):
        """
        Returns a formatted string for a pair of element and count.

        Parameters:
        - element (int/str): Element (atomic number or symbol).
        - count (int): Number of atoms.

        Returns:
        - str: Formatted string representing the pair.
        """
        
        atomic_symbol = self.symbol(element)
        if count > 1:
            return f"{atomic_symbol}{count}"
        elif count == 1:
            return atomic_symbol
        else:
            return ''    

    # Excercise i)
    def printFormula(self, formula):
        hill_chemistry_order = [
        'Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au',
        'B', 'Ba', 'Be', 'Bh', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Cn', 'Co', 'Cr', 'Cs', 'Cu', 'Db', 'Ds', 'Dy',
        'Er', 'Es', 'Eu', 'F', 'Fe', 'Fl', 'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'Hs', 'I', 'In', 'Ir', 'K', 'Kr',
        'La', 'Li', 'Lr', 'Lu', 'Lv', 'Mc', 'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Nh', 'Ni', 'No', 'Np', 'O', 'Og',
        'Os', 'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re', 'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se',
        'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'Ts', 'U', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr', 'X']
        sorted_elements = sorted(formula.items(), key=lambda x: (hill_chemistry_order.index(self.symbol(x[0])), x[0]))
         
        result = ''
        for element, count in sorted_elements:
            result += self.printPair(element, count)
        return result

    # Excercise j)    
    def __str__(self):
        return self.printFormula(self.__formula)
        
    def hasElement(self, element):
        """
        Checks if the formula contains a specific element.

        Parameters:
        - element (int/str): Element (atomic number or symbol).

        Returns:
        - bool: True if the element is present, False otherwise.
        """
        
        return self.numAtoms(element) > 0

    # Excercise k)
    # def mass(self, info):
    #     """
    #     Returns the mass of the formula.

    #     Parameters:
    #     - info (list): List of element information dictionaries.

    #     Returns:
    #     - float/str: Mass of the formula or 'Unknown Element' if not found.
    #     """
        
    #     for element in info:
    #         if element['atomic_number'] == self.atomic_number:
    #             return element['mass'] + self.implicit_hydrogens
    #     return 'Unknown Element'
    def mass(self, info):
        """
        Returns the mass of the formula.

        Parameters:
        - info (list): List of element information dictionaries.

        Returns:
        - float/str: Mass of the formula or 'Unknown Element' if not found.
        """
    
        total_mass = 0
        for atomic_number, count in self.__formula.items():
            element = next((elem for elem in info if elem['atomic_number'] == atomic_number), None)
            if element:
                total_mass += element['mass'] * count
            else:
                return 'Unknown Element'
        return total_mass
    
    def exactMass(self, info):
        """
        Returns the exact mass of the formula.

        Parameters:
        - info (list): List of element information dictionaries.

        Returns:
        - float/str: Exact mass of the formula or 'Unknown Element' if not found.
        """
        
        for element in info:
            if element['atomic_number'] == self.atomic_number:
                return element['exactMass'] + self.implicit_hydrogens
        return 'Unknown Element'

    # Excercise m)    
    def containsFormula(self, other_formula):
        """
        Checks if the formula contains another formula.

        Parameters:
        - other_formula (Formula/str): Another formula to check for inclusion.

        Returns:
        - bool: True if the formula contains the other formula, False otherwise.
        """
        
        if isinstance(other_formula, Formula):
            other_formula = other_formula.__formula
        elif isinstance(other_formula, str):
            other_formula = self.parseFormula(other_formula)

        for atomic_number, count in other_formula.items():
            if self.__formula.get(atomic_number, 0) < count:
                return False
        return True

    # Exercise n)
    def addFormula(self, other_formula):
        """
        Adds another formula to the current formula.

        Parameters:
        - other_formula (Formula/str): Another formula to add.

        Returns:
        - dict: Updated formula.
        """
        
        if isinstance(other_formula, Formula):
            other_formula = other_formula.__formula
        elif isinstance(other_formula, str):
            other_formula = self.parseFormula(other_formula)

        for atomic_number, count in other_formula.items():
            self.__formula[atomic_number] = self.__formula.get(atomic_number, 0) + count
        return self.__formula
