import streamlit as st
def style():
    hide_st_style = """
                <style>
                html {
                    overflow: hidden;
                    overscroll-behavior: none;
                }
                overflow: hidden;
                overscroll-behavior: none;
                body {
                    margin: 40px auto;
                    line-height: 1.6;
                    font-size: 18px;
                    color: #444;
                    /* padding: 0 10px; */
                    background-color: rgb(255, 255, 255);
                    font-family: Arial;
                    font-weight: 300; /* font thickness */
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
                h1, h2, h3 {
                    font-family: Helvetica;
                    line-height: 1;
                    font-weight: 375; /* font thickness */
                }
                a.link {
                    margin-left: 20px;
                    text-decoration: none;
                    font-family: inherit;
                    color: #4CAF50;
                    transition: text-decoration 0.3s ease;
                }
                a.link:hover {
                    text-decoration: underline;
                }
                a.h2link {
                    margin-left: 20px;
                    text-decoration: none;
                    font-family: inherit;
                    color: #adadad;
                    transition: text-decoration 0.3s ease;
                }
                a.h2link:hover {
                    text-decoration: underline;
                }
                /* Media Queries for Mobile Devices */
                @media only screen and (max-width: 480px) {
                    body {
                        padding-left: 20px;
                        padding-right: 20px;
                    }
                }
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(
            """
            <style>
            .centered-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .stButton button {
                background-color: #28a745;  /* Original green color */
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 24px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
            }
            .stButton button:hover {
                background-color: #FD5200;  /* Change this color to your preferred hover state */
                color: #ffffff;  /* Set the hover text color */
            }
            </style>
            """,
            unsafe_allow_html=True)
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    div.st
    </style>""", unsafe_allow_html=True)

def make_title(title):
    return f"""
        <div id="content" style="max-width: 95%; max-width: 665px; margin: auto; z-index: 1000;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: -2px;">
            <img src="/docs/CCBS.png" alt="Your Alt Text" style="width: 80px; flex: 0.2; margin: 0;">
            <h1 style="text-align: center; flex: 1; margin: 0;">{title}</h1>
            <div style="flex: 0.2;"></div>
        </div>
        <hr style="margin-top: 10px;">
    """

header =   """
<div style="position: fixed; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; height: 40px; display: flex; justify-content: center; align-items: center; background-color: #f0f0f0; top: 0; overflow: auto; padding-left: 20px; padding-right: 20px; box-sizing: border-box; z-index: 1000;">
    <div class="link" style="text-align: center;">
    <a href="https://cleanmybuilding.co" class="link" style="font-size: 0.85em;">Clean my building Co.</a>
    </div>

    <div class="link" style="text-align: right;">
    <a href="https://cleanmybuilding.co/employees/" class="h2link" style="font-size: 0.85em;">Employees</a>
    </div>
</div>
<div style="height: 50px;"></div>
<div id="content"></div>
"""

footer = """
<div style = "margin-top: 100px;">
    <div style="margin-bottom: -50vw; margin-left: -50vw; margin-right: -50vw; height: 200px; display: flex; justify-content: center; align-items: center; background-color: #f0f0f0; top: 0; top: 0; overflow: auto; padding-left: 20px; padding-right: 20px; box-sizing: border-box; z-index: 1000;">
            <div class="link" style="text-align: center;">
            <a href="https://cleanmybuilding.co" class="link" style="font-size: 0.76em;">Clean my building Co.</a>
            </div>

            <div class="link" style="text-align: right;">
            <a href="https://cleanmybuilding.co/employees/" class="h2link" style="font-size: 0.76em;">Employees</a>
            </div>
    </div>
"""

def get_request_body(subtitle, manager_name="Manager"):
    request_body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple HTML Page</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #FFFCF2; color: #513301; margin: 0; text-align: center;">
        <div class="header" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <h2>Clean my Building Co.</h2>
        </div>
        <div class="container" style="width: 70%; margin: 0 auto; background-color: white; padding: 50px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; text-align: center;">
            <h1 style="margin-bottom: 20px; color: #513301;">{subtitle}</h1>
            <p><a href="https://cleanmybuilding.co/employees/pto/approve/" class="btn" style="background-color: #3D2701; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: block; font-size: 16px; margin: 10px auto; cursor: pointer; border: none; border-radius: 8px; transition: background-color 0.3s; width: fit-content;"> ✓  Approve/Decline  ✕ </a></p>
            <p><a href="https://cleanmybuilding.co/employees/pto/calendar/" class="btn" style="background-color: #3D2701; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: block; font-size: 16px; margin: 10px auto; cursor: pointer; border: none; border-radius: 8px; transition: background-color 0.3s; width: fit-content;">📅 PTO Calendar</a></p>
        </div>
        <div class="footer" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <p>Clean my Building Co.</p>
        </div>
    </body>
    </html>
    """
    return request_body

def get_pto_confirmation_email():
    email = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>You have successfully requested PTO</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #FFFCF2; color: #513301; margin: 0; text-align: center;">
        <div class="header" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <h2>Clean my Building Co.</h2>
        </div>
        <div class="container" style="width: 70%; margin: 0 auto; background-color: white; padding: 50px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; text-align: center;">
            <h1 style="margin-bottom: 20px; color: #513301;">You have successfully requested PTO</h1>
            <p style="font-size: 18px;">Please wait for the approval email, your manager has to review the request</p>
            <a href="https://cleanmybuilding.co/employees/pto/total/" class="btn" style="background-color: #3D2701; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 20px auto; cursor: pointer; border: none; border-radius: 8px; transition: background-color 0.3s;">Check your PTO usage ➕ </a>
        </div>
        <div class="footer" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <p>Clean my Building Co.</p>
        </div>
    </body>
    </html>
    """
    return email

def get_pto_approval_email(startDate, endDate):
    email = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your PTO request has been reviewed!</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #FFFCF2; color: #513301; margin: 0; text-align: center;">
        <div class="header" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <h2>Clean my Building Co.</h2>
        </div>
        <div class="container" style="width: 70%; margin: 0 auto; background-color: white; padding: 50px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; text-align: center;">
            <h1 style="margin-bottom: 20px; color: #513301;">Congrats! Your PTO request has been reviewed</h1>
            <p style="font-size: 18px;">Your PTO from {startDate} to {endDate} has been reviewed. If you need to check your PTO usage, click the button below.</p>
            <a href="https://cleanmybuilding.co/employees/pto/total/" class="btn" style="background-color: #3D2701; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 20px auto; cursor: pointer; border: none; border-radius: 8px; transition: background-color 0.3s;">Check your PTO usage ➕ </a>
        </div>
        <div class="footer" style="width: 100%; text-align: center; padding: 10px 0; background-color: #CCC5B9; color: #513301;">
            <p>Clean my Building Co.</p>
        </div>
    </body>
    </html>
    """
    return email



