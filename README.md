- Alerting
    - key aspects: notify, automate, triage
- monitoring system
    - processing & storage
    - visualization
    - alerting  
- 구글에서 발표한 key monitoring principles for ML: After Deployment (2017)
    - monitor model predictions
    - computational performance

## Prometheus
- metrics-based system
- event logs나 individual events를 저장하는데 적절하지 않다
- usernames 같이 high cardinality data를 모니터링하기에 적절하지 않다

### PromQL Expression Evaluation Types
- instant vector
- range vector
- scalar
- string

나중에 ML 프로젝트를 진행할 때, Grafana를 사용하기로 한다.