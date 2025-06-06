from featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model

model = load_model('model/phishingdetection')


def predict(url):
    data = featureExtraction(url)
    result = predict_model(model, data=data)
    
    # Get the prediction score for the positive class (Phishing)
    prediction_score = result['prediction_score'][0]  
    prediction_label = result['prediction_label'][0]  
    domain_age = result['Domain_Age'][0]
    print('Result -> ', url)

    if prediction_label == 1:
        return "Phising Website"
    elif prediction_label == 0:
        return "Legit Website"
    # return {
    #     'prediction_label': prediction_label,
    #     'prediction_score': prediction_score * 100,
    # }

if __name__ == "__main__": 
    phishing_url_1 = 'https://bafybeifqd2yktzvwjw5g42l2ghvxsxn76khhsgqpkaqfdhnqf3kiuiegw4.ipfs.dweb.link/'
    phishing_url_2 = 'http://about-ads-microsoft-com.o365.frc.skyfencenet.com'
    phishing_url_3 = 'www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrcmd=_home-customer&nav=1/loading.php'
    real_url_1 = 'https://chat.openai.com'
    real_url_2 = 'https://github.com/'
    real_url_3 = 'https://google.com'

    
    
    print(predict(phishing_url_1))
    print(predict(phishing_url_2))
    print(predict(phishing_url_3))
    print(predict(real_url_1))
    print(predict(real_url_2))
    print(predict(real_url_3))
