import pytest
import function_home_task as f

def test_format_text_positive():
    assert f.format_text("""“Don't let the noise of others'
    opinions drown out your
            own inner voice.”
                    Steve Jobs""") == """“Don't let the noise of others' opinions
drown out yourown inner voice.”Steve Jobs"""

def test_unpaired_number_positive():
    assert f.unpaired_number(1, 7) == [3, 5]

def test_write_line_positive():
    assert f.write_line(15, "horizontal", "$") == "$$$$$$$$$$$$$$$"

def test_max_number_positive():
    assert f.max_number(1, 3, 23, -14) == 23

def test_sum_numbers_positive():
    assert f.sum_numbers(3, 8) == 33

def test_prime_num_positive():
    assert f.prime_num(293) == True

def test_lucky_number_positive():
    assert f.lucky_number(123060) == True