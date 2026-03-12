import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# --- ESTILO CUSTOMIZADO ---
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; }
    h1, h2, h3 {
        color: #D4AF37 !important; 
        text-align: center;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px #000000;
    }
    .mensagem-texto {
        color: #ffffff;
        font-family: 'Verdana', sans-serif;
        font-size: 18px;
        line-height: 1.8;
        text-align: center;
    }
    .assinatura {
        color: #D4AF37;
        font-weight: bold;
        font-size: 20px;
    }
    .stButton>button {
        background-color: #D4AF37;
        color: #001f3f;
        border-radius: 20px;
        border: none;
        font-weight: bold;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid #D4AF37;
        border-radius: 15px;
    }
    /* Estilo das fotos */
    .stImage > img {
        border: 3px solid #D4AF37;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }
    @keyframes hearts-fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); }
    }
    .heart {
        position: fixed;
        top: -10%;
        color: #D4AF37;
        font-size: 25px;
        user-select: none;
        z-index: 9999;
        animation: hearts-fall 5s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Inicial
st.title("💖 Uma surpresa para João Pedro")

# Lógica do Botão
if 'comecar' not in st.session_state:
    st.session_state.comecar = False

if not st.session_state.comecar:
    st.write(" ")
    col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
    with col_btn2:
        if st.button("🎁 ABRA O SEU PRESENTE"):
            st.session_state.comecar = True
            st.rerun()

if st.session_state.comecar:
    # Efeito de carregamento
    with st.status("Inicializando protocolos românticos...", expanded=True) as status:
        st.write("Conectando ao coração... ❤️")
        time.sleep(1.2)
        st.write("Carregando 1000% de saudades... ✨")
        time.sleep(1.2)
        status.update(label="Sincronização completa!", state="complete", expanded=False)

    st.balloons() 
    st.header("✨ Feliz Aniversário, Meu Amor! ✨")

    # Chuva de Corações
    st.markdown("""
        <div class="heart" style="left:5%; animation-delay:0s">❤️</div>
        <div class="heart" style="left:15%; animation-delay:2s">✨</div>
        <div class="heart" style="left:25%; animation-delay:1s">💛</div>
        <div class="heart" style="left:40%; animation-delay:4s">❤️</div>
        <div class="heart" style="left:55%; animation-delay:0.5s">✨</div>
        <div class="heart" style="left:70%; animation-delay:3s">💛</div>
        <div class="heart" style="left:85%; animation-delay:1.5s">✨</div>
        <div class="heart" style="left:95%; animation-delay:2.5s">❤️</div>
        """, unsafe_allow_html=True)

    # Imagens em uma única linha (3 colunas)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('1.jpeg', use_container_width=True)
    with col2:
        st.image('2.jpeg', use_container_width=True)
    with col3:
        st.image('3.jpeg', use_container_width=True)

    # Texto Emocionante
    st.write(" ")
    container = st.container(border=True)
    with container:
        st.markdown(f"""
        <div class="mensagem-texto">
        🎂 Feliz Aniversário, meu príncipe lindo!
                    
        Oi, meu amor! Vim aqui hoje, nesse dia tão especial, para te desejar toda a felicidade do mundo.

        Infelizmente não posso estar aí fisicamente com você, mas saiba que meu coração está aí, batendo pertinho do seu. Tentei fazer uma gracinha na linguagem que você mais utiliza para celebrar o seu dia

        Amor, hoje o dia é seu, mas o presente quem ganhou fui eu por ter você na minha vida. Você é uma pessoa incrível: carinhoso, inteligente, engraçado e o motivo de eu ser a pessoa mais feliz desse mundo.

        Desejo que seu dia seja maravilhoso, assim como você.

        Com todo o meu amor,

        Sua namorada que te ama demais! ❤️</span>
        </div>
        """, unsafe_allow_html=True)

    # Coração Pulsante Dourado
    st.markdown("<h1 style='font-size: 100px;'>💛</h1>", unsafe_allow_html=True)
    st.caption("Feito com ❤️ por quem te ama muito.")