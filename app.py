
import streamlit as st 
from scraper import get_rss_headlines

page = st.sidebar.radio(
    "Pages",
    ["Application", "Project Source Code"],index = 0
)
if page == 'Application':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('https://images.seeklogo.com/logo-png/29/2/galatasaray-universitesi-logo-png_seeklogo-298733.png',width = 200)

    st.title("News Headline Scraper Application")
    st.subheader("Data Science Master's Assignment" )
    st.text("This project was developed as an assignment for the Galatasaray University Master's Program in Data Science. The application  collects and aggregates news headlines from various online news websites.")
    st.sidebar.markdown("---")


        
    st.sidebar.markdown("### Author")
    st.sidebar.write("Ferhat Metin")

    st.sidebar.markdown(
        "[GitHub](https://github.com/ferhatmetin34)"
    )

    st.sidebar.markdown(
        "[Kaggle](https://kaggle.com/ferhatmetin34)"
    )

    st.sidebar.markdown(
        "[LinkedIn](https://linkedin.com/in/ferhatmetin)"
    )


    NEWS_SOURCES = {

        "BBC Türkçe": "https://feeds.bbci.co.uk/turkce/rss.xml",
        'BBC News English': "https://feeds.bbci.co.uk/news/rss.xml",
        "Cumhuriyet": "https://www.cumhuriyet.com.tr/rss",
        "Hürriyet": "https://www.hurriyet.com.tr/rss/anasayfa",
        "Habertürk": "https://www.haberturk.com/rss",
        "Sabah": "https://www.sabah.com.tr/rss/anasayfa.xml",
        "Yeni Çağ": "https://www.yenicaggazetesi.com.tr/rss.xml"
        
    }

    source = st.selectbox("Select News Source", list(NEWS_SOURCES.keys()))

    if st.button("Get News", type="primary"):

        rss_url = NEWS_SOURCES[source]
        headlines = get_rss_headlines(rss_url)

        st.subheader(source)

        for news in headlines:
            st.markdown("## " + news["title"])
            st.caption(news["date"])
            st.link_button("Read Article", news["link"])
            st.markdown("---")
            
if page == 'Project Source Code':
    st.title("Project Source Code")

    st.markdown("Below you can find the full source code of the project.")

    tab1, tab2 = st.tabs(["app.py", "scraper.py"])

    with tab1:
        with open("app.py", "r", encoding="utf-8") as f:
            st.code(f.read(), language="python")

    with tab2:
        with open("scraper.py", "r", encoding="utf-8") as f:
            st.code(f.read(), language="python")
            
    st.sidebar.markdown("### Author")
    st.sidebar.write("Ferhat Metin")

    st.sidebar.markdown(
        "[GitHub](https://github.com/ferhatmetin34)"
    )

    st.sidebar.markdown(
        "[Kaggle](https://kaggle.com/ferhatmetin34)"
    )

    st.sidebar.markdown(
        "[LinkedIn](https://linkedin.com/in/ferhatmetin)"
    )
