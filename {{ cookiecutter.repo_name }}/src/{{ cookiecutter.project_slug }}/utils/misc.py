import os
import logging
from typing import Union

import numpy as np
from datetime import datetime

try:
    import torch
    torch_availabe = True
except ImportError:
    torch_availabe = False


def int_or_str(x: str) -> Union[str, int]:
    """Function to cast to int or str.

    This is used to tackle precision which can be int (16, 32) or str (bf16)
    """
    try:
        return int(x)
    except ValueError:
        return x

def seed_all_rng(seed: int = None, deterministic: bool =False) -> None:
    """Set the random seed for the RNG in numpy, python and torch (if used).

    Args:
        seed (int): if None, will use a strong random seed.
        deterministic (bool): Whether to set the deterministic option for
            CUDNN backend, i.e., set `torch.backends.cudnn.deterministic`
            to True and `torch.backends.cudnn.benchmark` to False.
            Default: False.
    """
    if seed is None:
        seed = (
            os.getpid()
            + int(datetime.now().strftime("%S%f"))
            + int.from_bytes(os.urandom(2), "big")
        )
        logger = logging.getLogger(__name__)
        logger.info(f"Using a generated random seed {seed}")
    np.random.default_rng(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    else:
        torch.backends.cudnn.benchmark = True
