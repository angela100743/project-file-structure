from src.multiplication import perform_operation

def test_multiplication():
    # Assert
    assert perform_operation(1, 1) == 1
    assert perform_operation(10, 20) == 200
    assert perform_operation(55, 11) == 605
    