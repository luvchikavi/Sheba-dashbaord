import os
import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.figure_factory import create_gantt



# Automatically change the working directory to the script's directory
os.chdir(os.path.dirname(__file__))

# Set page configuration
st.set_page_config(page_title="Sheba Hospital Sustainability Dashboard", layout="wide")

# Define Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Landing Page", "Emission Overview", "Scenario Modeling", "Financial Models", "Compliance Tracker", "Recommendations"])

# Landing Page
if page == "Landing Page":
    col_logo, col_sheba_logo = st.columns([1, 1])
    with col_logo:
        st.image("oporto_logo.png", width=200)  # Oporto-Carbon Logo
    with col_sheba_logo:
        st.image("sheba_logo.png", width=200)  # Sheba Logo
    st.markdown("\n\n")  # Add spacing between logos and title
    st.title("Welcome to the Sheba Hospital Sustainability Dashboard")

    st.markdown(
        """
        ### About the Sheba Dashboard
        This tool is specifically designed to provide actionable insights into emissions management, compliance tracking, 
        and sustainability strategies for Sheba Hospital. It enables:

        - **Tracking Scope 1, Scope 2, and Scope 3 emissions**
        - **Aligning Sheba Hospital with international regulations**
        - **Streamlining decision-making for sustainability goals**
        - **Improving hospital operations through data-driven insights**

        ### About Oporto-Carbon
        Oporto-Carbon is a leader in lifecycle emissions analysis and regulatory compliance, delivering cutting-edge tools
        to streamline sustainability strategies. With experience working with hospitals, industries, and government bodies, 
        Oporto-Carbon specializes in integrating data from internal and external sources, ensuring real-time regulatory updates 
        and issue detection. By using advanced analytics and sustainability expertise, the platform provides actionable insights 
        for decision-making and future planning.

        ---

        Dr. Avi Luvchik is an internationally recognized expert in sustainability and emissions reduction. With over two decades 
        of experience, he has guided organizations globally to achieve compliance and sustainability excellence. His expertise 
        in lifecycle analysis, regulatory strategy, and tool development ensures that organizations can seamlessly integrate 
        sustainability into their operations.
        """
    )

    # Add the diagram image
    st.subheader("Data Processing Flow Diagram")
    st.image("data_processing_diagram1.svg", use_container_width=True)

    if st.button("Start Using Dashboard"):
        st.session_state.start = True

