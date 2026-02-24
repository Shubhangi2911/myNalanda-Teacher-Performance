import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

## --- 1. PAGE SETUP & HIGH-END THEME ---
st.set_page_config(page_title="myNalanda | AI Analytics", layout="wide")


st.markdown("""
    <style>
    /* 1. Animated Background Glow */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
        background-size: 200% 200%;
        animation: gradientBG 15s ease infinite;
        color: #f8fafc;
    }
    
    /* 2. Login Card with Subtle Pulse */
    .login-card {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(12px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(0, 206, 209, 0.4);
        box-shadow: 0 0 30px rgba(0, 206, 209, 0.15);
        margin-top: 50px;
        transition: transform 0.3s ease;
    }
    .login-card:hover {
        transform: translateY(-5px);
        border: 1px solid #00ced1;
    }

    /* 3. INPUT TEXT COLOR FIX (Very Important) */
    /* Input label visibility */
    .stTextInput label, .stSelectbox label {
        color: #00ced1 !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }

    .stTextInput input {
        color: #000000 !important;
        background-color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #00ced1 !important;
    }

    /* 4. BUTTON WITH ULTRA-MODERN NEON GLOW & PRESS EFFECT */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        /* Premium Cyan Gradient */
        background: linear-gradient(135deg, #00ced1 0%, #0891b2 100%);
        color: #000000 !important; /* Sharp Black Text for readability */
        font-weight: 1000 !important;
        font-size: 16px !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        border: none;
        height: 3.5em;
        
        /* 3.5D Shadow Effect */
        box-shadow: 0 4px 15px rgba(0, 206, 209, 0.4), 
                    inset 0 -3px 0 rgba(0, 0, 0, 0.2);
        
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    /* Hover Effect: Glow gets stronger and button lifts up */
    .stButton>button:hover {
        transform: translateY(-3px);
        background: linear-gradient(135deg, #07f3f7 0%, #00ced1 100%);
        box-shadow: 0 8px 25px rgba(0, 206, 209, 0.6);
        color: #000000 !important;
    }

    /* Active Effect: Button pushes down when clicked */
    .stButton>button:active {
        transform: translateY(1px);
        box-shadow: 0 2px 10px rgba(0, 206, 209, 0.4);
    }

    /* Adding a subtle shine reflection on the button */
    .stButton>button::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: rgba(255, 255, 255, 0.1);
        transform: rotate(45deg);
        transition: 0.5s;
        pointer-events: none;
    }

    .stButton>button:hover::after {
        left: 120%;
    }

    .stButton>button:hover {
        background-position: right center;
        box-shadow: 0 0 25px rgba(0, 206, 209, 0.6);
        color: #ffffff !important; /* Hover pe text white ho jayega */
    }

    /* 5. Dashboard Metrics & Sidebar Restoration */
    h1, h2, h3, span, p, .stMarkdown {
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    div[data-testid="stMetricValue"] {
        color: white !important;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0, 206, 209, 0.3);
    }
    
    div[data-testid="stMetricLabel"] {
        color: #00ced1 !important;
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 206, 209, 0.2);
        padding: 15px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATASET 
@st.cache_data
def load_data():
    try:
        
        df = pd.read_csv("Teacher_Dataset.csv", on_bad_lines='skip')
        return df
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return pd.DataFrame({
            "Teacher Name": ["Data Error"], 
            "Subject": ["N/A"], 
            "Compliance_Score": [0.0], 
            "Explanation": ["Check CSV formatting"]
        })

df = load_data()
# --- 3. LOGIN INTERFACE ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

def login_screen():
   
    _, col, _ = st.columns([1, 2, 1])
    
    with col:
        st.write("") 
        st.write("")
      
        st.markdown("<h1 style='text-align: center; color: #00ced1; font-size: 55px; margin-bottom: 0;'>myNalanda</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white; font-size: 16px; margin-top: 0;'>Ideal International School Analytics</p>", unsafe_allow_html=True)
        st.write("")

        with st.form("login_form", clear_on_submit=False):
            u = st.text_input("Username (admin)").strip().lower()
            p = st.text_input("Password (1234)", type="password").strip()
            role = st.selectbox("Login as", ["myN_Admin", "Principal", "Teacher"])
            
            submit = st.form_submit_button("LOGIN")
            
            if submit:
                # Login logic
                if u == "admin" and p == "1234":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Invalid Credentials. Please use admin / 1234")

        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
# --- 4. DASHBOARD CONTENT ---
if not st.session_state['auth']:
    login_screen()
else:
    # Sidebar navigation with white text
    st.sidebar.markdown("<h2 style='color: #00ced1 !important;'>🛠️ Navigation</h2>", unsafe_allow_html=True)
    page = st.sidebar.radio("Go to", ["Dashboard Overview", "Teacher Deep-Dive", "Late Counts & Attrition"])
    
    if st.sidebar.button("Logout"):
        st.session_state['auth'] = False
        st.rerun()

    if page == "Dashboard Overview":
        st.markdown("<h1 style='color: #00ced1 !important;'>🚀 Skills Analytics Dashboard</h1>", unsafe_allow_html=True)
        
        # KPI Row (Source 384: Metrics 55, 9, 137)
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Total Teachers", "55")
        k2.metric("Attrition Risk", "9", delta="-2")
        k3.metric("Late Counts", "137", delta="Current Month")
        k4.metric("Avg Quality", "5.6 / 10")

        st.divider()

        # Performance Indicators (Source 384: Gauges)
        st.markdown("<h2 style='color: white !important;'>Performance Indicators</h2>", unsafe_allow_html=True)
        g1, g2, g3, g4 = st.columns(4)
        
        def create_gauge(title, val, color, max_val=100):
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=val,
                title={'text': title, 'font': {'size': 18, 'color': 'white'}},
                gauge={'bar': {'color': color}, 'axis': {'range': [0, max_val], 'tickcolor': "white"}, 
                       'bgcolor': "rgba(0,0,0,0)", 'bordercolor': "rgba(255,255,255,0.3)"}))
            fig.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
            return fig

        g1.plotly_chart(create_gauge("Int. BM %", 62.8, "#00ced1"), use_container_width=True)
        g2.plotly_chart(create_gauge("Ext. BM %", 57.3, "#22c55e"), use_container_width=True)
        g3.plotly_chart(create_gauge("Compliance", 5.6, "#facc15", 10), use_container_width=True)
        g4.plotly_chart(create_gauge("Contribution", 6.3, "#f87171", 10), use_container_width=True)

        # Performance Landscape (Source 384: Area Chart)
        st.markdown("<h2 style='color: white !important;'>Performance Landscape</h2>", unsafe_allow_html=True)
        months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
        performance = [10, 15, 22, 45, 38, 55, 60, 65, 78, 85]
        fig_land = px.area(x=months, y=performance, labels={'x': 'Month', 'y': 'Score'})
        fig_land.update_traces(line_color='#00ced1', fillcolor='rgba(0, 206, 209, 0.2)')
        fig_land.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
        st.plotly_chart(fig_land, use_container_width=True)

    elif page == "Teacher Deep-Dive":
        st.markdown("<h1 style='color: #00ced1 !important;'>👩‍🏫 Individual Teacher Performance</h1>", unsafe_allow_html=True)
        
        selected = st.selectbox("Select Teacher Profile", df["Teacher Name"])
        t_data = df[df["Teacher Name"] == selected].iloc[0]

        # Status Logic: Score ke basis pe status decide karna
        if t_data['Compliance_Score'] >= 2.5:
            status = "🟢 ACTIVE"
            status_color = "#22c55e" # Green
        elif t_data['Compliance_Score'] >= 1.5:
            status = "🟡 MONITORING"
            status_color = "#facc15" # Yellow
        else:
            status = "🔴 AT RISK"
            status_color = "#f87171" # Red

        col_main, col_stats = st.columns([2, 1])
        
        with col_main:
            st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 15px; border-left: 8px solid #00ced1;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h2 style="margin:0; color: #00ced1 !important;">{selected}</h2>
                        <span style="background: {status_color}; color: black; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 14px;">
                            {status}
                        </span>
                    </div>
                    <p style="color: white; margin-top: 10px;">
                        <b>Subject:</b> {t_data['Subject']} | <b>Experience:</b> 11 Years
                    </p>
                    <hr style="opacity: 0.2;">
                    <p style="color: #94a3b8;"><b>HR Observations:</b></p>
                    <p style="color: white; font-style: italic;">"{t_data['Explanation']}"</p>
                    <br>
                    <p style="color: white;"><b>Detailed Skills:</b> Lesson Planning: ⭐⭐⭐ | Execution: ⭐⭐⭐</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col_stats:
            st.metric("Compliance Score", f"{t_data['Compliance_Score']} / 3.0")
            st.progress(t_data['Compliance_Score'] / 3.0) # Ek visual bar bhi add kar di
            st.markdown(f"<p style='text-align:center; color:{status_color}; font-weight:bold;'>Current Status: {status}</p>", unsafe_allow_html=True)

    elif page == "Late Counts & Attrition":
        st.markdown("<h1 style='color: #00ced1 !important;'>🕒 Attendance & Attrition Trends</h1>", unsafe_allow_html=True)
        c_left, c_right = st.columns([1, 1])
        
        with c_left:
            st.markdown("<h3 style='color: white !important;'>Late Arrival Trend (Monthly)</h3>", unsafe_allow_html=True)
            # Safe data handling for Plotly
            trend_df = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
                "Counts": [5, 8, 3, 12, 7, 9, 4, 6, 8, 5]
            })
            fig_late = px.line(trend_df, x="Month", y="Counts", markers=True)
            fig_late.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig_late, use_container_width=True)

        with c_right:
            st.markdown("<h3 style='color: white !important;'>Teacher Attrition Log</h3>", unsafe_allow_html=True)
            attrition_display = df[['Teacher Name', 'Compliance_Score', 'Explanation']].sort_values(by='Compliance_Score')
            st.dataframe(attrition_display, use_container_width=True)