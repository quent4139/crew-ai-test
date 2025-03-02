from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import JSONSearchTool

@CrewBase
class CreationDUneEquipePourAutomatiserLaLogistiqueOdooCrew():
    """CreationDUneEquipePourAutomatiserLaLogistiqueOdoo crew"""

    @agent
    def order_processing_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['order_processing_specialist'],
            tools=[],
        )

    @agent
    def transport_management_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['transport_management_expert'],
            tools=[],
        )

    @agent
    def project_focus_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['project_focus_coordinator'],
            tools=[],
        )

    @agent
    def reporting_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_specialist'],
            tools=[],
        )

    @agent
    def client_data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['client_data_collector'],
            tools=[],
        )


    @task
    def process_orders_task(self) -> Task:
        return Task(
            config=self.tasks_config['process_orders_task'],
            tools=[JSONSearchTool()],
        )

    @task
    def manage_transport_task(self) -> Task:
        return Task(
            config=self.tasks_config['manage_transport_task'],
            tools=[],
        )

    @task
    def focus_on_project_task(self) -> Task:
        return Task(
            config=self.tasks_config['focus_on_project_task'],
            tools=[],
        )

    @task
    def generate_reports_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_reports_task'],
            tools=[],
        )

    @task
    def collect_client_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_client_data_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CreationDUneEquipePourAutomatiserLaLogistiqueOdoo crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
