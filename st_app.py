# Import the required libraries
import streamlit as st
import json
import requests

# Define the endpoint of the FastAPI application
endpoint = "https://idsudd--example-fastapi-app-fastapi-app.modal.run/campaign"

# Set the title of the Streamlit application
st.title("Marketing Campaign Generator 🔥")

# Create a text area for the user to input their brand name and a short description of their brand
prompt = st.text_area("Enter your brand name and a short description of your brand. We will generate a marketing campaign for you 🚀.")



# Preparar el input para la API
input = {"prompt": prompt}

# Si se presiona el botón, enviar la solicitud y mostrar la respuesta
if st.button("Generate"):
    if not prompt.strip():
        st.warning("Por favor, ingresa una descripción de tu marca.")
    else:
        with st.spinner("Generando campaña..."):
            try:
                res = requests.post(url=endpoint, data=json.dumps(input))
                res.raise_for_status()
                res_json = res.json()
                st.subheader("Generated Campaign")
                st.markdown(res_json["campaign_text"])
            except requests.exceptions.RequestException as e:
                st.error(f"Error al conectar con el servidor: {e}")
            except json.JSONDecodeError:
                st.error("Error al procesar la respuesta del servidor.")
            except KeyError:
                st.error("Respuesta inesperada del servidor.")