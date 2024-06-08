import pandas as pd


def clean_food_truck_data():
    # Read the CSV file
    df = pd.read_csv("food-truck-data.csv")

    # Filter out food trucks with permit status not 'APPROVED'
    df = df[df["Status"] == "APPROVED"]

    # Select the desired columns
    desired_columns = [
        "Applicant",
        "FacilityType",
        "FoodItems",
        "Latitude",
        "Longitude",
        "LocationDescription",
        "dayshours",
    ]
    cleaned_df = df[desired_columns]

    # Save the cleaned data to a new CSV file
    cleaned_df.to_csv("food-truck-data-cleaned.csv", index=False)


clean_food_truck_data()
