#%%
class Animal:
    kingdom = "animalia"

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def make_sound(self, sound):
        print(f"The {self.name} says {sound}")

class Cat(Animal):

    def __init__(self, kind, name, breed):
        super().__init__(kind, name)
        self.breed = breed

    def make_sound(self):
        print(f"The {self.name} says Meow")

# %%
tabby = Cat("cat", "Smelly Doobie", "barn")
# %%
print(tabby.name)
print(tabby.kind)
print(tabby.breed)
# %%
tabby.make_sound()
# %%
