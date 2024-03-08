import streamlit as st

st.set_page_config(layout="wide")

def menu9BoxHtml(nome, page):
    menu9Box = f"""<div class="fixed">
            <div class="menu">
                <div class="logo">
                    <img src="https://raw.githubusercontent.com/RahyanRamos/LogoNineBox/main/logo.png" alt="Logo do 9Box">
                </div>
                <div class="botoes">
                    <div class="page"><p>{page}</p></div>
                </div>
                <div class="nome"><p>{nome}</p></div>
                <div class="icone">
                    <!-- <button type="button"><img src="https://cdn-icons-png.flaticon.com/128/5261/5261124.png" alt="ícone de configurações para alteração do módulo de uso"></button>
                    <div class="modulo">
                        <a href="https://meusprojetos-mpjj.streamlit.app/"><button type="button">Módulo de Execução</button></a>
                        <a href="https://meusprojetos-mpjj-mg.streamlit.app/"><button type="button">Módulo de Gestão</button></a>
                    </div> -->
                </div>
            </div>
        </div>"""
    return menu9Box

def menu9BoxCss():
    styleMenu9Box = f""".fixed{{
            position: fixed;
            top: 0;
            z-index: 999990;
            left: 50px;
            right: 50px;
        }}

        .menu{{
            display: flex;
            position: absolute;
            align-items: center;
            /*background: linear-gradient(to bottom, #06405c);*/
            background-color: #06405c;
            color: #fff;
            padding: 10px 20px;
            width: 100%;
            height: 46px;
            border-bottom-left-radius: 15px;
            border-bottom-right-radius: 15px;
        }}

        .logo,
        .botoes{{
            margin-right: auto;
        }}

        .logo img{{
            width: 100px;
            font-family: 'M PLUS Rounded 1c', sans-serif;
            font-size: 10px;
            margin: 0;
        }}

        .botoes{{
            margin-top: 10px;
        }}

        .botoes p{{
            font-weight: bold;
            background-color: #ffc000;
            padding: 0px 15px;
            border-radius: 8px;
            font-size: 18px;
            color: #06405c;
        }}

        .botoes button{{
            margin-right: 10px;
            padding: 0px 10px;
            border: none;
            background-color: transparent;
            color: #fff;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            transition: border-color 0.5s ease;
        }}

        .nome p{{
            margin-right: 10px;
            color: #ffc000;
            font-weight: bold;
            font-size: 16px;
            margin-top: 12px;
        }}

        .icone img{{
            width: 35px;
            height: 35px;
        }}

        .icone button{{
            background-color: #9fdafc;
            border-radius: 50%;
            cursor: pointer;
            border: none;
            width: 40px;
            height: 40px;
        }}

        .modulo{{
            display: none;
            position: absolute;
            top: auto;
            right: 0;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #9fdafc;
            height: auto;
            width: 175px;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }}

        .modulo button{{
            border-radius: 8px;
        }}

        .modulo:after{{
            content: "";
            width: 0;
            height: 0;
            position: absolute;
            border-left: 15px solid transparent;
            border-right: 15px solid transparent;
            border-bottom: 20px solid #9fdafc;
            top: -15px;
            right: 25px
        }}

        .icone:hover .modulo{{
            display: block;
        }}

        .modulo button{{
            display: block;
            width: 100%;
            padding: 5px;
            text-align: left;
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-weight: bold;
            color: #000;
            margin-bottom: 5px;
        }}

        .botoes button:hover{{
            border: none;
            border-bottom: 2px solid #26eda2;
            cursor: pointer;
        }}

        .modulo button:hover{{
            background-color: #91c1dd;
        }}

        .logo:hover{{
            text-decoration: underline;
        }}
        
        @media screen and (max-width: 650px){{
            .menu{{
                flex-direction: column;
                height: auto;
                max-height: 50px;
            }}

            .botoes{{
                margin-top: 10px;
            }}

            button{{
                margin: 5px 0;
            }}

            .icone{{
                margin-top: 10px;
            }}

            .modulo{{
                right: -20px;
            }}
        }}"""
    return styleMenu9Box

menuHtml = menu9BoxHtml(" ", "MAPA DE HORAS vs POSIÇÕES")
menuCss = menu9BoxCss()
st.write(f"<div>{menuHtml}</div>", unsafe_allow_html=True)
st.write(f"<style>{menuCss}</style>", unsafe_allow_html=True)

data =  {'Gerir investimentos': {'HorasExecutor': 2,
    'HorasGestor': 4,
    'HorasDono': 4,
    'HorasLider': 1},
   'Gerir fluxo de caixa': {'HorasExecutor': 35,
    'HorasGestor': 6,
    'HorasDono': 8,
    'HorasLider': 1},
   'Gerir contas a Receber': {'HorasExecutor': 31,
    'HorasGestor': 2,
    'HorasDono': 8,
    'HorasLider': 3},
   'Gerir planejamento e controle orçamentário': {'HorasExecutor': 35,
    'HorasGestor': 4,
    'HorasDono': 8,
    'HorasLider': 3},
   'Gerir contas a Pagar': {'HorasExecutor': 39,
    'HorasGestor': 6,
    'HorasDono': 9,
    'HorasLider': 3},
   'Gerir Contabilidade Geral': {'HorasExecutor': 34,
    'HorasGestor': 2,
    'HorasDono': 4,
    'HorasLider': 2}}

st.title("Administrar Recursos Financeiros")

st.dataframe(data, use_container_width=True, width=1)