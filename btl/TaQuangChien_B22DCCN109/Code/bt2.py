import pickle
import csv
import statistics
from title import header,row,row2,header2,rowsquad
import os
file_path_players = os.path.join(os.path.dirname(__file__), "players.pkl")
file_path_squads = os.path.join(os.path.dirname(__file__), "squads.pkl")
file_path_resultTop3 = os.path.join(os.path.dirname(__file__), "result3.csv")
file_path_result2 = os.path.join(os.path.dirname(__file__), "result2.csv")
# Đọc các đối tượng từ file
list_player=[]
with open(file_path_players, "rb") as file:
    list_player = pickle.load(file)

list_squad=[]
with open(file_path_squads, "rb") as file:
    list_squad = pickle.load(file)
print("Load data success!")

NUMBER_OF_ATTR=167 #loai bo 5 thuoc tinh dau


def findtop3():
    to_compare_list=[]
    for i in list_player:
        all_attr_of_player=row(i)
        for index,value in enumerate(all_attr_of_player):
            if(index<5): continue
            if value=="N/a":
                all_attr_of_player[index]=0
        to_compare_list.append(all_attr_of_player)

    with open(file_path_resultTop3, mode='w', newline='', encoding='utf-8') as file:#file result3 luu top 3 cac cau thu co thuoc tinh cao nhat o moi thuoc tinh
        writer = csv.writer(file)
        head=header[5:]
        writer.writerow(["Attr","Top 3 Highest","Top 3 Lowest"])
        for i in range(NUMBER_OF_ATTR):
            players_after_sort=sorted(to_compare_list,key=lambda x:x[5+i])
            top3H="Top 1: "+players_after_sort[-1][0]+"(Team: "+players_after_sort[-1][2]+")"+"\n"\
                    +"Top 2: "+players_after_sort[-2][0]+"(Team: "+players_after_sort[-2][2]+")"+"\n"\
                    +"Top 3: "+players_after_sort[-3][0]+"(Team: "+players_after_sort[-3][2]+")"
                     
            top3L="Top 1 from bottom: "+players_after_sort[1][0]+"(Team: "+players_after_sort[1][2]+")"+"\n"\
                    +"Top 2 from bottom: : "+players_after_sort[2][0]+"(Team: "+players_after_sort[2][2]+")"+"\n"\
                    +"Top 3 from bottom: : "+players_after_sort[3][0]+"(Team: "+players_after_sort[3][2]+")"
            writer.writerow([head[i],top3H,top3L])

    os.startfile(file_path_resultTop3)

def get_attr_array(list_player):
    all_list_attr_of_player=[] #1 phần tử là tất cả các thuộc tính của Player

    for i in list_player:
        arr=row(i)
        all_list_attr_of_player.append(arr[5:])  

    all_attr=[[] for _ in range(NUMBER_OF_ATTR)] #1 Phần tử là 1 dãy cùng 1 thuộc tính của các Player
    for i in range(NUMBER_OF_ATTR):
        for player_attr in all_list_attr_of_player:
            attr_value=player_attr[i]
            if attr_value!="N/a":
                all_attr[i].append(attr_value)
            
    return all_attr

