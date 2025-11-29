# customer-segmentation-project-using-python-and-tableau

# customer-segmentation-project
This project focused on understanding customer purchasing behavior and enhancing marketing strategies through data-driven insights.

content:

Data Collection & Preprocessing — cleaned and transformed e-commerce transactional data.

Exploratory Data Analysis (EDA) — uncovered sales patterns, top products, and customer spending trends.

Market Basket Analysis (MBA) — identified frequently co-purchased products and cross-selling opportunities.

Customer Segmentation (Clustering) — grouped customers based on Recency, Frequency, and Monetary (RFM) values.

Visualization & Business Insights — developed intuitive visual dashboards using tableau and Python.


# **📘 Project Summary – Retail Customer & Product Insights Using Python**

This project performs a complete end-to-end **retail data analysis**, including **data cleaning, exploratory analysis, customer segmentation, market basket analysis, and advanced visualizations**.
The goal is to identify customer behavior patterns, product associations, top-selling items, and segment customers into meaningful groups for business decision-making.

---

# **1. Data Collection & Preprocessing**

The project begins by loading raw retail transaction data using **pandas**, then performing comprehensive cleaning:

* Handling missing values
* Removing duplicates
* Filtering invalid quantities
* Converting date formats
* Creating new fields
* Standardizing numeric fields using **StandardScaler**

These preprocessing steps ensure that the dataset is accurate and ready for both statistical and machine learning analysis.

---

# **2. Exploratory Data Analysis (EDA)**

Using **matplotlib** and **seaborn**, various visualizations are created:

### Product-level insights:

* Top-selling products
* Revenue by country

### Customer-level insights:

* Spending distribution
* Customer purchase behavior

### Time-based analysis:

* Monthly sales trends
* Correlation heatmaps

These visualizations help identify business patterns such as seasonality, high-value customers, and product popularity.

---

# **3. Market Basket Analysis (Association Rule Learning)**

This project applies **FP-Growth**, a machine learning algorithm used in **association rule mining**, to identify frequently purchased product combinations.

Modules used:

* **mlxtend.frequent_patterns.FPgrowth**
* **mlxtend.frequent_patterns.association_rules**

Outputs include:

* Frequent itemsets
* Association rules based on support, confidence, and lift

This helps the business understand:

* Products often bought together
* Opportunities for cross-selling
* Product bundling strategies

---

# **4. Customer Segmentation (Machine Learning)**

Customer behavior is analyzed using **RFM metrics**:

* **Recency** (how recently a customer purchased)
* **Frequency** (how often they purchased)
* **Monetary** (how much they spent)

The project then applies **K-Means Clustering**, an unsupervised machine learning algorithm, to group customers into segments.

This allows insights like:

* High-value loyal customers
* Low-frequency shoppers
* High-spend but infrequent buyers
* Recently inactive customers

The resulting clusters are saved for further analysis.

---

# **5. Combined Visualizations**

The final part integrates all outputs and generates:

### ✔ Customer Segment Distribution

Shows how many customers fall in each cluster.

### ✔ Top 10 Customers by Spending

Highlights key customers contributing the most revenue.

### ✔ Product Association Network

Built using **NetworkX**, visualizing product-to-product relationships from association rules.

This combined visualization provides a complete business overview of customer behavior and product interactions.

---

# **Python Libraries Used & Their Purpose**

| Library                                  | Purpose                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| **pandas**                               | Data loading, cleaning, transformation, grouping, file saving           |
| **numpy**                                | Basic numerical operations (implicitly used in pandas)                  |
| **matplotlib.pyplot**                    | Core plotting library for charts and graphs                             |
| **seaborn**                              | Statistical data visualizations (countplot, histplot, barplot, heatmap) |
| **sklearn.preprocessing.StandardScaler** | Scaling of numeric columns for clustering                               |
| **sklearn.cluster.KMeans**               | Machine learning algorithm for customer segmentation                    |
| **mlxtend.frequent_patterns**            | FP-Growth and association rule mining                                   |
| **networkx**                             | Building and visualizing association networks                           |
| **os**                                   | Checking file existence before loading                                  |

---

# **Machine Learning Methods Used**

### ✔ **FP-Growth Algorithm (Association Rule Learning)**

* Used for market basket analysis
* Identifies item combinations frequently bought together
* Helps understand product associations

### ✔ **K-Means Clustering (Unsupervised ML)**

* Used for customer segmentation
* Groups customers based on Recency, Frequency, Monetary value



It uses powerful Python libraries like pandas, seaborn, sklearn, mlxtend, and networkx to deliver actionable business insights on customer behavior, product performance, and sales trends.


# **📘 Project Summary – Retail Customer & Product Insights Using tableau**


# **tableau dashboard**
**Dashboard 1 — Customer Segmentation**

Title: Customer Segmentation Dashboard

Description:
This dashboard provides an RFM-based segmentation of customers to understand purchasing behavior and value contribution. It helps identify high-value customers, at-risk customers, and medium-value groups using Frequency, Monetary, and Recency metrics.

Key Insights Shown:

Customer Segment Distribution: Displays how many customers fall into each segment (Cluster 0–3).

Average RFM Values per Segment: Highlights how each cluster differs in spending, frequency, and purchase recency.

RFM Scatter Plot: Visualizes relationships between Monetary value, Frequency, and Recency to understand cluster separation.

Business Insights: Text card summarizing the behavioral meaning of each cluster.

Purpose:
Enable marketing teams and managers to target customer groups with tailored retention, reactivation, and loyalty strategies.

<img width="1920" height="997" alt="customer segmantation" src="https://github.com/user-attachments/assets/e4168c8c-76b8-48c7-bcbf-f11f4432562f" />

**Dashboard 2 — Market Basket Analysis**
Title: Market Basket Dashboard

Description:
This dashboard visualizes product association patterns using Apriori-generated rules. It helps understand which items are frequently purchased together and identifies strong product relationships based on support, confidence, and lift.

Key Insights Shown:

Top Association Rules: A ranking of strongest rules by lift, showing product pairs that commonly occur together.

Support vs Confidence Scatter Plot: Highlights rule strength and reliability.

Association Rules Table: Detailed view of antecedents, consequents, support, confidence, and lift for further analysis.

Insights Section: Summarizes most actionable product bundling and cross-selling opportunities.

Purpose:
Help merchandising, pricing, and e-commerce teams improve product bundling, placement, promotions, and targeted recommendations.

<img width="1920" height="1003" alt="market basket analysis" src="https://github.com/user-attachments/assets/d5980819-3cc7-4224-b9e0-0d981ad2405a" />
