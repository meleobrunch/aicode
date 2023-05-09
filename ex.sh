#!/bin/bash
#4일간의 데이터를 바탕으로 추출한다. 근데 헤더가 없다 그건 extract.py로 해결한다
grep '2023-04-29.*' minering1.csv > FirDay.csv
grep '2023-04-30.*' minering1.csv > SecDay.csv
