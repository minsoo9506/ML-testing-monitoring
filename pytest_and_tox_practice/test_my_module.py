from pytest_and_tox_practice.my_module import square
import pytest

# @pytest.fixture 이용
@pytest.fixture
def input_value():
    return 4

def test_square_gives_correct_value(input_value):
    x = square(input_value)
    assert x == 16

# conftest.py를 이용
# conftest.py에 fixture로 만들어서 사용할 수도 있다
def test_square_gives_correct_value_with_conftest(use_conftest):
    x = square(use_conftest)
    assert x == 4

# @pytest.mark.parametrize 이용
# list에 있는 값들을 input으로 넣어서 확인가능
# test결과에도 각각 확인해서 결과가 나온다
@pytest.mark.parametrize('inputs', [2, 3, 4])
def test_square_return_value_type_is_int(inputs):
    x = square(inputs)
    assert isinstance(x, int)