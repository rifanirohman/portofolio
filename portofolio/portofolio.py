import streamlit as st

# Konfigurasi Halaman (Harus di paling atas)
st.set_page_config(
    page_title="Portofolio | Nama Anda",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Kustom untuk Tampilan Lebih Profesional ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .st-bb {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # Ganti dengan foto profil Anda
    st.title("Kontak Saya")
    st.write("📍 Surabaya, Indonesia")
    st.write("📧 email.anda@gmail.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/)")
    st.write("🐙 [GitHub](https://github.com/)")
    
    st.divider()
    st.write("© 2026 Dibuat dengan Streamlit")

# --- KONTEN UTAMA ---
st.title("Halo! Saya [Nama Anda] 👋")
st.subheader("Seorang Web Developer & Python Enthusiast")
st.write("""
Selamat datang di halaman portofolio saya. Saya berdedikasi untuk menciptakan solusi digital 
yang inovatif, efisien, dan memiliki dampak positif. Saya selalu antusias dalam mempelajari 
teknologi baru dan memecahkan masalah yang kompleks.
""")

st.divider()

# --- MEMBUAT TAB INTERAKTIF ---
tab1, tab2, tab3, tab4 = st.tabs(["Latar Belakang", "Minat & Bakat", "Hasil Projek Web", "Hubungi Saya"])

# --- TAB 1: LATAR BELAKANG ---
with tab1:
    st.header("Latar Belakang")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎓 Pendidikan")
        st.write("**Universitas Negeri Surabaya (2026)**")
        st.write("S1 PENDIDIKAN TEKNOLOGI INFORMASI")
        st.write("Fokus pada pengembangan perangkat lunak dan arsitektur sistem berbasis web.")
        
    with col2:
        st.subheader("💼 Pengalaman Kerja")
        st.write("**Junior Web Developer di PT ABC (2024 - Sekarang)**")
        st.write("- Mengembangkan aplikasi web internal perusahaan.")
        st.write("- Mengoptimalkan database dan API.")
        
with tab2:
    st.header("Minat & Bakat")
    st.write("Berikut adalah area keahlian dan hal-hal yang saya minati:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("💻 **Pengembangan Web** \n\n Menguasai Python (Django/Flask/Streamlit), HTML, CSS, dan JavaScript.")
    with col2:
        st.success("📊 **Analisis Data** \n\n Tertarik mengubah data mentah menjadi wawasan bisnis menggunakan Pandas & SQL.")
    with col3:
        st.warning("🎨 **UI/UX Design** \n\n Senang merancang antarmuka pengguna yang bersih, minimalis, dan fungsional.")

# --- TAB 3: HASIL PROJEK WEB ---
with tab3:
    st.header("Portofolio Projek Web")
    st.write("Beberapa karya yang pernah saya buat:")
    
    # Projek 1
    with st.expander("🛒 1. Sistem E-Commerce Sederhana (Buka untuk detail)"):
        st.write("**Deskripsi:** Aplikasi toko online yang dilengkapi dengan fitur keranjang belanja dan integrasi payment gateway.")
        st.write("**Teknologi:** Python (Django), PostgreSQL, Bootstrap.")
        st.write("🔗 [Lihat Demo](#) | 🐙 [Source Code](#)")
        
    # Projek 2
    with st.expander("📈 2. Dashboard Analitik Penjualan (Buka untuk detail)"):
        st.write("**Deskripsi:** Dashboard interaktif untuk memonitor grafik penjualan secara real-time.")
        st.write("**Teknologi:** Python (Streamlit), Pandas, Plotly.")
        st.write("🔗 [Lihat Demo](#) | 🐙 [Source Code](#)")

    # Projek 3
    with st.expander("📝 3. Blog Pribadi & CMS (Buka untuk detail)"):
        st.write("**Deskripsi:** Sistem manajemen konten (CMS) ringan untuk menulis dan mempublikasikan artikel.")
        st.write("**Teknologi:** Flask, SQLite, Tailwind CSS.")
        st.write("🔗 [Lihat Demo](#) | 🐙 [Source Code](#)")

# --- TAB 4: HUBUNGI SAYA ---
with tab4:
    st.header("Mari Berkolaborasi!")
    st.write("Apakah Anda memiliki pertanyaan atau tawaran kerja sama? Silakan tinggalkan pesan di bawah ini.")
    
    # Form interaktif
    with st.form("contact_form"):
        nama = st.text_input("Nama Anda")
        email = st.text_input("Email Anda")
        pesan = st.text_area("Pesan Anda")
        submitted = st.form_submit_button("Kirim Pesan")
        
        if submitted:
            # Karena ini hanya frontend statis, kita tampilkan notifikasi sukses saja
            st.success(f"Terima kasih, {nama}! Pesan Anda telah berhasil dikirim.")