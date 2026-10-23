# AI4I 2020 Industrial Machine Fault Prediction using TDD
"""TDD-based analysis project for AI4I 2020 dataset"""

import os
import sys


def init_project():
    """Initialize project by creating necessary directories"""
    for d in ['data', 'models', 'reports', 'tests']:
        os.makedirs(d, exist_ok=True)
    print("AI4I 2020 TDD Project initialized")


# Ensure directories exist on import
init_project()