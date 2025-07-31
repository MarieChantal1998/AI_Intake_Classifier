from classifier.py import classify_intake

if __name__ == "__main__":
    user_input = input("Paste client intake message here:\n")
    result = classify_intake(user_input)
    print("\n--- Classification Result ---")
    print(result)
