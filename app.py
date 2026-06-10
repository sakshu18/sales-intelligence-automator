import streamlit as st
import pandas as pd

from services.lead_processor import LeadProcessor

st.set_page_config(
    page_title="Sales Intelligence Automator",
    layout="wide"
)

st.title("Sales Intelligence Automator")

uploaded_file = st.file_uploader(
    "Upload Leads CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success(f"{len(df)} leads loaded")

    if st.button("Analyze Leads"):

        processor = LeadProcessor()

        results = []

        progress_bar = st.progress(0)

        for index, row in df.iterrows():

            result = processor.process(
                company_name=row.get("company_name"),
                website_url=row.get("website_url"),
                location=row.get("location")
            )

            results.append(result)

            progress_bar.progress(
                (index + 1) / len(df)
            )

        st.success("Analysis Complete")

        st.subheader("Generated Sales Briefs")

        for result in results:

            with st.expander(
                result.get("company_name", "Unknown")
            ):

                if result.get("status") == "Skipped":
                    st.warning(result["reason"])

                elif result.get("status") == "Failed":
                    st.error(result["error"])

                else:
                    st.write(
                        "**Company Overview:**",
                        result.get("company_overview")
                    )

                    st.write(
                        "**Core Product/Service:**",
                        result.get("core_product_service")
                    )

                    st.write(
                        "**Target Customer:**",
                        result.get("target_customer")
                    )

                    st.write(
                        "**B2B Qualified:**",
                        result.get("b2b_qualified")
                    )

                    st.write("**Sales Questions:**")

                    for question in result.get(
                        "sales_questions", []
                    ):
                        st.write(f"• {question}")