# TcpPackerCaptureAnalyzer

This project is a Packet Capture Analyzer. Depending upon the values of fields, captured packet have, it generates the output as HTML file with the plot of graph for Number vs Packet Length field. It has also tshark, the command line version of wireshark, while development.

COMPILING AND RUN
1. Install Virtualenv by command python3 -m pip install virtualenv
2. Create a virtual environment by command virtualenv env
3. Clone our repository
4. Install Dependencies by command - pip install -r requirements.txt
5. Capture some packets and generate pcap file.
7. Run the python script giving generated pcap file as the input by command: python script.py project.pcap
7. Run the flask server by command python3 app.py
8. Navigate through buttons to observe different renders pages

