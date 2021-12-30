import streamlit as st
import mysql.connector
from MySQL_cnx import get_cnx
from mysql.connector.errors import Error


def run_select_app():
    
    try :
        cnx = get_cnx()

        st.subheader ('모든 이용자')
        query = '''select id, email, age, address
                    from test_user;'''

        cursor = cnx.cursor()
        cursor.execute(query)

        # select 문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        for row in record_list:
            st.write(row)

        # DB id를 통한 조회
        st.subheader ('DB id 검색')
        id = st.number_input ('DB id 입력', min_value=1)

        query = '''select id, email, age, address
                    from test_user
                    where id = %s'''
        record = (id,)

        cursor.execute(query, record)
        # select 문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        for row in record_list:
            st.write(row)

        # email을 통한 조회
        st.subheader('email 검색')
        search = st.text_input ('검색어 입력')

        if st.button ('검색'):
            query = '''select id, email, age, address
            from test_user
            where email like '%'''+search+'''%';'''
            # or
            # like %s''' \n search = "%"+search+"%"
            # record = (search,)
            cursor.execute(query)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            for row in record_list:
                st.write(row)


    except mysql.connector.Error as e:
        print('Error while connecting to MySQL\n',e)

    finally :
        # cursor.closed()
        if cnx.is_connected():
            cnx.close()
            print('MySQL connection is closed')
        else:
            print('connection does not exist')
