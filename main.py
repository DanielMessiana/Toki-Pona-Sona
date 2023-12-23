import numpy as np
import streamlit as st
import random as rand
import time

rand.seed()

language = {
	'a':"emphasis",
	'akesi': "reptile, amphibian",
	'ala': "no or not/zero",
	'alasa': "to hunt/forage",
	'ali': "abundant, plentiful",
	'anpa': "bowing down",
	'ante': "",
	'anu': "or",
	'awen': "enduring",
	'e': "(before the direct object)",
	'en': "(between the multiple subjects)",
	'esun': "market, shop, business transaction",
	'ijo': "thing, object, phenomenon, matter",
	'ike': "bad, negative, irrelevant",
	'ilo': "tool, machine, implement",
	'insa': "center, inside, internal organ",
	'jaki': "disgusting, toxic, unclean",
	'jan': "person, human being",
	'jelo': "yellow",
	'jo': "carry, contain, hold",
	'kala': "fish, sea creature",
	'kalama': "to produce a sound, recite",
	'kama': "arriving, coming, future",
	'kasi': "plant, vegetation",
	'ken': "to be able to, can, possible",
	'kepeken': "to use, by means of",
	'kili': "fruit, vegetable, mushroom",
	'kin': "yes, too, indeed",
	'kiwen': "rock, metal, hard object",
	'ko': "clay, powder, dough, paste",
	'kon': "air, breath, essence",
	'kule': "colorful, painted",
	'kulupu': "community, group, society",
	'kute': "eat, listen, pay attention to",
	'la': "(between the context phrase and the main sentence)",
	'lape': "sleeping, resting",
	'laso': "blue, green",
	'lawa': "head, mind, lead, plan",
	'len': "cloth, fabric, cover, clothing",
	'lete': "cold, raw",
	'li': "between any subject (except mi or sina alone) and its verb. also to introduce a new verb for the same subject",
	'lili': "little, small, young",
	'linja': "long flexible thing, rope, thread, yarn",
	'lipu': "flat object, book, paper, website, card",
	'loje': "red",
	'lon': "located at, existing",
	'luka': "arm, hand, five",
	'lukin': "to look at, see, observe",
	'lupa': "door, window, hole",
	'ma': "earth, land, country, soil",
	'mama': "parent, ancestor, creator",
	'mani': "money, cash",
	'meli': "woman",
	'mi': "i, me, we, us",
	'mije': "man, male",
	'moku': "to eat, consume, drink",
	'monsi': "back, rear",
	'mu': "(animal noise or communication)",
	'mun': "moon, night sky object",
	'musi': "artistic, fun, playful",
	'mute': "many, several, much",
	'namako': "spice, extra",
	'nanpa': "-th (ordinal number); number",
	'nasa': "strange, crazy, drunk",
	'nasin': "way, method, path",
	'nena': "bump, mountain",
	'ni': "that, this",
	'nimi': "name, word",
	'noka': "foot, leg, organ of movement",
	'o': "hey! (vocatiave or imperative)",
	'oko': "eye",
	'olin': "to love, respect, show affection to",
	'ona': "he, she, it, they",
	'open': "to begin, open, turn on",
	'pakala': "broken, harmed, messed up, blunder",
	'pali': "to do, work on, build, prepare",
	'palisa': "long hard thing, branch, rod, stick",
	'pan': "cereal, barley, corn, bread, wheat, rice",
	'pana': "to give, provide, release",
	'pi': "of",
	'pilin': "feeling, a direct experience",
	'pimeja': "dark, unlit, black",
	'pini': "ago, ended, finished, past",
	'pipi': "bug, insect",
	'poka': "hip, side, next to, nearby",
	'pona': "good, useful, friendly, simple, thanks",
	'sama': "same, similar, fellow",
	'seli': "fire, heat source",
	'selo': "outer layer, bark, shell, skin",
	'seme': "what?, which?",
	'sewi': "highest part, divine, sacred",
	'sijelo': "body, physical state",
	'sike': "circular thing, ball, sphere, wheel",
	'sin': "new, more, another, fresh",
	'sina': "you",
	'sinpin': "face, front, wall",
	'sitelen': "image, symbol, mark",
	'sona': "knowledge, to know, have information on",
	'soweli': "animal, beast, land mammal",
	'suli': "big, large, tall, important, adult",
	'suno': "sun, light, shine, light source",
	'supa': "horizontal surface, thing to rest something on",
	'suwi': "sweet, cute, adorable",
	'tan': "by, from, because of",
	'taso': "but, however",
	'tawa': "go to, leave, toward, moving",
	'telo': "water, liquid, wet substance, beverage",
	'tenpo': "time, moment, occasion",
	'toki': "to communicate, speak, talk, think",
	'tomo': "indoor, home, room",
	'tu': "two",
	'unpa': "to have sexual relations with",
	'uta': "mouth, lips",
	'utala': "challenge, compete, struggle against",
	'walo': "white, light-colored, pale",
	'wan': "one, unique",
	'waso': "bird, winged animal",
	'wawa': "strong, powerful, energetic",
	'weka': "absent, ignored",
	'wile': "want, need, require",
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

def get_word():
	return rand.choice(list(language.items()))

def click_button():
	st.session_state.clicked = True

if side_menu == "Dictionary":
	st.title("Dictionary")
	rvg = st.checkbox("Random Vocabulary Generator")
	st.divider()

	if rvg:
		if 'current_word' not in st.session_state:
			st.session_state.current_word = get_word()

		word, meaning = st.session_state.current_word

		next_word = st.button("Next Word", type='primary')
		rvl = st.button("Reveal Meaning", on_click=click_button)
		st.header(word)

		if 'clicked' in st.session_state and st.session_state.clicked:
			st.subheader(meaning)
			st.session_state.current_word = get_word()
			st.session_state.clicked = False
	else:
		st.header("All words")
		for word, meaning in language.items():
			f"{word}; {meaning}"
			st.write(" ")

		st.divider()

# key: sentence, value: translation
tp_sentences = {
	'ona li toki': 'they are speaking',
	'mi sona': ['i know', 'i understand'],
	'kili li moku': 'fruit is food',
	'sina kute': 'you listen'
}

def get_sentence():
	return rand.choice(list(tp_sentences.items()))

if side_menu == "Sentence Game":
	st.title("Sentence Game")
	st.divider()

	st.write("Type this sentence in english")
	st.divider()

	sentence, translation = get_sentence()

	st.header(word)

	st.text_input("Write the answer in English here.")







		