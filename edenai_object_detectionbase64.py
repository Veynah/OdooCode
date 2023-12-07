import requests

url = "https://api.edenai.run/v2/image/object_detection"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": True,
    "providers": "microsoft",
    "fallback_providers": "google",
    "file": "data:image/jpeg;name=yoda.jpeg" #Il faut le code en base64 mais c'est trop long et fait buger l'IDE
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer laclé"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)