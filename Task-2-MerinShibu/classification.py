from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report


# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Iris dataset loaded successfully!")
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])
print("Target classes:", iris.target_names)


# 2. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# 3. Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature scaling completed successfully!")


# 4. Create and train the KNN model
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

print("KNN model trained successfully!")


# 5. Make predictions
y_pred = knn.predict(X_test)

print("Predictions completed successfully!")
print("Predicted classes:", iris.target_names[y_pred])


# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Model Accuracy (%):", accuracy * 100)


# 7. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# 8. F1 Score
f1 = f1_score(y_test, y_pred, average="weighted")

print("F1 Score:", f1)


# 9. Classification Report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))