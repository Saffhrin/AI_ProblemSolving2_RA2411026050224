# Rule-Based Insurance Claim Decision System

## Problem Description
This system evaluates insurance claims using rule-based inference and propositional logic. It determines whether a claim should be approved or rejected based on predefined logical rules.

## Algorithm Used
Rule-Based Inference using Propositional Logic.

## Rules
- IF Policy Active AND Documents Valid THEN Approve Claim  
- IF Accident Not Reported THEN Reject Claim  

## Input Facts
- Policy Active (Yes/No)  
- Documents Valid (Yes/No)  
- Accident Reported (Yes/No)  

## Execution Steps

### Run Locally
1. Navigate to InsuranceSystem folder  
2. Run:
   python main.py  

### Run Online (Web App)
Open the Streamlit application:  
https://aiproblemsolving2ra2411026050224-m4z5snsevsczqmjpmmmgnh.streamlit.app/

## Sample Input
Policy Active = Yes  
Documents Valid = Yes  
Accident Reported = Yes  

## Sample Output
Claim Approved  

## Output Display
- Input facts  
- Rules applied  
- Final decision  

## Contributed by
X.P.Saffhrin , RA2411026050224

## Conclusion
This project demonstrates how propositional logic can be used to automate decision-making in real-world applications like insurance claim processing.
