import asyncio
from crewai.flow.flow import Flow, start, listen
from state import SEOState
from crews import SEOCrews

class ParallelSEOFlow(Flow[SEOState]):

    @start()
    async def kickoff(self):
        """Kickoff the SEO analysis flow by initiating the auditor and competitor crews in parallel."""
        print("[System Log]: Kickstarting the Parallel SEO Analysis Flow...")
        print("[System Log] , Kickstarting the Parallel SEO Analysis Flow...")

        auditor_crew = SEOCrews.create_auditor_crew()
        competitor_crew = SEOCrews.create_competitor_crew()

        audit_future = auditor_crew.kickoff_async(inputs = {"website": self.state.website})
        competitor_future = competitor_crew.kickoff_async(inputs = {"website": self.state.website})

        audit_res , comp_res = await asyncio.gather(audit_future , competitor_future)

        self.state.audit_results = audit_res.raw
        self.state.competitor_list = comp_res.raw
        print("[System Log]: Auditor and Competitor Crews have completed their tasks. Proceeding to synthesizer crew...")

    @listen(kickoff)
    def generate_final_report(self) -> str:
        """Generate the final SEO strategy report by synthesizing the findings from the auditor and competitor crews."""

        print("[System Log]: Synthesizing the final SEO strategy report based on the audit results and competitor analysis...")
        synthesizer_crew = SEOCrews.create_synthesizer_crew()

        result = synthesizer_crew.kickoff(inputs={
            "website": self.state.website,                "audit_results": self.state.audit_results,
            "competitor_list": self.state.competitor_list
        })

        self.state.final_report = result.raw
        return result.raw