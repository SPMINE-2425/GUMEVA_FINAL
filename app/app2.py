import streamlit as st
import requests

# Función para realizar la solicitud POST a la API
def realizar_solicitud_post(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.text
    except Exception as e:
        return False, str(e)

st.set_page_config(page_title="🎓 Predicción Estudiantil", layout="centered")
st.title("🎓 Formulario de Datos Estudiantiles")
st.markdown("Completa la información para enviar los datos a la API y predecir el resultado.")

with st.form("api_form"):
    st.subheader("🆔 Información General")
    name = st.number_input("ID del estudiante", value=657)
    marital_status = st.selectbox("Estado civil", [0, 1, 2])
    app_mode = st.number_input("Modalidad de aplicación", value=51)
    app_order = st.number_input("Orden de aplicación", value=1)
    course = st.number_input("Código del curso", value=8014)
    attendance = st.selectbox("¿Asistencia diurna?", [0, 1])

    st.subheader("📚 Antecedentes Académicos")
    prev_qual = st.number_input("Calificación previa (categoría)", value=1)
    prev_qual_grade = st.number_input("Nota previa", value=121.0)
    admission_grade = st.number_input("Nota de admisión", value=112.3)

    st.subheader("👨‍👩‍👧 Familia")
    nationality = st.number_input("Nacionalidad", value=1)
    mother_qual = st.number_input("Nivel educativo madre", value=1)
    father_qual = st.number_input("Nivel educativo padre", value=38)
    mother_occ = st.number_input("Ocupación madre", value=5)
    father_occ = st.number_input("Ocupación padre", value=7)

    st.subheader("🧾 Datos Personales")
    displaced = st.selectbox("¿Desplazado?", [0, 1])
    special_needs = st.selectbox("¿Necesidades especiales?", [0, 1])
    debtor = st.selectbox("¿Es deudor?", [0, 1])
    tuition_up_to_date = st.selectbox("¿Matrícula al día?", [0, 1])
    gender = st.selectbox("Género", [0, 1])  # 0 = masculino, 1 = femenino
    scholarship = st.selectbox("¿Becado?", [0, 1])
    age = st.number_input("Edad al ingresar", value=22)
    international = st.selectbox("¿Estudiante internacional?", [0, 1])

    st.subheader("📊 Rendimiento Académico")
    # Curricular 1er semestre
    cu1_credited = st.number_input("1er sem - Unidades acreditadas", value=14)
    cu1_enrolled = st.number_input("1er sem - Unidades inscritas", value=16)
    cu1_evaluations = st.number_input("1er sem - Evaluaciones", value=16)
    cu1_approved = st.number_input("1er sem - Unidades aprobadas", value=13)
    cu1_grade = st.number_input("1er sem - Nota promedio", value=10.92)
    cu1_wo_eval = st.number_input("1er sem - Sin evaluación", value=0)

    # Curricular 2do semestre
    cu2_credited = st.number_input("2do sem - Unidades acreditadas", value=13)
    cu2_enrolled = st.number_input("2do sem - Unidades inscritas", value=13)
    cu2_evaluations = st.number_input("2do sem - Evaluaciones", value=13)
    cu2_approved = st.number_input("2do sem - Unidades aprobadas", value=11)
    cu2_grade = st.number_input("2do sem - Nota promedio", value=11.45)
    cu2_wo_eval = st.number_input("2do sem - Sin evaluación", value=0)

    st.subheader("📉 Contexto Económico")
    unemployment_rate = st.number_input("Tasa de desempleo", value=16.2)
    inflation_rate = st.number_input("Inflación", value=0.3)
    gdp = st.number_input("PIB", value=-0.92)

    submitted = st.form_submit_button("📩 Enviar")

    if submitted:
        datos_json = {
            "name": name,
            "Marital Status": marital_status,
            "Application mode": app_mode,
            "Application order": app_order,
            "Course": course,
            "Daytime/evening attendance": attendance,
            "Previous qualification": prev_qual,
            "Previous qualification (grade)": prev_qual_grade,
            "Nacionality": nationality,
            "Mother's qualification": mother_qual,
            "Father's qualification": father_qual,
            "Mother's occupation": mother_occ,
            "Father's occupation": father_occ,
            "Admission grade": admission_grade,
            "Displaced": displaced,
            "Educational special needs": special_needs,
            "Debtor": debtor,
            "Tuition fees up to date": tuition_up_to_date,
            "Gender": gender,
            "Scholarship holder": scholarship,
            "Age at enrollment": age,
            "International": international,
            "Curricular units 1st sem (credited)": cu1_credited,
            "Curricular units 1st sem (enrolled)": cu1_enrolled,
            "Curricular units 1st sem (evaluations)": cu1_evaluations,
            "Curricular units 1st sem (approved)": cu1_approved,
            "Curricular units 1st sem (grade)": cu1_grade,
            "Curricular units 1st sem (without evaluations)": cu1_wo_eval,
            "Curricular units 2nd sem (credited)": cu2_credited,
            "Curricular units 2nd sem (enrolled)": cu2_enrolled,
            "Curricular units 2nd sem (evaluations)": cu2_evaluations,
            "Curricular units 2nd sem (approved)": cu2_approved,
            "Curricular units 2nd sem (grade)": cu2_grade,
            "Curricular units 2nd sem (without evaluations)": cu2_wo_eval,
            "Unemployment rate": unemployment_rate,
            "Inflation rate": inflation_rate,
            "GDP": gdp
        }

        url = "http://127.0.0.1:8000/students/"  # Ajusta según tu endpoint

        exito, respuesta = realizar_solicitud_post(url, datos_json)

        if exito:
            st.success(f"✅ Solicitud exitosa. Respuesta: {respuesta}")
        else:
            st.error(f"❌ Error en la solicitud: {respuesta}")