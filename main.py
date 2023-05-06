import re

def parse_config(config_file):
    with open(config_file, "r", encoding= "utf-8") as f:
        config = f.read()
    config = re.sub(r'//.*', '', config)
    config_dict = {}
    for line in config.split('\n'):
        if line.startswith('#'):
            continue
        if line.strip() == '':
            continue
        key, value = line.split('=')
        config_dict[key.strip()] = value.strip()
    return config_dict
