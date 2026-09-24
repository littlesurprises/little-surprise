import streamlit as st
import streamlit.components.v1 as components


# ============================================================
#                    ✏️ CUSTOMIZE HERE
# ============================================================

NAME = "Aaaru"

QUESTION = f"{NAME}, will you accept this little surprise? 🙈"
YES_TEXT = "YES ❤️"
NO_TEXT = "NO 🙈"

WISH_TITLE = "Close your eyes..."
WISH_SUBTITLE = "Make a wish ✨"
BLOW_BUTTON = "Blow the candle 🕯️"
COUNTDOWN_MESSAGE = "Make your wish..."
CONTINUE_TEXT = "Continue →"

ENVELOPE_TITLE = "Something is waiting for you..."
ENVELOPE_SUBTITLE = "Open it when you're ready ✨"
OPEN_BUTTON = "Open it 💌"

LETTER_TITLE = f"Dear {NAME},"

LETTER_PARAGRAPHS = [
    "I just wanted to make something a little special for you.",
    "Sometimes the smallest things can carry the biggest smiles, and I hope this little surprise does exactly that.",
    "And once again, happy birthday sugar candy. You are so sweet.",
    "I hope this year brings you plenty of reasons to smile, laugh, dream, and enjoy every little moment.",

]

LETTER_SIGNATURE = "With lots of good wishes ✨"

FINAL_TITLE = "Lots of love for you ❤️"

FINAL_MESSAGE = (
    "Keep smiling, keep being you, and have the most wonderful day. "
    "I hope there are many more beautiful moments waiting for you ahead. ✨"
)

FINAL_BUTTON = "One more thing ✨"

FLOATING_EMOJI = "🙈"


# ============================================================
#                    STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="A Little Surprise",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
#       IMPORTANT: STREAMLIT OUTER PAGE RESET
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       KILL STREAMLIT'S NORMAL PAGE SPACING
       ======================================================== */

    html,
    body {
        margin: 0 !important;
        padding: 0 !important;

        width: 100% !important;
        height: 100% !important;

        overflow: hidden !important;
    }

    #root {
        width: 100% !important;
        height: 100% !important;
    }

    .stApp {
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }

    [data-testid="stAppViewContainer"] {
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }

    [data-testid="stAppViewContainer"] > .main {
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }

    [data-testid="stMain"] {
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }

    [data-testid="stMainBlockContainer"] {
        width: 100% !important;
        max-width: none !important;

        height: 100% !important;
        min-height: 0 !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }

    [data-testid="stAppViewBlockContainer"] {
        width: 100% !important;
        max-width: none !important;

        height: 100% !important;
        min-height: 0 !important;

        margin: 0 !important;
        padding: 0 !important;

        overflow: hidden !important;
    }


    /* ========================================================
       HIDE STREAMLIT UI
       ======================================================== */

    header {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    [data-testid="stHeader"] {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    #MainMenu {
        display: none !important;
    }


    /* ========================================================
       THE STREAMLIT COMPONENT / IFRAME

       IMPORTANT:
       We intentionally use a normal component height in Python
       so the iframe actually renders.

       CSS then takes that iframe OUT of normal document flow
       and makes it occupy the real browser viewport.
       ======================================================== */

    iframe {
        position: fixed !important;

        top: 0 !important;
        left: 0 !important;

        width: 100vw !important;

        height: 100vh !important;
        height: 100dvh !important;

        min-width: 100vw !important;

        min-height: 100vh !important;
        min-height: 100dvh !important;

        max-width: 100vw !important;

        max-height: 100vh !important;
        max-height: 100dvh !important;

        margin: 0 !important;
        padding: 0 !important;

        border: none !important;
        outline: none !important;

        display: block !important;

        overflow: hidden !important;

        z-index: 999999 !important;
    }


    /* Remove spacing from the element that Streamlit
       puts around the component. */

    [data-testid="stElementContainer"] {
        margin: 0 !important;
        padding: 0 !important;
    }


    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
#                    LETTER HTML
# ============================================================

paragraphs_html = ""

for paragraph in LETTER_PARAGRAPHS:
    paragraphs_html += f"<p>{paragraph}</p>"


# ============================================================
#                    COMPLETE WEBSITE
# ============================================================

html = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width,
             initial-scale=1.0,
             maximum-scale=1.0,
             user-scalable=no,
             viewport-fit=cover"
>

<title>A Little surprise</title>


<link rel="preconnect" href="https://fonts.googleapis.com">

<link
    href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Pacifico&display=swap"
    rel="stylesheet"
>


<style>

/* ============================================================
   GLOBAL
   ============================================================ */

* {{
    box-sizing: border-box;

    -webkit-tap-highlight-color: transparent;
}}

html,
body {{
    margin: 0 !important;
    padding: 0 !important;

    width: 100% !important;
    height: 100% !important;

    overflow: hidden !important;

    background: #fff7fb;

    overscroll-behavior: none;
}}

body {{
    font-family: "DM Sans", sans-serif;

    -webkit-font-smoothing: antialiased;
}}


/* ============================================================
   FULLSCREEN SCENE
   ============================================================ */

.scene {{
    position: fixed;

    top: 0;
    left: 0;

    width: 100vw;

    height: 100vh;
    height: 100dvh;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(255, 192, 217, 0.35),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 80%,
            rgba(255, 220, 232, 0.4),
            transparent 32%
        ),

        linear-gradient(
            135deg,
            #fff9fb 0%,
            #fff2f7 50%,
            #fff9fb 100%
        );

    isolation: isolate;
}}


