import streamlit as st
import requests

st.set_page_config(page_title="🎓 Predicción Estudiantil", layout="centered")

# ------------------------
# 🚀 Función de solicitud
# ------------------------
def enviar_datos(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.text
    except Exception as e:
        return False, str(e)

# ------------------------
# 🎯 Título principal
# ------------------------
st.title("🎓 Sistema de Predicción Estudiantil")
st.markdown("Bienvenido. Completa los campos para conocer el riesgo de deserción del estudiante.")

st.divider()

# ------------------------
# 📋 Formulario de entrada
# ------------------------
with st.form("formulario_prediccion"):

    col1, col2 = st.columns(2)

    with col1:
        estudiante_id = st.number_input("🆔 ID Estudiante", value=1001)
        edad = st.number_input("🎂 Edad", value=21)
        genero = st.selectbox("⚧️ Género", ["Masculino", "Femenino"])
        becado = st.selectbox("🎓 ¿Tiene beca?", ["Sí", "No"])
        modalidad = st.selectbox("📚 Modalidad", ["Presencial", "Virtual"])

    with col2:
        nota_admision = st.number_input("📝 Nota de admisión", value=110.0)
        curso = st.number_input("📘 Código de curso", value=8014)
        desempleo = st.slider("📉 Tasa de desempleo (%)", 0.0, 50.0, 12.5)
        inflacion = st.slider("💸 Inflación (%)", 0.0, 20.0, 3.2)
        pib = st.number_input("📊 PIB (%)", value=1.8)

    st.divider()

    st.markdown("### 📈 Rendimiento Académico")

    col3, col4 = st.columns(2)
    with col3:
        nota_sem1 = st.number_input("📕 Promedio Semestre 1", value=11.0)
        nota_sem2 = st.number_input("📗 Promedio Semestre 2", value=10.5)
    with col4:
        aprobadas_1 = st.number_input("✅ Aprobadas Sem 1", value=12)
        aprobadas_2 = st.number_input("✅ Aprobadas Sem 2", value=10)

    enviado = st.form_submit_button("🚀 Enviar a la API")

# ------------------------
# 🔁 Enviar datos y mostrar resultado
# ------------------------
if enviado:
    genero_val = 1 if genero == "Femenino" else 0
    becado_val = 1 if becado == "Sí" else 0
    modalidad_val = 0 if modalidad == "Presencial" else 1

    payload = {
        "ID": estudiante_id,
        "Age": edad,
        "Gender": genero_val,
        "Scholarship": becado_val,
        "Mode": modalidad_val,
        "AdmissionGrade": nota_admision,
        "CourseCode": curso,
        "UnemploymentRate": desempleo,
        "InflationRate": inflacion,
        "GDP": pib,
        "GPA_Sem1": nota_sem1,
        "GPA_Sem2": nota_sem2,
        "Approved_Sem1": aprobadas_1,
        "Approved_Sem2": aprobadas_2
    }

    url_api = "http://127.0.0.1:8000/predict"  # Ajusta según tu API

    exito, resultado = enviar_datos(url_api, payload)

    st.divider()

    if exito:
        st.success("✅ ¡Datos enviados correctamente!")
        st.markdown("### 🎯 Resultado de la Predicción")
        st.info(f"📌 Resultado: **{resultado.get('prediction', 'Desconocido')}**")
    else:
        st.error(f"❌ Error al enviar: {resultado}")