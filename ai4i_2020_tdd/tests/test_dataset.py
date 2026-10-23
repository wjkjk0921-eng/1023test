"""TDD tests for AI4I 2020 project - Dataset loading tests"""
import pytest
import sys
import os

def test_project_directory_exists():
    """Test that project directories are created"""
    assert os.path.isdir('ai4i_2020_tdd'), "Project directory should exist"


def test_init_module_importable():
    """Test that the init module can be imported"""
    sys.path.insert(0, '.')
    from ai4i_2020_tdd._init import init_project
    assert True


def test_ai4i_dataset_csv_exists():
    """Test that AI4I 2020 dataset CSV file exists"""
    # This test will fail initially - we'll create the dataset
    csv_path = 'ai4i_2020_tdd/data/ai4i_2020.csv'
    assert os.path.exists(csv_path), f"Dataset file should exist at {csv_path}"


def test_ai4i_dataset_has_required_columns():
    """Test that AI4I 2020 dataset has required columns"""
    import pandas as pd
    csv_path = 'ai4i_2020_tdd/data/ai4i_2020.csv'
    df = pd.read_csv(csv_path)
    # Expected columns for AI4I 2020 dataset
    required_cols = ['Air temperature [K]', 'Process temperature [K]', 
                     'Rotational speed [rpm]', 'Torque [Nm]', 
                     'Tool wear [min]', 'Machine failure']
    for col in required_cols:
        assert col in df.columns, f"Column '{col}' should exist in dataset"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])