/* ============================================================
   BACKGROUND GLOW
   ============================================================ */

.scene::before {{
    content: "";

    position: absolute;

    width: 500px;
    height: 500px;

    border-radius: 50%;

    background:
        rgba(255, 171, 204, 0.12);

    filter: blur(80px);

    top: -250px;
    left: -180px;

    pointer-events: none;
}}


.scene::after {{
    content: "";

    position: absolute;

    width: 500px;
    height: 500px;

    border-radius: 50%;

    background:
        rgba(255, 204, 224, 0.15);

    filter: blur(90px);

    right: -220px;
    bottom: -250px;

    pointer-events: none;
}}


/* ============================================================
   FLOATING EMOJIS
   ============================================================ */

.floating-layer {{
    position: absolute;

    inset: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    pointer-events: none;

    z-index: 2;
}}


.floating-emoji {{
    position: absolute;

    display: block;

    pointer-events: none;
    user-select: none;

    will-change: transform;

    animation:
        floatAround
        var(--duration)
        ease-in-out
        var(--delay)
        infinite
        alternate;
}}


@keyframes floatAround {{

    0% {{
        transform:
            translate(
                var(--x1),
                var(--y1)
            )
            rotate(var(--r1));
    }}

    50% {{
        transform:
            translate(
                var(--x2),
                var(--y2)
            )
            rotate(var(--r2));
    }}

    100% {{
        transform:
            translate(
                var(--x3),
                var(--y3)
            )
            rotate(var(--r3));
    }}

}}


/* ============================================================
   PAGE SYSTEM
   ============================================================ */

.page {{
    position: absolute;

    inset: 0;

    width: 100%;
    height: 100%;

    padding:
        max(18px, env(safe-area-inset-top))
        max(18px, env(safe-area-inset-right))
        max(18px, env(safe-area-inset-bottom))
        max(18px, env(safe-area-inset-left));

    display: flex;

    align-items: center;
    justify-content: center;

    overflow: hidden;

    opacity: 0;

    visibility: hidden;

    pointer-events: none;

    transform: scale(0.97);

    transition:
        opacity 0.7s ease,
        transform 0.7s ease,
        visibility 0.7s ease;

    z-index: 5;
}}


.page.active {{
    opacity: 1;

    visibility: visible;

    pointer-events: auto;

    transform: scale(1);

    z-index: 10;
}}


/* ============================================================
   COMMON CONTENT
   ============================================================ */

.content {{
    position: relative;

    z-index: 20;

    width: min(92vw, 680px);

    max-height: 94vh;
    max-height: 94dvh;

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;
}}


.eyebrow {{
    margin-bottom: 10px;

    color: #c487a0;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.2em;

    text-transform: uppercase;
}}


.title {{
    margin: 0 0 12px;

    color: #8d526c;

    font-family: "Pacifico", cursive;

    font-size: clamp(34px, 6vw, 58px);

    font-weight: 400;

    line-height: 1.15;
}}


.subtitle {{
    margin: 0 0 25px;

    color: #8d7781;

    font-size: clamp(15px, 2vw, 18px);

    line-height: 1.6;
}}


/* ============================================================
   BUTTONS
   ============================================================ */

.btn {{
    border: none;

    outline: none;

    border-radius: 999px;

    padding: 13px 25px;

    font-family: "DM Sans", sans-serif;

    font-size: 15px;

    font-weight: 700;

    cursor: pointer;

    user-select: none;

    touch-action: manipulation;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        opacity 0.25s ease;
}}


.btn:active {{
    transform: scale(0.95);
}}


.primary-btn {{
    color: white;

    background:
        linear-gradient(
            135deg,
            #d97c9f,
            #c65f88
        );

    box-shadow:
        0 12px 28px
        rgba(191, 89, 130, 0.25);
}}


.primary-btn:hover {{
    transform: translateY(-2px);

    box-shadow:
        0 16px 34px
        rgba(191, 89, 130, 0.3);
}}


.soft-btn {{
    color: #9d5877;

    background:
        rgba(255,255,255,0.85);

    border:
        1px solid
        rgba(218,143,173,0.25);

    box-shadow:
        0 10px 25px
        rgba(160,90,120,0.1);
}}


/* ============================================================
   PAGE 1 - BEAR
   ============================================================ */

.bear-area {{
    position: relative;

    width: 190px;
    height: 170px;

    margin-bottom: 10px;
}}


.bear {{
    position: absolute;

    width: 125px;
    height: 105px;

    top: 50%;
    left: 50%;

    transform:
        translate(-50%, -40%);

    background: #b98262;

    border-radius:
        55px 55px 48px 48px;

    box-shadow:
        inset 0 -7px 0
        rgba(117,69,46,0.12);

    animation:
        bearBounce
        3s
        ease-in-out
        infinite;
}}


