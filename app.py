import streamlit as st
import time
import os

# --- 1. Page Config ---
st.set_page_config(page_title="Jalwa Free Charge", page_icon="⚡", layout="centered")

# --- 2. CSS (Design) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp {
        background: linear-gradient(-45deg, #1A4FA2, #6C63FF, #00D2FF, #9D50BB) !important;
        background-size: 400% 400% !important;
        animation: gradient 6s ease infinite !important;
    }
    .main-box { background: white; padding: 15px; border-radius: 0 0 15px 15px; text-align: center; }
    .row-item-p1 { background-color: #F8F9FB; padding: 12px; margin-bottom: 8px; text-align: left; border-left: 5px solid #1A4FA2; border-radius: 8px; font-weight: bold; color: #333; }
    .system-title { color: white; font-size: 28px; font-weight: 900; text-align: center; margin-top: 30px; }
    .mira-patti { background: rgba(255, 255, 255, 0.25); backdrop-filter: blur(10px); padding: 10px; border-radius: 12px; color: white; font-weight: 800; text-align: center; margin: 15px auto; }
    .direct-link-btn { display: block; width: 100%; background: linear-gradient(90deg, #1A4FA2, #6C63FF); color: white !important; height: 55px; line-height: 55px; text-decoration: none; text-align: center; font-size: 18px; font-weight: 800; border-radius: 12px; margin-bottom: 15px; }
    .reward-box { background: #FFF9C4; border: 2px dashed #FBC02D; padding: 20px; border-radius: 15px; text-align: center; color: #000 !important; }
    .gift-code { font-family: monospace; font-size: 18px; font-weight: 900; background: #eee; padding: 10px; border-radius: 8px; color: #000 !important; margin-top: 10px; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. App States ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'reward_unlocked' not in st.session_state: st.session_state.reward_unlocked = False
if 'clicked_join' not in st.session_state: st.session_state.clicked_join = False

# Path setting for JPG
base_path = os.path.dirname(__file__)
banner_path = os.path.join(base_path, "banner.jpg") # Ab JPG dhundega

# ====== PAGE 1: UID INPUT & BANNER ======
if st.session_state.step == 1:
    # 🖼️ JPG BANNER DISPLAY
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)
    else:
        st.error(f"⚠️ File 'banner.jpg' nahi mili! Check karein: {banner_path}")

    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div style="color:#800020; font-size:26px; font-weight:800; margin-bottom:10px;">Jalwa Free Charge</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-item-p1">🔵 &nbsp; Step 1: Join VIP Channel</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-item-p1">💳 &nbsp; Step 2: Enter Jalwa UID</div>', unsafe_allow_html=True)
    
    uid_val = st.text_input("Jalwa UID Yahan Daalein:", placeholder="e.g. 583935")
    
    if st.button("☝️ CLAIM REWARD"):
        if uid_val:
            st.session_state.uid = uid_val
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ====== PAGE 2: VERIFICATION ======
else:
    st.markdown('<div class="system-title">Verification</div>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:white; font-weight:bold;'>UID: {st.session_state.uid} ✅</p>", unsafe_allow_html=True)

    if not st.session_state.reward_unlocked:
        st.markdown('<div class="mira-patti">Channel Join Karo Tabhi Gift Code Milega</div>', unsafe_allow_html=True)

        # Telegram Link (Single)
        st.markdown('<a href="https://t.me/+9ndzhPjLTP1iN2Jl" target="_blank" class="direct-link-btn">🚀 Join VIP Channel</a>', unsafe_allow_html=True)

        confirm = st.checkbox("Maine Join kar liya hai ✅")
        
        if st.button("Verify & Get Code"):
            if confirm:
                btn_p = st.empty()
                for i in range(5, 0, -1):
                    btn_p.button(f"Checking Status... {i}s")
                    time.sleep(1)
                st.session_state.reward_unlocked = True
                st.rerun()
            else:
                st.warning("⚠️ Pehle join karke tick karein!")

    # ====== CONGRATS PAGE ======
    else:
        st.balloons()
        st.markdown(f"""
            <div class="reward-box">
                <h2 style="color:#2E7D32;">🎉 Congratulations!</h2>
                <div class="gift-code">1C5278B274991FD67027B8299587E4ED</div>
                <p style="margin-top:10px; font-size:12px; color:red;">Copy karke app mein recharge karein.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Claim Another?"):
            st.session_state.step = 1
            st.session_state.reward_unlocked = False
            st.rerun()
