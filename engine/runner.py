
def launch_lab():
    print("🧠 Welcome to Prompt Injection Lab")
    print("1. Attack Mode")
    print("2. Defense Mode (Evolution)")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        level = input("Enter the level (1-5): ").strip()
        from attacker_mode.play import run_attacker_mode
        run_attacker_mode(level)
    elif choice == "2":
        from defender_mode.evolve import run_defender_mode
        run_defender_mode()
    elif choice == "3":
        from defender_mode.indirect import run_defender_mode2
        run_defender_mode2()
    else:
        print("Invalid choice.")
