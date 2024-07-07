import os.path as op
from pathlib import Path

FILE_ROOT = Path(__file__).parent.parent
with open(op.join(FILE_ROOT, 'VERSION')) as f:
    __version__ = f.read()