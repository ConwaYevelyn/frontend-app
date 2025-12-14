# utils.py
from functools import wraps
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def asyncify(func):
    """Decorator to convert a function to run in an asynchronous context."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        import asyncio
        loop = asyncio.get_event_loop()
        return loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper

def load_env_file(filename):
    """Loads environment variables from a file."""
    if not os.path.exists(filename):
        logger.warning(f"Environment file {filename} does not exist.")
        return {}
    with open(filename, 'r') as f:
        env_vars = {}
        for line in f:
            line = line.strip().split('=', 1)
            if len(line) == 2:
                env_vars[line[0]] = line[1]
        return env_vars

def merge_dicts(*dicts):
    """Merges multiple dictionaries into a single dictionary."""
    result = {}
    for d in dicts:
        result.update(d)
    return result