
def launch_lab():
    print("🧠 Welcome to Prompt Injection Lab")
    print("1. Attack Mode(Direct)")
    print("2. Attack Mode(Indirect)")
    print("3. Defense Mode (Indirect)")
    print("4. Defense Mode (Agent)")
    print("5. Defense Mode (Evolution)")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        level = input("Enter the level (1-5): ").strip()
        from attacker_mode.playdirect import run_attacker_mode
        run_attacker_mode(level)
    elif choice == "5":
        from defender_mode.evolve import run_defender_mode
        run_defender_mode()
    elif choice == "3":
        from defender_mode.indirect import run_defender_mode2
        run_defender_mode2()
    elif choice == "4":
        from defender_mode.agent import run_agent_constraint_lab
        run_agent_constraint_lab()
    elif choice == "2":
        levelnum = input("Enter the level (1-3): ").strip()
        from attacker_mode.playindirect import run_indirect_attack
        run_indirect_attack(levelnum)
    else:
        print("Invalid choice.")
