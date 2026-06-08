import re
import math
import random
import string


COMMON_PASSWORDS = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "password123",
    "abc123"
}


def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def generate_strong_password(length=16):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def analyze_password(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 16:
        score += 4
    elif len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        suggestions.append(
            "Increase password length to at least 12 characters."
        )

    # Complexity Checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        score = max(score - 3, 0)
        suggestions.append("Avoid commonly used passwords.")

    # Determine Strength
    if score <= 3:
        strength = "WEAK"
    elif score <= 6:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    entropy = calculate_entropy(password)

    return strength, score, entropy, suggestions


def main():
    print("=" * 50)
    print("      PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = input("\nEnter Password: ")

    strength, score, entropy, suggestions = analyze_password(password)

    print("\n----- ANALYSIS REPORT -----")
    print(f"Password Length : {len(password)}")
    print(f"Strength        : {strength}")
    print(f"Score           : {score}/8")
    print(f"Entropy         : {entropy} bits")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"• {suggestion}")

        print("\nSuggested Strong Password:")
        print(generate_strong_password())
    else:
        print("\nExcellent! Your password meets all criteria.")

    print("-" * 50)


if __name__ == "__main__":
    main()