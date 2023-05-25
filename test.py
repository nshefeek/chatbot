import streamlit as st

#adding a selectbox

choice1 = st.selectbox(

    'Select the items you want?',

    ('Pen','Pencil','Eraser','Sharpener','Notebook'),
    
    key='choice1',)



choice2 = st.selectbox(

    'Select the items you want?',

    ('Pen','Pencil','Eraser','Sharpener','Notebook'),
    
    key='choice2',)



#displaying the selected option
if st.button("Submit"):
    print(choice1)

    st.write('You have selected:', choice1)
    st.write('You have selected:' , choice2)