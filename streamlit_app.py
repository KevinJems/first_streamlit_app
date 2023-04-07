import streamlit

streamlit.title ('My Mom\'s New Healthy Diner')

streamlit.header ('Breakfast Favorites')
streamlit.text ('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
   
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)



from bs4 import BeautifulSoup

# Ouvrir le fichier HTML
with open('http://www.kirschpm.fr/cours/M1Gestion/pages/coursHTML-1.html', 'r') as f:
    contenu_html = f.read()

# Passer le contenu HTML à Beautiful Soup
soup = BeautifulSoup(contenu_html, 'html.parser')

# Rechercher tous les éléments qui contiennent la chaîne de caractères spécifiée
elements = soup.find_all(string='Important')

# Parcourir tous les éléments trouvés et extraire les données nécessaires
for element in elements:
    # Extraire les données de l'élément en utilisant les méthodes de Beautiful Soup
    donnees = element.parent.next_sibling.get_text()
    print(donnees)

# Fermer le fichier HTML
f.close()

# Display the table on the page.
streamlit.dataframe(donnees)

