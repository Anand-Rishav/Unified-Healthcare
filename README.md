# Personalised Healthcare Recommendations

> Internship Project • Unified Mentor Private Limited

A machine-learning pipeline that predicts whether a past blood donor will donate again, helping blood-donation centres run smarter, more targeted outreach campaigns.

---

## Table of Contents
1. Project Overview
2. Problem Statement
3. Tech Stack
4. Dataset
5. Project Structure
6. Setup & Installation
7. Usage
8. Results & Performance
9. Key Features
10. Roadmap
11. Contributing
12. License
13. Contact

---

## 1. Project Overview
During my data-science internship at **Unified Mentor Private Limited**, I built an end-to-end solution—from data ingestion to Dockerized API—that delivers personalised donation-return predictions for blood donors.

## 2. Problem Statement
Blood centres struggle to keep a consistent donor base. By forecasting which donors are likely to return, organisations can:
- Optimise communication spend
- Increase donation volume
- Reduce operational costs

## 3. Tech Stack
- Python 3.8  
- Pandas • NumPy  
- scikit-learn • XGBoost  
- Optuna (hyperparameter tuning)  
- SHAP (model interpretability)  
- FastAPI (REST service)  
- Docker (containerisation)  
- Matplotlib • Seaborn (visualisation)

## 4. Dataset
Fields include:  
- Recency – months since last donation  
- Frequency – total donations made  
- Monetary – total blood donated (cc)  
- Time – months since first donation  

## 5. Project Structure
~~~text
├── data/
│   ├── raw/                 # Original, unmodified data
│   ├── processed/           # Cleaned and pre-processed data
│   └── external/            # Additional data sources
├── notebooks/
│   ├── 01_eda.ipynb         # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data/
│   │   ├── data_ingestion.py
│   │   └── data_preprocessing.py
│   ├── models/
│   │   ├── train_model.py
│   │   ├── predict_model.py
│   │   └── model_evaluation.py
│   └── api/
│       └── app.py           # FastAPI application
├── models/                  # Trained model artefacts
├── docker/
│   └── Dockerfile
├── requirements.txt
└── README.md
~~~

## 6. Setup & Installation

### Local
~~~bash
# Clone repo
git clone https://github.com/Anand-Rishav/Unified-Healthcare.git
cd Unified-Healthcare

# Create and activate venv
python -m venv venv
source venv/bin/activate            # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
~~~

### Docker (optional)
~~~bash
docker build -t unified-healthcare .
docker run -p 8000:8000 unified-healthcare
~~~

## 7. Usage

Train model  
~~~bash
python src/models/train_model.py --data_path data/processed/train.csv
~~~

Make predictions  
~~~bash
python src/models/predict_model.py --model_path models/best_model.pkl --input_data data/test.csv
~~~

Run REST API  
~~~bash
uvicorn src.api.app:app --host 0.0.0.0 --port 8000
# Swagger UI → http://localhost:8000/docs
~~~

## 8. Results & Performance
| Metric     | Score |
|------------|-------|
| AUC-ROC    | 0.93  |
| Precision  | 0.89  |
| Recall     | 0.85  |
| F1-Score   | 0.87  |

Important drivers identified by SHAP: Recency, Frequency.

## 9. Key Features
- Automated data pipeline (ingestion → pre-processing)  
- Optuna-driven hyper-parameter search  
- Probability calibration for reliable outputs  
- SHAP visualisations for interpretability  
- FastAPI + Docker for production-ready deployment  

## 10. Roadmap
- [ ] Real-time model monitoring  
- [ ] A/B testing framework  
- [ ] Integration with donor-management CRMs  
- [ ] Mobile-app interface  
- [ ] Enhanced feature engineering  

## 11. Contributing
1. Fork the repo  
2. `git checkout -b feature/YourFeature`  
3. Commit changes  
4. Push & open PR  

## 12. License
Licensed under the MIT License. See `LICENSE` for details.

## 13. Contact
**Rishav Anand** • rishav6604@gmail.com  
GitHub: https://github.com/Anand-Rishav

⭐ If you find this repo useful, please give it a star!
