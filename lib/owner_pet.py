class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name,pet_type,owner = None):
        
        # Checking Validity of Pet_type
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception(f"Invalid pet type: {pet_type}")
        
        self.name = name
        self.owner = owner
        self.all.append(self)
            

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)