# Docker Python Debugging in VS Code: Issues & Fixes


## Key Issues and Solutions

- **Remote Debugging**: VS Code’s remote debugging with Docker often requires manual container restarts. Use VS Code tasks to automate restarts and process termination.
- **Package Management**: Install Python packages both locally and in Docker for faster local debugging. Keep `requirements.txt` synchronized between environments.
- **Workflow Efficiency**: Frequent container restarts slow down development. Use local debugging for rapid iteration and Docker for final testing.

## Practical Workflow Tips

1. **Fast Development**: Use VS Code’s local launch configuration (`Python: Launch app.py`) and install dependencies with `pip install -r requirements.txt`.
2. **Remote Debugging**: Set up VS Code tasks to restart Docker containers and kill processes before and after debugging sessions. Accept that this process is slower. Decide to use Docker primarily for integration testing and production-like runs.
3. **Cross-Platform Consistency**: Keep Docker configurations and `requirements.txt` updated. Use Docker for integration tests and production environments.
4. **Documentation & Onboarding**
Document these limitations clearly. Share the workflow so other developers understand why both environments are needed.
5. Consider using the WSL Python stack [see here TODO]() as an alternative workflow.
This stack contains the same template project but runs entirely inside a WSL environment.
It uses the Remote – WSL VS Code extension to build and debug directly inside WSL, avoiding many of the Docker remote-debugging limitations.

## Summary

While Docker and VS Code offer powerful tools for Python development, remote debugging presents challenges that require workarounds. Local debugging is recommended for rapid development, with Docker used for final testing and deployment.

---


<small>*Last Updated: 25 September 2025* </small>