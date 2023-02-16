## Differential testing
- compares the differences in execution from one system version to the next when the inputs are the same
- Differential testing requires that two or more comparable systems be available to the tester 

## tox를 이용하여 test
- old model과 new model의 차이에 대해 test [`.py`](./ml_api/tests/differential_tests/)
    - prediction값이 사전에 정한 threshold 이상으로 차이가 나면 error
- `tox -e differential_tests -r`
    - differential test만 실행

```
(study) minsoo@minsoo:~/Workspace/ML-testing-monitoring/ml_api$ tox -e differential_tests -r
differential_tests: install_deps> pip install -r requirements/test_requirements.txt
differential_tests: commands[0]> pytest -s -vv -m differential tests/
========================================================================= test session starts ==========================================================================
platform linux -- Python 3.8.13, pytest-5.4.3, py-1.11.0, pluggy-0.13.1 -- /home/minsoo/Workspace/ML-testing-monitoring/ml_api/.tox/integration_tests/bin/python
cachedir: .tox/integration_tests/.pytest_cache
rootdir: /home/minsoo/Workspace/ML-testing-monitoring/ml_api, inifile: tox.ini
collected 8 items / 7 deselected / 1 selected                                                                                                                          

tests/differential_tests/test_back_to_back_models.py::test_model_prediction_differentials PASSED

================================= 1 passed, 7 deselected in 1.64s ==================================
  differential_tests: OK (24.31=setup[22.23]+cmd[2.08] seconds)
  congratulations :) (24.37 seconds)
```