# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pandas as pd
import matplotlib.pyplot as plt

elec = pd.read_csv('C:/Users/Master/Downloads/연도별전력사용량.csv')

# 자치구 데이터 정리
data_filtered = elec.iloc[4:, [0, 3, 4, 5]]  # 예시로 2004년부터 3개 년도 선택
data_filtered.columns = ['자치구', '2004', '2005', '2006']  # 열 이름 변경


# 숫자 데이터로 변환 (전력 사용량이 숫자로 되어 있는지 확인)
data_filtered['2004'] = elec.to_numeric(data_filtered['2004'], errors='coerce')
data_filtered['2005'] = elec.to_numeric(data_filtered['2005'], errors='coerce')
data_filtered['2006'] = elec.to_numeric(data_filtered['2006'], errors='coerce')


# 자치구별로 그룹화 후 합계
data_grouped = data_filtered.groupby('자치구').sum()


# 차트 그리기
#data_grouped.plot(kind='bar', figsize=(10, 6))
# plt.title('자치구별 연도별 전력 사용량')
# plt.xlabel('자치구')
# plt.ylabel('전력 사용량')
# plt.show()