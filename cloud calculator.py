{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
def calculate_savings(num_servers, server_cost, server_lifetime, vmware_cost, power_cost, cooling_cost,\
                      it_staff_cost, maintenance_cost, backup_cost, security_cost):\
    # On-Premise Annual Costs\
    annual_server_cost = (num_servers * server_cost) / server_lifetime\
    total_on_prem_cost = (annual_server_cost + vmware_cost + power_cost + cooling_cost +\
                           it_staff_cost + maintenance_cost + backup_cost + security_cost)\
    \
    # Cloud Annual Costs (Estimated 50% Savings)\
    cloud_cost = total_on_prem_cost * 0.5\
    \
    # Savings Calculation\
    savings = total_on_prem_cost - cloud_cost\
    savings_percentage = (savings / total_on_prem_cost) * 100\
    \
    return total_on_prem_cost, cloud_cost, savings, savings_percentage\
\
# Streamlit UI\
st.title("Cloud Savings Calculator")\
st.write("Estimate your savings when migrating from on-premise to the cloud.")\
\
# User Inputs\
num_servers = st.number_input("Number of Physical Servers", min_value=1, value=10)\
server_cost = st.number_input("Cost per Server ($)", min_value=1000, value=5000)\
server_lifetime = st.number_input("Server Lifetime (Years)", min_value=1, value=5)\
vmware_cost = st.number_input("Annual VMware Licensing Cost ($)", min_value=0, value=20000)\
power_cost = st.number_input("Annual Power Cost ($)", min_value=0, value=12000)\
cooling_cost = st.number_input("Annual Cooling Cost ($)", min_value=0, value=8000)\
it_staff_cost = st.number_input("Annual IT Staff Cost for Maintenance ($)", min_value=0, value=50000)\
maintenance_cost = st.number_input("Annual Hardware Maintenance Cost ($)", min_value=0, value=10000)\
backup_cost = st.number_input("Annual Backup & Disaster Recovery Cost ($)", min_value=0, value=15000)\
security_cost = st.number_input("Annual Security Cost ($)", min_value=0, value=12000)\
\
# Calculate savings if the user clicks the button\
if st.button("Calculate Savings"):\
    total_on_prem_cost, cloud_cost, savings, savings_percentage = calculate_savings(\
        num_servers, server_cost, server_lifetime, vmware_cost, power_cost,\
        cooling_cost, it_staff_cost, maintenance_cost, backup_cost, security_cost)\
    \
    st.subheader("Results")\
    st.write(f"**On-Premise Annual Cost:** $\{total_on_prem_cost:,.2f\}")\
    st.write(f"**Cloud Annual Cost:** $\{cloud_cost:,.2f\}")\
    st.write(f"**Estimated Savings:** $\{savings:,.2f\} (\{savings_percentage:.2f\}% Reduction)")\
    \
    st.success("Moving to the cloud can help you significantly reduce costs!")\
}