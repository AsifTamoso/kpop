from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import seaborn as sns

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Demo"

df = pd.read_csv('https://raw.githubusercontent.com/AsifTamoso/kpop/main/kpop_idols_boy_groups.csv')
dfGirl = pd.read_csv('https://raw.githubusercontent.com/AsifTamoso/kpop/main/kpop_idols_girl_groups.csv')

# Create a Plotly Express scatter plot for boys group
fig1 = px.scatter(df, x='Members', y='Orig. Memb.')
fig1.update_layout(
    title='Members Vs Orig. Memb. Boys Group',
    xaxis_title='Members',
    yaxis_title='Orig. Memb.'
)

# Create a Plotly Express scatter plot for girls group
fig3 = px.box(dfGirl, x='Orig. Memb.', y='Active', title='Box Plot Girls Group')

# Create a Plotly Express box plot for boys group
fig2 = px.box(df, x='Orig. Memb.', y='Active', title='Box Plot Boys Group')

# Define the Dash layout with both Plotly Express scatter plots and box plots
app.layout = html.Div(
    [
        html.H1("Data Visualization KPOP"),
        dcc.Graph(figure=fig1),  # Plotly Express scatter plot for boys group
        dcc.Graph(figure=fig3),  # Plotly Express box plot for girls group
        dcc.Graph(figure=fig2)  # Plotly Express box plot for boys group
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
