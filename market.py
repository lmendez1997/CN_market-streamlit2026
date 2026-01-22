import streamlit as st
import pandas as pd

def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto):
    subtotal=float(precio_producto) * float(cantidad_producto)
    nueva_fila = {
        "Producto": nombre_producto,
        "Precio": precio_producto,
        "Cantidad": cantidad_producto,
        "Subtotal": subtotal}
    
    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, 
         pd.DataFrame([nueva_fila])],
        ignore_index=True

    )

if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["Producto", "Precio", "Cantidad", "Subtotal"]
    )

st.title("Mercado de Productos")

with st.form("product_form"):
    producto_nombre = st.text_input("Nombre del Producto")
    producto_precio = st.number_input("Precio del Producto", min_value=0.0, format="%.2f")
    producto_cantidad = st.number_input("Cantidad del Producto", min_value=1, step=1)
    
    subtotal_button = st.form_submit_button("Comprar Producto")

if subtotal_button:
    calcular_subtotal(producto_nombre, producto_precio, producto_cantidad)

st.dataframe(st.session_state.table_data)

if st.button("Calcular Total General"):
    total=(st.session_state.table_data["Precio"]*st.session_state.table_data["Cantidad"]).sum()

    st.subheader(f"Total General: ${total:.2f}")
    st.write("Precio total es: "+str(total))
    

