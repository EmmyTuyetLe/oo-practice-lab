############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        #we save the list of foods what you cane make from this melon 
        self.pairings.append(pairing) 
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code #we are updating the code for the melons (nickname)

all_melon_objects =[]

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk.name)
    all_melon_objects.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas.name)
    all_melon_objects.append(cas)
    
    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren.name)
    all_melon_objects.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermlon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw.name)
    all_melon_objects.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:

        #print(f"Name: {melon.name}:\n Reportin code:{melon.code}\n First harvest in {melon.first_harvest}\n Color:{melon.color}\n Pairs well with " f"{' '.join(melon.pairings)}\n {melon.is_seedless}")
        print (f"{melon.name} pairs well with " f"{' '.join(melon.pairings)}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_code = {}
    for melon in melon_types:
        if melon not in melons_by_code:
            melons_by_code[melon.code] = melon.name
    print(melons_by_code)
    return melons_by_code


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by
    
    def is_sellable(self):
        
        return True if self.shape_rating>5 and self.color_rating>5 and self.harvested_from_field !=3 else False
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    all_melons = []
    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    all_melons.append(melon_1)
    all_melons.append(melon_2)
    all_melons.append(melon_3)
    all_melons.append(melon_4)
    all_melons.append(melon_5)
    all_melons.append(melon_6)
    all_melons.append(melon_7)
    all_melons.append(melon_8)
    all_melons.append(melon_9)


    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        print(f"{melon.name} is sellable.") if melon.is_sellable() == True else print(f"{melon.name} is not sellable.")        
    

melon_types = make_melon_types()
print_pairing_info(all_melon_objects)
melon_dict = make_melon_type_lookup(all_melon_objects)
make_melons(melon_dict)