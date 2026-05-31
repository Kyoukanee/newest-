import streamlit as st
import random

# --- Configuration ---
st.set_page_config(page_title="HAO Resort & Spa Hotel", layout="wide", initial_sidebar_state="collapsed")

# --- Custom Luxury CSS ---
st.markdown("""
    <style>
    /* Global Theme */
    .stApp {
        background-color: #0B140D; /* Dark forest/olive green from design */
        color: #F5F5F5;
        font-family: 'Georgia', serif;
    }
    
    /* Headers */
    h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-weight: normal;
        text-align: center;
    }
    
    /* Buttons (Book Now / Sign Up) */
    div.stButton > button {
        background-color: #A8815F; /* Gold/Brown accent */
        color: white;
        border: none;
        border-radius: 0px;
        padding: 10px 30px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #8C6A4D;
        color: white;
    }
    
    /* Text Inputs (Search & Email) */
    .stTextInput input {
        background-color: transparent !important;
        color: white !important;
        border: 1px solid #A8815F !important;
        border-radius: 0px;
    }
    
    /* Room Type styling */
    .room-title {
        color: #A8815F;
        font-size: 28px;
        margin-bottom: 5px;
        text-align: left;
    }
    .room-specs {
        color: #CCCCCC;
        font-size: 16px;
        margin-bottom: 20px;
        text-align: left;
        font-style: italic;
    }
    
    /* Dividers */
    hr {
        border-color: #243B2A;
        margin-top: 50px;
        margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Base64 Logo ---
logo_base64_string = "iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAYAAAA8AXHiAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAwIDc5LjE1NjU3NiwgMjAyNC8wMS8zMC0wNzozMDo0NCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDI1LjUgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjNFNkQ5MUI1MkQyRjExRkY4RjY3OTk5NkM3QTU4NTREIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjNFNkQ5MUI2MkQyRjExRkY4RjY3OTk5NkM3QTU4NTREIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6M0U2RDkxQjMyRDJGMTFGRjhGNjc5OTk2QzdBNTg1NEQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6M0U2RDkxQjQyRDJGMTFGRjhGNjc5OTk2QzdBNTg1NEQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6E41ZkAAAFBklEQVR4nO3d3W7cRBAE0L41tE2R6wP6/pdpXyQfQh+jL9O2RjA1lM/O7q7VqgL/x/R5Z3q4H0/9dI3oO7t4+71b12b5P707V70v446aH14/n6w/P3m361iT/c+N7a3u794P9/kXz41m22x8bK/y91gQ/c29oQ7N134wF/nNf3a4bB/yV83x9o1qTzW/L5+e1S+N1L+0/3t33+N1s85/qR7e86k2+yT29r9e53M22vXy6jGzH2j7p5+i/53O2iW1iW0322w/G/985G1s97q899t76P6/r9zY8PqXk9k8+eT4Xk/H5/Xk1WfL0mS2/F/Wp8l1YV2zJj15d/55W01eP/9u2lR9S7L907Z+l+s618S2yS0u72T7Z6u7rS7bT8t1k+u6qO222u66/XJ9S/W7+H9/a+u/Xp/n9Xy22/F6Xl7L5z/r9V/W/x9Z/2b9+yP/Xb17N91/W59v/3eP5/P7m9/t81o/317/9X/a72199b9/7p39e/1vM7Z/868t/s/6/XpLpL9rX5/9vXy2s5/vj/99X8+q/37+9b/+/yL+7yP/XW+L67J/s+2/s303n/d6r/8e//f5f/v4t5r24/299v9y/u5f/W7n/5+a/3O2f2b3/yvO/8P9H/27/v1+iXb5/r4//0e9Nf+z1n6f/f/V9X2tH76u9e52516a/nZ9+3d65/r+u557/n7L6f9189m21/p+aXG2S27Z9H+23b+vL7/eS/t18fXb+t+L2p+z7R75e+b7jW52rU3+N/t77X13n9+v216y9+v/W9e+yq398T7W/XW91z7a36f7yM9r2d1396b7G0+m1/6tX2X2d1t+b094rW3t21Xv/l/tJ9t71V9pP3O9v/r9qX7+e4S1Lp7Y/q+a42f6/7sW5p1k21t+72f094i91u631Yn21e/9pS2vJ3e5621r5X1/vL2/fX2668r213q4z+2l75/O129l5X18d/u+v6L1fVd9X5X1+e9u/8H+P9+XlZ3X+O7281o/2+r+L/j9638H91b7d+5q9r/s31V372f+x3d+4a35v+u6v2/V9Zt7eR/yv1t7/N25N/x0b4b2T6m27H0L3+Hq52vU31f133fU9L3Xv63q3L9/73d7P9V72tT7y+6216/XW/n6T5P194e1u3f2/o26372X6d/X+Vv7H3d/nN6h/v+r3X8/4v+q5P4P94Xyv112/q7776z1T95L29849nL89p7yXz+f/j+7p4+631d5/g4H9/n2/1e9x88P1t7+B83t3919d3lV6q93lO/L938w13k9f/e7/0r+Xz1fVb7+s92/29/P7+VnN/5v4v7m7q/P+w797b5eH1e/nL+x+4s/y8f3Xn57LdJv9fH7/O/V87/hW53+6v3u3h/5m/6/8H309/G+P79h4vW/g96/70364f9/a9/n+7b38u/S38+t9t2l/x+L/x+39PzV+4Nf8R2a7f5l/674d8P9+Xz3u+T+1vJ25n4y/d/A/f98+r/T39P5f/2X/V9/w/5t7D3h+6v+7b7f9+Ld/9eXz83437/yP/hH/bO9f6/t+O/vPZc6/299v/9+R+4f7k9/p+d6/9d2f79j7/Yn/1f5n9e612f8/t7H92197f2/b6v4b3/a+/+9zN/35P5/+v+7+B/9v9rX/h34r69f1/Wf1t8T+z9+v+5f3r+s//xT/9+1/r+38y+h//1fW/8P/d/D39u9v/2V3n7P3m+37+P/f0fP8v6f4v+7j/9/X+P/b3+9/wA=="

# --- Initialize Hotel Data ---
def init_hotel_data():
    if 'hotel_data' not in st.session_state:
        hotel = {}
        for floor in [1, 2, 3]:
            for room in range(0, 11): # Generates 100-110, 200-210, 300-310
                room_num = str((floor * 100) + room)
                hotel[room_num] = {
                    "status": random.choice(["Vacant", "Occupied"]),
                    "type": random.choice(["Deluxe", "King Deluxe", "Bay View Suite", "Metropolitan Suite"])
                }
        st.session_state.hotel_data = hotel

init_hotel_data()

# ==========================================
# 1. HERO SECTION
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f'<center><img src="data:image/jpeg;base64,{logo_base64_string}" width="180"></center>', unsafe_allow_html=True)
st.markdown("""
    <h1 style='letter-spacing: 5px; font-size: 3rem; margin-bottom: 0px;'>HAO</h1>
    <h4 style='letter-spacing: 3px; font-size: 1rem; margin-top: 0px;'>RESORT & SPA HOTEL</h4>
    <p style='text-align: center; font-style: italic; color: #DDDDDD; margin-top: 20px;'>
        Leave everything behind. Stay for a night.<br>Your room is waiting and you have time.
    </p>
""", unsafe_allow_html=True)

# Centered layout for the hero elements
hero_col1, hero_col2, hero_col3 = st.columns([1, 1, 1])
with hero_col2:
    st.markdown("<br>", unsafe_allow_html=True)
    
# ==========================================
# 2. ROOM AVAILABILITY SEARCH
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2>Find out if your room<br>is available here!</h2>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: #BBBBBB; max-width: 600px; margin: 0 auto;'>
    HAO Hotel menawarkan fitur pencarian kamar otomatis untuk memudahkan resepsionis 
    mengecek kamar kosong dengan cepat. Sistem akan memindai setiap lantai dan berhenti 
    saat kamar tersedia ditemukan, sehingga proses menjadi lebih efisien.
    </p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
search_col1, search_col2, search_col3 = st.columns([1, 2, 1])
with search_col2:
    room_input = st.text_input("Room Number", placeholder="Enter Room Number (e.g., 101, 205)", label_visibility="collapsed")
    if st.button("CHECK HERE"):
        valid_rooms = [str((f * 100) + r) for f in [1, 2, 3] for r in range(0, 11)]
        if room_input in valid_rooms:
            info = st.session_state.hotel_data[room_input]
            if info["status"] == "Vacant":
                st.success(f"✅ Room {room_input} is currently {info['status']}! ({info['type']})")
            else:
                st.warning(f"❌ Room {room_input} is currently {info['status']}. ({info['type']})")
        else:
            st.error("Error: Invalid room number. Please enter a number between 100-110, 200-210, or 300-310.")

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# 3. ROOM TYPES (Mimicking the PDF layout)
# ==========================================
# Note: Using high-quality placeholder images directly from web so you don't need to upload files.
room_data = [
    {"name": "Deluxe", "specs": "Up to 2 guests | Queen bed or 2 double beds", "img": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=800&q=80"},
    {"name": "King Deluxe", "specs": "Up to 2 guests | 1 King bed", "img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80"},
    {"name": "Bay View Suite", "specs": "Up to 4 guests | 2 Queen beds", "img": "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=800&q=80"},
    {"name": "Metropolitan Suite", "specs": "Up to 3 guests | 1 King bed, 1 Single bed", "img": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=800&q=80"}
]

for room in room_data:
    r_col1, r_col2 = st.columns([1, 1.5], gap="large")
    with r_col1:
        st.image(room["img"], use_container_width=True)
    with r_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<div class='room-title'>{room['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='room-specs'>{room['specs']}</div>", unsafe_allow_html=True)
        # Using columns to make the button not span the whole width
        btn_col, _ = st.columns([1, 2])
        with btn_col:
            st.button(f"BOOK NOW", key=f"btn_{room['name']}")
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# 4. FLOOR PLANS (With Emoji Status)
# ==========================================
st.markdown("<h2>Denah Hotel</h2><br>", unsafe_allow_html=True)

floor_col1, floor_col2, floor_col3 = st.columns(3)

# Floor 1
with floor_col1:
    st.markdown("<h3 style='color:#A8815F !important;'>LANTAI 1</h3>", unsafe_allow_html=True)
    for r in range(100, 111):
        status = st.session_state.hotel_data[str(r)]["status"]
        status_color = "🟢" if status == "Vacant" else "🔴"
        st.markdown(f"**{status_color} Room {r}**: &nbsp;&nbsp; {status}")

# Floor 2
with floor_col2:
    st.markdown("<h3 style='color:#A8815F !important;'>LANTAI 2</h3>", unsafe_allow_html=True)
    for r in range(200, 211):
        status = st.session_state.hotel_data[str(r)]["status"]
        status_color = "🟢" if status == "Vacant" else "🔴"
        st.markdown(f"**{status_color} Room {r}**: &nbsp;&nbsp; {status}")

# Floor 3
with floor_col3:
    st.markdown("<h3 style='color:#A8815F !important;'>LANTAI 3</h3>", unsafe_allow_html=True)
    for r in range(300, 311):
        status = st.session_state.hotel_data[str(r)]["status"]
        status_color = "🟢" if status == "Vacant" else "🔴"
        st.markdown(f"**{status_color} Room {r}**: &nbsp;&nbsp; {status}")

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# 5. FOOTER: STAY IN TOUCH
# ==========================================
st.markdown("<h2>STAY IN TOUCH</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #BBBBBB;'>Subscribe to receive updates, access to exclusive deals, and more.</p>", unsafe_allow_html=True)

foot_col1, foot_col2, foot_col3 = st.columns([1, 2, 1])
with foot_col2:
    email_col, btn_col = st.columns([3, 1])
    with email_col:
        st.text_input("Email", placeholder="Enter your email address", label_visibility="collapsed")
    with btn_col:
        st.button("SIGN UP", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: #777777; font-size: 12px;'>
    HAO RESORT & SPA HOTEL<br>
    Jl. Cempaka Putih No. 12, Jakarta Pusat, Indonesia<br>
    © 2026 HAO Hotel. All Rights Reserved.
    </p>
""", unsafe_allow_html=True)