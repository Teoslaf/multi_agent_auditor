# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
	Creating Task Cheat Sheet:
    - Begin with the end in mind. Identify the specific outcome your task are aiming to achive.
    - Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
    - Ensure taks are descriptive, providing clear intrustions and expected deliverables.
    
    Goal:
    -    - Create a comprehensive smart contract security audit report that:
        1. Analyzes smart contract code for vulnerabilities and security risks
        2. Identifies potential gas optimization opportunities
        3. Reviews contract logic and business logic flaws
        4. Checks for compliance with best practices and standards
        5. Assesses centralization risks and trust assumptions
        6. Provides detailed recommendations for improvements
        7. Generates a professional audit report with findings severity levels
        
        Key Steps for Task Creation:
        1. Identify the Desired Outcome: Define what sucess looks like for your project.
			- A comprehensive smart contract security audit report.
            
        2. Task BreakDown: Divide the goal into smaller, managable tasks that agents can execute.
			-
        3. Assign Tasks to Agents: Match tasks with agents based on thair roles and expertise.
        
        4. Task Description Template:
        - Use this template as a guide to define each task in your crewAI aplication.
        - This template helps ensure that each task i clearly define, actionable and aligned with the overall goal.
"""
class SecurityAuditTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def initial_vulnerability_scan(self, agent, contract_code):
        return Task(
            description=dedent(f"""
                Perform an initial security vulnerability scan of the smart contract.
                
                Contract code to analyze:
                {contract_code}
                
                Focus on:
                1. Critical vulnerabilities (reentrancy, overflow, etc.)
                2. Access control issues
                3. Function visibility problems
                4. Unsafe external calls
                
                {self.__tip_section()}
                
                Provide a detailed report of all findings with severity levels.
            """),
            expected_output="JSON formatted report of security vulnerabilities with severity levels and descriptions",
            agent=agent
        )

    def business_logic_review(self, agent, contract_code, vulnerability_report):
        return Task(
            description=dedent(f"""
                Analyze the business logic and architecture of the smart contract.
                
                Contract code:
                {contract_code}
                
                Previous vulnerability findings:
                {vulnerability_report}
                
                Focus on:
                1. Contract architecture flaws
                2. Business logic inconsistencies
                3. State management issues
                4. Trust assumptions
                5. Centralization risks
                
                {self.__tip_section()}
                
                Provide detailed analysis of potential business logic issues.
            """),
            expected_output="Comprehensive report of business logic findings and architectural concerns",
            agent=agent
        )

    def exploit_scenario_analysis(self, agent, contract_code, previous_findings):
        return Task(
            description=dedent(f"""
                Analyze possible exploit scenarios and attack vectors.
                
                Use the contract code and previous findings:
                {contract_code}
                {previous_findings}
                
                Focus on:
                1. Creating proof of concept scenarios
                2. Identifying potential attack paths
                3. Assessing real-world exploit feasibility
                4. Calculating potential impact
                5. Ask yourself if its really an issue or not.
                
                
                {self.__tip_section()}
                
                Document all possible attack scenarios with detailed explanations.
            """),
            expected_output="Detailed attack scenarios and exploit possibilities with impact assessment",
            agent=agent
        )

    def final_report_compilation(self, agent, all_findings):
        return Task(
            description=dedent(f"""
                Compile a comprehensive security audit report.
                
                Use all previous findings:
                {all_findings}
                
                The report should include:
                1. Executive summary
                2. Detailed findings with severity levels
                3. Technical details and code snippets
                4. Recommendations for each issue
                5. Risk assessment matrix
                
                {self.__tip_section()}
                
                Format the report professionally and ensure all findings are clearly explained.
            """),
            expected_output="Professional audit report with all findings, recommendations, and severity classifications",
            agent=agent
        )
