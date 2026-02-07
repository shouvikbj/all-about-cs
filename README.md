## All About Computer Science

### process to setup python project
1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
    - On Windows
    ```bash
    env\Scripts\activate
    ```
    - On Unix or MacOS
    ```bash
    source env/bin/activate
    ```

3. Install packages for the first time:
    ```bash
    pip install <package-name>
    ```

4. Install required packages from requirements file:
    ```bash
    pip install -r requirements.txt
    ```

5. Run Python file:
    ```bash
    cd python
    python <file-name>.py
    ```