## Shadow deployment
- 이전까지의 test는 deploy이전의 단계였다면 이제 deploy단계에서 진행하는 것이다.
- 유저에게 들어나지 않고 내부적으로 test를 진행하는 것으로 이해할 수도 있다. (shadow!)
- 따라서 test를 하는 주제나 종류는 다양할 수 있다.

### Shadow Deployments at the application level
- 현재 model에게 가는 request와 동일한 request가 shadow model에도 간다.
- prediction이 저장되지만 유저에게 serve되지는 않는다.

## test 실행
- `docker-compose -f docker/docker-compose.test.yml up -d test_database`
    - test를 위해 db가 있는 container가 필요하다
- `tox -r`