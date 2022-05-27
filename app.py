import streamlit as st
import json
import pandas as pd
import plotly.graph_objects as go


make = ""
model = ""


JOB_HTML_TEMPLATE = """
<div style="width:100%;height:100%;
margin:10 px;
margin-bottom:25px;
padding:10px;
position:relative;
border-radius:5px #050A30;
border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #050A30;
background-color:#050A30;
 color:#ffffff;">
<h4 style="color:#B785B7">{}</h4>
<h4>{}</h4>
<h5>{}</h5>
<h6>{}</h6>
<h6>{}</h6>
<h6>Cylinder Specification:{}, {}</h6>
<h6>{}</h6>
<h6>{}</h6>
<h6>Fuel Specification: {}, {}</h6>
<h6>{}</h6>
<h6>{}</h6>
<h6>Wheels Details:{}, {}</h6>
<h6>Airbag details: {}, {}</h6>
</div>
"""


def get_data():
    f = open('cars.json', 'r')
    return json.loads(f.read())


def fun(element):
    if element['Make'] == make and element['Model'] == model:
        return True
    else:
        return False


def main():
    global make, model

    menu = ["Home", "About", "Visualization"]
    choice = st.sidebar.selectbox("Menu", menu)

    st.title("SearchCar.com")

    if choice == "Home":
        st.subheader("Home")

        # Nav  Search Form
        with st.form(key='searchform'):
            nav1, nav2, nav3 = st.columns([3, 2, 1])

            with nav1:
                make = st.text_input("Search car")
            with nav2:
                model = st.text_input("Model")

            with nav3:
                st.text("Search ")
                submit_search = st.form_submit_button(label='Search')

        st.success("You searched for {} in {}".format(make, model))

        # Results
        col1, col2 = st.columns([2, 3])

        with col1:
            if submit_search:
                # Create Search Query
                data = get_data()
                filtered = filter(fun, data)
                filtered_list = list(filtered)
                num_of_results = len(filtered_list)
                st.subheader("Showing {} Cars".format(num_of_results))

                with open('filt.json', 'w') as outputFile:
                    json.dump(filtered_list, outputFile)

                for i in filtered_list:
                    Make = i['Make']
                    Model = i['Model']
                    Variant = i['Variant']
                    Ex_Showroom_Price = i['Ex-Showroom_Price']
                    Displacement = i['Displacement']
                    Cylinders = i['Cylinders']
                    Cylinder_Configuration = i['Cylinder_Configuration']
                    Emission_Norm = i['Emission_Norm']
                    Engine_Location = i['Engine_Location']
                    Fuel_Tank_Capacity = i['Fuel_Tank_Capacity']
                    Fuel_Type = i['Fuel_Type']
                    ARAI_Certified_Mileage = i['ARAI_Certified_Mileage']
                    Power = i['Power']
                    Wheelbase = i['Wheelbase']
                    Wheels_Size = i['Wheels_Size']
                    Airbags = i['Airbags']
                    Number_of_Airbags = i['Number_of_Airbags']
                    st.markdown(JOB_HTML_TEMPLATE.format(Make, Model, Variant, Ex_Showroom_Price, Displacement, Cylinders, Cylinder_Configuration, Emission_Norm, Engine_Location, Fuel_Tank_Capacity, Fuel_Type, ARAI_Certified_Mileage, Power, Wheelbase, Wheels_Size, Airbags, Number_of_Airbags),
                                unsafe_allow_html=True)

        # with col2:
        # 	with st.form(key='email_form'):
        # 		st.write("Be the first to get new jobs info")
        # 		email = st.text_input("Email")

        # 		submit_email = st.form_submit_button(label='')

        # 		if submit_email:
        # 			st.success("A message was sent to {}".format(email))

    if choice == "About":
        st.subheader("About")
        df = pd.read_json('filt.json')
        st.table(df)
       

    if choice == "Visualization":
        st.subheader('Dashboard data set')
        data = pd.read_csv('cars_engage_2022.csv')
        c = pd.unique(data['Make'].value_counts(sort=False))
        st.write(c)
        a = pd.unique(data['Make'])
        st.write(a)

        fig = go.Figure(
            go.Pie(
                labels=a,
                values=c,
                hoverinfo="label+percent",
                textinfo="value"
            ))
        st.header("Cars of each company")
        st.plotly_chart(fig)


if __name__ == '__main__':
    main()
