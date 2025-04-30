# Group17-Noblis
## Sponsor Organization Name: Noblis  
### Sponsor POC:  
| Name & Title          | Dayton Jung, Technical Project Manager |  
|-----------------------|---------------------------------------|  
| Location              | Reston, VA                            |  
| Phone                 | 571-599-0190                          |  
| Email                 | Dayton.Jung@noblis.org                |  

### Sponsor Technical SME:  
| Name & Title          | Eric Epstein                          |  
|-----------------------|---------------------------------------|  
| Location              | Reston, VA                            |  
| Email                 | Eric.Epstein@noblis.org               |  

---

### I. Project Name:  
**The Design of a Framework for Synthetic PCAP Data Generation and Network Simulation**  

### II. Project Objectives:  
a. Designing and implementing a flexible framework to stand up various diverse network environments.  
b. Developing modules to simulate various network components, including different computer types, operating systems, printers, and enterprise tools (e.g., Microsoft Teams, PowerPoint, Outlook).  
c. Incorporating realistic internet browsing patterns and behaviors into the simulation.  
d. Implementing PCAP data collection mechanisms at multiple points within the simulated networks.  
e. Analyzing how network traffic patterns and PCAP data characteristics change with different network configurations and user behaviors.  

### III. Project Overview:  
This capstone project challenges undergraduate students to integrate knowledge from Cyber Security, Networking, and Data Collection to address a critical need in the field of network analysis. The focus is on developing a framework for generating synthetic Packet Capture (PCAP) data across various simulated network environments.  

There is a need for diverse and representative network traffic data to enhance threat detection, network analysis, and security tool development. However, obtaining relevant PCAP data from real networks poses privacy and logistical challenges. This project aims to address this concern by creating a versatile system for simulating different network architectures and generating corresponding PCAP data.  

---

### Group Implementation Plan  

#### **Tools and Technologies**  
1. **GNS3 for Network Building**:  
   - The team will use **GNS3** to design and simulate diverse network topologies, including enterprise environments with devices like routers, switches, and endpoints.  
   - GNS3 allows for integration with real and virtual devices, enabling realistic traffic generation and behavior modeling.  

2. **AWS Bare Metal for Hosting**:  
   - The simulated networks and data collection framework will be hosted on **AWS Bare Metal** instances to ensure scalability, performance, and reliability.  
   - AWS provides the flexibility to deploy custom environments and handle high-throughput PCAP data generation.  

3. **Python for Synthetic PCAP Generation and Configuration**:  
   - **Python scripts** will be developed to:  
     - Automate network configurations in GNS3.  
     - Generate synthetic PCAP data with customizable traffic patterns (e.g., HTTP, DNS, VoIP).  
     - Simulate user behaviors (e.g., browsing, email, video conferencing) using libraries like Scapy.  
   - Python will also be used to analyze traffic patterns and validate the realism of synthetic data.  

#### **Workflow**  
1. **Design Phase**:  
   - Create network topologies in GNS3 based on real-world scenarios (e.g., small office, enterprise).  
   - Define traffic profiles (e.g., normal vs. attack traffic) for synthetic data generation.  

2. **Implementation Phase**:  
   - Deploy GNS3 networks on AWS Bare Metal.  
   - Use Python to automate traffic generation and PCAP collection at strategic points.  

3. **Analysis Phase**:  
   - Compare synthetic PCAP data with real-world benchmarks to ensure fidelity.  
   - Adjust parameters (e.g., latency, packet size) to refine simulations.  

---

### IV. Major Deliverables  

#### a. Required Deliverables (must have)  
| Deliverable                          | Due Date      |  
|--------------------------------------|---------------|  
| Draft Penetration Testing Appendix   | Mid Fall      |  
| Final Penetration Testing Appendix   | Late-Fall     |  
| Draft Report                         | Early Spring  |  
| Final Report                         | Late Spring   |  
| Network Generation and Collection Framework | Late Spring   |  

#### b. Desired Deliverables (nice to haves)  
| Deliverable                          | Due Date      |  
|--------------------------------------|---------------|  
| Network Analysis Tool User Guide     | Late Spring   |  
| Network Structure Analysis           | Late Spring   |  

---

### V. Hours / Week  
2 hours/week with the ability to answer questions via email.  

### VI. Project Resources  
| Resource Type    | Description                          | Provided By (GMU or Sponsor) |  
|-------------------|--------------------------------------|-----------------------------|  
| Compute           | Virtual Lab resources                | GMU                         |  
| Software          | Enterprise Network Applications      | Free Online Applications (Zoom, Gmail, etc.), Microsoft services |  

### VII. Student Team: Skills and Size  
#### a. Required Skills  
- Familiarity with PCAP data and network structures.  
#### b. Desired Skills  
- Experience with network monitoring tools (e.g., Wireshark, physical TAPs).  
- Knowledge of virtual/physical infrastructure (e.g., VMware, GNS3).  
- Python programming for automation and data generation.  
#### c. Team Size  
4-5 students.  

### VIII. Citizenship:  
Yes  
