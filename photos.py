import streamlit as st
import pandas as pd
from handle import run_query, execute_query

def handle_photos(mode):
    st.header("Photos - Modify/Delete")
    
    if mode != "Modify/Delete":
        st.error("Only Modify/Delete functionality is available for Photos.")
        return

    # Display current photos
    st.subheader("Current Photos")
    query = "SELECT * FROM photos;"
    photos_data = run_query(query)
    if photos_data:
        df = pd.DataFrame(photos_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No photos available.")
        return

    # Select a photo based on its id_photo
    selected_id = st.selectbox("Select Photo ID", df["id_photo"])

    # Create two tabs for Modify and Delete
    action_tabs = st.tabs(["Modify", "Delete"])

    with action_tabs[0]:
        # Modify tab
        row = df[df["id_photo"] == selected_id].iloc[0]
        st.write("Modifying photo for Common Name:", row["common_name"])
        new_url = st.text_input("New Photo URL", value=row["photo_url"])
        if st.button("Update Photo"):
            if new_url:
                update_query = "UPDATE photos SET photo_url = %s WHERE id_photo = %s;"
                execute_query(update_query, (new_url, selected_id))
                st.success("Photo updated successfully!")
            else:
                st.error("Please provide a valid Photo URL.")

    with action_tabs[1]:
        # Delete tab
        if st.button("Delete Photo"):
            delete_query = "DELETE FROM photos WHERE id_photo = %s;"
            execute_query(delete_query, (selected_id,))
            st.success("Photo deleted successfully!")
