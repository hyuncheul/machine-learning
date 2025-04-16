import pandas as pd

data = pd.read_csv('3.1.2.temp.csv', encoding='cp949')
data

# 날짜 앞의 \t 없애기
data['날짜'] = data['날짜'].str.replace('\t', '')
# 날짜 컬럼의 object 타입을 날짜형식(datetime)으로 변환하기
data['날짜'] = pd.to_datetime(data['날짜'])
data.info()
# 최고 기온만 날짜와 함께 저장하기
result = data.iloc[:, [0,4]]
result
import matplotlib.pyplot as plt

plt.plot(result['최고기온(℃)'])   # x축 날짜는 생략
# 내가 태어난 달에 해당하는 기온 데이터만 추출하기
month_result = result[result['날짜'].dt.month == 1]       # 자기가 태어난 달로 바꿔보세요
month_result
plt.plot(month_result['최고기온(℃)'])   # x축 날짜는 생략
# 내 생일에 해당하는 온도만 추출
birthday_result = result[(result['날짜'].dt.month == 1) & (result['날짜'].dt.day == 24)]
birthday_result
plt.plot(birthday_result['최고기온(℃)'])   # x축 날짜는 생략
# 내 생일의 최저 기온과 최고 기온을 모두 추출하기
birthday_result2 = data[(data['날짜'].dt.month == 8) & (data['날짜'].dt.day == 16)]
birthday_result2
plt.plot(birthday_result2['최저기온(℃)'])
plt.plot(birthday_result2['최고기온(℃)'])
# x축 라벨을 추가해서 그리기
plt.plot(birthday_result2['날짜'], birthday_result2['최저기온(℃)'])
plt.plot(birthday_result2['날짜'], birthday_result2['최고기온(℃)'])
plt.plot(birthday_result2['날짜'], birthday_result2['최저기온(℃)'])
plt.plot(birthday_result2['날짜'], birthday_result2['최고기온(℃)'])
plt.title('내 생일의 기온 변화 그래프')