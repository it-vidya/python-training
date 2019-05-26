import configparser
config = configparser.ConfigParser()
config.read('first.ini')
print(config.sections())
print(config["database"]["User"])
print(config["database"]["Compression"])
