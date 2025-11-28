import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PowerTransformer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from radarChartPlot import drawRadarChart
from title import header,row
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
from object import Player_Manager


#Lua chon diem hoi tu cho thuat toan KMean

def Elbow_solution(data):
    wcss = []
    for k in range(1, 5):
        kmeans = KMeans(n_clusters=k, random_state=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)  # inertia_ là tổng WCSS

    # Vẽ đồ thị Elbow
    plt.plot(range(1, 5), wcss)
    plt.title('Phương pháp Elbow')
    plt.xlabel('Số cụm (k)')
    plt.ylabel('WCSS')
    plt.show()

def Silhouette_solution(data):
    from sklearn.metrics import silhouette_score

    # Thử k từ 2 đến 10 (k=1 không có ý nghĩa cho silhouette)
    silhouette_scores = []

    for k in range(2, 5):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        score = silhouette_score(data, kmeans.labels_)
        silhouette_scores.append(score)

    # Vẽ đồ thị Silhouette score
    plt.plot(range(2, 5), silhouette_scores)
    plt.title('Phương pháp Silhouette')
    plt.xlabel('Số cụm (k)')
    plt.ylabel('Silhouette Score')
    plt.show()

def normalizedata():
    players_attr_list=[] #1 phan tu la tat ca cac thuoc tinh cua player
    AttrToDelete=[]

    for i in list_player:
        arr=row(i)[5:]
        #thay cac gia tri N/a ve gia tri trung binh cua toan bo player
        for i in range(len(arr)):
            if arr[i]=="N/a": arr[i]=mean_value_list[i]
            elif arr[i]<0:
                AttrToDelete.append(i)
        players_attr_list.append(arr)

    non_negative_data=[]
    for player in players_attr_list:
        arr=[]
        for index,value in enumerate(player):
            if index not in AttrToDelete:
                arr.append(value)
        non_negative_data.append(arr)

    #chuan hoa du lieu
    data = np.array(non_negative_data)
    data_normalized = np.log(data+(1e-18))
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data_normalized)

    return data_normalized

def drawKmean(n,data_normalized):
    kmeans = KMeans(n_clusters=n, random_state=50)
    kmeans.fit(data_normalized)

    # Lưu trữ nhãn cụm
    labels = kmeans.labels_
    # Lấy tọa độ của các tâm cụm
    centroids = kmeans.cluster_centers_

    # Vẽ dữ liệu và các tâm cụm
    plt.figure(figsize=(8, 6))
    plt.scatter(data_normalized[:, 0], data_normalized[:, 1], c=labels, cmap='viridis', marker='o', label='Dữ liệu', alpha=0.7)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Tâm cụm')
    plt.title('Phân cụm dữ liệu bằng K-Means')
    plt.xlabel('Chiều 1')
    plt.ylabel('Chiều 2')
    plt.legend()
    plt.grid(True)
    plt.show()

def ComparePlayer():
    player_manager=Player_Manager()
    player_manager.list_player=list_player

    print("So sánh 2 cầu thủ\nDanh sách cầu thủ:")
    for index,player in enumerate(list_player):
        print(f"{player.name} (Team: {player.team} )")
    
    player1=None
    player2=None
    while(True):
        name1=input("Nhập tên cầu thủ thứ nhất: ")
        squad1=input("Nhập tên đội của cầu thủ thứ nhất: ")
        player1=player_manager.findPlayerByNameandTeam(name1,squad1)
        if player1==None:
            print("Cầu thủ không tồn tại")
        else: break

    while(True):
        name2=input("Nhập tên cầu thủ thứ hai: ")
        squad2=input("Nhập tên đội của cầu thủ thứ hai: ")
        player2=player_manager.findPlayerByNameandTeam(name2,squad2)
        if player1==None:
            print("Cầu thủ không tồn tại")
        else: break

    #RadaChart
    attr_list_to_draw=[]
    attr_quantity_to_draw=0
    while(True):
        try:
            attr_quantity_to_draw=int(input("Nhập số thuộc tính cần so sánh "))
            if attr_quantity_to_draw>167 or attr_quantity_to_draw<1: raise ValueError
            break
        except ValueError:
            print("Số lượng thuộc tính phải nhỏ hơn hoặc bằng 167 và lớn hơn 0")
    for index,attr_name in enumerate(header[5:]):
        print(attr_name,": Id=",index)

    print("Nhập các id của thuộc tính cần so sánh")
    for _ in range(attr_quantity_to_draw):
        n=0
        while(True):
            try:
                n=int(input("Id thuoc tinh: "))
                if n>167 or n<0: raise ValueError
                break
            except ValueError:
                print("Id không hợp lệ")

        attr_list_to_draw.append(n)
    #attr_list_to_draw=[0,1,11,12,13,47,67,68,69,71]
    drawRadarChart(player1,player2,attr_list_to_draw)


#Main...........................................................................................................................
#...............................................................................................................................
# Đọc các đối tượng từ file
file_path1 = os.path.join(os.path.dirname(__file__), "players.pkl")
list_player=[]
with open(file_path1, "rb") as file:
    list_player = pickle.load(file)

