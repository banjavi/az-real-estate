# Real Estate Price Prediction 🏠

Predicting house prices using Ridge Regression and Neural Networks.

## Comparison between Actual and Predicted Prices

![Actual vs Predicted Prices](images/actual_vs_prediction.png)

## Key Statistics 📈

- **Average House Price:** $531,494.03
- **Median House Price:** $419,240.00

## Metrics 📊

### Ridge Regression
- **Validation MAE:** $34,607.18
- **Test MAE:** $37,900.10
- **Training Time:** 0.08 seconds

### Neural Network
- **Validation MAE:** $43,002.42
- **Test MAE:** $43,957.03
- **Training Time:** 53.90 seconds

## Conclusions 📝

### Historical Context:
Historically, housing price prediction has been approached as a regression task due to the continuous nature of prices.

### Performance:
Ridge Regression outperforms Neural Network on this dataset, indicating the efficiency of simpler models, especially with limited data.

### Interpretability:
Ridge offers a clear understanding of feature impacts, unlike the black-box nature of Neural Networks.

### Training Time:
The swiftness of Ridge Regression can be pivotal for rapid deployment.

### Model Error:
Considering the average and median house prices, the MAE values for both models show an error margin of approximately 7-8%.

## Future Work 🔮

- **Data Enhancement:** Improve dataset for better Neural Network performance.
- **Tuning:** Optimize hyperparameters for both models.
- **Ensemble Methods:** Combine predictions for potentially better results.
- **Neural Network Exploration:** Refine predictions with different architectures.
- **API Limitation:** Address the 350-record limitation of the Redfin API for richer datasets.

[Issue Link](https://github.com/ryansherby/RedfinScraper/issues/7)
