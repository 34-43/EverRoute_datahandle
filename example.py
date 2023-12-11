from datahandler import *
from datetime import datetime

dh = datahandler()

dh.update() # raw를 통해 parsed 파일 갱신. 생략해도 됩니다.
dh.use_route(2) # 1 또는 2. 이동시간 시트 지정. 2로 사용합시다.

기구리스트 = dh.key_list
지점_간_이동시간 = dh.get_route_time('티익스프레스','썬더폴스')
기구의_현시점_대기시간 = dh.get_await_time('썬더폴스')
기구의_지정_대기시간 = dh.get_await_time('썬더폴스',datetime(2023,11,22,10,0,0))
탑승시간_더미값 = dh.get_ride_time('썬더폴스')

print(', '.join(기구리스트))
print("** 모든 단위는 분입니다 **")
print("지정 기구 간 (티->썬) 이동시간:\t", 지점_간_이동시간)
print("'썬더폴스' 현재시각 대기시간:\t", 기구의_현시점_대기시간)
print("'썬더폴스' 월 10AM 대기시간:\t", 기구의_지정_대기시간)
print("모든 기구 기본 탑승 소요시간:\t", 탑승시간_더미값)
