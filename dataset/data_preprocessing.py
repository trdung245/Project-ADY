import pandas as pd

def Remove_duplicate(df):
    # Convert the Date column to datetime format and keep only the year-month-day part
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    # Remove duplicate rows based on the Date column, keeping only the second occurrence for each day
    df = df.drop_duplicates(subset='Date', keep='last')

    return df

def filter_data_by_column(df1, df2, column_name):
    # Filter df1 to keep only rows where `column_name` values are in df2's `column_name`
    filtered_df = df1[df1[column_name].isin(df2[column_name])]

    return filtered_df


