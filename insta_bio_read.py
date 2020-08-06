import requests

user_name = 'hblauth'
url = f'https://instagram.com/{user_name}'

r = requests.get(url)

if r.status_code != 200:
    print('Page not found')

search_string = '"edge_followed-by":"{count":'

start_index = r.text.find(search_string) + len(search_string)
end_index = r.text.find('}', start_index)

follower_count = r.text[start_index:end_index]
print(follower_count)
