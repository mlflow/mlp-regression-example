# MLflow Pipelines Regression Example
This repository serves as an example project for the
[MLflow Regression Pipeline](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline).
Follow the instructions below to download the latest MLflow and this repository
to create a linear regressor and evaluate its performance, all out of box!

**Note** This example repo is intended for first-time MLflow Pipelines users to learn
its fundamental concepts and workflows.
For users already familiar with MLflow Pipelines, seeking a template repository
to solve a specific regression ML problem, consider using
[mlp-regression-template](https://github.com/mlflow/mlp-regression-template) instead.

**Note**: [MLflow Pipelines](https://mlflow.org/docs/latest/pipelines.html)
is an experimental feature in [MLflow](https://mlflow.org).
If you observe any issues,
please report them [here](https://github.com/mlflow/mlflow/issues).
For suggestions on improvements,
please file a discussion topic [here](https://github.com/mlflow/mlflow/discussions).
Your contribution to MLflow Pipelines is greatly appreciated by the community!

## The ML problem: NYC taxi fare prediction
In this example, we demonstrate how to use MLflow Pipelines
to predict the fare amount for a taxi ride in New York City,
given the pickup and dropoff locations, trip duration and distance etc. 
The original data was published by the [NYC gov](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
We show how to build and evaluate a very simple linear regressor step by step,
following the best practices of machine learning engineering.
By the end of this example,
you will learn how to use MLflow Pipelines to
- Ingest the raw source data.
- Splits the dataset into training/validation/test.
- Create a feature transformer and transform the dataset.
- Train a linear model (regressor) to predict the taxi fare.
- Evaluate the trained model, and improve it by iterating through the `transform` and `train` steps.
- Register the model for production inference.

All of these can be done with Jupyter notebook or on Databricks environment.
Finally, challenge yourself to build a better model. Try the following:
- Find a better data source with more training data and more raw feature columns.
- Clean the dataset to make it less noisy.
- Find better feature transformations.
- Fine tune the hyperparameters of the model.

## Installation instructions
Follow the [MLflow Pipelines installation guide](https://mlflow.org/docs/latest/pipelines.html#installation). 
You may need to install additional libraries for extra features:
- [Hyperopt](https://pypi.org/project/hyperopt/)  is required for hyperparameter tuning.
- [PySpark](https://pypi.org/project/pyspark/)  is required for distributed training or to ingest Spark tables.
- [Delta](https://pypi.org/project/delta-spark/) is required to ingest Delta tables.
These libraries are available natively in the [Databricks Runtime for Machine Learning](https://docs.databricks.com/runtime/mlruntime.html).

## Log to the designated MLflow Experiment
To log pipeline runs to a particular MLflow experiment:
1. Open `profiles/databricks.yaml` or `profiles/local.yaml`, depending on your environment.
2. Edit (and uncomment, if necessary) the `experiment` section, specifying the name of the
   desired experiment for logging.

## Development Environment -- Databricks
[Sync](https://docs.databricks.com/repos.html) this repository with
[Databricks Repos](https://docs.databricks.com/repos.html) and run the `notebooks/databricks`
notebook on a Databricks Cluster running version 11.0 or greater of the
[Databricks Runtime](https://docs.databricks.com/runtime/dbr.html) or the
[Databricks Runtime for Machine Learning](https://docs.databricks.com/runtime/mlruntime.html)
with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note**: When making changes to pipelines on Databricks,
it is recommended that you edit files on your local machine and
use [dbx](https://docs.databricks.com/dev-tools/dbx.html) to sync them to Databricks Repos, as
demonstrated [here](https://mlflow.org/docs/latest/pipelines.html#usage)

**Note**: data profiles display in step cards are not visually compatible with dark theme.
Please avoid using the dark theme if possible.

### Accessing MLflow Pipeline Runs
You can find MLflow Experiments and MLflow Runs created by the pipeline on the
[Databricks ML Experiments page](https://docs.databricks.com/applications/machine-learning/experiments-page.html#experiments).

## Development Environment -- Local machine
### Jupyter

1. Launch the Jupyter Notebook environment via the `jupyter notebook` command.
2. Open and run the `notebooks/jupyter.ipynb` notebook in the Jupyter environment.

**Note**: data profiles display in step cards are not visually compatible with dark theme.
Please avoid using the dark theme if possible.

### Command-Line Interface (CLI)

First, enter the example root directory and set the profile via environment variable
```
cd mlr-regression-example
```
```
export MLFLOW_PIPELINES_PROFILE=local
```

Then, try running the
following [MLflow Pipelines CLI](https://mlflow.org/docs/latest/cli.html#mlflow-pipelines)
commands to get started.
Note that the `--step` argument is optional.
Pipeline commands without a `--step` specified act on the entire pipeline instead.

Available step names are: `ingest`, `split`, `transform`, `train`, `evaluate` and `register`.

- Display the help message:
```
mlflow pipelines --help
```

- Run a pipeline step or the entire pipeline:
```
mlflow pipelines run --step step_name
```

- Inspect a step card or the pipeline dependency graph:
```
mlflow pipelines inspect --step step_name
```

- Clean a step cache or all step caches:
```
mlflow pipelines clean --step step_name
```

**Note**: a short cut to `mlflow pipelines` is installed as `mlp`.
For example, to run the ingest step,
instead of issuing `mlflow pipelines run --step ingest`, you may type
```
mlp -s ingest
```

### Accessing MLflow Pipeline Runs
To view MLflow Experiments and MLflow Runs created by the pipeline:

1. Enter the example root directory: `cd mlr-regression-example`

2. Start the MLflow UI

```sh
mlflow ui \
   --backend-store-uri sqlite:///metadata/mlflow/mlruns.db \
   --default-artifact-root ./metadata/mlflow/mlartifacts \
   --host localhost
```

3. Open a browser tab pointing to [http://127.0.0.1:5000](http://127.0.0.1:5000)
