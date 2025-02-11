from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#st.title("hello")
#st.sidebar.title("Select Meta and Year:")
#st.image("https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg", caption="World Happiness Dataset")
uploaded_file = st.file_uploader("Seleccionar archivo")
#proyect_list = ["Seleccionar Proyecto","Boxboard", "Maderas", "Boxia"]

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  #st.write(df)
  #Year Slider
  #score = st.sidebar.slider('Select Year', min_value=2022, max_value=2030, value = 2022) # Getting the input.
  #df[df['Year'] == score] # Filtering the dataframe.
  
  #select = st.sidebar.selectbox('Filter Proyect here:', proyect_list, key='1') 
  proyects = df['Proyecto'].unique()
  #st.write(type(proyects))
  #df1 = pd.DataFrame({0: ["Todos"]}, index=['3'])
  #st.write(type(df1))
  proyectss = proyects.tolist()
  proyectss.append('Todos')
  years = df['Year'].unique()
  select = st.sidebar.selectbox('Proyect', proyectss)
  year = df["Year"].loc[df["Proyecto"] == select].unique()
  year_choice = st.sidebar.selectbox('Year', year)
  #df['Year'] == score # Filtering the dataframe.
  if select == "Todos" : df.loc[(df['Year']==year_choice)]
  else : df.loc[(df['Proyecto']==select) & (df['Year']==year_choice)]
  
with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
