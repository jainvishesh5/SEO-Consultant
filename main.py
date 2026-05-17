import streamlit as st
import os
import asyncio
from flow import ParallelSEOFlow
from state import SEOState

st.set_page_config(page_title = "SEO Analysis Tool" , layout = "wide" ,page_icon = "📈")
st.title("SEO Analysis Tool")
st.caption("A comprehensive SEO analysis tool that provides insights into website performance, competitor strategies, and actionable recommendations for optimization.")

st.sidebar.title("Consfiguration")
openai_key = st.sidebar.text_input("OpenAI_API_Key:" , type = "password" , placeholder = "openAI_API_Key" )
serper_key = st.sidebar.text_input("Serper_API_Key:" , type = "password" , placeholder = "" )

website = st.text_input("Enter the target website URL:" , placeholder = "https://www.example.com")

if st.button("Run SEO Analysis" , type = "primary"):
    if not(openai_key and serper_key and website):
        st.sidebar.error("Please provide all the required inputs.")
    else:
         os.environ["OPENAI_API_KEY"] = openai_key
         os.environ["SERPER_API_KEY"] = serper_key
         os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

         with st.spinner("Running SEO Analysis... This may take a few moments."):
             flow = ParallelSEOFlow(SEOState(website = website))

             final_report = asyncio.run(flow.kickoff_async())

             st.success("SEO Analysis Completed!")

             st.subheader("Final SEO Strategy Report")
             st.markdown(final_report)