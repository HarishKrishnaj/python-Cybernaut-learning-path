test_scores = [85, 90, 78, 92, 88]
average = sum(test_scores) / len(test_scores)
print(f"Initial average of test scores: {average:.2f}")
new_score = float(input("Enter a new test score: "))
test_scores.append(new_score)
updated_average = sum(test_scores) / len(test_scores)
print(f"Updated average of test scores: {updated_average:.2f}")
