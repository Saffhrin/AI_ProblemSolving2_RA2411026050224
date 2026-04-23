import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Insurance Claim System", page_icon="🧠", layout="centered")

# -------------------------------
# Title
# -------------------------------
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

st.markdown("---")

# -------------------------------
# Button
# -------------------------------
if st.button("🔍 Evaluate Claim"):

    # Convert to boolean
    pa = policy_active == "Yes"
    dv = documents_valid == "Yes"
    ar = accident_reported == "Yes"

    # -------------------------------
    # Display Input Facts
    # -------------------------------
    st.subheader("📌 Input Facts")
    st.write(f"Policy Active: {pa}")
    st.write(f"Documents Valid: {dv}")
    st.write(f"Accident Reported: {ar}")

    st.markdown("---")

    # -------------------------------
    # Rule Evaluation
    # -------------------------------
    st.subheader("⚙️ Rules Applied")

    decision = ""

    if pa and dv:
        st.success("✔ Rule Applied: Policy Active AND Documents Valid → TRUE")
        decision = "Claim Approved"

    elif not ar:
        st.error("✔ Rule Applied: Accident Not Reported → TRUE")
        decision = "Claim Rejected"

    else:
        st.warning("No strong rule satisfied → Default Decision Applied")
        decision = "Claim Rejected"

    st.markdown("---")

    # -------------------------------
    # Final Decision
    # -------------------------------
    st.subheader("📊 Final Decision")

    if decision == "Claim Approved":
        st.success("✅ Claim Approved")
    else:
        st.error("❌ Claim Rejected")

    # -------------------------------
    # Info Box
    # -------------------------------
    st.info("This system uses propositional logic rules for decision-making.")
