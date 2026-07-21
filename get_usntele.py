from pyrogram import Client

def load_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

sessions = load_file('sessions.txt')

results = []

for i, session_string in enumerate(sessions):
    try:
        with Client(f"acc{i}", session_string=session_string, no_updates=True) as app:
            me = app.get_me()
            usn = me.username or ""
            results.append(usn)
            print(f"[{i+1}] @{usn} ({me.first_name})")
    except Exception as e:
        results.append("")
        print(f"[{i+1}] ERROR | {e}")

with open('usntele.txt', 'w') as f:
    for usn in results:
        f.write(usn + '\n')

print(f"\nDone. Tersimpan di usntele.txt ({len(results)} akun)")
