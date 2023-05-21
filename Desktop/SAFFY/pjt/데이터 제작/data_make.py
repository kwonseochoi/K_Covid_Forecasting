import requests
import json


# api_key = "cdb84e32fe9892b6b1fad1b2dceb89d0"
# base1_url = "https://api.themoviedb.org/3/movie/top_rated"
# language = "ko-KR"

# result1 = []

# fields = {
#     'id': 'id',
#     'genre_ids': 'genre',
#     'overview': 'overview',
#     'popularity': 'popularity',
#     'poster_path': 'poster_path',
#     'release_date': 'release_date',
#     'title': 'title',
#     'vote_average': 'vote_average',
#     'vote_count': 'vote_count'
# }

# for i in range(1, 51):
# #     url = f"{base1_url}?api_key={api_key}&language={language}&page={i}"
# #     response = requests.get(url)
# #     data = response.json()
    
# #     j = 1
# #     for item in data['results']:
# #         item_data = [{
# #             "model": "movies.movie",
# #             "pk": j,
# #             "fields": {fields[key]: item[key] for key in fields if key in item}
# #         }]
# #         # print(item_data)
# #         result1.extend(item_data)
# #         # print(result1)
# #         j += 1
# # id_lst = []
# # for i in result1:
# #     # print(i['id'], end='\n')
# #     id_lst.append(i['fields']['id'])
    
# # result2 = []
# # genre = []
# # for i in id_lst:
# #     api_url = f"https://api.themoviedb.org/3/movie/{i}?api_key={api_key}&language={language}"
# #     response = requests.get(api_url)
# #     data = response.json()
# #     genre_data = data['genres']
# #     for geners in genre_data:
# #         if not any(geners['id'] == genred['id'] for genred in genre):
# #             genre.append(geners)
# # gfields = {
# #     'id': 'id',
# #     'name': 'name',
# # }
# # genre1 = []        
# # j = 1
# # for item in genre:
#     # item_data = [{
#     #     "model": "movies.genre",
#     #     "pk": j,
#     #     "fields": {gfields[key]: item[key] for key in gfields if key in item}
#     # }]
#     # # print(item_data)
#     # genre1.extend(item_data)
#     # # print(result1)
#     # j += 1
#     # wanted_key = ['id', 'budget', 'revenue', 'runtime']
#     # new_data = {key: data[key] for key in wanted_key if key in data}
#     # result2.extend([new_data])

# # director data 코드
# # director = []
# # existing_ids = set()  # Existing id values

# # for i in id_lst:
# #     api_url = f"https://api.themoviedb.org/3/movie/{i}/credits?api_key={api_key}&language={language}"
# #     response = requests.get(api_url)
# #     data = response.json()
# #     crew_data = data['crew']
# #     for j in crew_data:
# #         if j['department'] == 'Directing' and j['job'] == 'Director':
# #             if j['id'] not in existing_ids:  # Check if id is already in the existing_ids set
# #                 director.append(j)
# #                 existing_ids.add(j['id'])

# # crew_fields = {
# #     'id' : 'id',
# #     'name' : 'name',
# # }
# # result6 = []
# # j = 1
# # for item in director:
# #     item_data = [{
# #         "model": "movies.director",
# #         "pk": j,
# #         "fields": {crew_fields[key]: item[key] for key in crew_fields if key in item}
# #     }]
# #     result6.extend(item_data)
# #     j += 1
# # # # actor 데이터

# tota_cast = []
# for i in id_lst:
#     api_url = f"https://api.themoviedb.org/3/movie/{i}/credits?api_key={api_key}&language={language}"
#     response = requests.get(api_url)
#     data = response.json()
#     cast_data = data['cast'][:30]
#     cast = []
#     for j in cast_data:    
#         if j['id'] not in existing_ids:
#             cast.append(j)
#             existing_ids.add(j['id'])
#     tota_cast.extend(cast[:3])
# cast_fields = {
#     'id' : 'id',
#     'name' : 'name',
# }
# result5 = []
# j = 1
# for item in tota_cast:
#     item_data = [{
#         "model": "movies.actor",
#         "pk": j,
#         "fields": {cast_fields[key]: item[key] for key in cast_fields if key in item}
#     }]
#     result5.extend(item_data)
#     j += 1

# 최종 movie data
# movie = []
# for i in id_lst:
#     api_url = f"https://api.themoviedb.org/3/movie/{i}/credits?api_key={api_key}&language={language}"
#     response = requests.get(api_url)
#     data = response.json()
#     movie.extend([data])

