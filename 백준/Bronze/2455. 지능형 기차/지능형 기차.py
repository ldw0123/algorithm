on = []
people = 0

for _ in range(4):
    out_num, in_num = map(int, input().split())
    people += in_num  # 타는 사람
    people -= out_num  # 내리는 사람
    on.append(people)  # 종착역 마다 사람 수 추가

print(max(on))