import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_excel("data.xlsx")
data_state = pd.read_excel("state_data.xlsx")
data_map = pd.read_csv('color_map.csv')
bubble_map = pd.read_csv('bubble_map.csv')
time_lagged_shotgun = pd.read_excel("shotgun-time-lagged-orrelations.xlsx")
time_lagged_9mm = pd.read_excel("9mm-time-lagged-orrelations.xlsx")

# Time Correlation - search query volume against gun background checks

# Figure 1

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=data['Month'], 
               y=data['Long Gun Background Checks'], 
               name="Background Checks"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=data['Month'], 
               y=data['Google Searches for "Shotgun"'], 
               name='Search Volume for "Shotgun"'),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    #title_text="Title"
)

fig.update_layout(legend=dict(x=0.053, y=0.9))

# Set x-axis title
fig.update_xaxes(title_text="Month", dtick = 1)

# Set y-axes titles
fig.update_yaxes(title_text='Long Gun Background Checks', secondary_y=False, dtick = 100000, range=[250000, 650000])
fig.update_yaxes(title_text='Internet Search Volume for "Shotgun"', showgrid=False, secondary_y=True, dtick = 4)

fig.show()

fig.write_image("images/fig1.eps")

# Figure 2

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=data['Month'], 
               y=data['Handgun Background Checks'], 
               name="Background Checks"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=data['Month'], 
               y=data['Google Searches for "9mm"'], 
               name='Search Volume for "9mm"'),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    #title_text="Title"
)

fig.update_layout(legend=dict(x=0.053, y=0.9))

# Set x-axis title
fig.update_xaxes(title_text="Month", dtick = 1)

# Set y-axes titles
fig.update_yaxes(title_text='Handgun Background Checks', secondary_y=False, dtick = 100000, range=[410000, 800000])
fig.update_yaxes(title_text='Internet Search Volume for "9mm"', showgrid=False, secondary_y=True, dtick = 4)

fig.show()

fig.write_image("images/fig2.eps")

# Figure 3

fig = px.line(time_lagged_shotgun, x="Time Lag (Months)", y="Correlation", color="Method")
fig.show()

fig.write_image("images/fig3.eps")

# Figure 4

fig = px.line(time_lagged_9mm, x="Time Lag (Months)", y="Correlation", color="Method")
fig.show()

fig.write_image("images/fig4.eps")


### Space Correlation - search query volume against gun background checks

# Figure 5

background_gun = data_state.drop(data_state.columns.difference(['Long Gun Background Checks Per 100,000 Residents','Google Searches for "Shotgun"']), 1,).dropna()
background = background_gun['Long Gun Background Checks Per 100,000 Residents']
gun = background_gun['Google Searches for "Shotgun"']

