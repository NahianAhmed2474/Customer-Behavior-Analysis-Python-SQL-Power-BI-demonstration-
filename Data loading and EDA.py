import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('customer_shopping_behavior.csv')

'''
print(df.head()) 
print(df.info()) 
print (df.describe())
print(df.decribe(include='all'))                                                                  
'''

'''
To fill missing data we can take the median value of existing data to fill it up. However, since the data
has been divided into categories, it is essential to take the medians categorically as opposed to overall 
to avoid any biases caused by each category onto each other
'''

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))



'''
For consistency and ease of use, we will convert all the column names to snake casing
'''

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

'''
Creating a new column age_group
'''

labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


'''
As the frequency of purchase is given in a string format, we will now convert it into integers to make it easier to wrok with
'''

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
    }

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


'''
If we observe the discount applied and promo code used columns, we can see that both hold the same data, so we can drop one (promo code in this case as it is
dependent on discount applied)
'''
'''print((df['discount_applied'] == df['promo_code_used']).all())'''### --> This tells us that both the columns are the same FOR THIS CASE, so we can drop it

df = df.drop('promo_code_used', axis=1)


'''
We can now connect to postgreSQL to do SQL based problem solving
'''

username = "postgres"
password = "2474"
host = "localhost"
port = "5432"
database = "customer behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

table_name = 'customer'
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name} in database '{database}'.")




