@keyframes bearBounce {{

    0%,
    100% {{
        transform:
            translate(-50%, -40%)
            translateY(0);
    }}

    50% {{
        transform:
            translate(-50%, -40%)
            translateY(-7px);
    }}
}}


.ear {{
    position: absolute;

    top: -13px;

    width: 40px;
    height: 40px;

    border-radius: 50%;

    background: #b98262;
}}


.ear::after {{
    content: "";

    position: absolute;

    inset: 8px;

    border-radius: 50%;

    background: #e3aa8c;
}}


.ear.left {{
    left: 6px;
}}


.ear.right {{
    right: 6px;
}}


.eye {{
    position: absolute;

    top: 42px;

    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #3f2921;
}}


.eye.left {{
    left: 37px;
}}


.eye.right {{
    right: 37px;
}}


.muzzle {{
    position: absolute;

    top: 51px;
    left: 50%;

    width: 47px;
    height: 33px;

    transform: translateX(-50%);

    border-radius: 50%;

    background: #e4ad91;
}}


.nose {{
    position: absolute;

    top: 7px;
    left: 50%;

    width: 11px;
    height: 8px;

    transform: translateX(-50%);

    border-radius: 50%;

    background: #503128;
}}


.mouth {{
    position: absolute;

    top: 14px;
    left: 50%;

    width: 13px;
    height: 7px;

    transform: translateX(-50%);

    border-bottom:
        2px solid #503128;

    border-radius:
        0 0 50% 50%;
}}


.question {{
    margin: 0 0 24px;

    color: #765564;

    font-size: clamp(20px, 3vw, 28px);

    font-weight: 600;

    line-height: 1.35;
}}


.answer-area {{
    position: relative;

    display: flex;

    align-items: center;
    justify-content: center;

    gap: 14px;

    width: 100%;

    min-height: 58px;
}}


.yes-btn {{
    z-index: 4;

    transition:
        transform 0.3s ease;
}}


.no-btn {{
    z-index: 3;

    color: #9d6f80;

    background:
        rgba(255,255,255,0.85);

    border:
        1px solid
        rgba(205,145,170,0.25);

    transition:
        left 0.18s ease,
        top 0.18s ease;
}}


/* ============================================================
   PAGE 2 - CAKE
   ============================================================ */

.cake-wrapper {{
    position: relative;

    width: 260px;
    height: 255px;

    margin:
        -5px 0
        -5px;
}}


.cake-shadow {{
    position: absolute;

    left: 50%;
    bottom: 23px;

    width: 190px;
    height: 20px;

    transform: translateX(-50%);

    border-radius: 50%;

    background:
        rgba(150,80,100,0.13);

    filter: blur(4px);
}}


.cake {{
    position: absolute;

    left: 50%;
    bottom: 40px;

    width: 190px;
    height: 95px;

    transform: translateX(-50%);
}}


.cake-base {{
    position: absolute;

    bottom: 0;

    width: 190px;
    height: 72px;

    border-radius:
        14px 14px 22px 22px;

    background:
        linear-gradient(
            to bottom,
            #f4a7b9,
            #df809c
        );

    box-shadow:
        inset 0 -8px 0
        rgba(155,71,99,0.1);
}}


.cake-cream {{
    position: absolute;

    top: 0;

    width: 190px;
    height: 22px;

    border-radius: 50%;

    background: #fff1f5;
}}


.cake-cream::before,
.cake-cream::after {{
    content: "";

    position: absolute;

    top: 7px;

    width: 25px;
    height: 20px;

    border-radius:
        0 0 50% 50%;

    background: #fff1f5;
}}


.cake-cream::before {{
    left: 28px;
}}


.cake-cream::after {{
    right: 28px;
}}


.candle {{
    position: absolute;

    top: -53px;
    left: 50%;

    width: 15px;
    height: 65px;

    transform: translateX(-50%);

    border-radius:
        6px 6px 3px 3px;

    background:
        repeating-linear-gradient(
            45deg,
            #f8b5ca 0px,
            #f8b5ca 6px,
            #fff4f7 6px,
            #fff4f7 12px
        );
}}


.flame {{
    position: absolute;

    top: -30px;
    left: 50%;

    width: 20px;
    height: 30px;

    transform:
        translateX(-50%)
        rotate(45deg);

    transform-origin:
        bottom right;

    border-radius:
        50% 0 50% 50%;

    background:
        linear-gradient(
            135deg,
            #ffd56b,
            #ff8c63
        );

    filter:
        drop-shadow(
            0 0 10px
            rgba(255,174,75,0.7)
        );

    animation:
        flame
        0.7s
        ease-in-out
        infinite
        alternate;
}}


@keyframes flame {{

    from {{
        transform:
            translateX(-50%)
            rotate(40deg)
            scale(0.95);
    }}

    to {{
        transform:
            translateX(-50%)
            rotate(50deg)
            scale(1.08);
    }}
}}


