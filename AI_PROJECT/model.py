import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv("network_data.csv")

data['protocol_type'] = data['protocol_type'].map({
    'tcp': 0,
    'udp': 1,
    'icmp': 2
})

X = data[['duration', 'protocol_type', 'src_bytes', 'dst_bytes']]
y = data['label']

model = GaussianNB()
model.fit(X, y)


def predict_attack(duration, protocol, src, dst):
    protocol_map = {'tcp': 0, 'udp': 1, 'icmp': 2}
    protocol_encoded = protocol_map.get(protocol, 0)

    features = [[duration, protocol_encoded, src, dst]]
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    classes = model.classes_

    prob_dict = dict(zip(classes, probabilities))
    confidence = round(prob_dict.get(prediction, 0) * 100, 1)

    return prediction, confidence