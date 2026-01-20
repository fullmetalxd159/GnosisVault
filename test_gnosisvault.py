# test_gnosisvault.py
"""
Tests for GnosisVault module.
"""

import unittest
from gnosisvault import GnosisVault

class TestGnosisVault(unittest.TestCase):
    """Test cases for GnosisVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GnosisVault()
        self.assertIsInstance(instance, GnosisVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GnosisVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
