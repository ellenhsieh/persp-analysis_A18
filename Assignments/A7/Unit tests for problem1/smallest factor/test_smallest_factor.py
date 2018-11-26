#test_smallest_factor.py
import smallest_factor as sf

def test_smallest_factor():
    
    assert sf.smallest_factor(100) == 2, "Incorrect answer"
    assert sf.smallest_factor(3) == 3, "Incorrect answer"
    assert sf.smallest_factor(27) == 3, "Incorrect answer"
    assert sf.smallest_factor(169) == 13, "Incorrect answer"



