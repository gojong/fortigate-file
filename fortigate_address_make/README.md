## 사용방법

* fortigate address cli로 한번에 붙여넣기 할려고 만든 프로그램 입니다.
* 프로그램 실행후 load input File에 example.txt 을 선택 하고 run 버튼을 클릭 하시면 됩니다.
* 유효하지 않는 IP는 자동으로 삭제되며 정상적인 IP만 출력 됩니다.

해당 example.txt 에는 아래처럼 아이피를 입력하시면 됩니다.
```
1.1.1.1 255.255.255.0
2.2.2.2/30
6.6.6.6 2222
9.9.9.99 23232323.232323
2.2222.2
4214214123
```

결과물 

```
config firewall address
edit "1.1.1.1/24"
set type ipmask
set subnet 1.1.1.1/24
next

edit "2.2.2.2/30"
set type ipmask
set subnet 2.2.2.2/30
next
end
```
