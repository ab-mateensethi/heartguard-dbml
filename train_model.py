import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# ---------------------------------------
# 1. Load Data
# ---------------------------------------
df = pd.read_csv("heart.csv")
print(df.head())
print(df.info())
# ---------------------------------------
# 2. Visualization
# ---------------------------------------
plt.hist(df["Age"])
plt.title("Distribution of Age")
plt.show()

sns.countplot(data=df, x="HeartDisease")
plt.title("Heart Disease Distribution (0 = No, 1 = Yes)")
plt.show()

# ---------------------------------------
# 3. Handle Missing Values
# ---------------------------------------
for col in df.columns:
    try:
        df[col] = df[col].fillna(df[col].median())
    except TypeError:
        df[col] = df[col].fillna(df[col].mode()[0])
# ---------------------------------------
# 4. Encode Categorical Columns
# ---------------------------------------
for col in df.select_dtypes(include="object"):
    df[col] = LabelEncoder().fit_transform(df[col])
print(df.select_dtypes)
# ---------------------------------------
# 5. Train-Test Split
# ---------------------------------------
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# 6. Train Models
# ---------------------------------------
dt = DecisionTreeClassifier()
log_reg = LogisticRegression(max_iter=200)
rf = RandomForestClassifier()

dt.fit(X_train, y_train)
log_reg.fit(X_train, y_train)
rf.fit(X_train, y_train)

# ---------------------------------------
# 7. Evaluate Random Forest 
# ---------------------------------------
y_pred = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Random Forest Confusion Matrix")
plt.show()

# ---------------------------------------
# 8. Save Model
# ---------------------------------------
joblib.dump(rf, "random_forest_model.pkl")