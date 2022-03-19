# asserlang-charmaker 어쩔랭 문자 생성기

String을 받아 [어쩔랭](https://github.com/assertive-lang/asserlang)의 [아스키코드를 담는 변수](https://github.com/assertive-lang/asserlang#%EC%95%84%EC%8A%A4%ED%82%A4%EC%BD%94%EB%93%9C%EB%A5%BC-%EB%8B%B4%EB%8A%94-%EB%B3%80%EC%88%98)를 선언하고 출력하는 .astv 파일 생성 스크립트 입니다. 

저의 needs에 따라 light하게 만들었습니다.

## 환경

- python 3.9.7

- asserlang v1

# 사용법

```python
python ussalami.py [string] ...
```

> 예1) ./ussalemi.py 어쩔티비
>
> 예2) python ./ussalemi.py 어쩔티비 저쩔티비
>

스크립트와 동일한 path에 .astv 파일이 생성됩니다. 


# 생성된 .astv 실행 결과

> 예1)
```
어
쩔
티
비
```

> 예2)
```
어
쩔
티
비
저
쩔
티
비
```

