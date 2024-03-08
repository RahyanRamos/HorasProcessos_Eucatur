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

def tabelaMacro():
    htmlMacro = f"""<table>
            <tr>
                <th>Executor</th>
                <th>Gestor</th>
                <th>Dono</th>
                <th>Líder</th>
            </tr>
            <tr>
                <td>20%</td>
                <td>10%</td>
                <td>5%</td>
                <td>33%</td>
            </tr>
            <tr>
                <td>20%</td>
                <td>10%</td>
                <td>5%</td>
                <td>33%</td>
            </tr>
            <tr>
                <td>20%</td>
                <td>10%</td>
                <td>5%</td>
                <td>33%</td>
            </tr>
            <tr>
                <td>20%</td>
                <td>10%</td>
                <td>5%</td>
                <td>33%</td>
            </tr>
            <tr>
                <td>20%</td>
                <td>10%</td>
                <td>5%</td>
                <td>33%</td>
            </tr>
        </table>"""
    
    return htmlMacro

def styleMacro():
    cssMacro = """table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: center;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }

        td {
           height: 30px;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }"""
    
    return cssMacro

menuHtml = menu9BoxHtml(" ", "MAPA DE HORAS vs POSIÇÕES")
menuCss = menu9BoxCss()
st.write(f"<div>{menuHtml}</div>", unsafe_allow_html=True)
st.write(f"<style>{menuCss}</style>", unsafe_allow_html=True)

data = {'Formulação Estratégica': {'HorasExecutor': 37,
  'HorasGestor': 0,
  'HorasDono': 7,
  'HorasLider': 2},
 'Relacionamento com Cliente - Pessoas': {'HorasExecutor': 110,
  'HorasGestor': 0,
  'HorasDono': 22,
  'HorasLider': 8},
 'Relacionamento com Cliente - Cargas': {'HorasExecutor': 129,
  'HorasGestor': 0,
  'HorasDono': 29,
  'HorasLider': 6},
 'Operar': {'HorasExecutor': 300,
  'HorasGestor': 0,
  'HorasDono': 62,
  'HorasLider': 14},
 'Administrar': {'HorasExecutor': 493,
  'HorasGestor': 0,
  'HorasDono': 88,
  'HorasLider': 32}}

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    form = st.button("Formulação Estratégica", use_container_width=True)
with col2:
    pes = st.button("RC. Pessoas", use_container_width=True)
with col3:
    car = st.button("RC. Cargas", use_container_width=True)
with col4:
    ope = st.button("Operar", use_container_width=True)
with col5:
    adm = st.button("Administrar", use_container_width=True)

if adm:
    st.switch_page("pages/Administrar.py.")
if ope:
    st.switch_page("pages/Operar.py")
if car:
    st.switch_page("pages/RCCargas.py")
if pes:
    st.switch_page("pages/RCPessoas.py")
if form:
    st.switch_page("pages/FormEstrategica.py")

st.dataframe(data, use_container_width=True)