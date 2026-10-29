from pathlib import Path

import pandas as pd
from model.predict import make_prediction

sample_input_data = pd.read_csv(Path(__file__).resolve().parent / "bankchurn_test.csv")
result = make_prediction(input_data=sample_input_data)
print(result)
