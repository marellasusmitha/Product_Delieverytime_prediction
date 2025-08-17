# Delivery Time Prediction System

## 📌 Project Overview
This project predicts whether a product will be delivered **on time or delayed**, based on features like cost, discount, weight, and shipment mode.  
It also estimates **expected delivery time (ETA)** in hours and days.

The project includes:
- 🧠 Machine Learning Model (`delivery_model.pkl`)
- 🌐 Flask Web Application (`app.py`)
- 📊 Exploratory Data Analysis (`notebooks/Product_Delivery_Time.ipynb`)
- 🎨 Frontend (HTML + CSS)

---

## Dataset
We used `train.csv` which contains:
- `mode_of_shipment`
- `cost_of_the_product`
- `discount_offered`
- `weight_in_gms`
- `delivery_time_hours` (synthetic)
- `delayed` (0 = On Time, 1 = Delayed)

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/product_delivery_time.git
   cd product_delivery_time
2.Run Flask app:
    python app.py
3.Open in browser:
    http://127.0.0.1:5000/

##Exploratory Data Analysis
Check analysis.md for detailed EDA insights with graphs.

📸 Screenshots-Output
(<img width="1919" height="1079" alt="Delievery_time_output" src="https://github.com/user-attachments/assets/7671c41e-7e2b-4920-9f93-eeb51c72908c" />)

##Future Improvements
Deploy on Streamlit / Heroku / Render
Add real-time data integration
Improve model accuracy with feature engineering
