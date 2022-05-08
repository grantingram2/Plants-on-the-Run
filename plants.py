import pandas as pd
from PIL import Image
import urllib.parse
from io import StringIO
import streamlit as st
from pprint import pprint
import json
import requests as requests 
import sys
import sys
peanuttree = Image.open("C:\\Users\\Grant Ingram\\Pictures\\peanuttree.png")
appletree = Image.open("C:\\Users\\Grant Ingram\\Pictures\\appletree.png")
charlie = Image.open("C:\\Users\\Grant Ingram\\Downloads\\error.jpg")
logo = Image.open("C:\\Users\\Grant Ingram\\Downloads\\Google Images\\Plantsontherun.png")
st.image(logo)
search = st.text_input("Start searching!")
query = search
st.title(query)
if query == "peanut": 
    query = "Arachis Hypogaea"
if query == "apple": 
    query = "Malus Domestica"
if query == "peanuts": 
    st.image(charlie)
    st.title("You Missed!")
if query != "peanuts":
    queryparsed = urllib.parse.quote(query)
    img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\Default.png")
    img2 = Image.open("C:\\Users\\Grant Ingram\\Downloads\\Google Images\\USPeanutMap.png")
    img3 = Image.open("C:\\Users\\Grant Ingram\\Downloads\\applemap.png")
    if query == "Arachis Hypogaea" : img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\Peanut.jpg")
    if query == "Malus Domestica" : img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\Apple.jpg")
    if query != "" :
        if query != "Arachis Hypogaea" :
            if query != "Malus Domestica" : 
                img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\UhOh.png")
    if query != "" :
        if query != "Malus Domestica":
            if query != "Arachis Hypogaea": 
                img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\UhOh.png")
    response = requests.get("https://api.gbif.org/v1/species/search?q=" + queryparsed)
    table = response.json().get("results")
    #data = json.loads(response.text())
    #print(data.offset)
    st.image(img)
    if query != "":

        for x in table:
            st.title(("Canonical Name"))
            st.write(x.get("canonicalName"))
            st.title("Kingdom")
            st.write(x.get("kingdom"))
            st.title("Class")
            st.write(x.get("class"))
            st.title("Phylum")
            st.write(x.get("phylum"))
            st.title("Family")
            st.write(x.get("family"))
            if x.get("genus") != None:
                st.title("Genus")
                st.write(x.get("genus"))
            st.title("Order")
            st.write(x.get("order"))
            st.title("Map")
            if query == "Arachis Hypogaea":
                st.image(img2)
                st.write("Places where Arachis Hypogaea is located, with samples prioritized for collection. The darker a sample, the higher the priority, with red being the highest.")
            if query == "Malus Domestica":
                st.image(img3)
                st.write("Places where Malus Domestica is located, with samples prioritized for collection. The darker a sample, the higher the priority, with red being the highest.")
            if query != "Arachis Hypogaea" :
                if query != "Malus Domestica" : 
                    img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\UhOh.png")
            if query != "Malus Domestica":
                if query != "Arachis Hypogaea": 
                    st.write("None Available")
        
            st.title("Geneological Data")
            if query == "Arachis Hypogaea":
            
                st.image(peanuttree)
            if query == "Malus Domestica":
            
                st.image(appletree)
            if query != "Arachis Hypogaea" :
                if query != "Malus Domestica" : 
                    img = Image.open("C:\\Users\\Grant Ingram\\Downloads\\UhOh.png")
            if query != "Malus Domestica":
                if query != "Arachis Hypogaea": 
                    st.write("None Available")
            break
    


