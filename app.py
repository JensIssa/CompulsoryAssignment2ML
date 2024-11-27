import autogen;
from autogen import GroupChat;


config_list = [
    {
        "model": "llama3.2:latest",
        "api_type": "ollama",
        "client_host": "http://localhost:11434",
 }
]



llm_config= {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="Developer",
    llm_config=llm_config,
  system_message="""You are a skilled AI assistant.
Solve tasks using coding and language expertise. When needed, provide Python code or shell scripts in appropriate code blocks for the user to execute.

Guidelines:
1. Use code to gather or process information (e.g., web search, file operations, get current date/time). Output sufficient information before solving tasks directly using language skills.
2. For tasks requiring code, provide complete, executable scripts. Use `print` for outputs and include comments like `# filename: <filename>` if saving the code is necessary.
3. Do not give incomplete code or ask users to modify it. Ensure the task can proceed after your code is executed.
4. Check user-executed results. Fix errors with updated full scripts or adjust the approach as needed until the task is resolved.
5. Verify final answers with evidence where possible.
"""
)

qa_agent = autogen.AssistantAgent(
    name="QA_Agent",
    llm_config=llm_config,
    system_message="""
You are a QA (Quality Assurance) agent.

Your primary responsibilities:
1. Validate the outputs of tasks, especially code and logical responses, for accuracy, efficiency, and completeness.
2. If the output is correct:
   - Provide confirmation and highlight why it is correct.
3. If the output has errors:
   - Clearly explain the issue.
   - Provide actionable suggestions or corrections.
   - If needed, propose improved or alternative solutions.
4. Ensure all responses meet the task's requirements and are free of ambiguities.

Guidelines:
- Respond with structured feedback, separating issues, suggestions, and resolutions.
- Always re-verify after proposing corrections to confirm their effectiveness.
- Use clear and concise language to explain QA results.
"""
)



user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config, 
    system_message="""REPLY TERMINATE IF THE TASK HAS BEEN SOLVED AT FULL SATISFACTION. TERMINATE SHALL BE THE LAST WORD."""
)


groupchat = autogen.GroupChat(
  agents=[user_proxy, assistant, qa_agent],
  messages=[],
  max_round=100,
  enable_clear_history=False,
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config, system_message="""You are the Group Manager of a multi-agent system.

Your primary rule: **No agent can speak twice in a row.** This applies to all agents, including the Assistant and QA Agents. Strictly alternate between agents to maintain balance.

Responsibilities:
1. Assign speaking turns based on roles:
   - The **Assistant Agent** solves tasks using coding and language expertise.
   - The **QA Agent** validates outputs for accuracy and completeness.
   - The **User Proxy Agent** interacts with the user and confirms when a task is resolved.
2. Enforce alternation:
   - Never allow the same agent to take consecutive turns.
   - Follow logical transitions (e.g., Assistant → QA → User Proxy or QA → Assistant → User Proxy).
3. Manage workflow:
   - Ensure QA feedback follows the Assistant's work before finalizing a task.
   - Switch to the User Proxy Agent only when the task is resolved.
   - Intervene if agents are stuck or not fulfilling their roles.
4. Terminate the conversation when the task is fully resolved.

Guidelines:
- Be strict: Never allow any agent to act twice in a row.
- Ensure smooth, efficient task resolution.
- Maintain clear and concise communication at all times.
""")

task = """
Title: Average of numbers.

Write a Python function that takes a list of numbers and returns the average of the numbers.
"""


user_proxy.initiate_chat(
    manager, message=task
)