print("Load data success!")

list_player=list(filter(lambda p:p.playing_time["minutes"]>90,list_player))
print(len(list_player))
#lay tu ket qua cua bai 2
mean_value_list=[19.627586206896552, 14.413793103448276, 1006.5134048257372, 1.8982758620689655, 0.16551724137931034, 
                 1.4810344827586206, 2.85, 0.1, 2.0760344827586206, 1.9296551724137931, 1.4937931034482759, 24.651724137931033, 
                 50.58448275862069, 50.06206896551724, 0.12525862068965518, 0.09162068965517242, 0.2168103448275862, 
                 0.1181551724137931, 0.20963793103448275, 0.14498275862068966, 0.10070689655172414, 0.2458448275862069, 
                 0.13843103448275862, 0.23946551724137932, 31.15, 2.24525, 91.3, 61.175, 65.44, 7.45, 4.1, 7.45, 3.925, 
                 19.61578947368421, 2.675, 2.4, 0.2, 0.075, 9.720689655172414, 2.0637931034482757, 17.9, 6.117241379310345, 
                 31.024516129032257, 1.354551724137931, 0.42579310344827587, 0.09219354838709677, 0.2941293532338308, 
                 16.532043010752687, 0.4879310344827586, 0.16551724137931034, 0.18448275862068966, 2.0760344827586206, 
                 1.9296551724137931, 0.10139784946236559, -0.012241379310344832, -0.03137931034482759, 541.5086206896551, 
                 670.7896551724137, 78.10578947368421, 9199.26551724138, 3251.863793103448, 260.3965517241379, 291.3724137931035, 
                 87.68645276292335, 220.91551724137932, 254.8448275862069, 83.14856115107914, 46.139655172413796, 88.82241379310345, 
                 54.3527724665392, 1.4810344827586206, 1.4937931034482759, 1.3217241379310345, -0.012758620689655177, 
                 13.587931034482759, 40.360344827586204, 11.686206896551724, 2.4362068965517243, 50.58448275862069, 
                 608.8534482758621, 59.43793103448276, 16.103448275862068, 2.2913793103448277, 3.463793103448276, 22.686206896551724, 
                 23.23448275862069, 7.086206896551724, 3.462068965517241, 2.070689655172414, 0.1706896551724138, 541.5086206896551, 
                 2.4982758620689656, 12.579310344827586, 31.81896551724138, 2.352051724137931, 23.294827586206896, 2.646551724137931, 
                 1.856896551724138, 2.0689655172413794, 1.3275862068965518, 0.6241379310344828, 3.5637931034482757, 
                 0.23093103448275862, 2.5068965517241377, 0.22413793103448276, 0.25862068965517243, 0.2810344827586207, 
                 0.22413793103448276, 0.06896551724137931, 23.137931034482758, 13.575862068965517, 11.21896551724138, 
                 8.648275862068965, 3.2706896551724136, 10.74655172413793, 21.936206896551724, 46.83616600790514, 11.189655172413794, 
                 16.04310344827586, 5.106896551724138, 10.936206896551724, 10.875862068965517, 34.01379310344828, 26.867241379310343, 
                 0.5672413793103448, 818.9931034482759, 91.19137931034483, 268.66896551724136, 350.03275862068966, 207.90862068965518, 
                 34.34827586206897, 818.8086206896552, 24.548275862068966, 11.189655172413794, 46.43340163934426, 10.74655172413793, 
                 42.50553278688525, 468.73275862068965, 2477.746551724138, 1273.6155172413794, 24.651724137931033, 17.386206896551723, 
                 7.85, 18.606896551724137, 12.391379310344828, 536.2344827586207, 50.06206896551724, 11.206434316353887, 
                 79.69574036511156, 7.116621983914209, 4.053619302949062, 19.389898989898988, 5.081769436997319, 1.3616494845360825, 
                 23.52920962199313, 23.457044673539517, 22.307241379310344, 22.231896551724137, 14.493103448275862, 13.98448275862069, 
                 2.4982758620689656, 22.686206896551724, 0.08448275862068966, 63.26379310344828, 17.5, 17.5, 47.19566037735849]

NUMBER_OF_ATTR=167 #loai bo 5 thuoc tinh dau
datanormalize=normalizedata()

print("Find k ---------------------------------------------------------------------------------------------------")
Elbow_solution(datanormalize)
Silhouette_solution(datanormalize)

#phân cụm với Kmean
print("Kmean ---------------------------------------------------------------------------------------------------")
drawKmean(2,datanormalize)

# Áp dụng PCA
print("PCA ---------------------------------------------------------------------------------------------------")
pca = PCA(n_components=2)
dataPCA = pca.fit_transform(datanormalize)
drawKmean(2,dataPCA)

print("Compare player ---------------------------------------------------------------------------------------------------")
#So sánh 2 cầu thủ
ComparePlayer()
