# uncertainty_quantification_scientific_ml

Prototype notebook on uncertainty quantification for a small Scientific Machine Learning problem.

## Objective

The project trains surrogate models on simulated physical data and compares a standard prediction workflow with a model that also returns uncertainty estimates. The target variable is a simplified lift coefficient computed from operating conditions and a physical correction factor.

## Business Context

In an industrial setting, physics-based simulations can be expensive to run for every design point. A surrogate model can provide fast estimates, but the prediction is only useful if the engineer can also see where the model is less reliable.

## Method

The notebook uses a synthetic aerodynamic dataset with:

- angle of attack;
- simplified Mach number;
- temperature;
- a geometry correction factor;
- a simulated lift coefficient with measurement noise.

Two models are trained:

- `RandomForestRegressor` as a simple reference model;
- `GaussianProcessRegressor` to produce a prediction and a predictive standard deviation.

The evaluation includes RMSE, MAE, R2 and 95 percent interval coverage for the Gaussian process.

## Repository Structure

```text
uncertainty_quantification_scientific_ml/
|-- README.md
|-- requirements.txt
|-- notebooks/
|   `-- uncertainty_quantification_scientific_ml.ipynb
|-- outputs/
|   |-- figures/
|   `-- metrics_summary.csv
`-- src/
    `-- data_simulation.py
```

## How To Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/uncertainty_quantification_scientific_ml.ipynb
```

Run the notebook from top to bottom. The output folders are created automatically if they are missing.

## Expected Results

The baseline model should give a reasonable estimate of the simulated lift coefficient. The Gaussian process should provide similar predictions while also showing wider uncertainty intervals near sparse or boundary regions of the input domain.

## Limitations

The data are simulated, the physical law is simplified, and the uncertainty is only an approximation from the chosen model. This is not a validation against real wind tunnel, CFD or production data.

## Industrial Link

The same workflow can be used as a first prototype for surrogate modeling around physical simulations: estimate a quantity quickly, identify risky zones, and decide where additional simulation or expert review is needed.
