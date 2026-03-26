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