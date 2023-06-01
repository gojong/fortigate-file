# 설명
* FORTIGATE webfilter local rating을 cli에서 한번에 적용 할려고 만든 프로그램 입니다.

# 사용방법
*  해당 example.txt 에는 아래처럼 url 입력하시면 됩니다.
```
ttt.com
adc.ttd.kr
```
* 프로그램에서 example.txt 선택하고 Rating Number 에는 숫자 입력해주고 RUN 하시면 됩니다.
* 만들어진 fortigate_webfilter_CLI.txt 는 바탕화면에 있습니다. 

결과물
```
config webfilter ftgd-local-rating
    edit "ttt.com"
        set rating 140
        set status enable
    next
    edit "adc.ttd.kr"
        set rating 140
        set status enable
    next
end
```

# Rating Number 확인방법
```
fortigate web에서 Web Rating Overrides -> Create New -> 
아무 URL 작성후
Category and Sub-Category 필요한걸로 선택
저장

CLI에서 show webfilter ftgd-local-rating 입력하시면 해당위치의 rating이 보입니다.
```
