# 1. Correct the file path (just use the filename)
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

from src.utils.paths import RAW_DATA_DIR
import pandas as pd
file_path = RAW_DATA_DIR / "train.csv"
df = pd.read_csv(file_path)

df_clean= df.drop(columns=['id'])

# 3. Handle Missing Values using SimpleImputer as per lecture slides

# --- For Numerical Columns: Use Median ---
# Median is often preferred over mean if there are potential outliers
num_cols = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']
num_imputer = SimpleImputer(strategy='median')
df_clean[num_cols] = num_imputer.fit_transform(df_clean[num_cols])

# --- For Categorical Columns: Use Most Frequent (Mode) ---
cat_cols = ['Stage_fear', 'Drained_after_socializing']
cat_imputer = SimpleImputer(strategy='most_frequent')
df_clean[cat_cols] = cat_imputer.fit_transform(df_clean[cat_cols])

# 4. Verify that there are no more missing values
print("Remaining Null Values:\n", df_clean.isnull().sum())

# View the result

binary_map = {'No': 0, 'Yes': 1}
df_clean['Stage_fear'] = df_clean['Stage_fear'].map(binary_map)
df_clean['Drained_after_socializing'] = df_clean['Drained_after_socializing'].map(binary_map)

# 2. Encoding the Target variable (Personality)
# We use LabelEncoder to turn 'Extrovert'/'Introvert' into 0/1 [cite: 621]
le = LabelEncoder()
df_clean['Personality'] = le.fit_transform(df_clean['Personality'])

# View the mapping for the target
print("Target Mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

# View the result
#print(df_clean.head())
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Split the data into Training (70%) and Testing (30%)
# This must happen BEFORE scaling to avoid data leakage
X = df_clean.drop('Personality', axis=1)
y = df_clean['Personality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Initialize the StandardScaler
# This calculates z = (x - mean) / std
scaler = StandardScaler()

# 3. Fit on Training Data ONLY
# Here, the scaler "learns" the mean and std of each numerical column
num_cols = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']
scaler.fit(X_train[num_cols])

# 4. Transform both Training and Test sets
# We apply the transformation to the numerical columns
X_train[num_cols] = scaler.transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# Verify results: Training mean should be ~0 and std should be ~1
print("Scaled Training Mean:\n", X_train[num_cols].mean())
print("\nScaled Training Std:\n", X_train[num_cols].std())
