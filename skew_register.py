import requests
import time

def load_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

emails = load_file('email.txt')
twitters = load_file('usnx.txt')
telegrams = load_file('usntele.txt')

url = "https://skew.trade/api/reach-out"
headers = {"Content-Type": "application/json"}

for i, (email, twitter, telegram) in enumerate(zip(emails, twitters, telegrams)):
    payload = {
        "email": email,
        "twitter": f"@{twitter}" if not twitter.startswith('@') else twitter,
        "telegram": f"@{telegram}" if not telegram.startswith('@') else telegram
    }

    try:
        res = requests.post(url, json=payload, headers=headers)
        data = res.json()
        if data.get("ok"):
            print(f"[{i+1}] ✅ {email} | contactId: {data.get('contactId')}")
        else:
            print(f"[{i+1}] ❌ {email} | {data}")
    except Exception as e:
        print(f"[{i+1}] ERROR {email} | {e}")

    if i < len(emails) - 1:
        time.sleep(10)

print("Done.")
