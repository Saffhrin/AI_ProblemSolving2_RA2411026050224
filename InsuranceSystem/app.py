import streamlit as st

st.title("Insurance Claim Decision System")

st.subheader("Enter Claim Details")

policy_active = st.selectbox("Policy Active?", ["Yes", "No"])
documents_valid = st.selectbox("Documents Valid?", ["Yes", "No"])
accident_reported = st.selectbox("Accident Reported?", ["Yes", "No"])

if st.button("Evaluate Claim"):

    pa = policy_active == "Yes"
    dv = documents_valid == "Yes"
    ar = accident_reported == "Yes"

    st.subheader("Input Facts")
    st.write(f"Policy Active: {pa}")
    st.write(f"Documents Valid: {dv}")
    st.write(f"Accident Reported: {ar}")

    st.subheader("Rules Applied")

    if pa and dv:
        st.write("Policy Active AND Documents Valid → TRUE")
        decision = "Claim Approved"

    elif not ar:
        st.write("Accident Not Reported → TRUE")
        decision = "Claim Rejected"

    else:
        decision = "Claim Rejected"

    st.subheader("Final Decision")
    st.success(decision)
