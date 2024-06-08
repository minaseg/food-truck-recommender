import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer


def export_food_truck_data():
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


export_food_truck_data()


def get_food_truck_recommendations(preferences, latitude, longitude):

    df = pd.read_csv("food-truck-data-cleaned.csv")

    # Preprocess food items using MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    df["FoodItems"] = df["FoodItems"].apply(
        lambda x: [item.strip() for item in x.split(":")]
    )
    food_item_matrix = mlb.fit_transform(df["FoodItems"])

    # Transform user preferences into the same format
    user_preferences_transformed = mlb.transform([preferences])[0]

    # Use NearestNeighbors to find the nearest trucks based on food items
    knn_food = NearestNeighbors(n_neighbors=10, metric="euclidean")
    knn_food.fit(food_item_matrix)
    food_distances, food_indices = knn_food.kneighbors([user_preferences_transformed])

    # Calculate proximity factor based on truck location
    user_location = np.array([[latitude, longitude]])
    truck_locations = df[["Latitude", "Longitude"]].values

    # Use NearestNeighbors to find the nearest trucks based on location
    knn_location = NearestNeighbors(n_neighbors=10, metric="euclidean")
    knn_location.fit(truck_locations)
    location_distances, location_indices = knn_location.kneighbors(user_location)

    # Combine food and location results
    combined_indices = np.concatenate((food_indices[0], location_indices[0]))
    unique_indices = np.unique(combined_indices)

    # Compute combined scores using weighted averaging
    food_scores = 1 - (food_distances[0] / np.max(food_distances[0]))
    location_scores = 1 - (location_distances[0] / np.max(location_distances[0]))

    combined_scores = []
    for idx in unique_indices:
        food_score = (
            food_scores[food_indices[0] == idx][0] if idx in food_indices[0] else 0
        )
        location_score = (
            location_scores[location_indices[0] == idx][0]
            if idx in location_indices[0]
            else 0
        )
        combined_scores.append((food_score + location_score) / 2)

    # Sort by combined scores and get the top 10
    top_indices = np.argsort(combined_scores)[-10:][::-1]
    top_food_trucks = df.iloc[unique_indices[top_indices]]

    # Filter out duplicate locations
    unique_locations = top_food_trucks.drop_duplicates(subset=["Latitude", "Longitude"])

    return unique_locations.to_json(orient="records")
