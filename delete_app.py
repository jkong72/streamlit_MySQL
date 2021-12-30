import streamlit as st
import mysql.connector
from MySQL_cnx import get_cnx
from mysql.connector.errors import Error

def run_delete_app():
    st.subheader('유저 삭제')

    id = st.number_input('삭제할 아이디 입력', min_value = 1)

    if st.button('삭제'):
        try :
            # DB와 연결
            cnx = get_cnx()
            # 쿼리문을 작성

            query='''delete from test_user
                        where id = %s;  '''
            # 단일 데이터 튜플은 (요소)가 아닌 (요소,)의 형식으로 작성한다.
            # 여러 데이터를 삽입 할 때에는 리스트를 통해 건네준다.
            record = (id,)
            
            # 연결로부터 커서를 가져옴
            cursor = cnx.cursor()

            # 쿼리문을 커서에 넣어 실행.
            cursor.execute(query, record)

            # 연결을 commit (DB에 반영)
            cnx.commit()

        except mysql.connector.Error as e:
            print('Error ', e)
        finally :
            if cnx.is_connected():
                cursor.close()  # 커서 닫음
                cnx.close()     # 연결 닫음
                print ('MySQL connection is closed')

                st.write('삭제가 완료 되었습니다.')