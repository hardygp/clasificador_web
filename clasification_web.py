import streamlit as st
import joblib

# Cargar el modelo de NLP desde el archivo
loaded_model = joblib.load('modelo_nlp.joblib')

# Definir una función para clasificar la URL
def classify_url(url):
    # Usar el modelo de NLP para procesar el texto (suponiendo que el modelo toma texto como entrada)
    result = loaded_model.predict([url])
    return result[0]

def main():
    # Título
    st.title('CLASIFICADOR WEB')

    # Entrada de URL
    url = st.text_input('Ingrese la URL del sitio web para clasificar su contenido:', '')

    # Botón para clasificar
    if st.button('Clasificar'):
        if url:
            # Clasificar la URL
            result = classify_url(url)

            # Mostrar el resultado
            st.success(f'Done! ✅ This website URL {url} is classified as {result}.')
            st.balloons()
            st.caption('You can see a summary of the website content on the "Websites Content" page.')

if __name__ == '__main__':
    main()
