# asserlang-charmaker 어쩔랭 문자 생성기

String을 받아 [어쩔랭](https://github.com/assertive-lang/asserlang)의 [아스키코드를 담는 변수](https://github.com/assertive-lang/asserlang#%EC%95%84%EC%8A%A4%ED%82%A4%EC%BD%94%EB%93%9C%EB%A5%BC-%EB%8B%B4%EB%8A%94-%EB%B3%80%EC%88%98)를 선언하고 출력하는 .astv 파일 생성 스크립트 입니다. 

※ 스크립트로 생성된 어쩔랭 코드에 웃음이 많을 수 있으니 킹받음 주의!

## 테스트 환경

- python 3.9.7

- Asserlang Node.JS 구현체 v1

# 사용법

```python
python ussalami.py [string] ...
```

> 예1) $ python ./ussalemi.py 어쩔티비
>
> 예2) $ python ./ussalemi.py 아무것도못하죠? 모르죠? 열받죠? 때리고 싶죠?
>

스크립트와 동일한 path에 `ㅋㅌ루삥뽕.astv` 파일이 생성됩니다. 


# 생성된 .astv 코드 실행 결과

> 예1)
```
$ node dist/index.js examples/ㅋㅌ루삥뽕.astv
어~쩔~티~비
```

> 예2)
```
$ node dist/index.js examples/ㅋㅌ루삥뽕.astv
아~무~것~도~못~하~죠~?
모~르~죠~?
열~받~죠~?
때~리~고
싶~죠~?
```

