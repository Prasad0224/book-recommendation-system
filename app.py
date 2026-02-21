import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="📚 Book Recommendation System",
    layout="wide"
)

st.title("📚 Book Recommendation System")
st.markdown("**Streamlit Frontend | FastAPI Backend | Confidence-Aware Recs**")

with st.spinner("Connecting to backend..."):
    try:
        health = requests.get(f"{API_BASE_URL}/health", timeout=3).json()
        if health["status"] == "OK":
            st.success("✅ Backend connected")
        else:
            st.warning("⚠️ Backend unhealthy")
    except Exception:
        st.error("❌ Cannot connect to backend")
        st.stop()

st.sidebar.header("⚙️ Controls")

rec_type = st.sidebar.radio(
    "Recommendation Type",
    ["Popular Books", "Similar Books"]
)

top_n = st.sidebar.slider(
    "Number of recommendations",
    5, 20, 10, 5
)

@st.cache_data
def fetch_books():
    res = requests.get(f"{API_BASE_URL}/books")
    res.raise_for_status()
    return res.json()["books"]

if rec_type == "Popular Books":
    st.subheader("🔥 Popular Books")

    if st.button("📈 Get Popular Books"):
        with st.spinner("Fetching popular books..."):
            res = requests.post(
                f"{API_BASE_URL}/popular",
                json={"top_n": top_n}
            )

        if res.status_code == 200:
            data = res.json()
            df = pd.DataFrame(data["books"])
            st.success(f"Top {data['count']} popular books")
            st.dataframe(df, width="stretch")
            
        else:
            st.error("Failed to fetch popular books")

else:
    st.subheader("🤝 Similar Books")

    try:
        books = fetch_books()
    except Exception:
        st.error("Failed to load book list")
        st.stop()

    selected_book = st.selectbox(
        "Select a book you like:",
        options=books,
        index=None,
        placeholder="Choose a book"
    )

    if selected_book and st.button("🔍 Recommend"):
        with st.spinner("Finding similar books..."):
            res = requests.post(
                f"{API_BASE_URL}/similar",
                json={
                    "book_name": selected_book,
                    "top_n": top_n
                }
            )

        if res.status_code == 200:
            data = res.json()
            df = pd.DataFrame(data["recommendations"])

            df = df.sort_values("confidence", ascending=False)

            st.success(f"Books similar to **{data['input_book']}**")

            st.dataframe(
                df.rename(columns={
                    "book_name": "Recommended Book",
                    "confidence": "Confidence (%)"
                }),
                width="stretch"
            )
        elif res.status_code == 404:
            st.error("Book not found")
        else:
            st.error("Recommendation failed")
