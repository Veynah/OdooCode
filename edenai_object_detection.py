import requests

url = "https://api.edenai.run/v2/image/object_detection"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": True,
    "providers": "microsoft",
    "fallback_providers": "amazon",
    "file_url": "https://www.muaythaitechnician.com/wp-content/uploads/2022/05/cover-photo-1.png"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer cléapi"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)