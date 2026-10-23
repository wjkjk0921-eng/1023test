"""TDD tests for AI4I 2020 project - Initial setup tests"""
import pytest
import sys
import os

def test_project_directory_exists():
    """Test that project directories are created"""
    # Should pass after _init.py runs
    assert os.path.isdir('ai4i_2020_tdd'), "Project directory should exist"


def test_init_module_importable():
    """Test that the init module can be imported"""
    sys.path.insert(0, '.')
    from ai4i_2020_tdd._init import init_project
    # Just test that import works
    assert True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])