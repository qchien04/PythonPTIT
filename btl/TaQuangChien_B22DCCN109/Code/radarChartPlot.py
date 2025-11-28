import numpy as np
import matplotlib.pyplot as plt

from title import row
from title import header

def drawRadarChart(p1, p2, arrOfAttr):
    # Lấy các nhãn tương ứng với các chỉ số
    head = header[5:]
    labels = [head[i] for i in arrOfAttr]

    # Lấy các giá trị chỉ số cho 2 cầu thủ
    values_player1 = []
    values_player2 = []
    attr_p1 = row(p1)[5:]
    attr_p2 = row(p2)[5:]

    for i in arrOfAttr:
        # Thay 'N/a' bằng giá trị 0
        value_p1 = 0 if attr_p1[i] == 'N/a' else float(attr_p1[i])
        value_p2 = 0 if attr_p2[i] == 'N/a' else float(attr_p2[i])
        values_player1.append(value_p1)
        values_player2.append(value_p2)

    # In ra để kiểm tra
    print("Values Player 1:", values_player1)
    print("Values Player 2:", values_player2)

    # Tính toán góc cho các trục radar chart
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    # Đảm bảo radar chart khép kín
    values_player1 += values_player1[:1]
    values_player2 += values_player2[:1]
    angles += angles[:1]

    # Tạo hình radar
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Vẽ radar cho cầu thủ 1
    ax.fill(angles, values_player1, color='blue', alpha=0.25)
    ax.plot(angles, values_player1, color='blue', linewidth=2, label=p1.name)

    # Vẽ radar cho cầu thủ 2
    ax.fill(angles, values_player2, color='red', alpha=0.25)
    ax.plot(angles, values_player2, color='red', linewidth=2, label=p2.name)

    # Thiết lập nhãn cho các trục và bỏ nhãn giá trị trên trục y
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Thêm tiêu đề và chú thích
    plt.title('So sánh chỉ số cầu thủ bóng đá')
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.show()
