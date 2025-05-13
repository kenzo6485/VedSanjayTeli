
🛡️ Phishing URL Detection Using Machine Learning

Student Name: Teli Ved Sanjay 

---
📌 Project Overview
This project focuses on detecting phishing URLs using a supervised machine learning approach. With the increasing risk of cyberattacks through deceptive websites, building an automated detection system helps enhance online security.

🧠 Model Used
Algorithm: Logistic Regression  
Why: It is simple, interpretable, and effective for binary classification tasks like identifying phishing (1) vs legitimate (0) URLs.

---
📂 Dataset
- Source: Kaggle  
- Type:Phishing and legitimate URLs with features extracted from the URL structure.  
- Key Features:
  - URL length  
  - Use of HTTPS  
  - Number of subdomains  
  - Presence of IP address or suspicious symbols like '@'

---
📈 Performance
- Accuracy: Approximately 85–90%  
- Evaluation: Train-test split with accuracy as the main metric

---
⚠️ Limitations
- Uses static features — may not adapt to new phishing strategies  
- No real-time detection or browser integration

---
🚀 Future Improvements
- Use deep learning (e.g., LSTM) to better capture URL patterns  
- Add real-time detection through a browser extension or API  
- Integrate live threat intelligence feeds (e.g., PhishTank)
