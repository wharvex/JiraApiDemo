import os
import re

def get_jira_config(filename="secrets.txt"):
    """
    Looks for a file named 'secrets.txt' in the current directory,
    expects it to have exactly four lines in the following format:
        JIRA_DOMAIN = your-domain.atlassian.net
        ISSUE_KEY = ABC-123
        EMAIL = your@email.com
        API_Token = your_api_token
    Returns a dictionary with keys: jira_domain, issue_key, email, api_token.
    Raises FileNotFoundError if file doesn't exist,
    ValueError if any line is missing or the format is wrong.
    """
    keys = ["JIRA_DOMAIN", "ISSUE_KEY", "EMAIL", "API_TOKEN"]
    config = {}

    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filename} not found in the current directory.")

    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        if len(lines) != 4:
            raise ValueError(f"Expected 4 lines in the file, got {len(lines)}.")

        for key, line in zip(keys, lines):
            match = re.match(rf'{key}\s*=\s*(.+)', line)
            if not match:
                raise ValueError(f"Line format incorrect for {key}: {line}")
            value = match.group(1).strip()
            config[key.lower()] = value

    # Rename keys for output dictionary
    return {
        "jira_domain": config.get("jira_domain"),
        "issue_key": config.get("issue_key"),
        "email": config.get("email"),
        "api_token": config.get("api_token"),
    }