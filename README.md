# Cognifyz Data Analysis Internship Project

## Overview

This project presents a complete data analysis of a restaurant dataset as part of the Cognifyz Technologies Data Analysis Internship. The aim of the project is to explore restaurant trends, identify important patterns, and present the results through an interactive dashboard.

The analysis focuses on cuisines, city-wise restaurant distribution, price ranges, online delivery, table booking, ratings, votes, restaurant chains, and geographic locations.

## Objective

The main objective of this project is to perform exploratory data analysis on the restaurant dataset and convert the findings into meaningful insights.

The project helps answer questions such as:

- Which cuisines are most common?
- Which city has the highest number of restaurants?
- How are restaurants distributed across price ranges?
- Do restaurants with online delivery have better ratings?
- What rating range is most common?
- Which cuisine combinations are popular?
- Are there restaurant chains in the dataset?
- Is there a relationship between votes and ratings?
- Are higher-priced restaurants more likely to offer table booking or online delivery?

## Dataset Description

The dataset contains restaurant information with multiple attributes, including:

- Restaurant ID
- Restaurant Name
- Country Code
- City
- Address
- Locality
- Longitude
- Latitude
- Cuisines
- Average Cost for Two
- Currency
- Table Booking Availability
- Online Delivery Availability
- Price Range
- Aggregate Rating
- Rating Color
- Rating Text
- Votes

This dataset is suitable for performing descriptive analysis, comparison-based analysis, and visual exploration.

## Project Features

This project includes:

- Data loading and preprocessing
- Missing value checking
- Cuisine analysis
- City-wise restaurant analysis
- Price range distribution analysis
- Online delivery analysis
- Rating distribution analysis
- Cuisine combination analysis
- Geographic location analysis
- Restaurant chain analysis
- Votes and rating correlation analysis
- Price range comparison with online delivery and table booking
- Interactive dashboard using Streamlit

## Internship Task Coverage

## Level 1

### Task 1: Top Cuisines

The project identifies the top three most common cuisines in the dataset and calculates the percentage of restaurants serving each cuisine.

### Task 2: City Analysis

The analysis identifies the city with the highest number of restaurants. It also calculates the average rating of restaurants in each city and finds the city with the highest average rating.

### Task 3: Price Range Distribution

The project visualizes the distribution of restaurants across different price range categories and calculates the percentage of restaurants in each price range.

### Task 4: Online Delivery

The analysis calculates the percentage of restaurants that offer online delivery and compares the average ratings of restaurants with and without online delivery.

## Level 2

### Task 1: Restaurant Ratings

The project analyzes the distribution of aggregate ratings and identifies the most common rating range. It also calculates the average number of votes received by restaurants.

### Task 2: Cuisine Combination

The analysis identifies the most common cuisine combinations and checks whether certain combinations tend to have higher ratings.

### Task 3: Geographic Analysis

The project uses latitude and longitude values to visualize restaurant locations and identify location-based patterns.

### Task 4: Restaurant Chains

The analysis identifies restaurant chains by finding repeated restaurant names. It then compares their outlet count, average rating, total votes, and popularity.

## Level 3

### Task 1: Restaurant Reviews

The given dataset does not contain text review columns. Therefore, review keyword analysis and review length analysis cannot be completed using this dataset alone.

### Task 2: Votes Analysis

The project identifies restaurants with the highest and lowest number of votes. It also calculates the correlation between votes and aggregate rating.

### Task 3: Price Range vs Online Delivery and Table Booking

The analysis checks whether restaurants in higher price ranges are more likely to offer online delivery and table booking services.

## Dashboard Description

The project includes an interactive dashboard built using Streamlit.

The dashboard contains:

- Overview KPIs
- City filter
- Price range filter
- Rating range filter
- Charts
- Tables
- Map visualization
- Level-wise task sections

The dashboard allows users to interact with the data and view results dynamically.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit

## How to Run the Project

Install the required libraries:

```bash
pip install streamlit pandas matplotlib
