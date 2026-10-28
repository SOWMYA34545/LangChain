
from web_search import (
    ask_question,
    load_prompt_rules,
    save_prompt_rules,
    DEFAULT_PROMPT_RULES
)


def change_prompt_rules():
    current_rules = load_prompt_rules()

    print("\nCURRENT PROMPT RULES:")

    for index, rule in enumerate(current_rules, start=1):
        print(f"{index}. {rule}")

    print("\n1. Keep DEFAULT rules and add extra rules")
    print("2. Replace all rules")
    print("3. Keep current rules")

    choice = input("Choose (1-3): ").strip()

    if choice == "1":
        new_rules = DEFAULT_PROMPT_RULES.copy()
        print("\nEnter extra rules. Type DONE when finished.")

    elif choice == "2":
        new_rules = []
        print("\nEnter new rules. Type DONE when finished.")

    elif choice == "3":
        print("Current rules kept.")
        return

    else:
        print("Invalid choice.")
        return

    while True:
        rule = input("\nRule: ").strip()

        if rule.upper() == "DONE":
            break

        if rule:
            new_rules.append(rule)

    if choice == "2" and not new_rules:
        print("No new rules entered. Existing rules kept.")
        return

    save_prompt_rules(new_rules)
    print("\nPrompt rules saved successfully!")


def main():
    while True:
        print("\n========== LANGCHAIN WEBQUERY AI ==========")
        print("1. Change prompt rules")
        print("2. Give a question")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            change_prompt_rules()

        elif choice == "2":
            question = input("\nEnter your question: ").strip()

            if not question:
                print("Please enter a question.")
                continue

            try:
                print("\nSearching the web and generating the answer...")
                answer = ask_question(question)

                print("\nANSWER:")
                print("-" * 50)
                print(answer)
                print("-" * 50)

            except Exception as error:
                print("\nERROR:", error)

        elif choice == "3":
            print("Program ended.")
            break

        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
