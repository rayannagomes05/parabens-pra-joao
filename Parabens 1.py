import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# Estilo customizado para as cores
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stText, .stMarkdown { color: #ff4b4b; font-family: 'Courier New', Courier, monospace; }
    h1 { color: #ff4b4b; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Título Inicial
st.title("💖 Uma surpresa para João Pedro")

# Botão para iniciar a experiência
if 'comecar' not in st.session_state:
    st.session_state.comecar = False

if not st.session_state.comecar:
    if st.button("Clique aqui para iniciar o sistema de amor"):
        st.session_state.comecar = True
        st.rerun()

if st.session_state.comecar:
    # Efeito de carregamento
    with st.status("Inicializando protocolos românticos...", expanded=True) as status:
        st.write("Conectando ao coração... ❤️")
        time.sleep(1.5)
        st.write("Carregando memórias felizes... ✨")
        time.sleep(1.5)
        st.write("Verificando nível de saudade... 1000%")
        time.sleep(1)
        status.update(label="Sistema Pronto!", state="complete", expanded=False)

    # Grande Título
    st.balloons() # Chuva de balões na tela!
    st.header("✨ Feliz Aniversário, João Pedro! ✨")

    # Texto Emocionante
    container = st.container(border=True)
    with container:
        texto = """
        Oi, meu amor...
        
        Hoje o calendário marca uma data especial, mas o meu coração celebra você todos os dias. 
        Você é o meu 'commit' favorito, a lógica que faz minha vida ter sentido e a luz que ilumina meus dias.
        
        Que o seu novo ciclo seja repleto de sonhos realizados, de sorrisos bobos e de nós dois, sempre juntos.
        
        Eu amo você, além de qualquer linha de código. ❤️
        """
        st.write(texto)

    # Coração Pulsante (Emoji Grande)
    st.markdown("<h1 style='font-size: 100px;'>❤️</h1>", unsafe_allow_html=True)
    
    st.snow() # Efeito visual de brilhos
    st.caption("Feito com ❤️ por quem te ama muito.")