.flame.extinguished {{
    opacity: 0;

    transform:
        translateX(-50%)
        rotate(45deg)
        scale(0.2);

    animation: none;

    transition:
        opacity 0.35s ease,
        transform 0.35s ease;
}}


.smoke {{
    position: absolute;

    top: -85px;
    left: 50%;

    width: 10px;
    height: 10px;

    transform:
        translateX(-50%)
        scale(0.5);

    border-radius: 50%;

    background:
        rgba(150,150,150,0.28);

    opacity: 0;
}}


.smoke.active {{
    animation:
        smokeUp
        2s
        ease-out
        forwards;
}}


@keyframes smokeUp {{

    0% {{
        opacity: 0.5;

        transform:
            translateX(-50%)
            translateY(0)
            scale(0.5);
    }}

    100% {{
        opacity: 0;

        transform:
            translateX(-50%)
            translateY(-50px)
            scale(2.3);
    }}
}}


.sparkles {{
    position: absolute;

    inset: 0;

    opacity: 0;

    pointer-events: none;
}}


.sparkles.active {{
    opacity: 1;
}}


.spark {{
    position: absolute;

    font-size: 18px;

    animation:
        sparkle
        1.4s
        ease-out
        forwards;
}}


.spark:nth-child(1) {{
    left: 22%;
    top: 25%;
}}


.spark:nth-child(2) {{
    left: 72%;
    top: 20%;

    animation-delay: 0.15s;
}}


.spark:nth-child(3) {{
    left: 30%;
    top: 50%;

    animation-delay: 0.3s;
}}


.spark:nth-child(4) {{
    left: 67%;
    top: 48%;

    animation-delay: 0.45s;
}}


@keyframes sparkle {{

    0% {{
        opacity: 0;

        transform:
            scale(0.3)
            translateY(10px);
    }}

    35% {{
        opacity: 1;
    }}

    100% {{
        opacity: 0;

        transform:
            scale(1.3)
            translateY(-35px);
    }}
}}


.countdown {{
    min-height: 22px;

    margin-top: 3px;

    color: #b77a91;

    font-size: 14px;

    font-weight: 600;
}}


/* ============================================================
   PAGE 3 - ENVELOPE
   ============================================================ */

.envelope-page {{
    flex-direction: column;
}}


.envelope-content {{
    width: min(92vw, 680px);

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;
}}


.envelope-wrapper {{
    position: relative;

    width: min(82vw, 390px);

    aspect-ratio: 1.55 / 1;

    margin:
        20px 0
        25px;

    perspective: 1200px;
}}


.envelope {{
    position: absolute;

    inset: 0;

    border-radius: 13px;

    background:
        linear-gradient(
            145deg,
            #f7b4c8,
            #e88daa
        );

    box-shadow:
        0 25px 55px
        rgba(158,80,108,0.2);

    overflow: visible;
}}


.envelope-body {{
    position: absolute;

    inset: 0;

    overflow: hidden;

    border-radius: 13px;

    z-index: 3;
}}


.envelope-body::before {{
    content: "";

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            145deg,
            transparent 49%,
            rgba(255,255,255,0.22) 50%,
            transparent 51%
        );
}}


.envelope-flap {{
    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 62%;

    clip-path:
        polygon(
            0 0,
            100% 0,
            50% 100%
        );

    transform:
        rotateX(0deg);

    transform-origin:
        top center;

    background:
        linear-gradient(
            135deg,
            #f9bfd1,
            #e894b0
        );

    transition:
        transform
        1.1s
        cubic-bezier(.65,.05,.36,1);

    backface-visibility: hidden;

    z-index: 6;
}}


.envelope-front {{
    position: absolute;

    bottom: 0;
    left: 0;

    width: 100%;
    height: 62%;

    clip-path:
        polygon(
            0 100%,
            0 0,
            50% 70%,
            100% 0,
            100% 100%
        );

    background:
        linear-gradient(
            135deg,
            #ed9bb6,
            #df819f
        );

    z-index: 5;
}}


.letter-preview {{
    position: absolute;

    left: 14%;
    bottom: 3%;

    width: 72%;
    height: 75%;

    padding: 25px 18px;

    border-radius: 7px;

    background: #fffdfd;

    box-shadow:
        0 8px 20px
        rgba(130,75,95,0.12);

    transform:
        translateY(10px)
        scale(0.94);

    transition:
        transform
        1.2s
        cubic-bezier(.65,.05,.36,1);

    overflow: hidden;

    z-index: 2;
}}


.letter-preview::before {{
    content: "";

    display: block;

    width: 40%;
    height: 4px;

    margin:
        5px auto
        15px;

    border-radius: 99px;

    background: #e6a1b7;
}}


.letter-preview::after {{
    content: "❤️";

    position: absolute;

    right: 16px;
    bottom: 12px;

    font-size: 25px;

    opacity: 0.6;
}}


.envelope-wrapper.open
.envelope-flap {{
    transform:
        rotateX(180deg);

    z-index: 1;
}}


.envelope-wrapper.open
.letter-preview {{
    transform:
        translateY(-80px)
        scale(1);

    z-index: 7;
}}


/* ============================================================
   PAGE 4 - LETTER
   ============================================================ */

