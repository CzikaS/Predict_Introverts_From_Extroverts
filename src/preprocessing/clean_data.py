import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from src.utils.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR

# 1. Load Data
file_path = RAW_DATA_DIR / "train.csv"
df = pd.read_csv(file_path)
df_clean = df.drop(columns=['id'])

# 2. Encode Categorical/Target Variables
binary_map = {'No': 0, 'Yes': 1}
df_clean['Stage_fear'] = df_clean['Stage_fear'].map(binary_map)
df_clean['Drained_after_socializing'] = df_clean['Drained_after_socializing'].map(binary_map)

le = LabelEncoder()
df_clean['Personality'] = le.fit_transform(df_clean['Personality'])

# 3. Split the data
X = df_clean.drop('Personality', axis=1)
y = df_clean['Personality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Impute Missing Values
num_cols = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']
num_imputer = SimpleImputer(strategy='median')
X_train[num_cols] = num_imputer.fit_transform(X_train[num_cols])
X_test[num_cols] = num_imputer.transform(X_test[num_cols]) # transform only!

cat_cols = ['Stage_fear', 'Drained_after_socializing']
cat_imputer = SimpleImputer(strategy='most_frequent')
X_train[cat_cols] = cat_imputer.fit_transform(X_train[cat_cols])
X_test[cat_cols] = cat_imputer.transform(X_test[cat_cols]) # transform only!

# 5. Scale Data
scaler = StandardScaler()
scaler.fit(X_train[num_cols])
X_train[num_cols] = scaler.transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# 6. Save Data
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
X_train.to_csv(PROCESSED_DATA_DIR / "X_train.csv", index=False)
X_test.to_csv(PROCESSED_DATA_DIR / "X_test.csv", index=False)
y_train.to_csv(PROCESSED_DATA_DIR / "y_train.csv", index=False)
y_test.to_csv(PROCESSED_DATA_DIR / "y_test.csv", index=False)

print(f"Data successfully cleaned, imputed, scaled, and saved to {PROCESSED_DATA_DIR}")