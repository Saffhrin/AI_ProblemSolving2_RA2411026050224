# Rule-Based Insurance Claim System

def evaluate_claim(policy_active, documents_valid, accident_reported):
    print("\n--- Evaluating Rules ---")

    # Rule 1
    if policy_active and documents_valid:
        print("Rule Applied: Policy Active AND Documents Valid → TRUE")
        return "Claim Approved"

    # Rule 2
    if not accident_reported:
        print("Rule Applied: Accident Not Reported → TRUE")
        return "Claim Rejected"

    return "Claim Rejected"


# -------------------------------
# User Input
# -------------------------------

print("Insurance Claim Decision System\n")

policy_active = input("Is Policy Active? (yes/no): ").lower() == "yes"
documents_valid = input("Are Documents Valid? (yes/no): ").lower() == "yes"
accident_reported = input("Was Accident Reported? (yes/no): ").lower() == "yes"

# -------------------------------
# Output
# -------------------------------

print("\n--- Input Facts ---")
print(f"Policy Active: {policy_active}")
print(f"Documents Valid: {documents_valid}")
print(f"Accident Reported: {accident_reported}")

decision = evaluate_claim(policy_active, documents_valid, accident_reported)

print("\n--- Final Decision ---")
print(decision)
