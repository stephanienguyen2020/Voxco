# Voxco
## Introduction
VoxcoPyAuto is a Python-based automation tool designed specifically to streamline the survey data collection process for the Poverty Tracker study conducted by the Center on Poverty & Social Policy at Columbia University. This project is part of a partnership with Robin Hood and Columbia University, aimed at understanding the dynamics of poverty, hardship, and disadvantage in New York City.

## Background
The Poverty Tracker is a critical initiative that follows a panel of approximately 2,000 to 3,000 New York City households, surveying them every three months over several years. This approach enables the collection of detailed and longitudinal data on income, material hardships, health, and well-being, thereby providing insights into the evolving nature of disadvantage in the city.

As a Research Assistant involved in this project, I encountered a significant challenge during my daily tasks, which involved making 40 to 60 calls to survey participants. After about 1000 calls, I observed a consistent pattern: approximately 90% of these calls ended up in voicemail, especially during daytime shifts. Recognizing this repetitive pattern, I identified an opportunity to optimize the process using automation.

## The Solution: VoxcoPyAuto
To address this challenge, I developed VoxcoPyAuto using Python and PyAutoGUI. This script is tailored to automatically mark calls that reach voicemail without a message (denoted as 'MACH' in Voxco) as complete. This automation significantly reduces the manual effort required in the survey process and increases efficiency in data collection.

### Demo
Stay tuned for a comprehensive video demonstration of VoxcoPyAuto in action! I'll be uploading a walkthrough video showcasing the program's functionality and features very soon.

### File Structure
- **voxco_demo.py**: This script provides a comprehensive start-to-finish demonstration of the program. It includes functions to open the browser (Safari in this case), navigate to the survey website, and enter login credentials (username, password, and survey code). The script then selects a survey (a test survey for the demo) and initiates the call process. It waits for a period between 170s and 230s, and if the call doesn't connect, it marks it as 'MACH' and proceeds to the next call. This demo version doesn't include a loop for multiple calls and omits actual login information for privacy.

- **test.py**: Designed for situations where you need to bypass survey selection (useful when manually choosing a survey or when there are multiple surveys to choose from). It retains the call-making process of voxco_demo.py with the addition of a for-loop set to run three times, which can be adjusted as needed.

- **position.py**: A utility script used to determine the screen positions of various elements. This is especially useful for adapting the script to different systems and browsers, as it doesn't rely on PyAutoGUI's image recognition and is more scalable across different operating systems.

- **log_in_only.py**: A simplified script that focuses solely on opening the browser, navigating to the survey website, and handling the login process.

- **TS_new_call.py** & **S2_new_call.py**: Variants of voxco_demo.py, these scripts are tailored for specific surveys (TS for the test survey and S2 for another survey). They exclude the login process, assuming the user is already logged in, and focus on initiating new calls.

### Features
- Automated Call Marking: Automatically marks calls as 'MACH' in Voxco when you reach voicemail without leaving a message. 
- User-Friendly: Easy to set up and use, requiring minimal technical expertise.
- Efficiency Boost: Reduces manual effort, allowing more focus on other critical aspects of the study.

### Installation
To use VoxcoPyAuto, you will need Python installed on your system along with PyAutoGUI. Check the following guides for detailed instructions
1. How to install [Python](https://www.python.org/downloads/)
2. How to install [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html)

### How to Run the Program
To use this tool, select an Integrated Development Environment (IDE) that suits your preference. I personally recommend Visual Studio Code. After forking this repository and cloning it to your local machine, you can run the script in any IDE you choose without requiring additional setup.

### Upcoming Enhancements
- Scheduled Login Automation with Calendar Analysis: Currently, the tool requires manual initiation at the start of each shift. I'm programming VoxcoPyAuto to analyze my Google Calendar to recognize my shift patterns, allowing the tool to automatically log in at the right times. This will allow the script to start and log into Voxco at predetermined times, aligning with varying shift schedules.

- Voice Recognition Integration: To make the tool more interactive and responsive, I am exploring the integration of voice recognition technology. This advancement will enable the script to detect and understand specific verbal requests from survey participants, such as scheduling a callback or opting to complete the survey online.

- Automated Survey Administration: A significant enhancement will be the automation of survey administration for participants willing to engage immediately. The script will play recorded questions, wait for the participant's response, and then intelligently analyze and record their answers before proceeding to the next question. This feature aims to make the survey process more efficient and less labor-intensive.

- Automatic Logout: To further automate the process, the tool will be upgraded to automatically log out of Voxco at the end of the shift. This feature will ensure that the session is securely closed each day without the need for manual intervention.

### Contributions
Feedback and contributions to VoxcoPyAuto are welcome. If you have suggestions or improvements, please feel free to submit a pull request or open an issue in the repository.

