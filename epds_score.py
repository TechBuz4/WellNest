
def list_answers(data):
    epds_score = sum(data)
    q3 = data[2]
    q4 = data[3]
    q5 = data[4]
    q10 = data[5]
    return epds_score, q3, q4, q5, q10

def assess_harm_risk(q10):
    """Check if there's potential harm or psychosis risk."""
    if q10 > 0:
        return {
            "Assessment": "POTENTIAL HARM/PSYCHOSIS / HIGH RISK",
            "Action": [
                "Assess harm intentions and for psychosis:",
                "  - Any previous harm attempts?",
                "  - Any current plan to harm self or others?",
                "  - Signs of psychosis (hallucinations, disorganized thoughts, etc.)",
                "Can we notify next of kin (if she agrees).",
                "Contact/take to: Family Doctor, Crisis Services, or Emergency Room.",
                "Arrange emergency medical assessment.",
                "Share findings with the health care team."
            ]
        }
    return None



def assess_depression_level(epds_score):
    """Determine the depression risk level and actions based on EPDS score."""
    if epds_score < 10:
        return {
            "Assessment": "UNLIKELY TO BE DEPRESSED / LOW RISK",
            "Action": [
                "  - Encourage joy, relaxation, and confidence.",
                "  - Exercise 20–30 minutes daily.",
                "  - Sleep 6 hours in 24.",
                "  - Eat healthy and stay hydrated.",
                "  - Avoid alcohol, tobacco, and drugs.",
                "  - Reach out for support and join mothers’ groups."
            ]
        }
    elif 10 <= epds_score <= 11:
        return {
            "Assessment": "POSSIBLE DEPRESSION / MID RISK",
            "Action": [
                "Confirm score and ask about harm thoughts.",
                "Discuss concerns and offer referral.",
                "Share concerns with healthcare team:",
                "  - Mental health services",
                "  - Community supports",
                "  - Family doctor or nurse practitioner",
                "Increase contact via visits or calls.",
                "Repeat EPDS in 2 weeks.",
                "Encourage family involvement."
            ]
        }
    else:
        return {
            "Assessment": "PROBABLE DEPRESSION / HIGH RISK",
            "Action": [
                "Confirm score and ask about harm thoughts.",
                "Take action: Offer referral to a Family Doctor or Nurse Practitioner for medical management.",
                "Share concerns with healthcare team.",
                "Encourage family involvement.",
                "Promote Positive Mental Health.",
                "Increase contact via visits.",
                "Offer EPDS to partner.",
                "Screen for depression."
            ]
        }


def assess_anxiety(q3, q4, q5):
    """Check if anxiety score is high based on Q3–Q5."""
    anxiety_score = q3 + q4 + q5
    if anxiety_score > 4:
        return {
            "Anxiety_Flag": True,
            "Additional_Action": [
                "Probable anxiety detected in EPDS.",
                "Confirm score and ask about harm thoughts.",
                "Promote mental well-being:",
                "  - Encourage relaxation and emotional support.",
                "  - Discuss concerns and share with healthcare team:",
                "    • Mental health services",
                "    • Community supports",
                "    • Family doctor or nurse practitioner",
                "Increase contact via visits or calls.",
                "Repeat EPDS in 2 weeks.",
                "Encourage family involvement."
            ]
        }
    else:
        return {"Anxiety_Flag": False}


def epds_assessment(epds_score, q3, q4, q5, q10):
    results = {
        "EPDS_Score": epds_score,
        "Questions": {
            "Q3": q3,
            "Q4": q4,
            "Q5": q5,
            "Q10": q10
        }
    }
    results.update(assess_harm_risk(q10))
    results.update(assess_depression_level(epds_score))
    results.update(assess_anxiety(q3, q4, q5))
    return results


def print_epds_results(results):
    print("\n" + "="*50)
    print(f"🩺 Assessment: {results['Assessment']}")
    print("="*50 + "\n")

    if 'Action' in results:
        print("📋 Recommended Actions:")
        for action in results['Action']:
            print(f" - {action}")
        print()

    if results.get('Anxiety_Flag'):
        print("⚠️ Additional Note: Probable Anxiety Detected")
        print("📋 Additional Recommended Actions:")
        for action in results.get('Additional_Action', []):
            print(f" - {action}")
        print()

