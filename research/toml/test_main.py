import toml

GLOBAL_CONFIG = {}

def load_toml():
    with open('config.toml', 'r') as toml_file:
        global GLOBAL_CONFIG 
        GLOBAL_CONFIG = toml.load(toml_file)

def calculate():
    x = 2
    my_dimensions = GLOBAL_CONFIG['parametes']
    res = x * my_dimensions['height'] * my_dimensions['width']
    return my_dimensions['name'], res

def printToml():
    params=GLOBAL_CONFIG["model"]["parameters"]
    print(params["epochs"])
    print(params["callback"])

if __name__=='__main__':
    load_toml()
    Location, area = calculate()
    print(f"The area of {Location} is {area}")
    printToml()
