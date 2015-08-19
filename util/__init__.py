import os
from config import load_config

config = load_config()
datasets_dir = config['datafiles']['directory']
datadir = os.path.join(datasets_dir,'mnist/')

version = "v0.1"
