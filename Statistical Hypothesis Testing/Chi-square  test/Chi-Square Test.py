import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats.distributions import chi2

df = pd.read_csv("titanic_dataset.csv", index_col='PassengerId',
                 usecols=['PassengerId', 'Pclass', 'Survived'])
print(df, df.info())
sns.displot(df.Pclass)
plt.title("Passenger Class")
plt.show()
sns.distplot(df.Survived)
plt.title("Survived or not")
plt.show()
PClass_survd: df = pd.pivot_table(df, index=['Pclass'], columns=['Survived'], aggfunc='size')
sns.heatmap(PClass_survd, annot=True, fmt='g', square=True, cmap='hot')
plt.title('Class Vs Survived', fontsize=20)
plt.show()
pct_class = PClass_survd.sum(axis=1) / 891
pct_survived = PClass_survd.sum(axis=0) / 891
print(pct_class.to_frame() @ (pct_survived.to_frame().T))
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.heatmap(PClass_survd, annot=True, fmt='g', square=True, cmap='hot')
plt.title('Observed', fontsize=20)

plt.subplot(1, 3, 3)
sns.heatmap(PClass_survd, annot=True, fmt='g', square=True, cmap='hot')
plt.title('Expected', fontsize=20)
plt.tight_layout()

plt.show()
Chi_table = ((PClass_survd) ** 2) / PClass_survd
Chi_value = Chi_table.sum().sum()

p_value = chi2.sf(Chi_value, 1)
chi2_stat, p_val, dof, ex = stats.chi2_contingency(PClass_survd)
print(Chi_table)
print("Chi square value is ", Chi_value)
print("P value is", p_value)
print("Chi square value is ", chi2_stat)
print("P value is", p_val)
print("Degrees of Freedom:", dof)
