import pandas as pd

data = pd.read_csv("Student_performance_data _.csv")

df = pd.DataFrame(data)
print(df.head(3))
print(df.info())
print(df.describe())
print(f"средний возраст {df['Age'].mean()}")

data2 = pd.read_csv("dz.csv")
df2=pd.DataFrame(data2)
mean_salary = df2.groupby("City")["Salary"].mean()
print(f'Средняя зарплата по городам {mean_salary}')