# Emission Overview Tab
elif page == "Emission Overview":
    st.image("sheba_logo.png", width=200)  # Sheba Logo on top of the page
    st.title("Emissions Overview")
    st.markdown(
        """
        This section provides an overview of Sheba Hospital's emissions across Scope 1, Scope 2, and Scope 3 categories. 
        Each parameter includes specific sources, emissions quantities, and the methodology used for data collection. 
        Additionally, compare Sheba's performance to global averages and see percentage differences.
        """
    )

    # Updated mock data for emissions overview with 25 parameters
    emissions_data = {
        "Scope": [
            "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 1", "Scope 2", "Scope 2", "Scope 2", "Scope 2", "Scope 2", "Scope 2", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3"
        ],
        "Parameter": [
            "Fuel consumption", "Fuel consumption", "Fuel consumption", "Refrigerants", "Refrigerants", "Heating Systems", "Backup Generators", "Natural Gas", "Medical Gases",
            "Electricity consumption", "Electricity consumption", "Electricity losses", "Renewable electricity", "Fossil fuels", "Grid electricity",
            "Staff transport", "Ambulance transport", "Patient transport", "Visitor transport", "Logistics", "Medical waste", "Chemical waste", "Biological waste", "Organic waste", "General waste"
        ],
        "Type": [
            "Diesel", "Gasoline", "Natural Gas", "R-123", "R-12", "Boilers", "Diesel generators", "Methane", "Nitrous oxide",
            "Solar", "Wind", "Transmission losses", "Solar panels", "Coal", "Grid electricity",
            "Buses", "Trucks", "Ambulances", "Cars", "Logistics vehicles", "Sharps", "Toxic chemicals", "Infectious waste", "Compost", "Non-recyclable"
        ],
        "Value": [400, 600, 1000, 12, 130, 200, 50, 1000, 800, 5000, 7000, 1000, 6000, 10000, 15000, 5000, 8000, 6000, 4000, 3000, 5, 3, 2, 2.5, 5],
        "Unit": ["liters", "liters", "cubic meters", "kg", "kg", "liters", "liters", "cubic meters", "cubic meters", "kWh", "kWh", "kWh", "kWh", "kWh", "kWh", "km", "km", "km", "km", "km", "tons", "tons", "tons", "tons", "tons"],
        "Emission Factor": [
            2.68, 2.31, 2.02, 1430, 1640, 2.8, 2.8, 1.9, 1.5, 0.3, 0.2, 0.1, 0.5, 1.1, 0.92, 0.12, 0.15, 0.1, 0.2, 0.3, 0.5, 1.2, 1.8, 0.5, 0.3
        ],
        "Emissions (tons CO₂e)": [
            1072, 1386, 2020, 17160, 21320, 560, 140, 1900, 1200, 1500, 1400, 100, 3000, 11000, 13800, 600, 1200, 600, 800, 900, 1.5, 1.8, 1.5, 1.25, 1.5
        ],
        "Source": [
            "Internal input", "Benchmark", "Internal input", "Internal input", "Internal input", "Internal input", "Internal input", "Benchmark", "Internal input",
            "Internal input", "Benchmark", "Benchmark", "Benchmark", "Benchmark", "Benchmark", "Internal input", "Benchmark", "Internal input", "Benchmark", "Internal input",
            "Assumption", "Assumption", "Assumption", "Assumption", "Assumption"
        ],
        "Global Average": [
            1100, 1400, 2100, 17500, 21500, 600, 150, 2000, 1300, 5100, 7000, 1500, 6000, 12000, 14000, 5200, 8000, 6200, 4200, 3500, 1.8, 2.0, 2.0, 2.7, 5.5
        ],
        "Comparison (%)": [
            -2.5, -1.0, -3.8, -2.0, -0.8, -6.7, -6.7, -5.0, -8.3, -6.7, -0.0, -33.3, 0.0, -8.3, -1.4, -3.8, -0.0, -3.2, -4.8, -14.3, -16.7, -10.0, -25.0, -7.4, -72.7
        ]
    }
    emissions_df = pd.DataFrame(emissions_data)

    # Display emissions table
    st.subheader("Detailed Emissions Table")
    st.dataframe(emissions_df)

    # Create a pie chart for total emissions
    st.subheader("Total Emissions by Scope")
    fig = px.pie(
        emissions_df,
        names="Scope",
        values="Emissions (tons CO₂e)",
        title="Total Emissions Distribution",
        hole=0.4,
        labels={"Scope": "Emission Scope"},
        color_discrete_sequence=px.colors.sequential.Blues
    )
    st.plotly_chart(fig)

# Scenario Modeling Tab
elif page == "Scenario Modeling":
    st.image("sheba_logo.png", width=200)  # Sheba Logo on top of the page
    st.title("Scenario Modeling")
    st.markdown(
        """
        Adjust key parameters to explore how changes impact emissions and costs. Use the sliders below to simulate different scenarios.
        """
    )

    renewable_energy = st.slider("Increase renewable energy (%)", 0, 100, 50)
    waste_reduction = st.slider("Reduce waste (%)", 0, 100, 30)
    transport_efficiency = st.slider("Improve transport efficiency (%)", 0, 100, 20)

    st.subheader("Scenario Results")
    emissions_reduction = (renewable_energy * 0.2) + (waste_reduction * 0.1) + (transport_efficiency * 0.15)
    st.write(f"Estimated emissions reduction: {emissions_reduction:.2f}%")

    st.subheader("Emissions Trends Over Time")
    trends_data = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031],
        "Scenario A (Reduction)": [12000, 11500, 11000, 10500 - (emissions_reduction * 10), 10000 - (emissions_reduction * 10), 9500, 9200, 8800, 8600, 8300, 8000],
        "Scenario B (Moderate)": [12000, 11600, 11200, 10800 - (emissions_reduction * 5), 10400 - (emissions_reduction * 5), 10200, 10000, 9800, 9600, 9400, 9200],
        "Scenario C (Business as Usual)": [12000, 12200, 12400, 12600, 12800, 13000, 13200, 13400, 13600, 13800, 14000]
    })
    fig_trends = px.line(
        trends_data,
        x="Year",
        y=["Scenario A (Reduction)", "Scenario B (Moderate)", "Scenario C (Business as Usual)"],
        title="Emissions Trends Over Time (Multiple Scenarios)",
        labels={"value": "Emissions (tons CO₂e)", "variable": "Scenarios"},
        markers=True
    )
    fig_trends.update_traces(line_dash="dash", selector=dict(name="Scenario C (Business as Usual)"))
    st.plotly_chart(fig_trends)

