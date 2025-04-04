import streamlit as st
from sidebar import sidebar_menu

selected_page = sidebar_menu()

if selected_page == "Data Entry":
    import table
    table.data_entry_page()
elif selected_page == "Search":
    import search
    search.search_page()
elif selected_page == "Images":
    # Display a clickable link that opens the GitHub images page in a new tab.
    st.markdown(
        '<h1 style="text-align:center;">Images</h1>'
        '<p style="text-align:center;">Click the link below to visit the images repository:</p>'
        '<div style="text-align:center;"><a href="https://github.com/AIforimpact22/photos/tree/main/images" target="_blank" style="font-size:20px; color:#007bff;">'
        'Open Images on GitHub</a></div>',
        unsafe_allow_html=True
    )
