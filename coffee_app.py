# ☕ Aesthetic Coffee Data App

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# -------------------- Data --------------------
coffee = ['Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Cold Brew']
price = [120, 180, 200, 220, 160]
sales = np.random.randint(20, 100, 5)

# Create DataFrame (NO EXTRA SPACE HERE ✅)
df = pd.DataFrame({
    'Coffee': coffee,
    'Price': price,
    'Sales': sales
})

print("\n☕ Coffee Menu Data:\n")
print(df)

# -------------------- Analysis --------------------
print("\n💡 Insights:")
print("Average Price:", df['Price'].mean())
print("Total Sales:", df['Sales'].sum())

# -------------------- Matplotlib Plot --------------------
plt.figure()
plt.bar(df['Coffee'], df['Sales'])
plt.title('Coffee Sales')
plt.xlabel('Coffee Type')
plt.ylabel('Sales')
plt.show()

# -------------------- Plotly Chart --------------------
fig = px.pie(df, names='Coffee', values='Sales', title='☕ Coffee Popularity')
fig.show()

# -------------------- Recommendation --------------------
best = df.loc[df['Sales'].idxmax()]
print(f"\n🔥 Most Loved Coffee: {best['Coffee']} with {best['Sales']} sales")