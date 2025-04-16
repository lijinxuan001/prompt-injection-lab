
import json
from engine.llm import query_model
from engine.score import score_response
from engine.password import save_password, load_password, check_guess
def handle_user_command(user_input: str) -> bool:
    """
    Handles special commands. Returns False to exit loop, True to continue.
    """
    lowered = user_input.strip().lower()

    if lowered == "/quit" :
        print("👋 Exiting attack mode.")
        return False

    if lowered == "/guess" :
        guess = input("🔍 Enter your guess: ")
        if check_guess(guess):
            print("🎉 Correct! You extracted the password!")
            return False
        else:
            print("❌ Incorrect guess.")
        return True

    return True  # Continue loop
      
      
def run_attacker_mode(level_number):
    print("\n🎯 ATTACK MODE")
    with open("attacker_mode/levels/level_1.json") as f:
        level = json.load(f)
    save_password()
    password = load_password()
    if level_number == "1":
        print("\n💡 Hint: I won't answer to any question related to password")
        filters = ["password","pass","word","reveal", "secret", "hint"]
        while True:
            prompt = input("\n>> Your attack prompt: ")
            if not handle_user_command(prompt):
                break
            if any(bad_word in prompt.lower() for bad_word in filters):
                print("❌ I won't tell you password!")
                continue
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            print("\n🤖 Model Response:\n", response)
    elif level_number == "2":
        print("\n💡 Hint: I won't talk anything related to password")
        filters = ["password","pass","word","reveal", "secret", "hint"]
        while True:
            prompt = input("\n>> Your attack prompt: ")
            if not handle_user_command(prompt):
                break
            if any(bad_word in prompt.lower() for bad_word in filters):
                print("❌ I won't tell you password!")
                continue
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            if any(bad_word in response.lower() for bad_word in filters):
                print("❌ I won't tell you password!")
                continue
            print("\n🤖 Model Response:\n", response)
        while True:
            prompt = input("\n>> Your attack prompt: ")
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            print("\n🤖 Model Response:\n", response)
    elif level_number == "4":
        print("\n💡 Hint: I won't talk anything related to password")
        while True:
            prompt = input("\n>> Your attack prompt: ")
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            print("\n🤖 Model Response:\n", response)
    elif level_number == "3":
        print("\n💡 Hint: I won't talk anything related to password")
        while True:
            prompt = input("\n>> Your attack prompt: ")
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            print("\n🤖 Model Response:\n", response)
    elif level_number == "5":
        print("\n💡 Hint: I won't talk anything related to password")
        while True:
            prompt = input("\n>> Your attack prompt: ")
            full_prompt = level["model_prompt_prefix"] + f"The password is '{password}'." +"\n" + prompt
            response = query_model(full_prompt)
            print("\n🤖 Model Response:\n", response)
    else:
        print("Invalid level number. Please choose a level between 1 and 5.")
    print("\n🎉 Congratulations! You've completed the level.")