# ans = []
# for item1 in result1:
#     for item2 in movie:
#         if item1['fields']['id'] == item2['id']:
#             crew_list = [j["id"] for j in item2["crew"] if
#              j["department"] == "Directing" and j["job"] == "Director"]
#             director_id = int(crew_list[0]) if crew_list else None
#             merge_data = [{
#                 "model" : item1["model"],
#                 "pk" : item1["pk"],
#                 "fields" : {
#                     **item1["fields"],
#                     "actors" : [],
#                     "director": director_id
#                 }
#             }]
#             ans.extend(merge_data)

import requests

api_key = "cdb84e32fe9892b6b1fad1b2dceb89d0"
language = "ko-KR"
base_url = "https://api.themoviedb.org/3/movie/top_rated"
movie = []
actor = []
director = []
j = 1
k = 1
p = 1
director_ids = set()
cast_ids = set()
for page in range(1, 51):
    api_url = f"{base_url}?api_key={api_key}&language={language}&page={page}"

    response = requests.get(api_url)
    data = response.json()

    for item in data['results']:
        movie_id = item['id']
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language={language}"
        movie_response = requests.get(movie_api_url)
        movie_data = movie_response.json()

        # Get additional movie details
        revenue = movie_data.get('revenue')
        runtime = movie_data.get('runtime')
        budget = movie_data.get('budget')

        # Step 2: Process data and retrieve director and cast information
        credits_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language={language}"
        credits_response = requests.get(credits_api_url)
        credits_data = credits_response.json()
        
        # Find the director's ID
        director_id = None
        director_name = None
        crew_list = credits_data['crew']
        for crew_member in crew_list:
            if crew_member['department'] == "Directing" and crew_member['job'] == "Director":
                if crew_member['id'] not in director_ids:
                    director_id = crew_member['id']
                    director_name = crew_member['name']
                    director_ids.add(director_id)
                    break
        
        
        # Find the first 3 unique cast members' IDs
        cast_data = credits_data['cast']
        cast_list = []
        
        for cast_member in cast_data:
            if cast_member['id'] == director_id:
                continue  # Skip if the cast member has the same ID as the director
            
            if cast_member['id'] not in cast_ids:
                cast_list.append(cast_member)
                cast_ids.add(cast_member['id'])
                if len(cast_list) == 3:
                    break
        
        # Create the new JSON data
        item_data = {
            "model": "movies.movie",
            "pk": j,
            "fields": {
                "id": item['id'],
                "title": item['title'],
                "director": director_id,
                "actors": [cast['id'] for cast in cast_list],
                "revenue": revenue,
                "runtime": runtime,
                "budget": budget,
                "genre": item['genre_ids'],
                "overview": item['overview'],
                "popularity": item['popularity'],
                "poster_path": item['poster_path'],
                "release_date": item['release_date'],
                "vote_average": item['vote_average'],
                "vote_count": item['vote_count']
            }
        }
        movie.append(item_data)
        j += 1
        if director_id == None and director_name == None:
            pass
        else:
            item_data1 = {
                "model" : "movies.director",
                "pk" : k,
                "fields" : {
                    "id" : director_id,
                    "name" : director_name
                }
            }
            director.append(item_data1)
            k += 1
        for i in range(len(cast_list)):
            item_data2 = {
                "models" : "movies.actor",
                "pk" : i+p,
                "fields" : {
                    "id" : cast_list[i]['id'],
                    "name" : cast_list[i]['name']
                }
            }
            actor.append(item_data2)
        p += 3
name = 'movies'
name2 = 'movie_detail'
name3 = 'genre'
name4 = 'actors'
name5 = 'directors'
file_path = f'{name}.json'
with open(file_path, "w", encoding='utf-8') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)
    # json.dump(result1, file, ensure_ascii=False, indent=2)
# file_path2 = f'{name2}_data.json'
# with open(file_path2, "w", encoding='utf-8') as file:
# json.dump(result2, file, ensure_ascii=False, indent=2)
# file_path3 = f'{name3}_data.json'
# with open(file_path3, "w", encoding='utf-8') as file:
# json.dump(genre1, file, ensure_ascii=False, indent=2)
file_path4 = f'{name4}.json'
with open(file_path4, "w", encoding='utf-8') as file:
    json.dump(actor, file, ensure_ascii=False, indent=2)
file_path5 = f'{name5}.json'
with open(file_path5, "w", encoding='utf-8') as file:
    json.dump(director, file, ensure_ascii=False, indent=2)
print('완성')