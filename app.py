import streamlit as st
from delete_app import run_delete_app

# 내부 패키지
from insert_app import run_insert_app
from select_app import run_select_app
from update_app import run_update_app

def main():
    # CRUD
    # Create, Read, Update, Delete
    menu = ['Insert', 'Select', 'Update', 'Delete']

    menu_sel = st.sidebar.selectbox('선택하세요', menu)

    # 사이드바 메뉴 Insert
    if menu_sel == menu[0]:
        run_insert_app()

    # 사이드바 메뉴 Select
    elif menu_sel == menu[1]:
        run_select_app()

    # 사이드바 메뉴 Update
    elif menu_sel == menu[2]:
        run_update_app()

    # 사이드바 메뉴 Delete
    elif menu_sel == menu[3]:
        run_delete_app()



if __name__ == '__main__':
    main()