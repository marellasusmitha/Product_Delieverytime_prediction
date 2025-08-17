
---

## analysis.md  

```markdown
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
-Countplot  <img width="755" height="537" alt="countplot" src="https://github.com/user-attachments/assets/09302883-5f4e-4db5-b608-5155584a317a" />  
-Histogram  <img width="744" height="541" alt="Histogram" src="https://github.com/user-attachments/assets/b2080cc3-890c-46f4-b436-429974c9e152" />  

---

## ✅ Conclusion
- Delivery time is influenced by **weight, shipment mode, and discounts**.  
- The ML model predicts both **delay likelihood** and **ETA**.  
- This can help **e-commerce & logistics companies** optimize delivery operations.
