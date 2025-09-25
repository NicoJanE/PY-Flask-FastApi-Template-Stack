# What

This is a Python Flask application(template) . Besides Python it contains the following libraries ( installed with **pip** via the **requirements** file):
1. Flask Web front-end
1. Redis (realtime Data Platform), an in memory database,see: https://redis.io/learn/howtos/quick-start/cheat-sheet
1. jinja2, modern day templating language for Python developers
1. debugpy, Enables debugging in the Flask Python app

---

## 1. Install


<details>  
  <summary class="clickable-summary">
  <span  class="summary-icon"></span> <!-- Square Symbol -->
  <b>&nbsp;&nbsp;&nbsp;&nbsp;Suggestion: Project markers</b>
  </summary> <!-- On same line is failure -->
>
>You can mark your projects with one or more specific folders to make them easily searchable with your favorite search tool or script. I use the following folder markers:
> - `.njerepo` Project is one of my own official GitHub repositories
> - `.njeprj` Official project, but not (yet) one of my own GitHub repositories
> - `.git`  GitHub repository
>
> I use a Powershell script like this to search for me projects [see here](https://github.com/NicoJanE/Powershell-Utilities/blob/master/FindStringInFile/findp.ps1)

</details>


- In `compose_python_cont.yml` check the if the **published port** (5070 and 5670) suits for needs 
- Decide to run the container in release mode or Debug mode. In `compose_python_cont.yml` set:
  - For **Debug mode** set FLASK_ENV = ${debugModeOn}   (default)
  - For **Release mode** set FLASK_ENV =${debugModeOn} 
- Open a CLI the folder `.\PythonWebService` and execute:  
``docker-compose -f compose_python_cont.yml up -d --build --force-recreate``
- When Using **Release mode** you can enter in a browser: [localhost:5070](localhost:5070)
- For **Debug mode** read [**3. Using VS Code**](#3-using-vs-code) section before starting the site, after running the remote debug action in VS Code you should be able to attach to the Web Site  [localhost:5070](localhost:5070)
- Note that after installation, the Python application is available in the (host) folder `./PythonWebService/app` (Mount Bind)

---

## 2. VS Code Development Workflow for Docker Template Project

**Overview**

We utilize VS Code on the Windows host for developing our Python Flask application, leveraging Docker for an isolated environment. The primary goal is to maintain source code in Windows while enabling cross-platform compatibility with Linux Docker remote builds. This guide outlines the workflow, including building the application both locally and in Docker, addressing known issues, and providing workarounds.


**Development Workflow**

1. **Source Code Management**: We use a bind mount with Docker to keep the source code in sync between the host (Windows) and the container. This approach facilitates development in VS Code while ensuring changes are reflected in the Docker environment.

1. **Building the Application:**
    - ***Remote Building***:
    Preferred method, performed directly in VS Code targeting the Docker container. This approach ensures dependencies are installed within the container, minimizing setup on the host machine.
    - ***Local Building:***:
    Requires manual installation of dependencies on the Windows host, as outlined below. This method may be necessary for specific development tasks or troubleshooting.


**Required Local Dependencies for Windows**  

To build and run the application locally on Windows, install the following dependencies:  
``` PowerShell
pip install redis flask jinja2 debugpy
```
<small>Note: These packages correspond to the dependencies listed in the Docker container's `requirements` file.</small>


**Known Issues and Workarounds**

Remote building from VS Code into Docker can present challenges, including:
- Connection issues between VS Code and the Docker container after the first run.
- Debugging sessions may not terminate cleanly, requiring manual intervention.
- These are solved by automatic VS Code task that will restart te container and shutdown the process after the debug session

For detailed troubleshooting steps and workarounds, refer to the:
more detail documentation file [`docker_python_vscode_debug.md`](docker_python_vscode_debug.md) (A copy is available in the project `app` folder)


---

## 3. Using VS Code

**1. Install this required extensions in VS Code**

- code --install-extension ms-vscode-remote.remote-containers

<details>  
  <summary class="clickable-summary">
  <span  class="summary-icon"></span> <!-- Square Symbol -->
  <b>Warning When Using Multiple VSC Instance</b>
  </summary> <!-- On same line is failure -->
 <br>

>> 
>> ##### For installing multiple VS Code Instance see [here](https://gist.github.com/NicoJanE/bd7a66e22b5fec1e29c01880c5511326)
>
>  
> When using a second, third, or nth VS Code program at another location (for example: `C:\Apps\VSC-Python\`), and you have renamed `code.exe` to `vsc-python.exe` (as explained in the above link), you need to install the above extension via your CLI like this:  
`C:\Apps\VSC-Python\vsc-python.exe  --install-extension [name]`   

<small> Note: Alternatively, you can install them manually if preferred.</small>

</details>


**2. Open template project in VS Code**

- Open VSC and activate the extension tab **Remote Explorer**
- Right Click on your container `pythonwebservice-py-flask-fastapi-1` and choose "Attache 
in New Window" a new VSC Window opens with your container
- The use the **Open folder** command to open the **local** `\.PythonWebService\app` folder in your project folder. IMPORTANT! Use local cause the VSC `Launch.json` and `task.json` will only work with these file
- Make sure the following extensions are installed in the **Container**
  - code --install-extension ms-python.vscode-pylance  (required)
  - code --install-extension ms-python.python  (required)
  - code --install-extension charliermarsh.ruff
  - code --install-extension humao.rest-client
  - code --install-extension cweijan.vscode-database-client2
- Background information
  - For debugging the code in **Appendix I** is required, this is already included in your template application 
  - Also for debugging the `debugpy python library` is required also this is already installed during the setup via the requirements filr(manuall setup `pip install debugpy`)
  - The `.vscode\launch.json` displayed in Appendix 2 is also already available so to debug the application select the debug button and make sure the option 'Python Debugger: Remote Attach' is selected. This should start the debug session
- Use the remote debug instruction below.


**3. Remote WSL Debug and Run**

Due to a bug in VS Code (since 2019), we need to restart the container before running the application. After running, we must terminate the started process in the container for the same reason (hence the `ask.json` items). These steps will be performed automatically but will increase the startup and shutdown time for the debug and run process in the remote container.

***Steps:***

1. In VS Code, select the "Run and Debug" tab.
2. From the dropdown, select `PY-Remote-Docker` to start your debug session.

Please not that the container gets restarted, before the debug run this can take a few seconds


**4. Local Debug and Run**

Ensure the Python libraries are locally installed. Refer to the "Required Local Dependencies for Windows" section mentioned earlier in this document.

***Steps:***

1. From the dropdown, select `PY-Local-Windows` to start your debug session.


<br><br>

---

<h3 style="margin-top:0; margin-bottom:0; font-style:italic;">
  <span style="color:#FFFFFF; font-size:28px;">Appendix I</span>
  &nbsp;
  <span style="color:#409EFF; font-size:18px;">Debug Code</span>
</h3> <br>

This code is required to debug the application

```
import debugpy
import os

debugModeOn = False;
if os.getenv('FLASK_ENV') == 'debugNOW_ON':
    debugModeOn = True;
    
def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if(debugModeOn):
    debug_port = 5670
    if not is_port_in_use(debug_port):            
        debugpy.listen(('127.0.0.1', debug_port)) 
        debugpy.wait_for_client()               
        debugpy.breakpoint()        
        print(f"Debugger is active on port {debug_port}")
    else:        
        print(f" Port {debug_port} is already in use, skipping debugpy setup.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=debugModeOn)   # Reload true in debug mode, monitors file in source(including sub directories) and reloads the server
                                                            # so that changes are direct viewable for a developer without need to restart server manually (python concept feature) 
                                                            
```

---

<h3 style="margin-top:0; margin-bottom:0; font-style:italic;">
  <span style="color:#FFFFFF; font-size:28px;">Appendix II</span>
  &nbsp;
  <span style="color:#409EFF; font-size:18px;">VSCode file: launch.json</span>
</h3><br>

This is the used launch.json file for debbuging inside VS Code

```
{
    // Use IntelliSense to learn about possible attributes.  PY-Remote-Docker  
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
    {
                "name": "PY-Local-Windows",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/app.py",
                "console": "integratedTerminal",
                "preLaunchTask": "Explain",
            },
            {
                "name": "PY-Remote-Docker",
                "type": "debugpy",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": 5670
                },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/app"
                    }
                ],
                "justMyCode": true,
                "preLaunchTask": "Restart Container",
                "postDebugTask": "Kill Python in Container"
            }
    ]
}   
	
