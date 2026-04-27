import streamlit as st
import requests
import pandas as pd
import time

# ---------------- CONFIG ----------------
API_URL = "Add api url here"

# ---------------- PROFESSIONAL STYLE ----------------
def set_professional_style():
    st.markdown("""
    <style>

    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }

    h1, h2, h3 {
        color: #38bdf8;
        font-weight: 600;
    }

    section[data-testid="stSidebar"] {
        background-color: #020617;
    }

    .stButton>button {
        background-color: #38bdf8;
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }

    .block-container {
        padding-top: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)

# ---------------- RISK CALCULATION ----------------
def calculate_risk_latest(df):
    if df.empty:
        return 0

    latest = df.iloc[-1]
    score = 0

    if latest.get("temperature", 0) > 50:
        score += 2
    if latest.get("gas", 0) > 300:
        score += 2
    if latest.get("smoke", 0) > 200:
        score += 2
    if latest.get("flame", 0) == 1:
        score += 4

    return score

# ---------------- APPLY STYLE ----------------
set_professional_style()

# ---------------- FORCE TOKEN ----------------
st.session_state.token = "bypass"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🔥 HazardNet OZO")
    st.markdown("---")

    option = st.radio(
        "Select View",
        ["All Data", "Temperature", "Gas", "Smoke", "Flame"]
    )

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>📊 Live Monitoring Dashboard</h1>", unsafe_allow_html=True)

headers = {
    "Authorization": f"Bearer {st.session_state.token}"
}

# ---------------- FETCH DATA ----------------
try:
    r = requests.get(API_URL + "/sensor_status", headers=headers)

    if r.status_code == 200:
        data = r.json()
        df = pd.DataFrame(data)

        if df.empty:
            st.warning("No sensor data available")
            st.stop()

        # -------- RISK --------
        risk_score = calculate_risk_latest(df)

        if risk_score >= 6:
            st.error("🔥 HIGH FIRE RISK")
        elif risk_score >= 3:
            st.warning("⚠️ MODERATE RISK")
        else:
            st.success("✅ SAFE CONDITIONS")

        st.markdown("---")

        # -------- OPTIONS --------
        if option == "All Data":
            st.subheader("📊 Sensor Data")
            st.dataframe(df)
            st.line_chart(df[["temperature", "gas", "smoke", "flame"]])

        elif option == "Temperature":
            st.subheader("🌡 Temperature")
            st.line_chart(df["temperature"])

        elif option == "Gas":
            st.subheader("🧪 Gas")
            st.line_chart(df["gas"])

        elif option == "Smoke":
            st.subheader("💨 Smoke")
            st.line_chart(df["smoke"])

        elif option == "Flame":
            st.subheader("🔥 Flame")
            st.line_chart(df["flame"])

        # -------- AUTO REFRESH --------
        time.sleep(5)
        st.rerun()

    else:
        st.error("Failed to fetch data from server")

except Exception as e:
    st.error("Server not reachable")
    st.write(e)