fig = px.scatter(background_gun, 
                 x='Long Gun Background Checks Per 100,000 Residents', 
                 y='Google Searches for "Shotgun"', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title="Long Gun Background Checks Per 100,000 Residents",
    yaxis_title='Internet Search Volume for "Shotgun" ',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.show()

fig.write_image("images/fig5.eps")

# Figure 6

background_gun = data_state.drop(data_state.columns.difference(['Handgun Background Checks Per 100,000 Residents','Google Searches for "9mm"']), 1,).dropna()
background = background_gun['Handgun Background Checks Per 100,000 Residents']
gun = background_gun['Google Searches for "9mm"']

fig = px.scatter(background_gun, 
                 x='Handgun Background Checks Per 100,000 Residents', 
                 y='Google Searches for "9mm"', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title="Handgun Background Checks Per 100,000 Residents",
    yaxis_title='Internet Search Volume for "9mm" ',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.show()

fig.write_image("images/fig6.eps")

# Figure 7

gun_deaths = data_state.drop(data_state.columns.difference(['Firearm Deaths Per 100,000 People (2017)','Google Searches for "Shotgun" (2017)']), 1,).dropna()
gun = gun_deaths['Google Searches for "Shotgun" (2017)']
deaths = gun_deaths['Firearm Deaths Per 100,000 People (2017)']

fig = px.scatter(gun_deaths, 
                 x='Google Searches for "Shotgun" (2017)', 
                 y='Firearm Deaths Per 100,000 People (2017)', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title='Internet Search Volume for "Shotgun"',
    yaxis_title='Firearm Related Deaths Per 100,000 Persons',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.show()

fig.write_image("images/fig7.eps")


# Figure 8

gun_deaths = data_state.drop(data_state.columns.difference(['Firearm Deaths Per 100,000 People (2017)','Google Searches for "9mm" (2017)']), 1,).dropna()
gun = gun_deaths['Google Searches for "9mm" (2017)']
deaths = gun_deaths['Firearm Deaths Per 100,000 People (2017)']

fig = px.scatter(gun_deaths,
                 x='Google Searches for "9mm" (2017)', 
                 y='Firearm Deaths Per 100,000 People (2017)', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title='Internet Search Volume for "9mm"',
    yaxis_title='Firearm Related Deaths Per 100,000 Persons',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.show()

fig.write_image("images/fig8.eps")

# Figure 9

law_gun = data_state.drop(data_state.columns.difference(['Gun-Law Strength','Google Searches for "Shotgun"']), 1,).dropna()
law = law_gun['Gun-Law Strength']
gun = law_gun['Google Searches for "Shotgun"']

fig = px.scatter(law_gun, 
                 x='Gun-Law Strength', 
                 y='Google Searches for "Shotgun"', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title='Restrictiveness of State-Level Firearm Policies',
    yaxis_title='Internet Search Volume for "Shotgun"',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.show()

fig.write_image("images/fig9.eps")

# Figure 10

law_ammo = data_state.drop(data_state.columns.difference(['Gun-Law Strength','Google Searches for "9mm"']), 1,).dropna()
law = law_ammo['Gun-Law Strength']
ammo = law_ammo['Google Searches for "9mm"']

fig = px.scatter(law_ammo, 
                 x='Gun-Law Strength', 
                 y='Google Searches for "9mm"', 
                 #hover_data=['State']
                )

fig.update_layout(
    #title="Plot Title",
    xaxis_title='Restrictiveness of State-Level Firearm Policies',
    yaxis_title='Internet Search Volume for "9mm"',
    font=dict(
        #family="Courier New, monospace",
        #size=18,
        #color="#7f7f7f"
    )
)

fig.write_image("images/fig10.eps")

# Figure 11

fig = go.Figure(data=go.Choropleth(
    locations= data_map['code'], # Spatial coordinates
    z = data_map['shotgun_raw'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = ["navy", "royalblue", "tomato", "red"],
    colorbar_title = "<b> Internet Search <br> Volume for 'Shotgun' <br> </b>",
))

fig.update_layout(
    #title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()

fig.write_image("images/fig11.eps")

# Figure 12

fig = go.Figure(data=go.Choropleth(
    locations=data_map['code'], # Spatial coordinates
    z = data_map['9mm_raw'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = ["navy", "royalblue", "tomato", "red"],
    colorbar_title = "<b> Internet Search <br> Volume for '9mm' <br> </b>",
))

fig.update_layout(
    #title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()

fig.write_image("images/fig12.eps")

# Figure 13

fig = go.Figure(data=go.Choropleth(
    locations=data_map['code'], # Spatial coordinates
    z = data_map['deaths'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = ["navy", "royalblue", "tomato", "red"],
    colorbar_title = "<b> Firearm-Related Deaths <br> per 100,000 Residents </b>",
))

fig.update_layout(
    #title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()

fig.write_image("images/fig13.eps")


# Figure 14

fig = go.Figure(data=go.Choropleth(
    locations=bubble_map['code'], # Spatial coordinates
    z = bubble_map['law'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = ["red", "tomato", "royalblue", "navy"],    
    colorbar_title = "<b> Restrictiveness Score of <br> State-Level Firearm Policies </b>",
))

fig.update_layout(
    #title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()

fig.write_image("images/fig14.eps")




