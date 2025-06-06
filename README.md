CODIGO USADO NO APP.PY 
import pandas as pd
import streamlit as st
import altair as alt  


df = pd.read_csv("dataset.csv")


chart = alt.Chart(df).mark_bar().encode(
    x="Segment:N",
    y="count(Product):Q",
    color="Segment:N"
)


st.title("Distribuição de Produtos por Segmento")
st.altair_chart(chart, use_container_width=True)



PARA RODAR LOCALMENTE O ARQUIVO DO EC2:
- Salvar a chave .pem em uma pasta para poder acessar amaquina virtual ec2
- Em seguida, abrir localmente o powershell (dentro da pasta onde esta a chave .pem) para acessar a maquina
- Para acessar a maquina colocar o comando "ssh -i "key.streamlit.pem" ubuntu@ec2-52-91-199-9.compute-1.amazonaws.com" assim ja vamos ter acesso a maquina ubuntu
- Verificar se o python3 esta instalado, e em seguida instalar o streamlit caso ainda não tenha instalado com o codigo "pip install streamlit --break-system-packages"
- Depois criar o nano app.py e fazer o codigo de streamlit para axecutar o gráfico segundo o arquivo dataset csv disponibilizado pelo professor, e salvar
- Agora é só dar um comando "streamlit run app.py" e esperar executar para ver se não tem algum erro
