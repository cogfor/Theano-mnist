import yaml

def load_config():
    with open('config.yaml', 'r') as configfile:
        config = yaml.load(configfile)
    print("loaded config")
    return config
