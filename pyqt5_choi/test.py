import json

# 저장할 데이터 (파이썬 딕셔너리 형태)
data = {
    "name": "주현",
    "age": 12,
    "school": "Elementary School"
}
# JSON 파일로 저장하기
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# JSON 파일을 불러오기

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)