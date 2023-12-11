# EverRoute_datahandle
EverRoute의 엑셀 데이터 분석 기능만을 추출하였습니다.

python 버전 3 이상입니다.

# 설명서
## 개요
```bash
EverRoute_datahandle.
│   .gitattributes
│   datahandler.py
│   example.py
│   README.md
│
├───parsed
│       exceldata_sheet0.csv
│       exceldata_sheet1.csv
│       exceldata_sheet2.csv
│
└───raw
        에버랜드데이터셋11.xlsx
        에버랜드데이터셋11_static.xlsx
```
    'datahandler.py'를 프로그램에 import하여 사용하며, 예제 'example.py'를 참고하시면 됩니다.
    datahandler는 parsed와 raw 안의 항목들에 종속적입니다.
    raw의 파일은 '슈팅코스트'->'슈팅고스트'로 수정하였고, 최종적으로 함수를 상수로 치환한 _static파일을 사용합니다.
    



## 실행
다음 순서대로 진행해주세요.
1. 필요 모듈 설치(가상 환경 권장드립니다.)
    ```shell
    #일괄 설치
    pip install -r req.txt

    #직접 설치
    pip install pandas
    pip install openpyxl
    ```
2. example.py 실행
    ```shell
    python example.py
    ```
---
## 결과
```txt
** 모든 단위는 분입니다 **
지정 기구 간 (티->썬) 이동시간:  16.0
'썬더폴스' 현재시각 대기시간:    40.0
'썬더폴스' 월 10AM 대기시간:     30.0
모든 기구 기본 탑승 소요시간:    5.0
```
예제의 함수 호출과 결과를 확인하고, 응용하여 활용 바랍니다.!