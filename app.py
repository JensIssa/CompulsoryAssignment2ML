import autogen;
from autogen.coding import LocalCommandLineCodeExecutor


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

Additional Rules:
- In Python, include runtime measurement using the `time` library.
- Conclude with "TERMINATE" only if the script runs successfully and prints a total runtime below 50ms. Otherwise, optimize and retry.
"""
)

executor = LocalCommandLineCodeExecutor(
    work_dir="web"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config, 
    system_message="""REPLY TERMINATE IF THE TASK HAS BEEN SOLVED AT FULL SATISFACTION."""
)

task = """
Title: Average of numbers.

Write a Python function that takes a list of numbers and returns the average of the numbers.
"""

user_proxy.initiate_chat(assistant,message="""Solve the following problem \n\n""" + task)



