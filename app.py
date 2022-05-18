# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc
import requests 
import json

base_url = "https://github.com/Kokatesrushti/Msengage_22/blob/main/unece.json?country={}&year={}"

# Fxn to Retrieve Data
def get_data(url):
	resp = requests.get(url)
	return resp.json()


def main():
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	st.title("DevDeeds -Search Jobs")

	if choice == "Home":
		st.subheader("Home")

		# Nav  Search Form
		with st.form(key='searchform'):
			nav1,nav2,nav3 = st.columns([3,2,1])

			with nav1:
				search_term = st.text_input("Search car")
			with nav2:
				location = st.text_input("Model")

			with nav3:
				st.text("Search ")
				submit_search = st.form_submit_button(label='Search')

		st.success("You searched for {} in {}".format(search_term,location))

		# Results
		col1, col2 = st.columns([2,3])

		with col1:
			if submit_search:
				# Create Search Query
				search_url = base_url.format(search_term,location)
				# st.write(search_url)
				data = get_data(search_url)

				# Number of Results
				num_of_results = len(data)
				st.subheader("Showing {} jobs".format(num_of_results))
				st.json(st.write(data)) 
		



		# with col2:
		# 	with st.form(key='email_form'):
		# 		st.write("Be the first to get new jobs info")
		# 		email = st.text_input("Email")

		# 		submit_email = st.form_submit_button(label='Subscribe')

		# 		if submit_email:
		# 			st.success("A message was sent to {}".format(email))







	else:
		st.subheader("About")




if __name__ == '__main__':
	main()