# Financial Models Tab
elif page == "Financial Models":
    st.image("sheba_logo.png", width=200)  # Sheba Logo on top of the page
    st.title("Financial Models")
    st.markdown(
        """
        Analyze the financial impact of emissions reduction strategies, including costs, carbon taxes, and ROI.
        """
    )

    st.subheader("Cost Analysis")
    renewable_cost = st.number_input("Cost of switching to renewables ($/MWh)", 50, 200, 100)
    waste_management_cost = st.number_input("Cost of waste reduction ($/ton)", 10, 100, 50)
    transport_upgrade_cost = st.number_input("Cost of transport upgrades ($/vehicle)", 500, 5000, 2000)

    total_cost = renewable_cost * 10 + waste_management_cost * 20 + transport_upgrade_cost * 5
    st.write(f"Total estimated cost: ${total_cost:,.2f}")

    st.subheader("ROI Calculation")
    # Ensure emissions_reduction is defined for this tab
    if 'emissions_reduction' not in locals():
        emissions_reduction = 0  # Default to 0 if not set in Scenario Modeling
    savings = emissions_reduction * 1000  # Assume $1000 savings per % reduction
    roi = (savings - total_cost) / total_cost * 100 if total_cost != 0 else 0
    st.write(f"Estimated ROI: {roi:.2f}%")

    # New ROI Trend Chart
    roi_trend_data = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024, 2025],
        "ROI (%)": [roi - 10, roi - 5, roi, roi + 5, roi + 10]
    })
    roi_chart = px.line(
        roi_trend_data,
        x="Year",
        y="ROI (%)",
        title="ROI Trends Over Time",
        markers=True
    )
    st.plotly_chart(roi_chart)

    # Cost Breakdown Chart
    st.subheader("Cost Breakdown")
    cost_data = pd.DataFrame({
        "Category": ["Renewable Energy", "Waste Management", "Transport Upgrades"],
        "Cost ($)": [renewable_cost * 10, waste_management_cost * 20, transport_upgrade_cost * 5]
    })
    cost_chart = px.pie(
        cost_data,
        names="Category",
        values="Cost ($)",
        title="Cost Distribution",
        hole=0.4
    )
    st.plotly_chart(cost_chart)

    # Cumulative Savings Chart
    st.subheader("Cumulative Savings")
    cumulative_savings_data = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024, 2025],
        "Cumulative Savings ($)": [0, savings * 1, savings * 2, savings * 3, savings * 4]
    })
    savings_chart = px.bar(
        cumulative_savings_data,
        x="Year",
        y="Cumulative Savings ($)",
        title="Cumulative Savings Over Time"
    )
    st.plotly_chart(savings_chart)

