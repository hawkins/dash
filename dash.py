#!/usr/bin/env python3

from dotenv import load_dotenv

from dc_dashboard import DCDashboard

if __name__ == "__main__":
    load_dotenv()
    d = DCDashboard()
    print(d.render())
