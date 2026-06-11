import streamlit as st
import pandas as pd
import json

from services.lead_processor import LeadProcessor

st.set_page_config(
    page_title="Sales Intelligence Automator",
    layout="wide"
)

st.title("Sales Intelligence Automator")
st.caption(
    "AI-powered lead research, qualification, and sales brief generation"
)

# Sidebar
with st.sidebar:
    st.header("Research Pipeline")
    st.caption("End-to-End Lead Intelligence Workflow")

    st.write("📥 Load Leads")
    st.write("🌐 Resolve Company Website")
    st.write("🕷️ Scrape Website")
    st.write("🧹 Clean Content")
    st.write("🤖 Gemini Analysis")
    st.write("📊 Generate Sales Brief")

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
        st.download_button(
            label="📥 Download Results JSON",
            data=json.dumps(results, indent=2),
            file_name="sales_briefs.json",
            mime="application/json"
)

        qualified_count = sum(
            1 for r in results
            if str(r.get("b2b_qualified")).lower()
            in ["true", "yes", "qualified"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Leads Processed",
                len(results)
            )

        with col2:
            st.metric(
                "Qualified Leads",
                qualified_count
            )

        with col3:
            st.metric(
                "Rejected Leads",
                len(results) - qualified_count
            )

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

                    if result.get("website_url"):
                        st.markdown(
                            f"**Website:** {result.get('website_url')}"
                        )

                    st.write(
                        "**Industry:**",
                        result.get("industry")
                    )

                    st.write(
                        "**Company Size:**",
                        result.get("company_size")
                    )

                    st.write(
                        "**Core Product/Service:**",
                        result.get("core_product_service")
                    )

                    st.write(
                        "**Target Customer:**",
                        result.get("target_customer")
                    )

                    if result.get("b2b_qualified") is True:
                        st.success("✅ Qualified B2B Lead")
                    else:
                        st.error("❌ Not a B2B Lead")

                    icp = result.get("icp", {})

                    st.markdown("---")
                    st.subheader("🎯 ICP Analysis")

                    score = icp.get(
                        "qualification_score",
                        0
                    )

                    st.metric(
                        "Qualification Score",
                        score
                    )

                    match_reason = icp.get(
                        "icp_match_reason",
                        ""
                    )

                    if match_reason:
                        st.info(
                            f"ICP Match Reason: {match_reason}"
                        )

                    rag_context = result.get(
                        "rag_context",
                        ""
                    )

                    if rag_context:

                        st.markdown("---")
                        st.subheader(
                            "📚 RAG Context Used"
                        )

                        st.info(rag_context)

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown(
                            "### 👥 Target Roles"
                        )

                        for role in icp.get(
                            "target_roles",
                            []
                        ):
                            st.write(f"• {role}")

                        st.markdown(
                            "### ⚠️ Pain Points"
                        )

                        for pain in icp.get(
                            "pain_points",
                            []
                        ):
                            st.write(f"• {pain}")

                        st.markdown(
                            "### 🚀 Trigger Events"
                        )

                        for event in icp.get(
                            "trigger_events",
                            []
                        ):
                            st.write(f"• {event}")

                    with col2:

                        st.markdown(
                            "### 📈 Buying Signals"
                        )

                        for signal in icp.get(
                            "buying_signals",
                            []
                        ):
                            st.write(f"• {signal}")

                        st.markdown(
                            "### 💻 Tech Stack Signals"
                        )

                        for tech in icp.get(
                            "tech_stack_signals",
                            []
                        ):
                            st.write(f"• {tech}")

                    st.markdown("---")

                    st.write(
                        "**Sales Questions:**"
                    )

                    for question in result.get(
                        "sales_questions",
                        []
                    ):
                        st.write(
                            f"• {question}"
                        )