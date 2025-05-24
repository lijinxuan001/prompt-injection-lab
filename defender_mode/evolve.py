
import json
from engine.llm import query_model
from engine.score import score_response

def run_defender_mode():
    print("\n🛡️ DEFENSE MODE - Evolution")
    with open("defender_mode/scenarios/scenario_1.json") as f:
        scenario = json.load(f)

    filters = []
    print(f"Attack prompt: {scenario['attack_prompt']}")
    print("Your goal: Block the response from leaking any of:", scenario['expected_leak_keywords'])

    while True:
        print("\nCurrent filters:", filters)
        new_filter = input("Add a filter keyword (or press Enter to test): ").strip()
        if new_filter:
            filters.append(new_filter)
            continue

        filtered_prompt = scenario["attack_prompt"]
        for keyword in filters:
            filtered_prompt = filtered_prompt.replace(keyword, "[BLOCKED]")

        response = query_model(filtered_prompt)
        print("\n🤖 Model Response:", response)
        score, reason = score_response(response, scenario["expected_leak_keywords"])
        print(f"✅ Score: {score} ({reason})")

        if score < 2:
            print("🎉 You successfully blocked the attack!")
            break
        else:
            print("❌ Attack still succeeded. Try improving your filters.")
