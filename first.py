
# Student Performance Prediction System

print("=== STUDENT PERFORMANCE PREDICTOR ===")

# Collect student data
name = input("Enter student name: ")

attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Daily study hours: "))
previous_marks = float(input("Previous exam percentage: "))

# Simple prediction logic
score = (
    attendance * 0.30 +
    min(study_hours / 8 * 100, 100) * 0.30 +
    previous_marks * 0.40
)

print("\n--- Prediction Result ---")
print("Student:", name)
print("Predicted Performance Score:", round(score, 2))

if score >= 50:
    print("Prediction: Likely to PASS")
else:
    print("Prediction: At Risk of FAILING")

print("Note: This is a rule-based demo, not a trained AI model.")
