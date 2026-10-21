import pandas as pd
import numpy as np

def clean_retail_data(df, imputation_values=None, is_train=True):
    """
    Cleans and preprocesses the retail store inventory dataset.
    
    Parameters:
    - df (pd.DataFrame): Raw input dataframe.
    - dict: Pre-computed median/mode values for imputation (required for val/test sets).
    - bool: True if processing the training set, False for validation/test sets.
    
    Returns:
    - tuple: (cleaned_dataframe, computed_imputation_values)
    """
    # Create a copy to avoid SettingWithCopyWarning
    df_clean = df.copy()
    
    # 1. Type Conversions
    if 'Date' in df_clean.columns:
        df_clean['Date'] = pd.to_datetime(df_clean['Date'])
        
    # Ensure numerical columns are properly typed
    numeric_cols = ['Inventory Level', 'Units Sold', 'Units Ordered', 
                    'Demand Forecast', 'Price', 'Discount', 'Competitor Pricing']
    for col in numeric_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # 2. Correct Anomalous Negative Values (e.g., Demand Forecast)
    # Convert invalid negative values to NaN so they can be properly imputed
    if 'Demand Forecast' in df_clean.columns:
        df_clean.loc[df_clean['Demand Forecast'] < 0, 'Demand Forecast'] = np.nan
        
    # Also check other columns where negative values shouldn't normally exist
    for col in ['Inventory Level', 'Units Sold', 'Units Ordered', 'Price']:
        if col in df_clean.columns:
            df_clean.loc[df_clean[col] < 0, col] = np.nan

    # 3. Handle Imputation
    if is_train:
        # Compute statistics strictly from the training data to prevent data leakage
        imputation_values = {}
        for col in numeric_cols:
            if col in df_clean.columns:
                imputation_values[col] = df_clean[col].median()
                
        # Categorical modes
        categorical_cols = ['Category', 'Region', 'Weather Condition', 'Holiday/Promotion']
        for col in categorical_cols:
            if col in df_clean.columns:
                imputation_values[col] = df_clean[col].mode()[0] if not df_clean[col].mode().empty else 'Unknown'
    
    # Apply imputation values (either newly computed from train, or passed from train to val/test)
    if imputation_values:
        for col, val in imputation_values.items():
            if col in df_clean.columns:
                if col in numeric_cols:
                    df_clean[col] = df_clean[col].fillna(val)
                else:
                    df_clean[col] = df_clean[col].fillna(val)

    # Fill any remaining categorical blanks with "Unknown"
    categorical_cols = ['Category', 'Region', 'Weather Condition', 'Holiday/Promotion']
    for col in categorical_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna('Unknown')

    return df_clean, imputation_values

# preprocess.py
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def build_preprocessor(X_train):
    """
    Identifies feature types and builds a scikit-learn preprocessing pipeline.
    """
    # Identify feature types from the training set
    numeric_features = X_train.select_dtypes(
        include=["number", "bool"]
    ).columns.tolist()

    categorical_features = [
        col for col in X_train.columns
        if col not in numeric_features
    ]

    print("Numeric features:", numeric_features)
    print("Categorical features:", categorical_features)

    # Compatibility with different scikit-learn versions
    try:
        encoder = OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        )
    except TypeError:
        encoder = OneHotEncoder(
            handle_unknown="ignore",
            sparse=False
        )

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", encoder)
    ])

    transformers = []

    if numeric_features:
        transformers.append(
            ("numeric", numeric_pipeline, numeric_features)
        )

    if categorical_features:
        transformers.append(
            ("categorical", categorical_pipeline, categorical_features)
        )

    preprocessor = ColumnTransformer(
        transformers=transformers,
        remainder="drop"
    )

    print("\nPreprocessing pipeline created successfully!")
    return preprocessor, numeric_features, categorical_features