def findMeanMedianStddev():
    with open(file_path_result2, mode='w', newline='', encoding='utf-8') as file:
        #start all player
        all_attr=get_attr_array(list_player)#1 Phần tử là 1 dãy cùng 1 thuộc tính của các Player,Độ dài của 1 phần tử là số lượng Player
        mean_value_list=[0]*NUMBER_OF_ATTR
        median_value_list=[0]*NUMBER_OF_ATTR
        std_dev_list=[0]*NUMBER_OF_ATTR

        for index,arr in enumerate(all_attr):
            mean_value_list[index]=statistics.mean(arr)
            median_value_list[index]=statistics.median(arr)
            std_dev_list[index]=statistics.stdev(arr)

        writer = csv.writer(file)
        writer.writerow(header2)

        r=row2(0,"All",median_value_list,mean_value_list,std_dev_list)
        writer.writerow(r)
        # #end all player


        #start team
        for stt,squad in enumerate(list_squad):
            all_attr=get_attr_array(squad.players)#1 Phần tử là 1 dãy cùng 1 thuộc tính của các Player,Độ dài của 1 phần tử là số lượng Player trong team


            mean_value_list=[0]*NUMBER_OF_ATTR
            median_value_list=[0]*NUMBER_OF_ATTR
            std_dev_list=[0]*NUMBER_OF_ATTR


            for index,arr in enumerate(all_attr):
                mean_value_list[index]=statistics.mean(arr)
                median_value_list[index]=statistics.median(arr)
                if len(arr)<2:
                    std_dev_list[index]="N/a"
                else: std_dev_list[index]=statistics.stdev(arr)
            
            writer = csv.writer(file)
            r=row2(stt+1,squad.name,median_value_list,mean_value_list,std_dev_list)
            writer.writerow(r)
        #end team
        
    print("Write result2 Success")
    import subprocess
    #subprocess.Popen(["start", r"result2.csv"], shell=True)
    os.startfile(file_path_result2)

def drawHistogram():
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    with PdfPages('histogramsAllPlayer.pdf') as pdf:
        #start all player
        all_attr=get_attr_array(list_player)#1 phan tu la 1 thuoc tinh cua tat ca player,do dai 1 phan tu la so luong player

        for index,arr in enumerate(all_attr):
            plt.figure(figsize=(8, 6))
            plt.hist(arr, bins=30, color='blue', alpha=0.7, edgecolor='black')
            plt.title(f'Histogram of Data {header[5+index]}')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            pdf.savefig()  # Lưu biểu đồ vào tệp PDF
            plt.close()  # Đóng biểu đồ
    print("Các biểu đồ đã được lưu vào 'histogramsAllPlayer.pdf'")

    # Vẽ histogram cho team
    for stt,squad in enumerate(list_squad):
        with PdfPages(f'histogramsSquad{squad.name.replace(" ","")}.pdf') as pdf:
            all_attr=get_attr_array(squad.players)#1 phan tu la 1 thuoc tinh cua tat ca player,do dai 1 phan tu la so luong player
            for index,arr in enumerate(all_attr):
                plt.figure(figsize=(8, 6))
                plt.hist(arr, bins=30, color='blue', alpha=0.7, edgecolor='black')
                plt.title(f'Histogram of Data {header[5+index]}')
                plt.xlabel('Value')
                plt.ylabel('Frequency')
                pdf.savefig()  # Lưu biểu đồ vào tệp PDF
                plt.close()  # Đóng biểu đồ
        print(f"Các biểu đồ đã được lưu vào 'histogramsSquad{squad.name.replace(" ","")}.pdf'")

def findBestSquad():
    biggest_attr_value=[-1e9]*NUMBER_OF_ATTR
    best_team_in_one_attr=[""]*NUMBER_OF_ATTR
    for i in list_squad:
        arr=rowsquad(i)[5:]
        for index,value in enumerate(arr):
            if value!="N/a" and value>biggest_attr_value[index]:
                biggest_attr_value[index]=value
                best_team_in_one_attr[index]=i.name
                
            elif value=="N/a" and biggest_attr_value[index]==-1e9 and best_team_in_one_attr[index]=="":
                biggest_attr_value[index]=0
                best_team_in_one_attr[index]=i.name
    for index,i in enumerate(best_team_in_one_attr):
        print(header[5+index]+": ",i)

    #đội nào có phong độ tốt nhất giải ngoại Hạng Anh mùa 2023-2024
    from collections import Counter
    squad_ranking=Counter(best_team_in_one_attr)
    print("Best Squad in Competition is: ",(squad_ranking.most_common(1)[0][0]))

print("Find top3 ---------------------------------------------------------------------------------------------------")
findtop3()

print("Find mean-median-std ---------------------------------------------------------------------------------------------------")
findMeanMedianStddev()

print("Draw histogram ---------------------------------------------------------------------------------------------------")
# drawHistogram()

print("Find best squad ---------------------------------------------------------------------------------------------------")
findBestSquad()

