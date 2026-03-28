# Introverts vs. Extroverts Prediction

## 🚀 How to set up the environment (PyCharm Professional)

We are using Docker Compose to ensure everyone has the exact same Python environment and package versions. You do not need to install any packages locally!

### Step 1: Start the Container
1. Open the project in PyCharm.
2. Open the `docker-compose.yml` file.
3. Click the **double green play arrows** in the gutter next to `services:`, OR open your terminal and run:
   `docker-compose up -d`

### Step 2: Configure PyCharm
To get autocomplete and remove the red squiggly lines, point PyCharm to the Docker container:
1. Go to **Settings / Preferences** > **Python** > **Interpreter**.
2. Click **Add Interpreter** > **On Docker Compose...**
3. Select the `docker-compose.yml` file.
4. In the Service dropdown, select `jupyter_env` and click **OK**.
5. Wait a minute for PyCharm to index the packages. You're done!

### Step 3: Connect PyCharm to the Jupyter Server
PyCharm sometimes struggles to manage the Dockerized Jupyter server automatically. To fix this and run notebook cells:
1. Open any `.ipynb` notebook file.
2. In the top right corner of the notebook editor, click the dropdown menu (it might say "IDE-Managed Server (Auto)" or have a gear icon).
3. Click **Configure Jupyter Server...**
4. Click the `+` button to add a new configuration.
5. Select **External Server**.
6. In the URL box, enter: `http://localhost:8888/?token=kaggle123`
7. Leave all checkboxes unchecked and click **Apply** / **OK**.