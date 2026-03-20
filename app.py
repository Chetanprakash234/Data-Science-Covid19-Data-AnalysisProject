import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output

# Write pandas code here
patients = pd.read_csv('IndividualDetails.csv')

total = patients.shape[0]
active = patients[patients['current_status']=='Hospitalized'].shape[0]
recovered = patients[patients['current_status']=='Recovered'].shape[0]
deaths = patients[patients['current_status']=='Deceased'].shape[0]

pbar = patients.groupby('current_status').count()['id'].reset_index()

main = pd.read_csv('covid_19_india.csv')
main['total']=main['ConfirmedIndianNational']+main['ConfirmedForeignNational']
#main['total']*np.cumsum(main['total'].values)

age= pd.read_csv('AgeGroupDetails.csv')

# external Css
external_stylesheets=[
    {
        "href":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css",
        "rel":"stylesheet",
        "integrity":"sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB",
        "crossorigin":"anonymous"
    }
]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Corona Virus Pandemic",style={'color':'#AB8780','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases",className='text-light'),
                    html.H4("600",className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases",className='text-light'),
                    html.H4("600",className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases",className='text-light'),
                    html.H4("600",className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths Cases",className='text-light'),
                    html.H4("600",className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
    ],className='row'),
    html.Div([],className='row'),
    html.Div([],className='row')
],className='container')

if __name__=="__main__":
    app.run(debug=True)
'''
options = [
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'},
]
'''