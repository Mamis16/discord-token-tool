import requests

def create_discord_account(email, username, password, captcha_key):
    url = "https://discord.com/api/v9/auth/register"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "email": email,
        "username": username,
        "password": password,
        "captcha_key": captcha_key,
        "consent": True,
        "date_of_birth": "2000-01-01"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Hesap oluşturuldu!")
        print("Token:", response.json().get("token"))
    else:
        print("Hata oluştu:", response.text)

if __name__ == "__main__":
    email = input("Email: ")
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")
    captcha_key = input("Captcha Key (tarayıcıdan alın): ")
    create_discord_account(email, username, password, captcha_key)
