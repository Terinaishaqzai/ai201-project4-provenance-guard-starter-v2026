#!/usr/bin/env python3
"""
Start Provenance Guard as if PyTorch were not installed. Capstone criterion 4.

    python run_without_torch.py

Everything else is the normal service. Any `import torch` raises
ModuleNotFoundError, which is what a machine without torch would do.
"""

import importlib.abc
import sys


class _BlockTorch(importlib.abc.MetaPathFinder):
    def find_spec(self, name, path, target=None):
        if name == "torch" or name.startswith("torch."):
            raise ModuleNotFoundError(f"No module named '{name}' (blocked by run_without_torch.py)")
        return None


sys.meta_path.insert(0, _BlockTorch())

import app  # noqa: E402

app.main()
