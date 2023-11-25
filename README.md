
# Alzheimer Disease Classification

**The main goal of this is to classify brain scans into different stages of Dementia.**

![](https://github.com/sudhanshu2198/Alzheimer-Detection/blob/main/images/intro_img.jpeg)

Alzheimer's disease is a brain disorder that gets worse over time. It's characterized by changes in the brain that lead to deposits of certain proteins. Alzheimer's disease causes the brain to shrink and brain cells to eventually die. Alzheimer's disease is the most common cause of dementia — a gradual decline in memory, thinking, behavior and social skills. These changes affect a person's ability to function.

People with Alzheimer's disease may
- Repeat statements and questions over and over.
- Forget conversations, appointments or events.
- Misplace items, often putting them in places that don't make sense.
- Have trouble finding the right words for objects, expressing thoughts or taking part in conversations."

## 🔗 Links

 - [App Link](https://alzheimer-detection-deepchecks.streamlit.app/)
 - [Kaggle Notebook link](https://www.kaggle.com/code/sudhanshu2198/alzheimer-s-detection/notebook)


## 🛠 Skills
Python, Pandas, Numpy, Matplotlib, Pytorch, Torchvision, Deepchecks, Streamlit, Git. 

## Directory Tree
```bash

├── html_files
│   ├── data_integrity.html
│   │── model_validation.html
│   └── train_test_validation.html 
├── images
│   ├── alzheimer_img
│   └── intro_img.webp
├── pages
│   ├── Data_Integrity.py
├   ├── Inference.py
├   ├── Model_Validation.py
│   └── Train_Test_Validation.py
├── weights
│   ├── alheimer_weight.pth 
├── Introduction.py
├── README.md
├── alzheimer_notebook.ipynb
└── requirements.txt
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/sudhanshu2198/Alzheimer-Detection
```

Change to project directory

```bash
  cd Alzheimer-Detection
```

Create Virtual Environment

```bash
  python3 -m venv .venv
  .venv/Scripts/activate
```


Now install all requirements

```bash
  pip install -r requirements.txt
```

Run Streamlit Web App
```bash
  streamlit run Introduction.py
```

