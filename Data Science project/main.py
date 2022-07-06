# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
data = pd.read_csv("./data/Enrollment-in-school-2011-12-India.csv")

pd.set_option("display.max_columns", data.shape[1])
data.head()


# %%
data.set_index("States / Union Territories", inplace=True)
data.head()


# %%
data.columns


# %%
data.columns = [i.split(" - ", 1)[1] for i in data.columns]
data.columns


# %%
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")


# %%
total_boys = data["GrandTotal-Pre-Primary- XII - Boys"].sum()
total_girls = data["GrandTotal-Pre-Primary- XII - Girls"].sum()
total_boys, total_girls


# %%
plt.title("Total girls & boys enrollment in 2011-12")
plt.pie([total_boys, total_girls], labels=["Total boys", "Total girls"],
        colors=["#00FFCC", "#00CCFF"], autopct="%.2f%%",
        wedgeprops={"edgecolor": "black"}, shadow=True)
plt.show()


# %%
top_10_total_girls = data["GrandTotal-Pre-Primary- XII - Girls"].nlargest(11)[
    1:]
top_10_total_boys = data["GrandTotal-Pre-Primary- XII - Boys"].nlargest(11)[1:]
girls_index = top_10_total_girls.index
boys_index = top_10_total_boys.index


# %%
plt.title("Top 10 States / UT having highest girls Enrollment")
plt.barh(girls_index, top_10_total_girls)
plt.xlabel("Enrollments (in log)")
plt.ylabel("States/UT")
plt.show()


# %%
plt.title("Top 10 States / UT having highest boys Enrollment")
plt.barh(boys_index, top_10_total_boys)
plt.xlabel("Enrollments (in log)")
plt.ylabel("States/UT")
plt.show()
