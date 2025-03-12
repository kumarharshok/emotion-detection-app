# 😊 Emotion Detection App 🎭

## 📌 Project Overview
This **Emotion Detection App** predicts human emotions based on text input. The model uses **TF-IDF Vectorization** and **Naïve Bayes classification** to classify emotions into categories such as **joy, anger, sadness, love, fear, and surprise**.

## 🚀 Features
✅ Enter any text and get **real-time emotion prediction**.  
✅ Supports multiple emotions with **emoji-based results**.  
✅ **Deployed on Streamlit Cloud** for easy access.  
✅ Built using **Python, Scikit-learn, Streamlit, and Joblib**.  

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** (for web app)
- **Scikit-learn** (for machine learning model)
- **Pandas** (for data handling)
- **Joblib** (for saving/loading the model)

## 📂 Project Structure
```
📦 emotion-detection-app
├── app.py                  # Main Streamlit app
├── emotion_model.pkl       # Trained ML model
├── tfidf_vectorizer.pkl    # TF-IDF vectorizer
├── requirements.txt        # Required Python packages
├── train.csv               # Training dataset
├── README.md               # Project documentation
```

## 📥 Installation & Setup
Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/emotion-detection-app.git
cd emotion-detection-app
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 🌍 Deploying on Streamlit Cloud
1️⃣ Push your project to **GitHub**.  
2️⃣ Go to [Streamlit Cloud](https://share.streamlit.io/) and log in.  
3️⃣ Click **New App**, select your repository, and deploy!  

## 📊 Example Predictions
| Input Text | Predicted Emotion |
|------------|------------------|
| "I am very happy today!" | Joy 😃 |
| "I feel so sad and lonely." | Sadness 😢 |
| "I am really angry right now!" | Anger 😡 |

## 📢 Contributing
Feel free to **fork** the repository and improve the project! Pull requests are welcome. 🚀

## 📜 License
This project is **open-source** and available under the MIT License.

