import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("bank_marketing.csv")

# Clean, format, and restructure the data.
df["year"] = 2022
df["month"] = pd.to_datetime(df["month"], format='%b').dt.month
df["last_contact_date"] = pd.to_datetime(df[["year", "month","day"]])
df.drop(columns=["year", "month","day"], inplace=True)

df["job"] = df["job"].str.replace(".","_")
df["education"] = df["education"].str.replace(".","_")
df.loc[df["education"]=="unknown","education" ] = np.nan

columns_to_convert = {
    "credit_default": "yes",
    "mortgage": "yes",
    "campaign_outcome": "yes",
    "previous_outcome": "success"
}

for column, true_value in columns_to_convert.items():
    df[column] = df[column].map(lambda x: 1 if x == true_value else 0).astype(bool)

client_cols_to_subset = ["client_id","age", "job", "marital","education","credit_default","mortgage"]
campaign_cols_to_subset =["client_id", "number_contacts", "contact_duration","previous_campaign_contacts","previous_outcome","campaign_outcome","last_contact_date"]
economics_cols_to_subset =["client_id","cons_price_idx", "euribor_three_months"]


client_subset = df[client_cols_to_subset]
campaign_subset = df[campaign_cols_to_subset]
economics_subset = df[economics_cols_to_subset]

# Save the cleaned and transformed data into new CSV files.

client_subset.to_csv("client.csv", index=False)
campaign_subset.to_csv("campaign.csv", index=False)
economics_subset.to_csv("economics.csv", index=False)
