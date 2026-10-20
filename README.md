# 🛍️ DukaanAI — Retail Intelligence Platform

DukaanAI is a machine-learning project focused on exploring retail data and developing tools that can help understand sales patterns, forecast product demand, and derive useful inventory and product insights.

The project is being developed as a team project. It combines a Python-based data and machine-learning pipeline with a Streamlit dashboard for presenting insights and experiments.

> **Project status:** Under active development. The dashboard currently contains an overview prototype, while the data-processing, feature-engineering, model-training, prediction, and evaluation modules are being built. Do not treat planned capabilities as production-ready results.

---

## 🎯 Project Goals

DukaanAI aims to develop a workflow for:

- Auditing and preparing retail inventory data.
- Exploring sales, product, and store-level patterns.
- Engineering features for machine-learning experiments.
- Establishing a baseline model and evaluating its performance.
- Exploring demand forecasting, product segmentation, and inventory insights through a dashboard.
- Keeping the project maintainable through reusable Python modules, tests, configuration, and documentation.

The usefulness and availability of each insight will depend on the dataset fields and the models ultimately implemented.

## ✨ Planned Platform Areas

| Area | Purpose | Current status |
|---|---|---|
| Overview dashboard | Introduce the platform and show project status | Prototype in `app/app.py` |
| Demand forecasting | Compare historical demand with model predictions | Planned; model pipeline in development |
| Product segmentation | Explore groups of products with similar sales behaviour | Planned |
| Inventory insights | Explore inventory-related patterns where supported by the data | Planned |
| ML Lab | Review model experiments and visualizations | Planned |

The current Streamlit sidebar references additional pages that are not yet present in the repository structure. Those pages should be added as the dashboard is developed.

## 🧰 Technology Stack

- **Language:** Python
- **Data processing:** pandas, NumPy
- **Machine learning:** scikit-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Web dashboard:** Streamlit
- **Model persistence:** joblib
- **Development and quality:** Jupyter Notebook, pytest-compatible test files, GitHub Actions workflow

Dependencies are listed in [`requirements.txt`](requirements.txt).

## 📁 Repository Structure

```text
rajnityanand-dukaan-ai/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── app/
│   └── app.py
├── configs/
│   └── baseline.yaml
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── setup_guide.md
├── models/
│   └── .gitkeep
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_baseline_model.ipynb
│   └── 06_model_evaluation.ipynb
├── src/
│   └── dukaanai/
│       ├── __init__.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── load_data.py
│       │   └── preprocess.py
│       ├── features/
│       │   ├── __init__.py
│       │   └── build_features.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── evaluate.py
│       │   ├── predict.py
│       │   └── train.py
│       └── utils/
│           ├── __init__.py
│           └── logging_config.py
├── tests/
│   ├── test_features.py
│   ├── test_predict.py
│   └── test_preprocess.py
└── .github/
    └── workflows/
        └── tests.yml
```

### What the main folders are for

- `app/` — Streamlit user interface.
- `configs/` — model and experiment configuration, including baseline settings.
- `docs/` — architecture, dataset field definitions, and setup documentation.
- `models/` — location reserved for saved model artifacts. Generated model files may be excluded from version control.
- `notebooks/` — exploratory analysis and step-by-step ML experiments.
- `src/dukaanai/data/` — reusable data-loading and preprocessing code.
- `src/dukaanai/features/` — reusable feature-building logic.
- `src/dukaanai/models/` — model training, prediction, and evaluation code.
- `src/dukaanai/utils/` — shared utilities such as logging.
- `tests/` — automated checks for preprocessing, features, and prediction.
- `.github/workflows/` — CI workflow configuration.

The repository layout describes the intended organization; some modules and documentation files are still placeholders.

## 📊 Dataset

The current data-audit notebook is designed to inspect a CSV file named:

```text
retail_store_inventory.csv
```

Place the dataset in this local path before running the audit notebook:

```text
data/raw/retail_store_inventory.csv
```

If the `data/raw/` folders do not exist, create them inside the repository. The dataset is not shown in the current repository tree, so you must obtain it separately and place it at the expected path. Check the dataset's original source and license before redistributing it.

### Dataset snapshot from the current audit

The existing audit notebook reports the following for the dataset it inspected:

