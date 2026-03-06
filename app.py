import streamlit as st
import time

# --- 1. Page Config ---
st.set_page_config(page_title="Jalwa Free Charge", page_icon="⚡", layout="centered")

# --- 2. CSS FOR DESIGN & BLACK TEXT ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    .block-container {
        padding-top: 0px !important;
        padding-bottom: 0px !important;
        padding-left: 15px !important;
        padding-right: 15px !important;
    }

    /* Moving Background */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: linear-gradient(-45deg, #1A4FA2, #6C63FF, #00D2FF, #9D50BB) !important;
        background-size: 400% 400% !important;
        animation: gradient 6s ease infinite !important;
    }

    /* Page 1 Box (LOCKED) */
    .main-box {
        background: white;
        padding: 15px;
        margin: -5px 0px 15px 0px; 
        border-radius: 0 0 15px 15px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
        text-align: center;
    }

    .row-item-p1 {
        background-color: #F8F9FB;
        padding: 12px;
        margin-bottom: 8px;
        text-align: left !important;
        border-left: 5px solid #1A4FA2;
        border-radius: 8px;
        font-weight: bold;
        color: #333;
    }

    /* Page 2 Styles */
    .system-title {
        color: white;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        margin-top: 30px;
    }

    .mira-patti {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 10px;
        border-radius: 12px;
        color: white;
        font-weight: 800;
        text-align: center;
        margin: 15px auto;
        font-size: 15px;
    }

    /* VIP & Direct Buttons */
    .direct-link-btn {
        display: block;
        width: 100%;
        background: linear-gradient(90deg, #1A4FA2, #6C63FF);
        color: white !important;
        height: 55px;
        line-height: 55px;
        text-decoration: none;
        text-align: center;
        font-size: 17px;
        font-weight: 800;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }

    /* Verification Counter Box */
    .verify-box-locked {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        font-weight: 900;
        font-size: 18px;
        border: 2px dashed rgba(255,255,255,0.5);
        width: 80%;
        margin: 15px auto;
    }

    /* CONGRATS BOX (Force Black Text) */
    .reward-box {
        background: #FFF9C4;
        border: 2px dashed #FBC02D;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: #000000 !important; /* FIXED BLACK TEXT */
    }

    .gift-code {
        font-family: monospace;
        font-size: 18px;
        font-weight: 900;
        background: #eee;
        padding: 10px;
        border-radius: 8px;
        color: #000000 !important; /* FIXED BLACK TEXT */
        margin-top: 10px;
    }

    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. App States ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'reward_unlocked' not in st.session_state:
    st.session_state.reward_unlocked = False

# ====== PAGE 1: UID INPUT (LOCKED) ======
if st.session_state.step == 1:
    st.image("banner.jpg", use_container_width=True)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div class="headline" style="color:#800020; font-size:26px; font-weight:800; margin-bottom:10px;">Jalwa Free Charge</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-item-p1">🔵 &nbsp; Deposit Instructions</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-item-p1">💳 &nbsp; Enter Jalwa UID</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-item-p1">👤 &nbsp; Instant Verification</div>', unsafe_allow_html=True)
    uid_val = st.text_input("Jalwa UID Yahan Daalein:", placeholder="e.g. 583935")
    if st.button("☝️ CLAIM REWARD"):
        if uid_val:
            st.session_state.uid = uid_val
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ====== PAGE 2: VERIFICATION ======
else:
    st.markdown('<div class="system-title">System Verification</div>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:white; font-weight:bold;'>UID: {st.session_state.uid} ✅</p>", unsafe_allow_html=True)

    if not st.session_state.reward_unlocked:
        st.markdown('<div class="mira-patti">Dono Channel Join Karo Tabhi Reward Khulega</div>', unsafe_allow_html=True)

        # Direct Link Buttons (Instant Open)
        st.markdown('<a href="https://t.me/+VjTmDNmVmF41N2Q1" target="_blank" class="direct-link-btn">Premium VIP Channel 1</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://t.me/+BSldTgoZeJ81NGZl" target="_blank" class="direct-link-btn">Premium VIP Channel 2</a>', unsafe_allow_html=True)

        st.write("") 

        # Verify Action with Timer
        if st.button(f"Verify - Click to Start Check"):
            btn_p = st.empty()
            for i in range(5, 0, -1):
                btn_p.button(f"Checking Membership {i}s...")
                time.sleep(1)
            st.session_state.reward_unlocked = True
            st.rerun()
    
    # --- CONGRATULATIONS & GIFT CODE (BLACK TEXT FIX) ---
    else:
        st.balloons()
        st.markdown(f"""
            <div class="reward-box">
                <h2 style="color:#2E7D32;">🎉 Congratulations!</h2>
                <p style="font-size:16px;">Aapka Gift Code ready hai:</p>
                <div class="gift-code">1C5278B274991FD67027B8299587E4ED</div>
                <p style="margin-top:10px; font-size:12px; color:red;">Ise copy karke app mein use karein.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("Claim Another?"):
            st.session_state.step = 1
            st.session_state.reward_unlocked = False
            st.rerun()

    if not st.session_state.reward_unlocked:
        if st.button("← GO BACK"):
            st.session_state.step = 1
            st.rerun()
