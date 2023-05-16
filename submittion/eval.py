from sklearn.metrics import f1_score, accuracy_score

# Read the predicted values from preds.txt
with open('preds.txt', 'r') as file:
    preds = file.readlines()

# Read the true values from true.txt
with open('true.txt', 'r') as file:
    true = file.readlines()

# Remove any trailing whitespaces or newlines from the lines
preds = [line.strip() for line in preds]
true = [line.strip() for line in true]

# Calculate weighted F1 score
f1_weighted = f1_score(true, preds, average='weighted')

# Calculate accuracy
accuracy = accuracy_score(true, preds)

# Print the results
print("Weighted F1 Score:", f1_weighted)
print("Accuracy:", accuracy)
