import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


DATASET_PATH = r"C:\Users\ASUS TUF\Downloads\Dataset .csv"


st.set_page_config(
    page_title="Cognifyz Data Analysis Dashboard",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    data.columns = data.columns.str.strip()
    return data


def plot_bar(series, title, xlabel, ylabel, color="#2563eb", rotation=30):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    series.plot(kind="bar", ax=ax, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=rotation)
    plt.tight_layout()
    st.pyplot(fig)


def plot_grouped_bar(df, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(9, 4.8))
    df.plot(kind="bar", ax=ax, color=["#22c55e", "#8b5cf6"])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=0)
    plt.tight_layout()
    st.pyplot(fig)


def yes_percentage_by_group(data, group_col, target_col):
    return (
        data.groupby(group_col)[target_col]
        .apply(lambda x: (x.astype(str).str.lower() == "yes").mean() * 100)
        .round(2)
    )


df = load_data(DATASET_PATH)

st.title("Cognifyz Data Analysis Dashboard")
st.caption("Interactive restaurant dataset dashboard for internship presentation")

st.sidebar.header("Dashboard Filters")

city_options = sorted(df["City"].dropna().unique())
selected_cities = st.sidebar.multiselect(
    "Select cities",
    options=city_options,
    default=[],
)

price_options = sorted(df["Price range"].dropna().unique())
selected_price_ranges = st.sidebar.multiselect(
    "Select price ranges",
    options=price_options,
    default=price_options,
)

rating_min, rating_max = st.sidebar.slider(
    "Aggregate rating range",
    min_value=float(df["Aggregate rating"].min()),
    max_value=float(df["Aggregate rating"].max()),
    value=(float(df["Aggregate rating"].min()), float(df["Aggregate rating"].max())),
    step=0.1,
)

filtered_df = df.copy()
if selected_cities:
    filtered_df = filtered_df[filtered_df["City"].isin(selected_cities)]

filtered_df = filtered_df[filtered_df["Price range"].isin(selected_price_ranges)]
filtered_df = filtered_df[
    (filtered_df["Aggregate rating"] >= rating_min)
    & (filtered_df["Aggregate rating"] <= rating_max)
]

if filtered_df.empty:
    st.warning("No restaurants match the selected filters. Please change the sidebar filters.")
    st.stop()

st.subheader("Overview")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Restaurants", f"{len(filtered_df):,}")
kpi2.metric("Cities", f"{filtered_df['City'].nunique():,}")
kpi3.metric("Average Rating", f"{filtered_df['Aggregate rating'].mean():.2f}")
online_rate = (filtered_df["Has Online delivery"].str.lower() == "yes").mean() * 100
kpi4.metric("Online Delivery", f"{online_rate:.2f}%")

