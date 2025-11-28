class KH:
    stt = 0
    
    def __init__(self, name, diem, dantoc, khuvuc):
        self.name = ' '.join([word.capitalize() for word in name.strip().split()])
        KH.stt += 1
        self.ma = f"TS{KH.stt:02d}"
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc
        self.total = self.get_ut(khuvuc) + diem + (0 if dantoc == "Kinh" else 1.5)
    
    def get_total(self):
        return self.total
    
    def get_ut(self, khuvuc):
        if khuvuc == 1:
            return 1.5
        elif khuvuc == 2:
            return 1.0
        else:
            return 0.0
    
    def __str__(self):
        ketqua = "Do" if self.total >= 20.5 else "Truot"
        return f"{self.ma} {self.name} {self.total:.1f} {ketqua}"

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        name = input().strip()
        diem = float(input().strip())
        dantoc = input().strip()
        khuvuc = int(input().strip())
        a.append(KH(name, diem, dantoc, khuvuc))
    a.sort(key=lambda x: (-x.get_total(), x.ma))
    for kh in a:
        print(kh)
