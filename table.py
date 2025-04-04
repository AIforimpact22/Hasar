import streamlit as st
import nurseries
import trees
import inventory
import payment  # New module for payments
import photos   # New module for photos

def data_entry_page():
    st.title("Data Entry")
    table_option = st.selectbox("Select Table", ["Nurseries", "Trees", "Nursery_Tree_Inventory", "Payments", "Photos"])
    
    # For Payments and Photos, only Modify/Delete is available
    if table_option == "Payments":
        st.info("Payments supports only Modify/Delete functionality.")
        payment.handle_payments("Modify/Delete")
    elif table_option == "Photos":
        st.info("Photos supports only Modify/Delete functionality.")
        photos.handle_photos("Modify/Delete")
    else:
        entry_type = st.radio("Select Entry Type", ["Single Entry", "Bulk Entry", "Modify/Delete"])
        if table_option == "Nurseries":
            nurseries.handle_nurseries(entry_type)
        elif table_option == "Trees":
            trees.handle_trees(entry_type)
        elif table_option == "Nursery_Tree_Inventory":
            inventory.handle_inventory(entry_type)
