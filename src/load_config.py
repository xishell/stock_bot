import cfg_load
from dotenv import load_dotenv, find_dotenv

def load_cfg():
    load_dotenv(find_dotenv())
    base_cfg = cfg_load.load('./config.yaml')
    env_mapping = cfg_load.load('./env_mapping.yaml')
    cfg = base_cfg.apply_env(env_mapping)
    return dict(cfg)