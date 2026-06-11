from ai.gemini_client import GeminiClient
from ai.prompts import SALES_BRIEF_PROMPT
from config.default_icp import DEFAULT_ICP
from models.sales_brief import SalesBrief
from rag.retriever import Retriever

import json


class LeadAnalyzer:

    def __init__(self):
        self.gemini = GeminiClient()

        self.retriever = Retriever()

        self.retriever.build_from_file(
            "knowledge/company_services.txt"
        )

    def analyze(
        self,
        company_content: str,
        company_name: str = "Unknown"
    ) -> SalesBrief:

        rag_context = self.retriever.get_context(
            company_content,
            top_k=3
        )

        prompt = SALES_BRIEF_PROMPT.format(
            content=company_content[:10000],
            icp=json.dumps(DEFAULT_ICP, indent=2),
            rag_context=rag_context
        )

        response = self.gemini.generate_sales_brief(
            prompt
        )

        if not response:
            response = {}

        # -----------------------------
        # Required field defaults
        # -----------------------------

        response.setdefault(
            "company_name",
            company_name
        )

        response.setdefault(
            "company_overview",
            "Not available"
        )

        response.setdefault(
            "industry",
            "Unknown"
        )

        response.setdefault(
            "company_size",
            "Unknown"
        )

        response.setdefault(
            "core_product_service",
            "Not available"
        )

        response.setdefault(
            "target_customer",
            "Not available"
        )

        response.setdefault(
            "b2b_qualified",
            False
        )

        # -----------------------------
        # Sales questions defaults
        # -----------------------------

        default_questions = [
            "How do you currently acquire new customers?",
            "What are your biggest business challenges?",
            "Do you use any CRM or sales tools?"
        ]

        if "sales_questions" not in response:

            response["sales_questions"] = (
                default_questions
            )

        elif len(
            response["sales_questions"]
        ) < 3:

            missing = (
                3 -
                len(
                    response[
                        "sales_questions"
                    ]
                )
            )

            response[
                "sales_questions"
            ].extend(
                default_questions[:missing]
            )

        # -----------------------------
        # ICP defaults
        # -----------------------------

        if "icp" not in response:

            response["icp"] = {
                "target_roles": [],
                "pain_points": [],
                "buying_signals": [],
                "trigger_events": [],
                "tech_stack_signals": [],
                "qualification_score": 0,
                "icp_match_reason":
                    "No ICP analysis available."
            }

        else:

            response["icp"].setdefault(
                "target_roles",
                []
            )

            response["icp"].setdefault(
                "pain_points",
                []
            )

            response["icp"].setdefault(
                "buying_signals",
                []
            )

            response["icp"].setdefault(
                "trigger_events",
                []
            )

            response["icp"].setdefault(
                "tech_stack_signals",
                []
            )

            response["icp"].setdefault(
                "qualification_score",
                0
            )

            response["icp"].setdefault(
                "icp_match_reason",
                "No ICP analysis available."
            )

        # -----------------------------
        # RAG Context
        # -----------------------------

        response["rag_context"] = (
            rag_context
        )

        return SalesBrief(**response)