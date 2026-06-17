"""Put the scripts/ dir on sys.path so the BOM-pipeline modules import by name.

``bom_common`` is a plain sibling module (not an installed package), and the
pipeline scripts import it as ``from bom_common import ...`` relying on the
script's own directory being ``sys.path[0]`` when run directly. Tests run from
elsewhere, so add that directory explicitly here.
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
