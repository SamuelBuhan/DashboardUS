import streamlit as st
import pandas as pd
import plotly.express as px



# Load some example data
@st.cache_data  # Cache the data so it doesn't reload unnecessarily
def load_data(path):
    df = pd.read_csv(path)
    df.drop(df.columns[df.columns.str.contains(
    'unnamed', case=False)], axis=1, inplace=True)
    return df.drop_duplicates(subset=["Metro"], keep=False, ignore_index=True) 


def main():
    st.set_page_config(page_title="US jobs Dashboard",
                        layout="wide",
                        initial_sidebar_state="expanded")
    st.title("Welcome to dashboard")
    df = load_data("SofwareDeveloperIncomeExpensesperUSACity.csv")
    st.write(df)
    with st.sidebar:
        template_list =  ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white"]
        selected_template = st.selectbox('Select a plotly template', template_list)
        selected_x = st.selectbox('Select x to plot', df.columns.values)
        selected_y = st.selectbox('Select y to plot', df.columns.values)
    create_window(df, selected_x, selected_y, selected_template)

def create_window(df, x, y, template):
    print(f"template {template}")
    st.subheader(f"{x} vs {y}")
    cs_bar = px.bar(df, x=x, y=y,template=template)
    st.plotly_chart(cs_bar, use_container_width=False)

if __name__ == "__main__":
    main()