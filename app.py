import streamlit as st

from ui.eda import run_eda

def main() :
    st.title('Game')

    menu=['Main','데이터 분석']
    choice=st.sidebar.selectbox('menu',menu)

    if choice==menu[0] :
        pass
    elif choice==menu[1] :
        run_eda()


    pass

if __name__ == '__main__' :
    main()