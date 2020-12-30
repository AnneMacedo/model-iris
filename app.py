import streamlit as st
import joblib as jb

def main():
    st.title("Estimador de especies")
    st.write("Escolha abaixo os valores da planta:")
    val1 = st.slider("sepal length (cm)", 1.0,10.0, value = 5.0)
    val2 = st.slider("sepal width (cm)", 1.0,10.0, value = 5.0)
    val3 = st.slider("petal length (cm)", 1.0,10.0, value = 5.0)
    val4 = st.slider("petal width (cm)", 1.0,10.0, value = 5.0)

    botao = st.button("Clique aqui para estimar")

    if botao == True:
        model = jb.load("modelo_iris.pkl")
        result = model.predict([[val1,val2,val3,val4]])[0]
        st.markdown(f"De acordo com os valores, o resultado é: **{result}** :hibiscus:")

if __name__ == "__main__":
    main()