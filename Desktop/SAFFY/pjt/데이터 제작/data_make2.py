import json

with open('movie_data.json', 'r', encoding='utf-8') as file:
    result1 = json.load(file)
with open('movie_detail_data.json', 'r', encoding='utf-8') as file:
    result2 = json.load(file)

# print(genre)
ans = []
for item1 in result1:
    for item2 in result2:
        if item1['fields']['id'] == item2['id']:
            merged_item = {**item1['fields'], **item2}  # 병합된 항목 생성
            ans.append(merged_item)
            break
       
fields = {
    'id': 'id',
    'genre': 'genre',
    'overview': 'overview',
    'popularity': 'popularity',
    'poster_path': 'poster_path',
    'release_date': 'release_date',
    'title': 'title',
    'vote_average': 'vote_average',
    'vote_count': 'vote_count',
    'budget': 'budget',
    'revenue' : 'revenue',
    'runtime' : 'runtime',
    'actors' : 'actors',
    'director' : 'director'
}
result3 = []
j = 1        
for item in ans:
        # print(item, end='\n')
        item_data = [{
            "model": "movies.movie",
            "pk": j,
            "fields": {fields[key]: item[key] for key in fields if key in item}
        }]
        result3.extend(item_data)
        j += 1
        # result1.extend(item_data)
# total = []
# for data in ans:
#     wanted_key = ['id', 'genre', 'overview', 'popularity', 'poster_path',
#                   'release_date', 'title', 'vote_average', 'vote_count',
#                   'revenue', 'runtime', 'budget']
#     new_data = {key : data[key] for key in wanted_key if key in data}
#     total.extend([new_data])
name3 = 'movie1'
file_path = f'{name3}_data.json'
with open(file_path, "w", encoding='utf-8') as file:
    json.dump(result3, file, ensure_ascii=False, indent=2)