
from object import Tranfer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pickle
import os

file_pathTranfer = os.path.join(os.path.dirname(__file__), "tranfers.pkl")
file_slugAndAge = os.path.join(os.path.dirname(__file__), "slugAndAge.pkl")

list_tranfer=[]
name_slug_age=[]
with open(file_pathTranfer, "rb") as file:
    list_tranfer = pickle.load(file)
print(len(list_tranfer))
with open(file_slugAndAge, "rb") as file:
    name_slug_age = pickle.load(file)
print(len(list_tranfer))

price_arr=[]
skill_arr=[]
pot_arr=[]
matches_arr=[]
minutesPlay_arr=[]
goals_arr=[]
assists_arr=[]
yellowCards_arr=[]
yellowRedCards_arr=[]
redCards_arr=[]
averageETV_arr=[]
lastTranfer_arr=[]
age_arr=[]

for i in list_tranfer:
    price_arr.append(i.price)
    skill_arr.append(i.skill)
    pot_arr.append(i.pot)
    matches_arr.append(i.matches)
    minutesPlay_arr.append(i.minutes_play)
    goals_arr.append(i.goals)
    assists_arr.append(i.assists)
    yellowCards_arr.append(i.yellow_cards)
    yellowRedCards_arr.append(i.yellow_red_cards)
    redCards_arr.append(i.red_cards)
    averageETV_arr.append(i.averageETV)
    lastTranfer_arr.append(i.lastTranfer)
    age=0 #Xác định tuổi
    for j in name_slug_age:
        if i.statLink.split(r'/')[-1]==j[1]:
            age=j[0]
    age_arr.append(age)


player=[]
for i in list_tranfer:
    arr=[]
    arr.append(i.name)
    arr.append(i.price)
    arr.append(i.skill)
    arr.append(i.pot)
    arr.append(i.matches)
    arr.append(i.minutes_play)
    arr.append(i.goals)
    arr.append(i.assists)
    arr.append(i.yellow_cards)
    arr.append(i.yellow_red_cards)
    arr.append(i.red_cards)
    arr.append(i.averageETV)
    arr.append(i.lastTranfer)
    age=0 #Xác nhận tuổi
    for j in name_slug_age:
        if i.statLink.split(r'/')[-1]==j[1]:
            age=j[0]
    arr.append(age)
    player.append(arr)



y = np.array([price_arr]).T
X1 = np.array([skill_arr]).T
X2 = np.array([pot_arr]).T
X3 = np.array([matches_arr]).T
X4 = np.array([minutesPlay_arr]).T
X5 = np.array([goals_arr]).T
X6 = np.array([assists_arr]).T
X7 = np.array([yellowCards_arr]).T
X8 = np.array([yellowRedCards_arr]).T
X9 = np.array([redCards_arr]).T
X10 = np.array([averageETV_arr]).T
X11 = np.array([lastTranfer_arr]).T
X12 = np.array([age_arr]).T


# Tạo ma trận đặc trưng mở rộng Xbar với cột 1
one = np.ones((X1.shape[0], 1))  # Cột 1 để tính phần bù
Xbar = np.concatenate((one,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12), axis=1)

# Sử dụng Scikit-learn để huấn luyện mô hình hồi quy tuyến tính
regr = LinearRegression(fit_intercept=False) 
regr.fit(Xbar, y)

print( 'Solution found by scikit-learn     : ', regr.coef_ )
test=int(input("Nhập id cầu thủ cần kiểm tra: "))

new_player = np.array([([1]+player[test][2:])])
predicted_price = regr.predict(new_player)
print(f"Dự đoán giá cầu thủ {player[test][0]}:", f"{predicted_price[0,0]:.0f}" if predicted_price[0,0]>0 else "0","|| Giá trị thực: ",player[test][1])
print("Độ lệch",f"{abs(predicted_price[0,0]-player[test][1]):.0f}" if predicted_price[0,0]>0 else f"{abs(player[test][1]):.0f}")

mini_different=0
small_different=0 #Độ lệch nhỏ hơn 2tr
mid_different=0 #Độ lệch nhỏ hơn 4tr lớn hơn 2tr
big_different=0 #Độ lệch nhỏ hơn 8tr lớn hơn 4tr
supper_different=0 #Độ lệch lớn hơn 8tr
for i in range(len(player)):
    new_player = np.array([([1]+player[i][2:])])
    predicted_price = regr.predict(new_player)
    tmp=abs(predicted_price[0,0]-player[i][1])
    if tmp<1000000: mini_different+=1
    elif tmp<2000000: small_different+=1
    elif tmp<4000000: mid_different+=1
    elif tmp<8000000: big_different+=1
    else: supper_different+=1

print("Độ lệch nhỏ hơn 1tr:",mini_different)
print("Độ lệch nhỏ hơn 2tr lớn hơn 1tr:",small_different)
print("Độ lệch nhỏ hơn 4tr lớn hơn 2tr:",mid_different)
print("Độ lệch nhỏ hơn 8tr lớn hơn 4tr:",big_different)
print("Độ lệch lớn hơn 8tr:",supper_different)   



from sklearn.metrics import r2_score
y_pred = regr.predict(Xbar)
r2 = r2_score(y, y_pred)
print("R^2 Score:", r2)

