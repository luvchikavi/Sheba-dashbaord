import graphviz

# Updated DOT string with size adjustment
dot_string_resized = """
digraph G {
    rankdir=TB;
    graph [bgcolor="#343541", size="8,6", ratio="compress"];
    node [style="filled,rounded", shape="rectangle", gradientangle=270, color="grey", fillcolor="white:lightgrey", fontname="Helvetica", fontcolor="#343541"];
    edge [color="#AAAAAA", fontname="Helvetica", fontsize=12, fontcolor="#EEEEEE", arrowsize=1];

    subgraph cluster_internal_sources {
        label = "Internal Data Sources";
        style = "dashed";
        node [fillcolor="#AEC6CF"];
        finance [label="Finance System"];
        invoice [label="Invoice Management System"];
        energy [label="Energy Consumption Logs"];
        transport [label="Transportation Data"];
        waste [label="Waste Management Reports"];
        procurement [label="Procurement System"];
        hr [label="HR Systems (employee commuting data)"];
    }

    subgraph cluster_external_sources {
        label = "External Data Sources";
        style = "dashed";
        node [fillcolor="#B4D7A8"];
        un_databases [label="International Databases (UNFCCC, IPCC)"];
        openlca [label="OpenLCA Libraries"];
        industry [label="Industry Benchmarks"];
        regulatory [label="Regulatory Bodies (EU, National Agencies)"];
    }

    subgraph cluster_online_connectivity {
        label = "Online Connectivity";
        style = "dashed";
        node [fillcolor="#F4C2C2"];
        compliance [label="Real-time Compliance Services"];
        external_apis [label="External APIs for Carbon Pricing & Benchmarks"];
        live_updates [label="Live Updates on Regulatory Frameworks"];
    }

    subgraph cluster_processing {
        label = "Processing Layer";
        style = "solid";
        node [fillcolor="white"];
        integration [label="Data Integration"];
        model_core [label="Model Core"];
        analytics [label="Advanced Analytics"];
    }

    subgraph cluster_outputs {
        label = "Outputs";
        style = "solid";
        node [fillcolor="#FED8B1"];
        ghg_reports [label="GHG Emissions by Scope"];
        compliance_status [label="Regulation Compliance Status"];
        roi_analysis [label="ROI Analysis & Trends"];
        recommendations [label="Recommendations for Sustainability Goals"];
        forecasting [label="Future Emissions Projections"];
        benchmarking [label="Benchmarking Insights"];
    }

    # Connections
    finance -> integration;
    invoice -> integration;
    energy -> integration;
    transport -> integration;
    waste -> integration;
    procurement -> integration;
    hr -> integration;

    un_databases -> integration;
    openlca -> integration;
    industry -> integration;
    regulatory -> integration;

    compliance -> integration;
    external_apis -> integration;
    live_updates -> integration;

    integration -> model_core;
    model_core -> analytics;

    analytics -> ghg_reports;
    analytics -> compliance_status;
    analytics -> roi_analysis;
    analytics -> recommendations;
    analytics -> forecasting;
    analytics -> benchmarking;
}
"""

# Rendering the resized graph
graph_resized = graphviz.Source(dot_string_resized, format='svg')
resized_rendered_graph = graph_resized.render(filename='/mnt/data/data_processing_diagram_resized', view=False, cleanup=True)
resized_rendered_graph
