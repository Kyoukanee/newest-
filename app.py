import streamlit as st
import random

# Konfigurasi Halaman
st.set_page_config(page_title="RestEase - GrandDeluxe", layout="wide")

# Inisialisasi Data Hotel (Simulasi)
def init_hotel_data():
    if 'hotel_data' not in st.session_state:
        hotel = {}
        room_types = ["Deluxe", "King Deluxe", "Suite"]
        
        for lantai in range(1, 4): # Lantai 1-3
            hotel[lantai] = {}
            for nomor in range(1, 11): # Kamar 1-10
                # Random status untuk simulasi (bisa diganti logic lain)
                status = random.choice(["Vacant", "Occupied"])
                # Menentukan tipe kamar berdasarkan nomor
                if nomor <= 3: tipe = room_types[0]
                elif nomor <= 7: tipe = room_types[1]
                else: tipe = room_types[2]
                
                hotel[lantai][f"{lantai}{nomor:02d}"] = {
                    "status": status,
                    "tipe": tipe
                }
        st.session_state.hotel_data = hotel

init_hotel_data()

# --- HEADER ---
st.title("🏨 RestEase: GrandDeluxe Hotel")
st.subheader("Sistem Pencarian Kamar Otomatis")

# --- VISUALISASI DENAH ---
st.write("### Denah Lantai Hotel")
tabs = st.tabs(["Lantai 1", "Lantai 2", "Lantai 3"])

for i, tab in enumerate(tabs):
    lantai_idx = i + 1
    with tab:
        cols = st.columns(5)
        for idx, (no_kamar, data) in enumerate(st.session_state.hotel_data[lantai_idx].items()):
            color = "green" if data["status"] == "Vacant" else "red"
            cols[idx % 5].metric(label=f"Kamar {no_kamar}", value=data["status"], help=f"Tipe: {data['tipe']}")

# --- LOGIKA PENCARIAN (SESUAI FLOWCHART) ---
st.divider()
st.write("### Panel Resepsionis")

if st.button("Cari Kamar Kosong (Scan Otomatis)"):
    found = False
    result_kamar = None
    result_lantai = None
    
    # PROSES LOOP SESUAI PSEUDOCODE
    # Loop Luar: Lantai
    for lantai in range(1, 4):
        
        # Loop Dalam: Nomor Kamar
        for nomor in range(1, 11):
            room_id = f"{lantai}{nomor:02d}"
            
            # Pengecekan Status
            if st.session_state.hotel_data[lantai][room_id]["status"] == "Vacant":
                result_kamar = room_id
                result_lantai = lantai
                found = True
                break # Break Inner Loop
        
        if found:
            break # Break Outer Loop
    
    # OUTPUT HASIL
    if found:
        st.success(f"✅ Kamar ditemukan: Lantai {result_lantai}, No {result_kamar}")
        st.balloons()
    else:
        st.error("❌ Maaf, semua kamar di lantai 1-3 penuh.")

# Tombol Reset untuk simulasi ulang
if st.button("Reset Status Kamar (Simulasi)"):
    del st.session_state.hotel_data
    st.rerun()