# Text-Summarizer
## About

An Abstractive text summarizer trained using lstm based sequence to sequence model with attention mechanisim. The attention model is used for generating each word of the summary conditioned on the input sentence.

- Used CNN_DailyMail dataset.
- Code + Deployment : https://www.youtube.com/watch?v=LFZBA99NOpU

[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/LFZBA99NOpU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCQacvrk4iyXIEhzufcyLKd9ZWHlQ)](https://www.youtube.com/watch?v=LFZBA99NOpU)

### Training Model Overview

loss graph

![Output](./model/train_log.jpeg "loss overview")

encoder-decoder overview
![Output1](./model/model_plot.jpeg "model overview")

## Conclusion
- 🫶  The machine learning model to convert a text document to abstract is done successfully.
- 🫶  Created a Flask app using an api call from my hugging face repository & deployed the app in heroku app.

## Deployment:
![Output2](./deployment/static/images/SS1.jpeg "deployment")
- 🫶  https://text-summariser-v1.herokuapp.com/
