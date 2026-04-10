from functools import lru_cache
from random import choice


@lru_cache(maxsize=1)
def _load_user_agents() -> tuple:
    file_path = 'src/pinkerton/data/user-agents.txt'
    with open(file_path) as f:
        return tuple(line.strip() for line in f if line.strip())


def get_user_agent() -> str:
    return choice(_load_user_agents())
