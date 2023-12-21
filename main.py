import numpy as np
import streamlit as st
import random as rand

language = {
	'a':"emphasis",
	'akesi': "reptile, amphibian",
	'ala': "no or not/zero",
	'alasa': "to hunt/forage",
	'ali': "",
	'anpa': "bowing down",
	'ante': "",
	'anu': "or",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
	'': "",
}

st.sidebar.title("Learn Toki Pona")

options = ["Home", "Dictionary"]
side_menu = st.sidebar.radio("Side Menu Widgets", options, label_visibility="hidden")


if side_menu == "Home":	
	st.title("Toki Pona Sona")
	st.caption("This is a website for you to learn toki pona!")

	st.divider()


	st.header("What is Toki Pona?")
	st.write(" ")

	st.write("Toki Pona is a simple language created by Sonja Lang.")


if side_menu == "Dictionary":
	st.title("Dictionary")
	st.divider()

	for word, meaning in language.items():
		f"{word}; {meaning}"
		st.write(" ")

		