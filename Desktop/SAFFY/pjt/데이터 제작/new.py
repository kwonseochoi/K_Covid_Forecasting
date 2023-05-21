import requests
import json

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
# cast_ids = set()
# movie 만들기
for page in range(1, 51):
    api_url = f"{base_url}?api_key={api_key}&language={language}&page={page}"

    response = requests.get(api_url)
    data = response.json()

    for item in data['results']:
        movie_id = item['id']
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language={language}"
        movie_response = requests.get(movie_api_url)
        movie_data = movie_response.json()

        movie
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
                # if crew_member['id'] not in director_ids:
                director_id = crew_member['id']
                director_name = crew_member['name']
                break
        
        
        # Find the first 3 unique cast members' IDs
        cast_data = credits_data['cast']
        cast_ids = set()
        cast_list = []
        
        for cast_member in cast_data:
            if cast_member['id'] == director_id:
                continue  # Skip if the cast member has the same ID as the director
            
            if cast_member['id'] not in cast_ids:
                cast_list.append(cast_member)
                cast_ids.add(cast_member['id'])
                if len(cast_list) == 3:
                    break
                
        video_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language={language}"
        video_response = requests.get(video_api_url)
        video_data = video_response.json()
        
        trailers = video_data['results']
        trailer_key = None
        
        for trailer in trailers:
            if trailer['type'] == 'Trailer':
                if not trailer_key or trailer['published_at'] > trailer_key['published_at']:
                    trailer_key = trailer
        
        # Create the new JSON data
        item_data = {
            "model": "movies.movie",
            "pk": j,
            "fields": {
                "id": item['id'],
                "title": item['title'],
                "genre": item['genre_ids'],
                "director": director_id,
                "actors": [cast['id'] for cast in cast_list],
                "overview": item['overview'],
                "popularity": item['popularity'],
                "poster_path": item['poster_path'],
                "video_key": trailer_key['key'] if trailer_key else None,
                "release_date": item['release_date'],
                "vote_average": item['vote_average'],
                "vote_count": item['vote_count'],
                "revenue": revenue,
                "runtime": runtime,
                "budget": budget
            }
        }
        movie.append(item_data)
        j += 1
        
        # credits_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language={language}"
        # credits_response = requests.get(credits_api_url)
        # credits_data = credits_response.json()
        
        # # Find the director's ID
        # director_id = None
        # director_name = None
        # crew_list = credits_data['crew']
        # for crew_member in crew_list:
        #     if crew_member['department'] == "Directing" and crew_member['job'] == "Director":
        #         # if crew_member['id'] not in director_ids:
        #         director_id = crew_member['id']
        #         director_name = crew_member['name']
        #         break
        
        # # if director_id == None and director_name == None:
        # #     continue
        # # else:
        # #     item_data1 = {
        # #         "model" : "movies.director",
        # #         "pk" : k,
        # #         "fields" : {
        # #             "id" : director_id,
        # #             "name" : director_name
        # #         }
        # #     }
        # #     director.append(item_data1)
        # #     k += 1
        
        # cast_data = credits_data['cast']
        # cast_list = []
        
        # for cast_member in cast_data:
        #     if cast_member['id'] == director_id:
        #         continue  # Skip if the cast member has the same ID as the director
            
        #     if cast_member['id'] not in cast_ids:
        #         cast_list.append(cast_member)
        #         cast_ids.add(cast_member['id'])
        #         if len(cast_list) == 10:
        #             break
        
        # for i in range(len(cast_list)):
        #     item_data2 = {
        #     "model" : "movies.actor",
        #     "pk" : i+p,
        #     "fields" : {
        #         "id" : cast_list[i]['id'],
        #         "name" : cast_list[i]['name']
        #         }
        #     }  
        #     actor.append(item_data2)
        # p += 10
        
#
# if director_id == None and director_name == None:
#             pass
#         else:
#             item_data1 = {
#                 "model" : "movies.director",
#                 "pk" : k,
#                 "fields" : {
#                     "id" : director_id,
#                     "name" : director_name
#                 }
#             }
#             director.append(item_data1)
#             k += 1
#         for i in range(len(cast_list)):
#             item_data2 = {
#                 "models" : "movies.actor",
#                 "pk" : i+p,
#                 "fields" : {
#                     "id" : cast_list[i]['id'],
#                     "name" : cast_list[i]['name']
#                 }
#             }
#             actor.append(item_data2)
#         p += 3
        
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
# file_path4 = f'{name4}.json'
# with open(file_path4, "w", encoding='utf-8') as file:
#     json.dump(actor, file, ensure_ascii=False, indent=2)
# file_path5 = f'{name5}.json'
# with open(file_path5, "w", encoding='utf-8') as file:
#     json.dump(director, file, ensure_ascii=False, indent=2)
print('완성')