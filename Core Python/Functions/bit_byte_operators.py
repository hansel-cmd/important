# print(hex(0xdc143c &
#           0xff << 8))


# Quartz color
from typing import Any


quartz = (81, 65, 79)

def convert_rgb_to_hex(r, g, b):
    red = r << 16
    green = g << 8
    blue = b << 0
    return hex(red | green | blue)

# print(convert_rgb_to_hex(*quartz))

def convert_hex_to_rgb(num):
    if type(num) == str:
        hexadecimal = int(num, base=16)
    elif type(num) == int:
        hexadecimal = num

    r = (hexadecimal & (0xff << 16)) >> 16
    g = (hexadecimal & (0xff << 8)) >>  8
    b = hexadecimal & 0xff

    return r, g, b

# print(convert_hex_to_rgb(0x51414f))

class SlotGenerator:

    def __init__(self):
        self._mask = 0
    
    def __call__(self, *args, **kwds):
        id = 1 << self._mask
        self._mask += 1
        return id

def is_favorite(favorites, person):
    return favorites & person

def unfavorite(ppl, person):
    return ppl & ~person

def add_favorite(ppl, person):
    # Check if slot is taken
    if is_favorite(ppl, person):
        raise ValueError("Person is already in favorites.")

    return ppl | person

def is_cat_lover(cat_lovers, person):
    return True if cat_lovers & person else False

def is_cat_lover_and_dog_lover(cat_lovers, dog_lovers, person):
    return True if cat_lovers & person & dog_lovers else False

def get_dog_lovers_but_not_cat_lovers(dog_lovers, cat_lovers):
    return dog_lovers & ~cat_lovers

def get_only_either_dog_or_cat_lovers(dog_lovers, cat_lovers):
    return dog_lovers ^ cat_lovers

    
generator = SlotGenerator()

velvet = generator()
winter = generator()
karina = generator()
giselle = generator()
ningning = generator()
joohyun = generator()


print(velvet, winter, karina, giselle, ningning)

favorites = velvet | winter | karina | giselle | ningning
car_owners = winter | karina
cat_lovers = winter | karina | velvet | giselle | ningning
dog_lovers = ningning | giselle | joohyun

favorites = unfavorite(favorites, velvet)
favorites = add_favorite(favorites, joohyun)

print(is_cat_lover(cat_lovers, ningning))
print(is_cat_lover_and_dog_lover(cat_lovers, dog_lovers, giselle))

print(bin(get_dog_lovers_but_not_cat_lovers(dog_lovers, cat_lovers)))
print(bin(get_only_either_dog_or_cat_lovers(dog_lovers, cat_lovers)))
