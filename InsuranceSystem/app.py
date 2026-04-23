import streamlit as st
import pandas as pd

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="Insurance Claim System", page_icon="🧠")

st.title("🧠 Insurance Claim Decision System")
st.markdown("### Rule-Based Inference using Propositional Logic")
st.markdown("---")

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📥 Enter Claim Details")

col1, col2 = st.columns(2)

with col1:
    policy_active = st.selectbox("Policy Active?", ["Yes", "No"])
    documents_valid = st.selectbox("Documents Valid?", ["Yes", "No"])

with col2:
    accident_reported = st.selectbox("Accident Reported?", ["Yes", "No"])
    fraud_detected = st.selectbox("Fraud Detected?", ["Yes", "No"])

st.markdown("---")

# -------------------------------
# Solve Button
# -------------------------------
if st.button("🔍 Evaluate Claim"):

    # Convert to boolean
    pa = policy_active == "Yes"
    dv = documents_valid == "Yes"
    ar = accident_reported == "Yes"
    fr = fraud_detected == "Yes"

    # -------------------------------
    # Input Facts Table
    # -------------------------------
    st.subheader("📌 Input Facts")

    facts_df = pd.DataFrame({
        "Parameter": ["Policy Active", "Documents Valid", "Accident Reported", "Fraud Detected"],
        "Value": [pa, dv, ar, fr]
    })

    st.table(facts_df)

    st.markdown("---")

    # -------------------------------
    # Rule Definitions
    # -------------------------------
    rules = [
        ("Policy Active AND Documents Valid", pa and dv, "Approve"),
        ("Accident NOT Reported", not ar, "Reject"),
        ("Fraud Detected", fr, "Reject")
    ]

    # -------------------------------
    # Rule Evaluation Table
    # -------------------------------
    st.subheader("⚙️ Rule Evaluation")

    rule_results = []

    for rule, condition, result in rules:
        rule_results.append({
            "Rule": rule,
            "Condition Result": condition,
            "Action": result if condition else "-"
        })

    rules_df = pd.DataFrame(rule_results)
    st.table(rules_df)

    st.markdown("---")

    # -------------------------------
    # Decision Logic
    # -------------------------------
    decision = "Reject"

    if pa and dv:
        decision = "Approve"
    elif not ar or fr:
        decision = "Reject"

    # -------------------------------
    # Final Decision
    # -------------------------------
    st.subheader("📊 Final Decision")

    if decision == "Approve":
        st.success("✅ Claim Approved")
    else:
        st.error("❌ Claim Rejected")

    # -------------------------------
    # Explanation
    # -------------------------------
    st.subheader("🧾 Explanation")

    if decision == "Approve":
        st.info("Approved because policy is active and documents are valid.")
    else:
        st.info("Rejected due to rule violation (fraud detected, missing report, or invalid documents).")
