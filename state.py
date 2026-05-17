from pydantic import BaseModel

class SEOState(BaseModel):
	website : str
	audit_results: str = ""
	competitor_list: str = ""
	final_report: str = ""
