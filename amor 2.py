import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# Estilo customizado para as cores
st.markdown("""
    <style>
    .main { background-color: #1a237e; }
    .stText, .stMarkdown { color: #ffffff; font-family: 'Courier New', Courier, monospace; }
    h1 { color: #ffffff; text-align: center; }
    /* Estilo para o texto da mensagem ficar branco e legível */
    .mensagem-texto {
        color: white;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        line-height: 1.6;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Inicial
st.title("💖 Uma surpresa para João Pedro")

# Botão para iniciar a experiência
if 'comecar' not in st.session_state:
    st.session_state.comecar = False

if not st.session_state.comecar:
    st.write(" ")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎁 ABRA O SEU PRESENTE"):
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
        status.update(label="Sincronização completa!", state="complete", expanded=False)

    # Grande Título e Balões
    st.balloons() 
    st.header("✨ Feliz Aniversário, Meu Amor! ✨")

    # Texto Emocionante
    container = st.container(border=True)
    with container:
        st.markdown(f"""
        <div class="mensagem-texto">
        Oi meu príncipe lindo, vim hoje nesse dia especial te desejar um feliz aniversário!<br><br>
        Infelizmente não posso estar aí com você, mas saiba que meu coração está aí, e que eu te amo muito muito muito. 
        Tentei fazer uma gracinha na programação pra te desejar um feliz aniversário na linguagem que você mais utiliza.<br><br>
        Amor, hoje é seu dia, mas o presente quem ganhou fui eu, por ter você na minha vida. Uma pessoa incrível, carinhosa, 
        inteligente, engraçada e que me faz a pessoa mais feliz desse mundo. Eu te amo com todas as minhas forças, e te desejo um dia maravilhoso.<br><br>
        <b>Com amor, sua namorada que te ama muito.</b>
        </div>
        """, unsafe_allow_html=True)

    # Coração Pulsante (Emoji Grande)
    st.markdown("<h1 style='font-size: 100px;'>❤️</h1>", unsafe_allow_html=True)
    
    # --- EFEITO DE CORAÇÕES CAINDO ---
    st.markdown("""
        <style>
        @keyframes hearts-fall {
            0% { top: -10%; transform: translateX(0) rotate(0deg); }
            100% { top: 100%; transform: translateX(100px) rotate(360deg); }
        }
        .heart {
            position: fixed;
            top: -10%;
            color: #ff4b4b;
            font-size: 25px;
            user-select: none;
            z-index: 9999;
            animation: hearts-fall 5s linear infinite;
        }
        </style>
        <div class="heart" style="left:5%; animation-delay:0s">❤️</div>
        <div class="heart" style="left:15%; animation-delay:2s">💖</div>
        <div class="heart" style="left:25%; animation-delay:1s">💗</div>
        <div class="heart" style="left:40%; animation-delay:4s">❤️</div>
        <div class="heart" style="left:55%; animation-delay:0.5s">💕</div>
        <div class="heart" style="left:70%; animation-delay:3s">❤️</div>
        <div class="heart" style="left:85%; animation-delay:1.5s">💘</div>
        <div class="heart" style="left:95%; animation-delay:2.5s">❤️</div>
        """, unsafe_allow_html=True)

    st.caption("Feito com ❤️ por quem te ama muito.")