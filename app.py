#!/usr/bin/env python
# coding: utf-8

# In[7]:


import leafmap.foliumap as leafmap
img1 = "2.png"
img2 = "1.png"
leafmap.image_comparison(
    img1,
    img2,
    label1="2024",
    label2="2019",
    starting_position=50,
    out_html="image_comparison.html"
)


# In[6]:


import streamlit as st
import streamlit.components.v1 as components
import leafmap.foliumap as leafmap

# Leafmap haritasını oluştur
m = leafmap.Map()

# Haritaya katmanlar veya veri ekleyin
# Örnek: m.add_basemap('OpenStreetMap')

# Haritayı bir HTML dosyası olarak dışa aktar
m.to_html(outfile='map.html')

# Streamlit uygulamasında haritayı göster
HtmlFile = open('map.html', 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=600)


# In[ ]:




