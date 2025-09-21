
### FILE: src/level_loader.py
"""
Level loader: read JSON or CSV files describing levels.
For now, provide a simple JSON level format and a loader placeholder.
"""
import json
from objects import Block
from traps import Fire
from config import TILE_SIZE
from utils import load_block


def load_level_from_json(path):
    """Return lists: blocks, traps, meta
    JSON format example:
    {
      "blocks": [[x_index, y_index], ...],
      "fires": [[x_index, y_index], ...],
      "meta": {"background": "Pink.png"}
    }
    Coordinates are grid indices multiplied by TILE_SIZE.
    """
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[WARN] Failed to load level {path}: {e}")
        return [], [], { }

    blocks = []
    traps = []
    meta = data.get('meta', {})

    block_image = load_block(TILE_SIZE)

    for b in data.get('blocks', []):
        x, y = b
        blocks.append(Block(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, block_image))

    for fpos in data.get('fires', []):
        x, y = fpos
        traps.append(Fire(int(x * TILE_SIZE + TILE_SIZE/4), int(y * TILE_SIZE - TILE_SIZE/2), 16, 32))

    return blocks, traps, meta
