# NBA Prediction

# Name: EBIET MATTHEW MONDAY

# NBA Playoff Prediction for the 2022-2023 Season

This project aims to predict NBA teams that would qualify for the 2022-2023 playoffs from both the East and West conferences and simulate playoff outcomes for a fictional team of randomly selected players.

# Project Structure

- **Trained Model**: Pre-trained model files for playoff predictions.
- **Results**: Folder containing inference results for team playoff qualification.
- **Scripts**: Python scripts used for data preprocessing, model training, and predictions.

# Requirements

To run the project, ensure you have the following dependencies installed:

- Python 3.8+
- pandas
- numpy
- scikit-learn
- xgboost
- streamlit

You can install the dependencies using:

```bash
pip install -r requirements.txt




## Data Source

    The data used in this project includes:
  - Team Data: Contains team-level statistics for the 2022-2023 NBA season.
  - Player Data: Contains individual player statistics for the 2022-2023 NBA season.

## How to Run

1. **Run the streamlit app**:
   - Clone the repository.
   - Ensure all data files are placed in the correct location (`players_advance_stats.csv`, `teams_advance_stats.csv`, `teams_traditional_stats.csv`).
   - Launch the streamlit app using the following command:

   ```bash
   streamlit run main.py
   ```

2. **Prediction**:
   - The app will allow you to select a team from the 2022-2023 NBA season and predict its playoff qualification.

3. **Fictional Team Simulation**:
   - A fictional team of 15 randomly selected players is evaluated for playoff chances based on their aggregated stats.

## Files Included

- `main.py`: Main script for loading data, training models, and predicting playoff teams.
- `teams_advance_stats.csv` and `teams_traditional_stats.csv`: Team statistics for the 2022-2023 NBA season.
- `players_advance_stats.csv`: Player statistics for the 2022-2023 NBA season.
- `Trained Model`: Directory containing trained models for inference.
- `Results`: Directory containing prediction results for each team.

## Model Explanation

- **Model**: XGBoostClassifier and RandomForestClassifier were chosen due to their ability to handle structured data efficiently and perform well on classification tasks.
- **Features**: Important features are selected and used for the prediction.
- **Playoff Prediction**: The model classifies teams with a win percentage above 50% as likely to qualify for the playoffs.

## Fictional Team Assumptions

- The fictional team is formed by randomly selecting 15 players from the 2022-2023 season player pool.
- The team’s playoff chances are evaluated based on the average stats of the selected players.



```

This solution addresses all aspects of the test problem, from data preprocessing to model training, deployment, and submission. The Streamlit app adds interactivity to visualize the playoff predictions.
