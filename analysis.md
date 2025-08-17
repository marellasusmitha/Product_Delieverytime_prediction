
---

## analysis.md  

markdown
# Exploratory Data Analysis (EDA) – Delivery Time Prediction

This document highlights key findings from the dataset.

---

## 1️⃣ Delivery Status Distribution
- The dataset shows both **on-time** and **delayed deliveries**.
- `delayed = 0` → On-Time
- `delayed = 1` → Delayed

📉 **Insight**: Majority of deliveries are on-time, but a significant portion gets delayed.

---

## 2️⃣ Delivery Time Distribution
- `delivery_time_hours` ranges widely.
- Most deliveries fall within **24 – 120 hours**.
- Longer delivery times have a higher chance of being delayed.

---

## 3️⃣ Relationship Between Features
- **Weight**: Heavier packages tend to have longer delivery times.
- **Discounts**: Higher discounts sometimes correlate with delays.
- **Mode of Shipment**: Courier vs. Ship vs. Flight impacts ETA.

---

## 4️⃣ Key Graphs
1. **Countplot** → On-time vs Delayed Deliveries  
2. **Histogram** → Distribution of Delivery Time (hours)  

Images
![countplot](images/countplot.png)
![Histogram](images/Histogram.png)
 

---

## ✅ Conclusion
- Delivery time is influenced by **weight, shipment mode, and discounts**.  
- The ML model predicts both **delay likelihood** and **ETA**.  
- This can help **e-commerce & logistics companies** optimize delivery operations.
