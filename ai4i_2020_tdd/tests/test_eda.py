"""TDD tests for AI4I 2020 project - EDA tests"""
import pytest
import sys
import os
import pandas as pd

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
    csv_path = 'ai4i_2020_tdd/data/ai4i_2020.csv'
    assert os.path.exists(csv_path), f"Dataset file should exist at {csv_path}"


def test_ai4i_dataset_has_required_columns():
    """Test that AI4I 2020 dataset has required columns"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    required_cols = ['Air temperature [K]', 'Process temperature [K]', 
                     'Rotational speed [rpm]', 'Torque [Nm]', 
                     'Tool wear [min]', 'Machine failure']
    for col in required_cols:
        assert col in df.columns, f"Column '{col}' should exist in dataset"


def test_dataset_has_valid_shapes():
    """Test that dataset has valid shape (non-empty)"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    assert len(df) > 0, "Dataset should have at least one row"
    assert len(df.columns) == 6, "Dataset should have 6 columns"


def test_machine_failure_column_is_binary():
    """Test that Machine failure column contains only 0 and 1"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    unique_values = df['Machine failure'].unique()
    assert set(unique_values).issubset({0, 1}), \
        f"Machine failure should be binary (0/1), got {unique_values}"


def test_basic_statistics_exist():
    """Test that basic statistics can be computed"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    stats = df.describe()
    assert stats is not None, "Should be able to compute basic statistics"
    # Dataset has 6 columns (5 features + 1 target), statistics should include numeric columns
    numeric_cols = stats.columns.difference(['Machine failure'])
    assert len(numeric_cols) > 0, "Should have numeric columns for statistics"