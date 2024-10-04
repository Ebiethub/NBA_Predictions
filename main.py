# Importing packages

import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn.preprocessing import StandardScaler

# Declaring the teams

teams = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets',
    'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers',
    'Miami Heat', 'Milwaukee Bucks', 'New York Knicks', 'Orlando Magic',
    'Philadelphia 76ers', 'Toronto Raptors', 'Washington Wizards', 'Dallas Mavericks',
    'Denver Nuggets', 'Golden State Warriors', 'Houston Rockets',
    'LA Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Minnesota Timberwolves',
    'New Orleans Pelicans', 'Oklahoma City Thunder', 'Phoenix Suns', 'Portland Trail Blazers',
    'Sacramento Kings', 'San Antonio Spurs', 'Utah Jazz']



# Loading the saved model
pipe = pickle.load(open('model.pkl', 'rb'))
st.title('NBA PLAYOFFS QUALIFICATION')


# Developing Streamlit app
nba_teams = st.selectbox('Select a team', sorted(teams))

GP = st.number_input('Games Played')

W_PCT = st.number_input('Win Percentage')

L = st.number_input('Loss')

AST_PCT = st.number_input('Assist Percentage')

OREB_PCT = st.number_input('Offensive Rebound Percentage')

AST_RATIO = st.number_input('Assist Ratio')

E_NET_RATING = st.number_input('Estimated Net Rating')

E_OFF_RATING = st.number_input('Estimated Offensive Rating')

AGE = st.number_input('AGE')

E_DEF_RATING = st.number_input('Estimated Defensive Rating')



if st.button('Predict Qualification'):


    input_df = pd.DataFrame({'GP': [GP], 'W_PCT': [W_PCT], 'L': [L], 'AST_PCT': [AST_PCT],
                             'OREB_PCT': [OREB_PCT], 'AST_RATIO': [AST_RATIO], 'E_NET_RATING': [E_NET_RATING],
                             'E_OFF_RATING': [E_OFF_RATING], 'AGE': [AGE], 'E_DEF_RATING': [E_DEF_RATING]})

    # Scale the data for better performance

    scaler = StandardScaler()
    X_selected_scaled = scaler.fit_transform(input_df)

    # Make Prediction
    result = pipe.predict_proba(X_selected_scaled)

    newmapper = {0: nba_teams + ' ' + 'does not Qualify', 1: nba_teams + ' ' +  'Qualify'}

    st.title(newmapper[int(result[0][0])])




