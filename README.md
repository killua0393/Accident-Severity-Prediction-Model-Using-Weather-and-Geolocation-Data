
```markdown
# 🚦 Accident Severity Prediction Model Using Weather and Geolocation Data

This project predicts the severity of road accidents based on historical accident data, weather conditions, and geolocation insights. It uses a machine learning model trained on real-world datasets to help anticipate the impact and risk of traffic incidents.

## 📊 Features

- Random Forest-based severity prediction
- Integration of weather and location data
- Cleaned and pre-processed datasets
- Flask-based web app interface
- Modular code and model serialization

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- Flask
- Matplotlib / Seaborn

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/killua0393/Accident-Severity-Prediction-Model-Using-Weather-and-Geolocation-Data.git
   cd Accident-Severity-Prediction-Model-Using-Weather-and-Geolocation-Data
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the trained Random Forest model** (`rf_model.pkl`) from the link below and place it in the project root folder:

   📦 [Download rf_model.pkl from Google Drive](https://drive.google.com/file/d/1IFKJKHE1W0hrnIFZ5CWDU4Ne7VtPe-E3/view?usp=sharing)

5. Run the Flask app:
   ```bash
   python app.py
   ```

## 📌 Note

Due to GitHub's 100MB file size limit, the trained model file is hosted on Google Drive. Please download and place it manually.
