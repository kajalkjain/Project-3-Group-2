#conda install dash pandas plotly
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

# Load the data from CSV file
df = pd.read_csv('data\cleaned_healthcare_dataset.csv')

# Create age groups
df['Age Group'] = pd.cut(df['Age'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '21-40', '41-60', '61-80', '81+'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout for look and feel on the browser
#layout will set the 
app.layout = html.Div([
    html.H1("Healthcare Data Dashboard"),
 # populate the values in the drop down from dataframe 
 # dcc(Dash Core Components) allows you to create interactive components like graphs, dropdowns, or date ranges.  
    dcc.Dropdown(
        id='condition-dropdown',
        options=[{'label': condition, 'value': condition} for condition in df['Medical Condition'].unique()],
        value='All',
        multi=False,
        placeholder="Select a Medical Condition"
    ),
    
    dcc.Graph(id='age-condition-chart'),
    
    dcc.Graph(id='billing-chart'),
    
    dcc.Graph(id='test-results-chart')
])

# Callback for updating the age-condition chart - Interactive Dash App where the Input is the value that user selects from the drop down and output is the graph that changes based on the input value
@app.callback(
    Output('age-condition-chart', 'figure'),
    [Input('condition-dropdown', 'value')]
)
#function below is called when the user changes the input in the drop down
def update_age_condition_chart(selected_condition):
    if selected_condition == 'All' or selected_condition == '' or selected_condition is None:
        filtered_df = df
    else:
        filtered_df = df[df['Medical Condition'] == selected_condition]
    # this is a new dataframe with 3 columns - Age Group, Medical Condition and Count
    age_condition_data = filtered_df.groupby(['Age Group', 'Medical Condition']).size().reset_index(name='Count')
    
    fig = px.line(age_condition_data, x='Age Group', y='Count', color='Medical Condition',
                  title='Medical Conditions Across Age Groups',
                  labels={'Count': 'Number of Patients'})
    return fig

# Callback for updating the billing chart
@app.callback(
    Output('billing-chart', 'figure'),
    [Input('condition-dropdown', 'value')]
)
def update_billing_chart(selected_condition):
    if selected_condition == 'All' or selected_condition == '' or selected_condition is None:
        filtered_df = df
    else:
        filtered_df = df[df['Medical Condition'] == selected_condition]
    
    fig = px.box(filtered_df, x='Medical Condition', y='Billing Amount',
                 title='Billing Amount Distribution by Medical Condition')
    return fig

# Callback for updating the test results chart
@app.callback(
    Output('test-results-chart', 'figure'),
    [Input('condition-dropdown', 'value')]
)
def update_test_results_chart(selected_condition):
    if selected_condition == 'All' or selected_condition == '' or selected_condition is None:
        filtered_df = df
    else:
        filtered_df = df[df['Medical Condition'] == selected_condition]
    
    test_results = filtered_df['Test Results'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=test_results.index, values=test_results.values)])
    fig.update_layout(title='Test Results Distribution')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)