.letter-card {{
    position: relative;

    width: min(90vw, 680px);

    max-height: 82vh;
    max-height: 82dvh;

    padding:
        clamp(24px, 5vw, 45px)
        clamp(22px, 5vw, 50px);

    border:
        1px solid
        rgba(219,145,172,0.2);

    border-radius: 25px;

    background:
        rgba(255,255,255,0.84);

    box-shadow:
        0 25px 70px
        rgba(157,85,112,0.13);

    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);

    text-align: left;

    overflow: hidden;
}}


.letter-card::before {{
    content: "✦";

    position: absolute;

    top: 15px;
    right: 22px;

    color: #e4a0b7;

    font-size: 20px;

    opacity: 0.65;
}}


.letter-card h2 {{
    margin:
        0 0
        clamp(15px,3vw,25px);

    color: #965b73;

    font-family: "Pacifico", cursive;

    font-size:
        clamp(27px,5vw,40px);

    font-weight: 400;
}}


.letter-card p {{
    margin:
        0 0
        14px;

    color: #755f69;

    font-size:
        clamp(14px,1.8vw,16px);

    line-height: 1.75;
}}


.signature {{
    margin-top: 20px;

    color: #ad6685;

    font-family: "Pacifico", cursive;

    font-size:
        clamp(18px,3vw,23px);
}}


.letter-button-area {{
    display: flex;

    justify-content: center;

    margin-top: 25px;
}}


/* ============================================================
   PAGE 5
   ============================================================ */

.final-content {{
    width: min(92vw, 700px);
}}


.final-heart {{
    position: relative;

    width:
        clamp(100px,17vw,145px);

    height:
        clamp(100px,17vw,145px);

    margin:
        0 auto
        30px;

    transform:
        rotate(-45deg);

    border-radius:
        20px 0 20px 20px;

    background:
        linear-gradient(
            135deg,
            #ee91ad,
            #d96e94
        );

    box-shadow:
        0 20px 45px
        rgba(208,99,139,0.25);

    animation:
        heartBeat
        1.4s
        ease-in-out
        infinite;
}}


.final-heart::before,
.final-heart::after {{
    content: "";

    position: absolute;

    width: 100%;
    height: 100%;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #ee91ad,
            #d96e94
        );
}}


.final-heart::before {{
    top: -50%;
    left: 0;
}}


.final-heart::after {{
    top: 0;
    left: 50%;
}}


@keyframes heartBeat {{

    0%,
    100% {{
        transform:
            rotate(-45deg)
            scale(1);
    }}

    50% {{
        transform:
            rotate(-45deg)
            scale(1.08);
    }}
}}


.final-message {{
    width: min(90vw, 570px);

    margin:
        0 auto
        30px;

    color: #7e6872;

    font-size:
        clamp(15px,2vw,18px);

    line-height: 1.7;
}}


.final-sparkles {{
    position: absolute;

    inset: 0;

    overflow: hidden;

    pointer-events: none;

    z-index: 1;
}}


.final-sparkle {{
    position: absolute;

    color: #df91ad;

    opacity: 0;

    animation:
        finalSparkle
        3s
        ease-in-out
        infinite;
}}


.final-sparkle:nth-child(1) {{
    left: 20%;
    top: 25%;
}}


.final-sparkle:nth-child(2) {{
    left: 78%;
    top: 22%;

    animation-delay: 0.7s;
}}


.final-sparkle:nth-child(3) {{
    left: 15%;
    top: 70%;

    animation-delay: 1.4s;
}}


.final-sparkle:nth-child(4) {{
    left: 82%;
    top: 68%;

    animation-delay: 2.1s;
}}


.final-sparkle:nth-child(5) {{
    left: 50%;
    top: 15%;

    animation-delay: 1s;
}}


@keyframes finalSparkle {{

    0%,
    100% {{
        opacity: 0;

        transform:
            scale(0.4)
            rotate(0deg);
    }}

    35% {{
        opacity: 0.8;
    }}

    60% {{
        opacity: 0.4;

        transform:
            scale(1.2)
            rotate(90deg);
    }}
}}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 600px) {{

    .page {{
        padding:
            max(14px, env(safe-area-inset-top))
            max(14px, env(safe-area-inset-right))
            max(14px, env(safe-area-inset-bottom))
            max(14px, env(safe-area-inset-left));
    }}

    .content {{
        width: 92vw;

        max-height: 94dvh;
    }}

    .bear-area {{
        transform: scale(0.88);

        margin-top: -5px;

        margin-bottom: -5px;
    }}

    .question {{
        font-size: 20px;

        margin-bottom: 20px;
    }}

    .answer-area {{
        gap: 10px;
    }}

    .btn {{
        padding:
            12px 20px;

        font-size: 14px;
    }}

    .cake-wrapper {{
        transform: scale(0.82);

        margin-top: -25px;

        margin-bottom: -25px;
    }}

    .envelope-wrapper {{
        width: 84vw;

        margin:
            15px 0
            20px;
    }}

    .letter-card {{
        width: 92vw;

        max-height: 78dvh;

        padding:
            25px 21px;
    }}

    .letter-card p {{
        line-height: 1.6;

        margin-bottom: 10px;
    }}

    .signature {{
        margin-top: 14px;
    }}

    .letter-button-area {{
        margin-top: 18px;
    }}

    .final-heart {{
        margin-bottom: 24px;
    }}

    .final-message {{
        line-height: 1.6;

        margin-bottom: 24px;
    }}
}}