```
In addition this `Task.json` is required 

```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Restart Container",
            "type": "shell",
            "command": "Write-Host \"- Restarts container - fix Remote bug in VS code, since 2019`n- Debugs program`n- Choose manually File ->Stop to kill the process\" ; docker restart pythonwebservice-py-flask-fastapi-1;",
            "presentation": {
                "close": true
            }                    
        },
        {
            "label": "Kill Python in Container",
            "type": "shell",
            "command": "docker exec pythonwebservice-py-flask-fastapi-1 pkill -f app.py",
            "presentation": {
                "close": true
            }                    
        }
        ,
        {
            "label": "Explain",
            "type": "shell",
            "command": "Write-Host \"- Local was not preffered cause the idea was to install al dependencies in docker and run it out of the box.`nWith local you have to install the python dependencies in Windows your self, see the documentation in the project.`nBut Remote run requres an docker restart due to a long standing bug!  \"",
            "presentation": {
                "close": false,
                "reveal": "always",
                "panel": "new"
            }                    
        }
    ]
}

```

<!--
<h3 style="margin-top:0; margin-bottom:0; font-style:italic;">
  <span style="color:#FFFFFF; font-size:28px;">Appendix III</span>
  &nbsp;
  <span style="color:#409EFF; font-size:18px;">Additional technical insights</span>
</h3><br>
-->