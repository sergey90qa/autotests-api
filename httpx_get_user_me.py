import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json= login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}
users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers= headers)
users_me_response_data = users_me_response.json()
print("Status code: ", users_me_response.status_code)
print("Response: ", users_me_response_data)


