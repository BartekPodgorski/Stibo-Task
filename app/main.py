from fastapi import FastAPI
import requests
import json


app = FastAPI()

# http://localhost:80/rickandmorty/episodes/by/character/?character_name=Rick%20Sanchez
@app.get(f"/rickandmorty/episodes/by/character/")
async def get_episodes_by_character(character_name: str):
    url = f"https://rickandmortyapi.com/api/character/?name={character_name}"
    response_character = requests.get(url)
    if response_character.status_code != 200:
        return f"We got status: {response_character.status_code}, something wrong with {character_name}"
    else:
        occur_in_episode = []
        character_data = response_character.json()['results']
        for data in character_data:
            episodes = data['episode'][:10]
            for episode in episodes:
                response_episode = requests.get(episode)
                epi = response_episode.json()
                occur_in_episode.append({"episode": epi['episode'], "episode_name": epi['name']})
            break
        return response_character.status_code, json.dumps(occur_in_episode)