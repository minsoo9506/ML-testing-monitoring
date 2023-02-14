## pytest
- 기본적인 사용법은 따로 익히길!
- `@pytest.fixture` [`.py`](./pytest_and_tox_practice/test_my_module.py)
    - test에서 반복적으로 사용할 값
- `@pytest.mark.parametrize` [`.py`](./pytest_and_tox_practice/test_my_module.py)
    - 여러 값들을 넣어서 test

## tox
- `tox.ini` 파일 생성 [`tox.ini`](./pytest_and_tox_practice/tox.ini)
  - `tox` 명령어를 치면 python 3.8 버전의 환경에서 `pytest`명령어를 진행한다. 아래와 같은 결과가 나온다.

```bash
(study) minsoo@minsoo:~/Workspace/ML-testing-monitoring/pytest_and_tox_practice$ tox
py38: install_deps> python -I -m pip install pytest
py38: commands[0]> pytest
============================ test session starts =============================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
cachedir: .tox/py38/.pytest_cache
rootdir: /home/minsoo/Workspace/ML-testing-monitoring
collected 5 items                                                            

test_my_module.py .....                                                [100%]

============================= 5 passed in 0.01s ==============================
  py38: OK (1.86=setup[1.69]+cmd[0.16] seconds)
  congratulations :) (1.91 seconds)
```

## Unit test
- preprocessing [`.py`](./gradient_boosting_model/tests/test_preprocess.py)
- config [`.py`](./gradient_boosting_model/tests/test_config.py)
- input validation [`.py`](./gradient_boosting_model/tests/test_input_validation.py)
- pipeline [`.py`](./gradient_boosting_model/tests/test_pipeline.py)
- predict [`.py`](./gradient_boosting_model/tests/test_predict.py)