/* ============================================================
   SMALL HEIGHT PHONES
   ============================================================ */

@media (
    max-height: 680px
) and (
    max-width: 600px
) {{

    .bear-area {{
        transform: scale(0.72);

        margin-top: -28px;

        margin-bottom: -25px;
    }}

    .question {{
        font-size: 18px;

        margin-bottom: 14px;
    }}

    .cake-wrapper {{
        transform: scale(0.68);

        margin-top: -55px;

        margin-bottom: -60px;
    }}

    .title {{
        font-size: 31px;
    }}

    .subtitle {{
        font-size: 14px;

        margin-bottom: 17px;
    }}

    .letter-card {{
        max-height: 78dvh;

        padding:
            19px 18px;
    }}

    .letter-card h2 {{
        margin-bottom: 12px;

        font-size: 27px;
    }}

    .letter-card p {{
        margin-bottom: 8px;

        font-size: 13px;

        line-height: 1.48;
    }}

    .signature {{
        margin-top: 10px;

        font-size: 17px;
    }}

    .letter-button-area {{
        margin-top: 12px;
    }}

    .final-heart {{
        width: 82px;
        height: 82px;

        margin-bottom: 20px;
    }}
}}

</style>

</head>


<body>


<div
    class="scene"
    id="scene"
>


    <!-- ======================================================
         FLOATING EMOJIS
         ====================================================== -->

    <div
        class="floating-layer"
        id="floatingLayer">
    </div>


    <!-- ======================================================
         PAGE 1
         ====================================================== -->

    <section
        class="page active"
        id="page1"
    >

        <div class="content">


            <div class="bear-area">

                <div class="bear">

                    <div class="ear left"></div>
                    <div class="ear right"></div>

                    <div class="eye left"></div>
                    <div class="eye right"></div>

                    <div class="muzzle">

                        <div class="nose"></div>

                        <div class="mouth"></div>

                    </div>

                </div>

            </div>


            <div class="eyebrow">
                A tiny surprise
            </div>


            <p class="question">
                {QUESTION}
            </p>


            <div class="answer-area">

                <button
                    class="btn yes-btn"
                    id="yesBtn"
                >
                    {YES_TEXT}
                </button>


                <button
                    class="btn no-btn"
                    id="noBtn"
                >
                    {NO_TEXT}
                </button>

            </div>

        </div>

    </section>



    <!-- ======================================================
         PAGE 2
         ====================================================== -->

    <section
        class="page"
        id="page2"
    >

        <div class="content">


            <div class="eyebrow">
                A little birthday magic
            </div>


            <h1 class="title">
                {WISH_TITLE}
            </h1>


            <p class="subtitle">
                {WISH_SUBTITLE}
            </p>


            <div class="cake-wrapper">

                <div class="cake-shadow"></div>


                <div class="cake">

                    <div class="cake-base"></div>

                    <div class="cake-cream"></div>


                    <div class="candle">

                        <div
                            class="flame"
                            id="flame"
                        ></div>


                        <div
                            class="smoke"
                            id="smoke"
                        ></div>

                    </div>

                </div>


                <div
                    class="sparkles"
                    id="cakeSparkles"
                >

                    <span class="spark">
                        ✦
                    </span>

                    <span class="spark">
                        ✧
                    </span>

                    <span class="spark">
                        ✦
                    </span>

                    <span class="spark">
                        ✧
                    </span>

                </div>

            </div>


            <div
                class="countdown"
                id="countdownText"
            >
                {COUNTDOWN_MESSAGE}
            </div>


            <button
                class="btn primary-btn"
                id="blowBtn"
            >
                {BLOW_BUTTON}
            </button>


            <button
                class="btn soft-btn"
                id="wishContinueBtn"
                style="
                    display:none;
                    margin-top:12px;
                "
            >
                {CONTINUE_TEXT}
            </button>

        </div>

    </section>



    <!-- ======================================================
         PAGE 3
         ====================================================== -->

    <section
        class="page envelope-page"
        id="page3"
    >

        <div class="envelope-content">


            <div class="eyebrow">
                Just for you
            </div>


            <h1 class="title">
                {ENVELOPE_TITLE}
            </h1>


            <p class="subtitle">
                {ENVELOPE_SUBTITLE}
            </p>


            <div
                class="envelope-wrapper"
                id="envelopeWrapper"
            >

                <div class="envelope">


                    <div class="letter-preview">

                        <div
                            style="
                                font-family:'Pacifico',cursive;
                                color:#b66b86;
                                font-size:19px;
                            "
                        >
                            A little note...
                        </div>

                    </div>


                    <div class="envelope-body"></div>

                    <div class="envelope-front"></div>

                    <div class="envelope-flap"></div>

                </div>

            </div>


            <button
                class="btn primary-btn"
                id="openEnvelopeBtn"
            >
                {OPEN_BUTTON}
            </button>

        </div>

    </section>



    <!-- ======================================================
         PAGE 4
         ====================================================== -->

    <section
        class="page"
        id="page4"
    >

        <div class="content">


            <div class="letter-card">


                <h2>
                    {LETTER_TITLE}
                </h2>


                {paragraphs_html}


                <div class="signature">
                    {LETTER_SIGNATURE}
                </div>


                <div class="letter-button-area">

                    <button
                        class="btn primary-btn"
                        id="letterContinueBtn"
                    >
                        {FINAL_BUTTON}
                    </button>

                </div>

            </div>

        </div>

    </section>



    <!-- ======================================================
         PAGE 5
         ====================================================== -->

    <section
        class="page"
        id="page5"
    >


        <div class="final-sparkles">

            <span class="final-sparkle">
                ✦
            </span>

            <span class="final-sparkle">
                ✧
            </span>

            <span class="final-sparkle">
                ✦
            </span>

            <span class="final-sparkle">
                ✧
            </span>

            <span class="final-sparkle">
                ✦
            </span>

        </div>


        <div class="content final-content">


            <div class="final-heart"></div>


            <div class="eyebrow">
                And one last thing...
            </div>


            <h1 class="title">
                {FINAL_TITLE}
            </h1>


            <p class="final-message">
                {FINAL_MESSAGE}
            </p>


            <div
                style="
                    font-size:14px;
                    color:#c0879f;
                "
            >
                Made with a little bit of love ✨
            </div>

        </div>

    </section>


