"""TDD tests for AI4I 2020 project - Machine Learning tests"""
import pytest
import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


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


def test_train_test_split_works():
    """Test that dataset can be split into train and test sets"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    assert len(X_train) > 0, "Training set should have samples"
    assert len(X_test) > 0, "Test set should have samples"
    assert len(X_train) + len(X_test) == len(X), "Train + Test should equal total"


def test_logistic_regression_model_trainable():
    """Test that Logistic Regression model can be trained and evaluated"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    assert 0 <= accuracy <= 1, "Accuracy should be between 0 and 1"
    assert accuracy > 0.5, "Model should perform better than random (for this synthetic dataset)"


def test_random_forest_model_trainable():
    """Test that Random Forest model can be trained and evaluated"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    assert 0 <= accuracy <= 1, "Accuracy should be between 0 and 1"
    assert accuracy > 0.5, "Model should perform better than random"


def test_feature_importance_available():
    """Test that feature importance can be extracted from tree-based models"""
    df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    # Check that feature importance is available
    importances = model.feature_importances_
    assert len(importances) == 5, "Should have 5 feature importances"
    assert all(imp >= 0 for imp in importances), "Feature importances should be non-negative"