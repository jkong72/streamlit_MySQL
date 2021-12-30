import streamlit as st
import mysql.connector
from MySQL_cnx import get_cnx

def run_insert_app():
    st.subheader('회원가입')
    email = st.text_input('이메일 입력')
    pw = st.text_input('비밀번호 입력', type='password', max_chars=12)
    age = st.number_input('나이 입력', min_value=1)
    address = st.text_input('주소 입력')

    
    if st.button('입력'):
        
        try :
            cnx = get_cnx()
            query='''insert into test_user
                    (email,password,age,address)
                    values
                    (%s, %s, %s, %s);  '''
            # 단일 데이터 튜플은 (요소)가 아닌 (요소,)의 형식으로 작성한다.
            # 형식을 맞춰주지 않으면 데이터가 삽입되지 않는다. (빈 데이터, .format이나 f스트링 이용등..)
            # 
            record = (email, pw, age, address)
            
            # 연결로부터 커서를 가져옴
            cursor = cnx.cursor()

            # 쿼리문을 커서에 넣어 실행
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
                st.write('회원 가입되었습니다.')