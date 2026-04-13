import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')

sns.set_theme(
    style="dark",
    rc={
        "axes.facecolor": "#0f0f0f",
        "figure.facecolor": "#000000",
        "grid.color": "#444444",
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white"
    }
)

sns.set_palette("magma")

plt.rcParams['figure.figsize'] = (24, 12)

#HOW TO  LOAD DATA
df = pd.read_csv("netflix_titles.csv")

# THIS LINE USE FOR DATA CLEANING
df.drop_duplicates(inplace=True)

df['country'] = df['country'].fillna("Not Specified")
df['director'] = df['director'].fillna("Not Available")

# -------------------------------
# 🔍 KEY INSIGHTS (NEW 🔥)
# -------------------------------
print("🔍 Key Insights:")
print(f"✔ Total Content: {len(df)}")
print(f"✔ Movies: {df['type'].value_counts().get('Movie', 0)}")
print(f"✔ TV Shows: {df['type'].value_counts().get('TV Show', 0)}")


# LINE FOR DATA ANALYSIS 
type_count = df['type'].value_counts()
top_countries = df['country'].value_counts().head(10)
year_trend = df['release_year'].value_counts().sort_index().tail(10)
ratings = df['rating'].value_counts().head(10)

added_year = df['date_added'].dropna().apply(lambda x: x.split(",")[-1].strip())
added_year = added_year.value_counts().sort_index().tail(10)

#  MORE INSIGHTS
print(f"✔ Top Country: {df['country'].value_counts().idxmax()}")
print(f"✔ Most Common Rating: {ratings.idxmax()}")


# CREATING A DASHBOARD
fig, axes = plt.subplots(2, 3)

fig.patch.set_facecolor('#000000')

# THIS LINE FOR PIE CHART
colors = sns.color_palette("magma", len(type_count))
axes[0,0].pie(type_count,
              labels=type_count.index,
              autopct='%1.1f%%',
              startangle=90,
              colors=colors,
              radius=0.75)
axes[0,0].set_title("Content Distribution: Movies vs TV Shows",
                    fontsize=13, fontweight='bold', color='#FFA500')

#  TOP MOST COUNTRIES
sns.barplot(x=top_countries.values,
            y=top_countries.index,
            palette="magma",
            ax=axes[0,1])
axes[0,1].set_title("Top 10 Countries by Total Content Available",
                    fontsize=13, fontweight='bold', color='#FFA500')
axes[0,1].set_xlabel("Total Content Available", color='#00BFFF')
axes[0,1].set_ylabel("Country", color='#00BFFF')

# CONTENT GROWTH OVER THE YEARS
sns.lineplot(x=year_trend.index,
             y=year_trend.values,
             marker='o',
             linewidth=2.5,
             ax=axes[0,2])
axes[0,2].set_title("Yearly Content Release Trend (Last 10 Years)",
                    fontsize=13, fontweight='bold', color='#FFA500')
axes[0,2].set_xlabel("Year", color='#00BFFF')
axes[0,2].set_ylabel("Total Content Released", color='#00BFFF')

# CONTENT RATINGS
sns.barplot(x=ratings.index,
            y=ratings.values,
            palette="magma",
            ax=axes[1,0])
axes[1,0].set_title("Content Distribution by Rating",
                    fontsize=13, fontweight='bold', color='#FFA500')
axes[1,0].set_xlabel("Rating Category", color='#00BFFF')
axes[1,0].set_ylabel("Total Content Available", color='#00BFFF')
axes[1,0].tick_params(axis='x', rotation=40)

# HOW TO  CONTENT ADDED
sns.lineplot(x=added_year.index,
             y=added_year.values,
             marker='o',
             linewidth=2.5,
             ax=axes[1,1])
axes[1,1].set_title("Yearly Content Added on Netflix",
                    fontsize=13, fontweight='bold', color='#FFA500')
axes[1,1].set_xlabel("Year Added to Platform", color='#00BFFF')
axes[1,1].set_ylabel("Total Content Added", color='#00BFFF')
axes[1,1].tick_params(axis='x', rotation=40)

axes[1,2].axis('off')

for ax in axes.flat:
    ax.set_facecolor("#0f0f0f")
    ax.grid(alpha=0.2)

plt.figtext(0.5, 0.93,
            "Analyzing Content Trends, Ratings & Country Distribution",
            ha="center", fontsize=12, color='white')

# TITEL FOR PROJECT
plt.suptitle("Netflix Data Analysis & Visualization Dashboard",
             fontsize=18,
             fontweight='bold',
             color='#FF4C4C')


plt.tight_layout(pad=2.5)


manager = plt.get_current_fig_manager()
manager.window.state('zoomed')

plt.show()