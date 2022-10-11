from .settings import settings
from .vmachine import vmachine
from .model import Model
from .versioning import Versioning
from .global_functions import globalFunctions

settings

settings.package_version = "0.0.1.dev"
settings.premade_main_code_data = """# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response


model_name = "Breast Cancer Wisconsin (Diagnostic)"
version = "v1.0.0"


# Input for data validation
class Input(BaseModel):
    concavity_mean: float = Field(..., gt=0)
    concave_points_mean: float = Field(..., gt=0)
    perimeter_se: float = Field(..., gt=0)
    area_se: float = Field(..., gt=0)
    texture_worst: float = Field(..., gt=0)
    area_worst: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "concavity_mean": 0.3001,
            "concave_points_mean": 0.1471,
            "perimeter_se": 8.589,
            "area_se": 153.4,
            "texture_worst": 17.33,
            "area_worst": 2019.0,
        }


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int


@app.get('/')
async def model_info():
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    return {
        "ok"
    }


@app.post('/predict', response_model=Output)
async def model_predict(input: Input):
    response = get_model_response(input)
    return response

"""
settings.premade_function_code_data = """# Import packages
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib
import gzip


# Load the dataset
data = pd.read_csv('data/breast_cancer.csv')

# Preselected feature
selected_features = [
    'concavity_mean',
    'concave_points_mean',
    'perimeter_se',
    'area_se',
    'texture_worst',
    'area_worst'
]

# Preprocess dataset
data = data.set_index('id')
data['diagnosis'] = data['diagnosis'].replace(['B', 'M'], [0, 1])  # Encode y, B -> 0 , M -> 1

# Split into train and test set, 80%-20%
y = data.pop('diagnosis')
X = data
X = X[selected_features.copy()]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an ensemble of 3 models
estimators = []
estimators.append(('logistic', LogisticRegression()))
estimators.append(('cart', DecisionTreeClassifier()))
estimators.append(('svm', SVC()))

# Create the Ensemble Model
ensemble = VotingClassifier(estimators)

# Make preprocess Pipeline
pipe = Pipeline([
    ('imputer', SimpleImputer()),  # Missing value Imputer
    ('scaler', MinMaxScaler(feature_range=(0, 1))),  # Min Max Scaler
    ('model', ensemble)  # Ensemble Model
])

# Train the model
pipe.fit(X_train, y_train)

# Test Accuracy
print("Accuracy: %s%%" % str(round(pipe.score(X_test, y_test), 3) * 100))

# Export model
joblib.dump(pipe, gzip.open('model/model_binary.dat.gz', "wb"))


"""
settings.premade_requirements_data = """anyio==3.5.0
asgiref==3.5.0
click==8.1.2
cycler==0.11.0
fastapi==0.75.2
fonttools==4.32.0
h11==0.13.0
idna==3.3
joblib==1.1.0
kiwisolver==1.4.2
matplotlib==3.5.1
numpy==1.22.3
packaging==21.3
pandas==1.4.2
Pillow==9.1.0
pydantic==1.9.0
pyparsing==3.0.8
python-dateutil==2.8.2
pytz==2022.1
scikit-learn==1.0.2
scipy==1.8.0
six==1.16.0
sklearn==0.0
sniffio==1.2.0
starlette==0.17.1
threadpoolctl==3.1.0
typing_extensions==4.2.0
uvicorn==0.17.6
"""
settings.premade_documentation_data = """# POST method predict
curl -d '{"concavity_mean": 0.3001, "concave_points_mean": 0.1471, "perimeter_se": 8.589, "area_se": 153.4, "texture_worst": 17.33, "area_worst": 2019.0}' \
     -H "Content-Type: application/json" \
     -XPOST http://0.0.0.0:8000/predict

# GET method info
curl -XGET http://localhost:8000/info

# GET method health
curl -XGET http://localhost:8000/health
"""
