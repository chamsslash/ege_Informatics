import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']].dropna()

X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = ['Age', 'Fare']
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_features = ['Sex', 'Embarked']
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(random_state=42))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, 'model_pipeline.joblib')
print("Модель сохранена!")

loaded_model = joblib.load('model_pipeline.joblib')
print("Loaded model accuracy:", accuracy_score(y_test, loaded_model.predict(X_test)))


def train_and_save_model(data_url, model_path):
    df = pd.read_csv(data_url)
    df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']].dropna()
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    joblib.dump(pipeline, model_path)
    return accuracy_score(y_test, y_pred)


accuracy = train_and_save_model(url, 'model_pipeline.joblib')
print(f"Pipeline завершён. Accuracy: {accuracy:.2%}")
