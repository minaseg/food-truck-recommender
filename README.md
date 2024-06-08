# Food Truck Recommendation System

This is a Django-based web application that provides food truck recommendations based on user preferences and location. The application uses machine learning algorithms to recommend food trucks that best match the user's preferences and are in proximity to the user's location.

## Features

- User can input their location and food preference to get recommendations for nearby food trucks.
- Stores user preferences in the database.
- Provides recommendations using a custom algorithm.

## Technologies Used

- Django REST Framework
- Pandas
- NumPy
- Scikit-learn

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python >= 3.5
- pip
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/food-truck-recommendation-system.git
   cd food-truck-recommendation-system
   ```

2. **Create a virtual environment**

   ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Instance the dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the development server**

   ```sh
   python manage.py runserver
   ```

   The application will be available at http://127.0.0.1:8000/.

## Usage

1.  **Access the API endpoint**

    ```sh
    POST /recommend_food_trucks/
    ```

    ## Example JSON Body

    Here is an example of a JSON body that you can use for your request:

    ```json
    {
      "latitude": 10.023942,
      "longitude": 209342,
      "preference": "hot dog"
    }
    ```

## Improvements for the Food Truck Recommendation System

- Utilize the "dayshour" Column:

  - For food trucks where the "dayshour" column is empty, make assumptions based on common practices.
  - Gather more specific data from these food trucks to improve accuracy.
