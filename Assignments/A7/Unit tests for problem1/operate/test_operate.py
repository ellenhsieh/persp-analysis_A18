#test_operate.py
import pytest
import operate as op

def test_operate():

    with pytest.raises(TypeError) as excinfo:
        op.operate(1, 2, 34)
    assert excinfo.value.args[0] == "oper must be a string"
    assert op.operate(3, 4, '+') == 7, "Unexpected value for operator +"
    assert op.operate(10, 1, '-') == 9, "Unexpected value for operator -"
    assert op.operate(5, 6, '*') == 30, "Unexpected value for operator *"
    assert op.operate(9, 3, '/') == 3, "Unexpected value for operator /"
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(5, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        op.operate(7, 8, '**')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"


