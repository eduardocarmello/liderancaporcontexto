import streamlit as st

# ============================================================
# CONFIGURAÇÃO — troque o link do curso aqui quando tiver o definitivo
# ============================================================
COURSE_LINK = "COLOQUE_AQUI_O_LINK_DO_CURSO"

st.set_page_config(page_title="Liderança por Contexto", page_icon="🧭", layout="centered")

# ============================================================
# ESTILO
# As cores de fundo/texto/destaque vêm do .streamlit/config.toml
# (é o jeito confiável de themar os componentes nativos do Streamlit).
# Aqui só refinamos tipografia e alguns detalhes visuais.
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Work+Sans:wght@400;500;600&display=swap');

    .block-container{
        max-width: 640px;
        border-top: 4px solid #B9893C;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }
    .brand{
        font-family: 'Work Sans', sans-serif;
        font-size: 13px;
        color: #7E9AA0;
        margin-bottom: 2px;
    }
    h1.title{
        font-family: 'Fraunces', serif;
        font-size: 32px;
        line-height: 1.15;
        margin: 0 0 14px 0;
        color: #1B1A15;
    }
    p.lede{
        font-family: 'Work Sans', sans-serif;
        font-size: 16px;
        line-height: 1.55;
        color: #3A382F;
        max-width: 52ch;
    }
    p.context-label{
        font-family: 'Work Sans', sans-serif;
        font-size: 12px;
        color: #7E9AA0;
        margin-bottom: 4px;
    }
    div.context-box{
        border-left: 3px solid #B9893C;
        padding: 4px 0 4px 16px;
        margin-bottom: 18px;
    }
    div.context-box p{
        font-family: 'Work Sans', sans-serif;
        margin: 0;
        font-size: 16px;
        line-height: 1.55;
        color: #2A2921;
    }
    .progress-label{
        font-family: 'Work Sans', sans-serif;
        font-size: 12px;
        color: #7E9AA0;
        margin-bottom: 10px;
    }
    .score-number{
        font-family: 'Fraunces', serif;
        font-size: 60px;
        font-weight: 700;
        color: #1B1A15;
        line-height: 1;
    }
    .score-max{
        font-family: 'Work Sans', sans-serif;
        font-size: 16px;
        color: #7E9AA0;
    }
    .band-label{
        font-family: 'Fraunces', serif;
        font-size: 20px;
        font-weight: 700;
        color: #1B1A15;
        margin: 12px 0 8px 0;
    }
    .band-text{
        font-family: 'Work Sans', sans-serif;
        font-size: 15px;
        line-height: 1.6;
        color: #3A382F;
        margin-bottom: 18px;
    }
    .cta-note{
        font-family: 'Work Sans', sans-serif;
        font-size: 13px;
        color: #7E9AA0;
        margin-top: 8px;
    }
    a.course-btn{
        display: inline-block;
        background: #1B1A15;
        color: #EFE7D8 !important;
        padding: 12px 24px;
        text-decoration: none;
        font-family: 'Work Sans', sans-serif;
        font-weight: 600;
        font-size: 15px;
    }
    a.course-btn:hover{
        background: #1E3B44;
    }

    /* opções do quiz — usa os elementos reais do Streamlit, sem depender de wrapper */
    div[data-testid="stRadio"] label{
        border: 1px solid #C9BC9C;
        border-left: 3px solid #C9BC9C;
        padding: 10px 14px;
        width: 100%;
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# CONTEÚDO DO QUIZ
# Cada pergunta tem 4 alternativas; a de weight=2 é a mais adequada ao contexto.
# ============================================================
QUESTIONS = [
    {
        "context": "Uma pessoa acabou de entrar no time e nunca executou esta tarefa antes. Está motivada, mas insegura sobre como fazer certo.",
        "options": [
            {"text": "Explico o passo a passo com clareza, defino prazos curtos e acompanho de perto cada etapa.", "weight": 2},
            {"text": "Explico a tarefa e já abro espaço para ela trazer ideias sobre como executar.", "weight": 1},
            {"text": "Combino apenas os pontos principais e deixo que decida como conduzir.", "weight": 1},
            {"text": "Delego a tarefa por completo e cobro apenas o resultado final.", "weight": 1},
        ],
    },
    {
        "context": "Já na segunda semana, essa pessoa entende o básico da tarefa, mas ainda erra detalhes e hesita antes de agir sozinha.",
        "options": [
            {"text": "Assumo o controle total de novo, como se fosse o primeiro dia.", "weight": 1},
            {"text": "Continuo explicando o porquê de cada decisão, mas já pergunto o que ela faria antes de dar a resposta.", "weight": 2},
            {"text": "Deixo que decida sozinha e só reviso o resultado final.", "weight": 1},
            {"text": "Delego a próxima entrega inteira, sem checkpoints.", "weight": 1},
        ],
    },
    {
        "context": "Um colaborador domina tecnicamente a função, mas voltou desanimado depois de um feedback duro recebido de outro gestor.",
        "options": [
            {"text": "Volto a dar instruções detalhadas, como se ele precisasse reaprender o trabalho.", "weight": 1},
            {"text": "Explico de novo os processos técnicos, mesmo sabendo que ele já os domina.", "weight": 1},
            {"text": "Escuto o que está pesando, reconheço a competência dele e decidimos juntos os próximos passos.", "weight": 2},
            {"text": "Deixo totalmente por conta dele, sem abrir espaço para conversar sobre o momento.", "weight": 1},
        ],
    },
    {
        "context": "Uma pessoa da equipe entrega com consistência há meses, antecipa problemas e raramente precisa de ajuda.",
        "options": [
            {"text": "Mantenho reuniões diárias de acompanhamento detalhado, como faço com quem está começando.", "weight": 1},
            {"text": "Sigo negociando cada decisão em conjunto antes de ela agir.", "weight": 1},
            {"text": "Ofereço apoio emocional frequente, mesmo sem sinal de que ela precise disso agora.", "weight": 1},
            {"text": "Defino o resultado esperado e dou autonomia total sobre como chegar lá.", "weight": 2},
        ],
    },
    {
        "context": "Um prazo crítico surgiu de última hora e um erro pode gerar prejuízo real, mesmo a equipe sendo experiente.",
        "options": [
            {"text": "Aproveito para desenvolver autonomia e deixo o time definir sozinho como agir.", "weight": 1},
            {"text": "Abro uma longa negociação sobre como cada um prefere conduzir sua parte.", "weight": 1},
            {"text": "Assumo o comando direto da situação, dou instruções claras e defino prioridades imediatas.", "weight": 2},
            {"text": "Ofereço apoio emocional ao grupo, mas não entro nos detalhes operacionais.", "weight": 1},
        ],
    },
    {
        "context": "A empresa mudou um processo importante. A equipe é experiente, mas está insegura e ansiosa com o novo modelo de trabalho.",
        "options": [
            {"text": "Dou instruções rígidas sobre o novo processo, sem abrir espaço para dúvidas ou opiniões.", "weight": 1},
            {"text": "Reconheço a experiência do time, escuto as inseguranças e construímos juntos a adaptação ao novo processo.", "weight": 2},
            {"text": "Delego a adaptação inteira ao time, sem me envolver no processo de mudança.", "weight": 1},
            {"text": "Trato a situação como se ninguém tivesse experiência prévia nenhuma.", "weight": 1},
        ],
    },
]

TOTAL = len(QUESTIONS)

# ============================================================
# ESTADO
# ============================================================
if "step" not in st.session_state:
    st.session_state.step = 0  # 0 = intro | 1..TOTAL = perguntas | TOTAL+1 = resultado
if "answers" not in st.session_state:
    st.session_state.answers = [None] * TOTAL


def go_next():
    st.session_state.step += 1


def go_back():
    st.session_state.step -= 1


def restart():
    st.session_state.step = 0
    st.session_state.answers = [None] * TOTAL


def compute_score():
    raw = sum(QUESTIONS[i]["options"][st.session_state.answers[i]]["weight"] for i in range(TOTAL))
    min_raw, max_raw = TOTAL * 1, TOTAL * 2
    return round(1 + (raw - min_raw) * (29 / (max_raw - min_raw)))


# ============================================================
# TELA: INTRODUÇÃO
# ============================================================
if st.session_state.step == 0:
    st.markdown('<p class="brand">Avaliação de estilo de liderança</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="title">Liderança por Contexto</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="lede">Nenhum estilo de liderança funciona igual em toda situação. '
        'Ao longo de 6 cenários, escolha a atitude que você tomaria — e veja o quanto '
        'sua leitura de contexto está afiada.</p>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.button("Começar avaliação", on_click=go_next)

# ============================================================
# TELAS: PERGUNTAS
# ============================================================
elif 1 <= st.session_state.step <= TOTAL:
    idx = st.session_state.step - 1
    q = QUESTIONS[idx]
    options_texts = [o["text"] for o in q["options"]]

    st.markdown(
        f'<p class="progress-label">Pergunta {idx + 1} de {TOTAL}</p>',
        unsafe_allow_html=True,
    )
    st.markdown('<p class="context-label">Situação</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="context-box"><p>{q["context"]}</p></div>', unsafe_allow_html=True)

    current_index = st.session_state.answers[idx]
    choice = st.radio(
        "opções",
        options_texts,
        index=current_index,
        key=f"radio_{idx}",
        label_visibility="collapsed",
    )
    if choice is not None:
        st.session_state.answers[idx] = options_texts.index(choice)

    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        if idx > 0:
            st.button("Voltar", on_click=go_back)
    with col2:
        label = "Ver resultado" if idx == TOTAL - 1 else "Próxima"
        st.button(label, on_click=go_next, disabled=st.session_state.answers[idx] is None)

# ============================================================
# TELA: RESULTADO
# ============================================================
else:
    score = compute_score()

    st.markdown('<p class="brand">Resultado</p>', unsafe_allow_html=True)
    st.markdown(
        f'<span class="score-number">{score}</span> <span class="score-max">/ 30</span>',
        unsafe_allow_html=True,
    )
    st.progress(score / 30)

    if score <= 10:
        band = "Leitura de contexto em construção"
        text = (
            "Você ainda tende a repetir um mesmo estilo de liderança independente da "
            "situação. Entender quando ser mais diretivo, mais apoiador ou mais delegador "
            "é justamente o que separa quem lidera pessoas de quem só lidera tarefas."
        )
    elif score <= 20:
        band = "Leitura de contexto em desenvolvimento"
        text = (
            "Você já percebe que o contexto importa e acerta em parte das situações, mas "
            "ainda hesita em alguns cenários — principalmente quando maturidade técnica e "
            "momento emocional da pessoa não caminham juntos."
        )
    else:
        band = "Leitura de contexto consistente"
        text = (
            "Você lê bem o momento de cada pessoa e ajusta seu estilo de acordo com a "
            "situação, não com o piloto automático. Aprofundar essa habilidade é o que vai "
            "te diferenciar em cenários mais complexos de liderança."
        )

    st.markdown(f'<p class="band-label">{band}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="band-text">{text}</p>', unsafe_allow_html=True)

    st.markdown(
        f'<a class="course-btn" href="{COURSE_LINK}" target="_blank" rel="noopener">'
        f'Quero me inscrever no curso</a>',
        unsafe_allow_html=True,
    )
    st.markdown('<p class="cta-note">Link de inscrição a definir.</p>', unsafe_allow_html=True)

    st.write("")
    st.button("Refazer avaliação", on_click=restart)
