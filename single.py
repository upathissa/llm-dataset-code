import requests
i = 701
api_url = f"https://tripitaka.online/sutta/live/sutta/{i}"
response = requests.get(api_url)

data = response.json()

content_list = [item["content"] for item in data["data"]]

output_file_path = f"textdata2/{i}.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for content in content_list:
        output_file.write(content.replace('“', '').replace("”", '').replace("‘", '') + "\n")
print(f"i: {i} file_saved")
