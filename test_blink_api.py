import requests

url = "https://rest-prod.immedia-semi.com"

client_id = 968541

r = requests.post(url + "/api/v5/account/login",
                  data={
                      "email": "ravikumar.guntuku@gmail.com",
                      "password": "Fadd3n$6120",
                      "unique_id": client_id,
                      "reauth": True
                  }
                  )

response = r.json()

print(response)

account_id = response["account"]["account_id"]
client_id = response["account"]["client_id"]
account_tier = response["account"]["tier"]

auth_token = response["auth"]["token"]

print(auth_token)

r = requests.post(url + "/api/v4/account/"+str(account_id)+"/client/"+str(client_id)+"/pin/verify",
                  headers={
    "token-auth": auth_token
}, data={
    "pin": input("Enter pin: ")
}
)

print(r.json())

garage_camera_id = "G8V1-9001-3113-34AR"

# url = f"https://rest-prod-{account_tier}.immedia-semi.com"
# print(url)

r = requests.get(url + "/api/v4/accounts/"+str(account_id) +
                 "/homescreen", headers={"token-auth": auth_token})

response = r.json()

print(response)
