## 1. Unit testing Input Data
- input value의 schema나 range(min, max 등)에 대한 test [`notebook`](./01_unit_testing_input_values.ipynb`)
- python 기본 라이브러리 `unittest` 사용

## 2. Unit testing Data Engineering Code
- data processing (scaler 등등)에 관련한 test [`notebook`](./02_unit_testing_data_engineering.ipynb)
    - data 관련한 처리가 원하는 대로 이루어졌는지? 수치적인 test 등등
- test 코드의 좋은 점 중 하나는 우리가 `test_`로 작성한 부분과 직접적인 부분 이외에도 에러가 있는 것을 발견할 수 있다.

## 3. Unit testing model quality
- model의 성능에 대한 test [`notebook`](./03_unit_testing_model_quality.ipynb)
    - simple benchmark model보다 좋은 성능을 보여주는지?
    - 이전에 개발한 model보다 좋은 성능을 보여주는지? 등등

## 4. Unit testing model config
-  model config에 대한 test [`notebook`](./04_unit_testing_model_config.ipynb)
    - 적절한 config가 들어갔는지? 등등