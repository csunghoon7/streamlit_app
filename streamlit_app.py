import streamlit
import pandas


streamlit.title('고객 주문 관리 내역')

streamlit.header('헤더 입니다')

streamlit.text('텍스트 입니다')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index(“Fruit”)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) 
streamlit.dataframe(my_fruit_list)

