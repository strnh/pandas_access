import unittest
import patch
import pandas as pd
import numpy as np 
# target
from pandas_access import _extract_dtype 

class TestPandasAccess(unittest.TestCase):
    def test_extract_dtype_double(self):
        self.assertEqual(_extract_dtype('double'),np.float64)
    def test_extract_dtype_long(self):
        self.assertEqual(_extract_dtype('long'),'Int64')
    def test_extract_dtype_unknown(self):
        self.assertIsNone(_extract_dtype('unknown'))

if __name__=='__main__':
    unittest.main()