- **Rows:** 73,100
- **Columns:** 15
- **Fields:** date, store and product identifiers, category, region, inventory level, units sold, units ordered, demand forecast, price, discount, weather, holiday/promotion, competitor pricing, and seasonality.
- **Negative demand forecasts detected:** 673 in the audit run.

The current exploratory notebook clips negative `Demand Forecast` values to zero. This is a working data-cleaning assumption, not a verified statement that every negative value is erroneous. Review the field's meaning and document the chosen treatment before using it in the final pipeline.

For the intended field definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md) as it is completed.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd rajnityanand-dukaan-ai
```

Replace `<YOUR_REPOSITORY_URL>` with the actual Git repository URL.

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add the dataset

Create the folders if needed:

```text
data/
└── raw/
    └── retail_store_inventory.csv
```

Do not commit private, restricted, or very large dataset files unless the project's data license and repository policy permit it.

### 5. Launch the Streamlit overview

From the repository root, run:

```bash
streamlit run app/app.py
```

Streamlit will print a local URL in the terminal, usually `http://localhost:8501`.

> The overview is a development prototype. Forecasting, segmentation, inventory analysis, and ML experiment pages should not be assumed to work until their pages and model pipeline are implemented.

### 6. Open the notebooks

Open the repository in VS Code with the Python and Jupyter extensions installed, or launch Jupyter:

```bash
jupyter notebook
```

Start with `notebooks/01_data_audit.ipynb`, then proceed to data cleaning, feature engineering, baseline modeling, and evaluation as those notebooks are completed and validated.

If a notebook fails to open, check that it is a valid `.ipynb` JSON notebook. A Python script or exported text file renamed to `.ipynb` is not a valid Jupyter notebook.

## 🔬 Intended ML Workflow

The planned workflow is:

1. **Data audit** — inspect dimensions, types, missing values, duplicates, date validity, and numeric ranges.
2. **Data cleaning** — document and apply justified data-quality rules.
3. **Exploratory analysis** — study demand and sales patterns across time, stores, products, and categories.
4. **Feature engineering** — create suitable date-based, historical, and categorical features without leaking future information.
5. **Baseline modeling** — establish a simple, reproducible benchmark before trying more complex approaches.
6. **Evaluation** — evaluate predictions with appropriate metrics and a time-aware validation strategy for forecasting.
7. **Dashboard integration** — expose verified data summaries and model outputs through Streamlit.

This is the intended workflow, not a claim that all steps or models are already implemented.

## 🧪 Testing

Test modules are planned under `tests/`:

- `test_preprocess.py`
- `test_features.py`
- `test_predict.py`

Once the test setup and project configuration are implemented, tests can be run from the repository root with:

```bash
pytest
```

The current `pyproject.toml`, test modules, and CI workflow may still need configuration and implementation before this command can pass. Install pytest separately if it is not added to the project's dependencies:

```bash
pip install pytest
```

## 🗺️ Development Roadmap

- [x] Establish the repository structure.
- [x] Create the initial Streamlit overview prototype.
- [x] Begin auditing the retail inventory dataset.
- [ ] Finalize and validate the data-cleaning notebook.
- [ ] Implement reusable data loading and preprocessing modules.
- [ ] Complete exploratory data analysis and the data dictionary.
- [ ] Implement and test feature engineering.
- [ ] Configure and train a baseline model.
- [ ] Evaluate model performance with an appropriate validation strategy.
- [ ] Integrate verified predictions and insights into the dashboard.
- [ ] Complete automated tests, CI configuration, and setup documentation.

## 👥 Team Members

- **Nityanand Raj**
- **Mukul Mitawa**
- **Mayank Chhipa**
- **Naitik Tiwari**

## 🤝 Contributing

Team members should work on clearly defined tasks and use feature branches for substantial changes.

Suggested workflow:

1. Pull the latest changes from the shared branch.
2. Create a feature branch.
3. Make focused changes and test them locally.
4. Open a pull request with a short summary and any relevant screenshots or evaluation results.
5. Merge only after reviewing the changes and resolving conflicts.

Keep notebooks focused, move reusable logic into `src/dukaanai/`, and document important data-cleaning and modeling decisions.

## 📄 License

A `LICENSE` file exists in the repository, but it is currently empty. Add the license chosen by the team before describing the project as licensed for reuse.

---

**DukaanAI** · Retail Intelligence Platform · Machine Learning Project · *Under Development*
