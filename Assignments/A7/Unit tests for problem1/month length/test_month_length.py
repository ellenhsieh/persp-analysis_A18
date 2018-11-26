#test_month_length.py
import month_length as ml

def test_month_length():
    
    assert ml.month_length("jkisld") == None, "Not a correct input for month"
    assert ml.month_length("September") == 30, "Unexpected days for September"
    assert ml.month_length("March") == 31, "Unexpected days for March"
    assert ml.month_length("February") == 28, "Unexpected days for February not in leap year"
    assert ml.month_length("February", leap_year = True) == 29, "Unexpected days for February in leap year"