# Compliance Tracker Tab
elif page == "Compliance Tracker":
    st.image("sheba_logo.png", width=200)  # Sheba Logo on top of the page
    st.title("Compliance Tracker")
    st.markdown(
        """
        Track Sheba Hospital's progress in meeting key environmental regulations.
        """
    )

    regulations = {
        "JCI Regulation": 70,
        "ISO 14001 Certification": 80,
        "EU Emissions Standards": 50,
        "National Waste Reduction Targets": 90,
        "Renewable Energy Transition": 60
    }

    for reg, progress in regulations.items():
        st.subheader(reg)
        st.progress(progress)
        st.markdown(f"**{progress}% completed**")
        tasks = pd.DataFrame({
            "Task": ["Develop compliance plan", "Conduct audit", "Submit documentation"],
            "Time to Complete": ["2 months", "1 month", "3 months"],
            "Responsibility": ["Sustainability Officer", "Environmental Manager", "Compliance Team"],
            "Percentage of Completion": [progress - 10, progress - 20, progress],
            "Priority": ["High", "Medium", "Low"]
        })
        st.table(tasks)

elif page == "Recommendations":
    st.image("sheba_logo.png", width=200)  # Sheba Logo on top of the page
    st.title("General Overview and Recommendations")
    st.markdown(
        """
        Based on the collected data and analyses, here are the top recommendations prioritized by importance and time sensitivity.
        Additionally, set your internal goals and explore offset and inset processes to achieve net-zero emissions.
        """
    )

    # Goal Setting
    st.subheader("Set Internal Goals")
    goals = pd.DataFrame({
        "Goal": ["Net-zero emissions by 2030", "Offset 30% emissions by 2025", "Implement inset projects by 2026"],
        "Status": ["In Progress", "Not Started", "In Progress"],
        "Priority": ["High", "Medium", "High"]
    })
    st.table(goals)

    # Recommendations
    st.subheader("Top Recommendations")
    recommendations = pd.DataFrame({
        "Recommendation": [
            "Increase renewable energy usage",
            "Implement advanced waste management systems",
            "Optimize transportation routes",
            "Conduct staff training on sustainability"
        ],
        "Priority": ["High", "Medium", "High", "Low"],
        "Timeframe": ["1 year", "2 years", "6 months", "1 year"]
    })
    st.table(recommendations)

    # Visualizations
    st.subheader("Progress Towards Goals")
    progress_data = pd.DataFrame({
        "Category": ["Renewable Energy", "Waste Management", "Transportation Optimization"],
        "Progress (%)": [60, 40, 50]
    })
    progress_chart = px.bar(
        progress_data, x="Category", y="Progress (%)", title="Goal Progress",
        labels={"Progress (%)": "Completion Percentage"},
        color="Category", color_discrete_sequence=px.colors.sequential.Viridis
    )
    st.plotly_chart(progress_chart)

    # Gantt Chart for Task Tracking
    st.subheader("Dynamic Task Gantt Chart")

    # Sample task data with Owner and Status
    tasks = [
        {
            "Task": "Develop compliance plan",
            "Start": "2023-12-01",
            "Finish": "2023-12-15",
            "Resource": "High",
            "Completion": 50,
            "Owner": "Sustainability Officer",
            "Status": "In Progress"
        },
        {
            "Task": "Conduct audit",
            "Start": "2023-12-16",
            "Finish": "2023-12-31",
            "Resource": "Medium",
            "Completion": 30,
            "Owner": "Environmental Manager",
            "Status": "Pending"
        },
        {
            "Task": "Submit documentation",
            "Start": "2024-01-01",
            "Finish": "2024-01-10",
            "Resource": "Low",
            "Completion": 10,
            "Owner": "Compliance Team",
            "Status": "Not Started"
        },
    ]

    # Convert tasks to a DataFrame
    task_df = pd.DataFrame(tasks)

    # Display Gantt chart
    try:
        gantt_chart = create_gantt(
            task_df,
            index_col="Resource",
            show_colorbar=True,
            group_tasks=True,
            title="Task Gantt Chart",
            showgrid_x=True,
            showgrid_y=True,
        )
        st.plotly_chart(gantt_chart, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to create Gantt chart: {e}")

    # Display updated task list with Owner and Status
    st.write("### Detailed Task List")
    st.dataframe(task_df)

