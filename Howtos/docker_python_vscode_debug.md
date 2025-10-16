# Docker Python Debugging in VS Code: Issues & Fixes

## Key Issues and Solutions

- **Remote Debugging**: VS Code’s remote debugging with Docker often requires manual container restarts. Use VS Code tasks to automate restarts and process termination.
- **Package Management**: Install Python packages both locally and in Docker for faster local debugging. Keep `requirements.txt` synchronized between environments.
- **Workflow Efficiency**: Frequent container restarts slow down development. Use local debugging for rapid iteration and Docker for final testing.

## Practical Workflow Tips

1. **Fast Development**: Use VS Code’s **local launch** configuration (`PY-Local-Windows`) and install dependencies using: `pip install -r requirements.txt`.
2. **Remote Debugging**: Set up VS Code tasks to restart Docker containers and kill processes before and after debugging sessions. Accept that this process is slower. Decide to use Docker primarily for integration testing and production-like runs, this already configured like so, use Launch item: (`PY-Remote-Docker`).
3. **Cross-Platform Consistency**: Keep Docker configurations and `requirements.txt` updated. Use Docker for integration tests and production environments.
4. **Documentation & Onboarding**
Document these limitations clearly. Share the workflow so other developers understand why both environments are needed.
5. Consider using the WSL Python container [see here](https://nicojane.github.io/PY-Flask-FastApi-Template-WSL-Stack/) as an alternative workflow.
This stack contains the same template project but runs entirely inside a WSL environment.
It uses the Remote – WSL VS Code extension to build and debug directly inside WSL, avoiding many of the Docker remote-debugging limitations.

## Summary

While Docker and VS Code offer powerful tools for Python development, remote debugging presents challenges that require workarounds(which are implemented). Local debugging can be considered for rapid development, with Docker remote building used for final testing and deployment. Alternatively one can consider to use the WSL container.

---


<small>*Last Updated: 16 Ocktober 2025* </small>