</div>


<script>

/* ============================================================
   PAGE NAVIGATION
   ============================================================ */

function goToPage(number) {{

    const pages =
        document.querySelectorAll(".page");


    pages.forEach(function(page) {{

        page.classList.remove("active");

    }});


    const target =
        document.getElementById(
            "page" + number
        );


    if (target) {{

        target.classList.add("active");

    }}

}}


/* ============================================================
   FLOATING EMOJIS
   ============================================================ */

const floatingLayer =
    document.getElementById(
        "floatingLayer"
    );


function createFloatingEmoji() {{

    const emoji =
        document.createElement("span");


    emoji.className =
        "floating-emoji";


    emoji.textContent =
        "{FLOATING_EMOJI}";


    const size =
        18 + Math.random() * 24;


    const left =
        Math.random() * 100;


    const top =
        Math.random() * 100;


    const opacity =
        0.08 + Math.random() * 0.17;


    const blur =
        Math.random() * 1.3;


    const duration =
        5 + Math.random() * 8;


    const delay =
        Math.random() * -10;


    const x1 =
        (Math.random() - 0.5) * 35;


    const x2 =
        (Math.random() - 0.5) * 70;


    const x3 =
        (Math.random() - 0.5) * 45;


    const y1 =
        (Math.random() - 0.5) * 35;


    const y2 =
        (Math.random() - 0.5) * 70;


    const y3 =
        (Math.random() - 0.5) * 45;


    const r1 =
        (Math.random() - 0.5) * 20;


    const r2 =
        (Math.random() - 0.5) * 40;


    const r3 =
        (Math.random() - 0.5) * 25;


    emoji.style.left =
        left + "%";


    emoji.style.top =
        top + "%";


    emoji.style.fontSize =
        size + "px";


    emoji.style.opacity =
        opacity;


    emoji.style.filter =
        "blur(" + blur + "px)";


    emoji.style.setProperty(
        "--duration",
        duration + "s"
    );


    emoji.style.setProperty(
        "--delay",
        delay + "s"
    );


    emoji.style.setProperty(
        "--x1",
        x1 + "px"
    );


    emoji.style.setProperty(
        "--x2",
        x2 + "px"
    );


    emoji.style.setProperty(
        "--x3",
        x3 + "px"
    );


    emoji.style.setProperty(
        "--y1",
        y1 + "px"
    );


    emoji.style.setProperty(
        "--y2",
        y2 + "px"
    );


    emoji.style.setProperty(
        "--y3",
        y3 + "px"
    );


    emoji.style.setProperty(
        "--r1",
        r1 + "deg"
    );


    emoji.style.setProperty(
        "--r2",
        r2 + "deg"
    );


    emoji.style.setProperty(
        "--r3",
        r3 + "deg"
    );


    floatingLayer.appendChild(
        emoji
    );

}}


const emojiCount =
    window.innerWidth <= 600
        ? 18
        : 28;


for (
    let i = 0;
    i < emojiCount;
    i++
) {{

    createFloatingEmoji();

}}


/* ============================================================
   PAGE 1 - NO BUTTON
   ============================================================ */

const noBtn =
    document.getElementById(
        "noBtn"
    );


const yesBtn =
    document.getElementById(
        "yesBtn"
    );


let yesScale = 1;


