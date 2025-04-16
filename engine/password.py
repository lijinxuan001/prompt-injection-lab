import base64
import string
import random
import json
def generate_random_password(length=8):
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits  # Letters and numbers
    return ''.join(random.choices(characters, k=length))

def save_password():
    password = generate_random_password()
    encoded = base64.b64encode(password.encode()).decode()
    with open("attacker_mode/levels/secret.json", "w") as f:
        json.dump({"password_b64": encoded}, f)

def load_password():
    with open("attacker_mode/levels/secret.json", "r") as f:
        data = json.load(f)
    return base64.b64decode(data["password_b64"]).decode()
def check_guess(guess: str) -> bool:
    real = load_password()
    return guess.strip() == real