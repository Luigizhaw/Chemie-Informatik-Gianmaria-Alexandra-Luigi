import Data

info = Data.info

# Exercise a)
for index, element in enumerate(info):
    element['atomic_number'] = index

fromSymbol = {element['atomic_number']: element['symbol'] for element in info}

# Exercise b)
class Atom:
    """
    Represents an atom with its properties.

    Attributes:
    - atomic_number (int): The atomic number of the atom.
    - implicit_hydrogens (int): The number of implicit hydrogens.
    - charge (int): The charge of the atom.

    Methods:
    - mass(): Returns the mass of the atom.
    - exactMass(): Returns the exact mass of the atom.
    - __str__(): Returns a string representation of the atom.
    - symbol(): Returns the symbol of the atom.
    """
    # Excercise f)
    def __init__(self, atomic_number_or_symbol, implicit_hydrogens=0, charge=0):
        """
        Initializes an Atom instance.

        Parameters:
        - atomic_number_or_symbol (int/str): Atomic number (int) or element symbol (str).
        - implicit_hydrogens (int): Number of implicit hydrogens (default is 0).
        - charge (int): Charge of the atom (default is 0).

        Raises:
        - ValueError: If an invalid element symbol is provided.
        - TypeError: If an invalid input type is provided.
        """
        if isinstance(atomic_number_or_symbol, int):
            self.atomic_number = atomic_number_or_symbol
        elif isinstance(atomic_number_or_symbol, str):
           # Excercise g) 
            symbol_to_number = {symbol: number for number, symbol in fromSymbol.items()}
            self.atomic_number = symbol_to_number.get(atomic_number_or_symbol)
            if self.atomic_number is None:
                raise ValueError("Invalid element symbol provided")
        else:
            raise TypeError("Invalid input type. Provide an atomic number (int) or element symbol (str)")

        self.implicit_hydrogens = implicit_hydrogens
        self.charge = charge

    # Excercise d) - Add mass, exact mass
    def mass(self):
        """
        Initializes an Atom instance.

        Parameters:
        - atomic_number_or_symbol (int/str): Atomic number (int) or element symbol (str).
        - implicit_hydrogens (int): Number of implicit hydrogens (default is 0).
        - charge (int): Charge of the atom (default is 0).

        Raises:
        - ValueError: If an invalid element symbol is provided.
        - TypeError: If an invalid input type is provided.
        """
        for element in info:
            if element['atomic_number'] == self.atomic_number:
                return element['mass'] + self.implicit_hydrogens
        return 'Unknown Element'

    def exactMass(self):
        """
        Returns the exact mass of the atom.

        Returns:
        - float: The exact mass of the atom.
        - str: 'Unknown Element' if the element is not found in the database.
        """
        for element in info:
            if element['atomic_number'] == self.atomic_number:
                return element['exactMass'] + self.implicit_hydrogens
        return 'Unknown Element'

    # Excercise e)
    def __str__(self):
        """
        Returns a string representation of the atom.

        Returns:
        - str: String representation of the atom.
        """
        symbol = fromSymbol.get(self.atomic_number, 'Unknown')
        atom_str = symbol

        if self.implicit_hydrogens == 1:
            atom_str += 'H'
        if self.implicit_hydrogens > 1:
            atom_str += 'H' + str(self.implicit_hydrogens)

        if self.charge == 1: 
            atom_str += '+'
        if self.charge == -1:
            atom_str += '-'
        if self.charge > 1:
            atom_str += '+' + str(self.charge)
        if self.charge < -1:
            atom_str += str(self.charge)

        return atom_str

    def symbol(self):
        """
        Returns the symbol of the atom.

        Returns:
        - str: The symbol of the atom.
        """
        return fromSymbol.get(self.atomic_number, 'Unknown')

