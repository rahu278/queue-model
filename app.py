import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🏥 Hospital OPD Queue Model (M/M/c)")

# User Inputs
arrival_rate = st.number_input("Enter patient arrival rate (λ):", min_value=0.0, step=0.1)
service_rate = st.number_input("Enter service rate per doctor (μ):", min_value=0.0, step=0.1)
doctors = st.number_input("Enter number of doctors (c):", min_value=1, step=1)

if st.button("Calculate"):
    rho = arrival_rate / (doctors * service_rate) if service_rate > 0 else 0

    if rho >= 1:
        st.error("⚠️ System is overloaded! Increase number of doctors.")
    else:
        W = 1 / (doctors * service_rate - arrival_rate)

        st.subheader("📊 Results")
        st.write("Utilization factor:", round(rho, 2))
        st.write("Average waiting time:", round(W, 3))

        # Graph
        lam_values = np.arange(1, doctors * service_rate, 1)
        waiting_times = 1 / (doctors * service_rate - lam_values)

        fig, ax = plt.subplots()
        ax.plot(lam_values, waiting_times, marker='o')
        ax.set_xlabel("Arrival Rate")
        ax.set_ylabel("Waiting Time")
        ax.set_title("Hospital OPD Queue Model (M/M/c)")
        ax.grid(True)

        st.pyplot(fig)