with st.expander("Preview Dataset"):
    st.dataframe(filtered_df.head(50), use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Level 1", "Level 2", "Level 3"])

with tab1:
    st.header("Level 1 Tasks")

    st.subheader("Task 1: Top Cuisines")
    cuisines = filtered_df["Cuisines"].dropna().str.split(",").explode().str.strip()
    top_cuisines = cuisines.value_counts().head(3)
    top_cuisine_percentages = (top_cuisines / len(filtered_df) * 100).round(2)
    top_cuisine_result = pd.DataFrame(
        {
            "Restaurant Count": top_cuisines,
            "Percentage of Restaurants": top_cuisine_percentages,
        }
    )
    left, right = st.columns([1, 1])
    with left:
        st.dataframe(top_cuisine_result, use_container_width=True)
    with right:
        plot_bar(top_cuisines, "Top 3 Cuisines", "Cuisine", "Number of Restaurants")

    st.subheader("Task 2: City Analysis")
    city_counts = filtered_df["City"].value_counts()
    city_average_ratings = (
        filtered_df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
    )
    st.write(
        f"City with highest number of restaurants: "
        f"**{city_counts.idxmax()}** with **{city_counts.max():,}** restaurants."
    )
    st.write(
        f"City with highest average rating: "
        f"**{city_average_ratings.idxmax()}** with **{city_average_ratings.max():.2f}** average rating."
    )
    left, right = st.columns([1, 1])
    with left:
        plot_bar(
            city_counts.head(10),
            "Top 10 Cities by Restaurant Count",
            "City",
            "Number of Restaurants",
            color="#6366f1",
            rotation=45,
        )
    with right:
        st.dataframe(city_average_ratings.head(10).round(2), use_container_width=True)

    st.subheader("Task 3: Price Range Distribution")
    price_counts = filtered_df["Price range"].value_counts().sort_index()
    price_percentages = (price_counts / len(filtered_df) * 100).round(2)
    price_result = pd.DataFrame(
        {"Restaurant Count": price_counts, "Percentage": price_percentages}
    )
    left, right = st.columns([1, 1])
    with left:
        st.dataframe(price_result, use_container_width=True)
    with right:
        plot_bar(
            price_counts,
            "Price Range Distribution",
            "Price Range",
            "Number of Restaurants",
            color="#f97316",
            rotation=0,
        )

    st.subheader("Task 4: Online Delivery")
    rating_by_delivery = (
        filtered_df.groupby("Has Online delivery")["Aggregate rating"].mean().round(2)
    )
    st.write(f"Percentage of restaurants offering online delivery: **{online_rate:.2f}%**")
    left, right = st.columns([1, 1])
    with left:
        st.dataframe(rating_by_delivery, use_container_width=True)
    with right:
        plot_bar(
            rating_by_delivery,
            "Average Rating by Online Delivery",
            "Has Online Delivery",
            "Average Rating",
            color="#22c55e",
            rotation=0,
        )

with tab2:
    st.header("Level 2 Tasks")

    st.subheader("Task 1: Restaurant Ratings")
    rating_bins = [-0.01, 1, 2, 3, 4, 5]
    rating_labels = ["0-1", "1-2", "2-3", "3-4", "4-5"]
    filtered_df = filtered_df.copy()
    filtered_df["Rating Range"] = pd.cut(
        filtered_df["Aggregate rating"],
        bins=rating_bins,
        labels=rating_labels,
        include_lowest=True,
    )
    rating_distribution = filtered_df["Rating Range"].value_counts().sort_index()
    most_common_rating_range = rating_distribution.idxmax()
    average_votes = filtered_df["Votes"].mean()
    st.write(f"Most common rating range: **{most_common_rating_range}**")
    st.write(f"Average number of votes: **{average_votes:.2f}**")
    left, right = st.columns([1, 1])
    with left:
        plot_bar(
            rating_distribution,
            "Rating Range Distribution",
            "Rating Range",
            "Number of Restaurants",
            color="#10b981",
            rotation=0,
        )
    with right:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.hist(filtered_df["Aggregate rating"], bins=20, color="#0ea5e9", edgecolor="white")
        ax.set_title("Aggregate Rating Histogram")
        ax.set_xlabel("Aggregate Rating")
        ax.set_ylabel("Number of Restaurants")
        st.pyplot(fig)

    st.subheader("Task 2: Cuisine Combination")
    common_cuisine_combinations = filtered_df["Cuisines"].dropna().value_counts().head(10)
    cuisine_combination_ratings = (
        filtered_df.dropna(subset=["Cuisines"])
        .groupby("Cuisines")
        .agg(
            Restaurant_Count=("Restaurant ID", "count"),
            Average_Rating=("Aggregate rating", "mean"),
            Average_Votes=("Votes", "mean"),
        )
        .query("Restaurant_Count >= 5")
        .sort_values(["Average_Rating", "Restaurant_Count"], ascending=[False, False])
        .head(10)
        .round(2)
    )
    left, right = st.columns([1, 1])
    with left:
        st.write("Most common cuisine combinations")
        st.dataframe(common_cuisine_combinations, use_container_width=True)
    with right:
        st.write("Higher rated cuisine combinations, minimum 5 restaurants")
        st.dataframe(cuisine_combination_ratings, use_container_width=True)

    st.subheader("Task 3: Geographic Analysis")
    geo_df = filtered_df[(filtered_df["Latitude"] != 0) & (filtered_df["Longitude"] != 0)].copy()
    st.write(f"Restaurants with valid coordinates: **{len(geo_df):,}**")
    if not geo_df.empty:
        map_df = geo_df.rename(columns={"Latitude": "lat", "Longitude": "lon"})
        st.map(map_df[["lat", "lon"]])

    st.subheader("Task 4: Restaurant Chains")
    restaurant_chains = (
        filtered_df.groupby("Restaurant Name")
        .agg(
            Outlet_Count=("Restaurant ID", "count"),
            Average_Rating=("Aggregate rating", "mean"),
            Total_Votes=("Votes", "sum"),
            Average_Votes=("Votes", "mean"),
        )
        .query("Outlet_Count > 1")
        .sort_values(["Outlet_Count", "Total_Votes"], ascending=False)
        .round(2)
    )
    st.write(f"Number of restaurant chains found: **{len(restaurant_chains):,}**")
    st.dataframe(restaurant_chains.head(25), use_container_width=True)

with tab3:
    st.header("Level 3 Tasks")

    st.subheader("Task 1: Restaurant Reviews")
    possible_review_columns = [
        col
        for col in filtered_df.columns
        if any(word in col.lower() for word in ["review", "comment", "feedback", "text"])
    ]
    if possible_review_columns:
        st.success(f"Review columns found: {possible_review_columns}")
    else:
        st.warning(
            "The provided dataset does not contain a review/comment text column. "
            "So positive/negative keyword analysis and review-length analysis cannot be completed from this CSV alone."
        )

    st.subheader("Task 2: Votes Analysis")
    highest_votes_restaurant = filtered_df.loc[filtered_df["Votes"].idxmax()]
    lowest_votes_restaurant = filtered_df.loc[filtered_df["Votes"].idxmin()]
    votes_rating_correlation = filtered_df["Votes"].corr(filtered_df["Aggregate rating"])
    left, right, third = st.columns(3)
    left.metric("Highest Votes", f"{int(highest_votes_restaurant['Votes']):,}")
    right.metric("Lowest Votes", f"{int(lowest_votes_restaurant['Votes']):,}")
    third.metric("Votes-Rating Correlation", f"{votes_rating_correlation:.3f}")
    st.write("Highest voted restaurant")
    st.dataframe(
        highest_votes_restaurant[
            ["Restaurant Name", "City", "Votes", "Aggregate rating"]
        ].to_frame("Value"),
        use_container_width=True,
    )
    st.write("Lowest voted restaurant")
    st.dataframe(
        lowest_votes_restaurant[
            ["Restaurant Name", "City", "Votes", "Aggregate rating"]
        ].to_frame("Value"),
        use_container_width=True,
    )
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.scatter(
        filtered_df["Votes"],
        filtered_df["Aggregate rating"],
        alpha=0.45,
        s=14,
        color="#2563eb",
    )
    ax.set_title("Votes vs Aggregate Rating")
    ax.set_xlabel("Votes")
    ax.set_ylabel("Aggregate Rating")
    st.pyplot(fig)

    st.subheader("Task 3: Price Range vs Online Delivery and Table Booking")
    online_delivery_by_price = yes_percentage_by_group(
        filtered_df, "Price range", "Has Online delivery"
    )
    table_booking_by_price = yes_percentage_by_group(
        filtered_df, "Price range", "Has Table booking"
    )
    services_by_price = pd.DataFrame(
        {
            "Online Delivery Yes %": online_delivery_by_price,
            "Table Booking Yes %": table_booking_by_price,
        }
    )
    left, right = st.columns([1, 1])
    with left:
        st.dataframe(services_by_price, use_container_width=True)
    with right:
        plot_grouped_bar(
            services_by_price,
            "Service Availability by Price Range",
            "Price Range",
            "Restaurants Offering Service (%)",
        )
