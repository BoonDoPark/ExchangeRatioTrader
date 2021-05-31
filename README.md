# ExchangeRatioTrader
## Overview
해당 프로젝트는 **환율 정보를 조회 및 자동 거래**를 목표로 합니다. 
기술 조사 후 실현 가능성 여부에 따라 SNS 앱을 통한 **푸시 알림**, 
**백엔드 서버 프레임워크(Django)를 활용**하여 고객에게 *지속적인 서비스를 제공*하는 방향으로 진행될 예정입니다.

## Technical Stacks
### Module
* selenium
* matplotlib
* requests
  
### Framework
* PyQT

## Rule
### Class
Big-Camel Case
```python
class ExampleClass:
    ...
```

### Function
Snake Case
```python
def example_function():
    ...
```

### Field
Snake Case
```python
class ExampleClass:
    def __init__(self):
        self._example_field = None
```

## Functions
### 환율정보 조회
[>> detail..](./markdowns/00_recieve.md)
### 환율정보 시각화
[>> detail..](./markdowns/01_visualize.md)
### 자동 거래
[>> detail..](./markdowns/02_trade.md)