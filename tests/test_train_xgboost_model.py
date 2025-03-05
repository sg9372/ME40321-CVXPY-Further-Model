import unittest
import numpy as np
import xgboost as xgb
from src.train_xgboost_model import train_xgboost_model
from src.extract_values import extract_values

class TestTrainXGBoostModel(unittest.TestCase):

    def setUp(self):
        # Set up some example data
        self.current_values = np.random.rand(100, 10)  # Example current period values (100 samples, 10 companies)
        self.future_values = np.random.rand(100, 10)  # Example future period values (100 samples, 10 companies)

    def test_model_training(self):
        # Test if the model is trained without errors
        model, predictions = train_xgboost_model(self.current_values, self.future_values)
        self.assertIsNotNone(model)
        self.assertIsNotNone(predictions)

    def test_predictions_shape(self):
        # Test if the predictions have the correct shape
        model, predictions = train_xgboost_model(self.current_values, self.future_values)
        self.assertEqual(predictions.shape, (2,))  # 20% of 100 is 20

    def test_predictions_type(self):
        # Test if the predictions are of type numpy array
        model, predictions = train_xgboost_model(self.current_values, self.future_values)
        self.assertIsInstance(predictions, np.ndarray)

    def test_model_type(self):
        # Test if the model is of type XGBRegressor
        model, predictions = train_xgboost_model(self.current_values, self.future_values)
        self.assertIsInstance(model, xgb.XGBRegressor)
    
    def  test_values(self):
        # Test if the model predictions are close to the average future values
        companies = [
            "STAN.L", "CRDA.L", "ANTO.L", "BNZL.L", "SGE.L", 
            "SVT.L", "BLND.L", "ICAG.L", "REL.L", "SMIN.L"
        ]
        
        curr_values,_ = extract_values("Monthly FTSE Data - New.xlsx", companies, "01/01/2020", "01/02/2020")
        fut_values,_ = extract_values("Monthly FTSE Data - New.xlsx", companies, "01/02/2020", "01/03/2020")
        
        model, predictions = train_xgboost_model(curr_values, fut_values)
        fut_averages = np.mean(fut_values, axis=0)
        print("Predictions: ", predictions)
        print("Future Averages: ", fut_averages)
        self.assertTrue(np.allclose(predictions, fut_averages[8:], rtol=0.3))