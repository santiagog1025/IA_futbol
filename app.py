import streamlit as st
import requests

# URL del modelo de Flowise
API_URL = "https://flowise-0jhl.onrender.com/api/v1/prediction/57fce68a-870f-4f49-8e53-2df56755c7bf"

# Función para enviar una pregunta al modelo
def query(payload):
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}

# Configuración de la app
st.set_page_config(page_title="Asistente de futbol", page_icon="🤖")

st.title("⚽ Asistente de futbol")
st.markdown("Este asistente es para expandir tu conocimiento en futbol.")

# Session state para mantener el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial del chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Mostrar el mensaje del usuario
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener respuesta del modelo
    response = query({"question": prompt})

    # Mostrar la respuesta
    answer = response.get("text", "❌ No se pudo obtener respuesta del modelo.")
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