function moveNoButton() {{

    const area =
        document.querySelector(
            ".answer-area"
        );


    if (!area) return;


    const areaRect =
        area.getBoundingClientRect();


    const btnRect =
        noBtn.getBoundingClientRect();


    const maxX =
        Math.max(
            10,
            areaRect.width -
            btnRect.width -
            10
        );


    const x =
        Math.random() *
        maxX;


    const y =
        (Math.random() - 0.5) *
        100;


    noBtn.style.position =
        "relative";


    noBtn.style.left =
        x + "px";


    noBtn.style.top =
        y + "px";


    yesScale =
        Math.min(
            yesScale + 0.10,
            1.65
        );


    yesBtn.style.transform =
        "scale(" +
        yesScale +
        ")";

}}


noBtn.addEventListener(
    "mouseenter",
    moveNoButton
);


noBtn.addEventListener(
    "touchstart",
    function(event) {{

        event.preventDefault();

        moveNoButton();

    }},
    {{
        passive: false
    }}
);


noBtn.addEventListener(
    "click",
    function(event) {{

        event.preventDefault();

        moveNoButton();

    }}
);


/* ============================================================
   PAGE 1 - YES
   ============================================================ */

yesBtn.addEventListener(
    "click",
    function() {{

        yesBtn.style.transform =
            "scale(1.05)";


        setTimeout(
            function() {{

                goToPage(2);

            }},
            450
        );

    }}
);


/* ============================================================
   PAGE 2 - CANDLE
   ============================================================ */

const blowBtn =
    document.getElementById(
        "blowBtn"
    );


const flame =
    document.getElementById(
        "flame"
    );


const smoke =
    document.getElementById(
        "smoke"
    );


const cakeSparkles =
    document.getElementById(
        "cakeSparkles"
    );


const countdownText =
    document.getElementById(
        "countdownText"
    );


const wishContinueBtn =
    document.getElementById(
        "wishContinueBtn"
    );


let blowing = false;


blowBtn.addEventListener(
    "click",
    function() {{

        if (blowing) return;


        blowing = true;


        blowBtn.disabled =
            true;


        blowBtn.style.opacity =
            "0.55";


        let count = 5;


        countdownText.textContent =
            count;


        const timer =
            setInterval(
                function() {{

                    count--;


                    if (count > 0) {{

                        countdownText.textContent =
                            count;

                    }}

                    else {{

                        clearInterval(timer);

                        extinguishCandle();

                    }}

                }},
                800
            );

    }}
);


function extinguishCandle() {{

    flame.classList.add(
        "extinguished"
    );


    smoke.classList.add(
        "active"
    );


    cakeSparkles.classList.add(
        "active"
    );


    countdownText.textContent =
        "Wish made ✨";


    blowBtn.style.display =
        "none";


    wishContinueBtn.style.display =
        "inline-block";

}}


wishContinueBtn.addEventListener(
    "click",
    function() {{

        goToPage(3);

    }}
);


/* ============================================================
   PAGE 3 - ENVELOPE
   ============================================================ */

const envelopeWrapper =
    document.getElementById(
        "envelopeWrapper"
    );


const openEnvelopeBtn =
    document.getElementById(
        "openEnvelopeBtn"
    );


let envelopeOpened = false;


openEnvelopeBtn.addEventListener(
    "click",
    function() {{

        if (envelopeOpened) return;


        envelopeOpened = true;


        envelopeWrapper.classList.add(
            "open"
        );


        openEnvelopeBtn.style.opacity =
            "0";


        openEnvelopeBtn.style.pointerEvents =
            "none";


        setTimeout(
            function() {{

                goToPage(4);

            }},
            1500
        );

    }}
);


/* ============================================================
   PAGE 4 - LETTER
   ============================================================ */

const letterContinueBtn =
    document.getElementById(
        "letterContinueBtn"
    );


letterContinueBtn.addEventListener(
    "click",
    function() {{

        goToPage(5);

    }}
);


/* ============================================================
   HARD SCROLL LOCK
   ============================================================ */

document.documentElement.style.overflow =
    "hidden";


document.body.style.overflow =
    "hidden";


document.addEventListener(
    "wheel",
    function(event) {{

        event.preventDefault();

    }},
    {{
        passive: false
    }}
);


document.addEventListener(
    "touchmove",
    function(event) {{

        /*
           There is intentionally no scrolling anywhere
           on this birthday experience.
        */

        event.preventDefault();

    }},
    {{
        passive: false
    }}
);


/* ============================================================
   VIEWPORT SAFETY
   ============================================================ */

function forceViewport() {{

    document.documentElement.style.width =
        "100%";


    document.documentElement.style.height =
        "100%";


    document.body.style.width =
        "100%";


    document.body.style.height =
        "100%";


    document.body.style.margin =
        "0";


    document.body.style.padding =
        "0";


    document.body.style.overflow =
        "hidden";

}}


forceViewport();


window.addEventListener(
    "resize",
    forceViewport
);


window.addEventListener(
    "orientationchange",
    function() {{

        setTimeout(
            forceViewport,
            200
        );

    }}
);

</script>

</body>

</html>
"""


# ============================================================
#                  RENDER THE WEBSITE
# ============================================================

# DO NOT change this to height=1.
#
# The iframe needs a real height to render.
# The outer CSS above removes it from normal document flow
# and makes it occupy the browser viewport.

components.html(
    html,
    height=900,
    scrolling=False,
)