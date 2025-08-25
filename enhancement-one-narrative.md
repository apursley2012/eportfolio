---
layout: default
title: Enhancement One Narrative 
permalink: /enhancement-one-narrative/
---


<!-- Simple nav -->
<nav style="margin-bottom: 20px;">
  <a href="./index.md">Home</a> |
  <a href="/enhancement-one-narrative/">Enhancement 1 Narrative</a> |
  <a href="/enhancement-two-narrative/">Enhancement 2 Narrative</a> |
  <a href="/enhancement-three-narrative/">Enhancement 3 Narrative</a> |
   <a href="https://github.com/apursley2012/eportfolio/tree/main/enhancement-one">Enhancement 1 Project</a> |
  <a href="https://github.com/apursley2012/eportfolio/tree/main/enhancement-two">Enhancement 2 Project</a> |
  <a href="https://github.com/apursley2012/eportfolio/tree/main/enhancement-three">Enhancement 3 Project</a> |
   <a href="https://corner-grocer-alyshaspradlin.replit.app">Enhancement Demo</a> 

<!-- Enhancement 1 Narrative — Software Design & Engineering -->
# Software Design &amp; Engineering Enhancement

## Artifact Overview

&nbsp;&nbsp;&nbsp;&nbsp; The artifact I’m enhancing is a C++ console program called CornerGrocerApp.cpp, originally created in CS 210: Programming Languages. The application reads grocery item data from a text file, counts how often each item appears, and displays the results either in a simple list or a histogram. The program uses a std::map to track frequencies and runs entirely in the terminal with a basic menu system. It’s clean and functional, but it’s also limited—there’s no error messaging for failed operations, and it doesn’t support any kind of expansion or integration outside of its current setup.

### Justification for Inclusion

&nbsp;&nbsp;&nbsp;&nbsp; I selected this artifact for my ePortfolio because it is a strong example of my ability to design and implement a functional software solution from start to finish. It addresses a real problem—tracking and displaying frequency data from inventory records—and clearly shows my understanding of programming logic, user interaction, and data organization.

&nbsp;&nbsp;&nbsp;&nbsp; For this enhancement, I rewrote the artifact in Python, maintaining the original functionality while improving its design and expanding its capabilities. The enhanced version introduces a class-based structure with a GroceryFrequency class, improved input validation, and stronger error handling. I also added new menu options to back up both the frequency list and the histogram to separate text files. Each backup feature now provides a clear confirmation message that includes the full file path when a save is successful, or an error message if it fails. These improvements not only make the application more robust and user-friendly but also demonstrate my ability to modernize existing code and apply current best practices.

### Course Outcomes and Skills Demonstrated

**_This enhancement clearly aligns with the software engineering and design category. It touches on several course outcomes and builds on a wide range of technical skills:_**

•	**Language Portability:** Rewriting the entire application in Python while keeping the original functionality intact shows I can translate logic between languages.

•	**Programming Proficiency:** The core logic—reading data, counting items, sorting results, and interacting with users—is now implemented using Python best practices.

•	**Software Design Principles:** I used a class-based structure to keep things organized and modular, which makes future changes easier to manage.

•	**Input Validation:** Every input is now validated to make sure the program can’t crash due to unexpected values. This includes menu selections and item searches.

•	**File I/O and Error Handling:** I added try-except blocks to handle file errors gracefully. If something goes wrong, the program tells the user instead of crashing.

•	**New Features:** The app now includes two backup options—one for the frequency list and one for the histogram. Each one confirms whether the file was saved successfully.

•	**Commenting and Documentation:** Every part of the program includes clear, useful comments that explain both what the code is doing and why. This makes the program easier to read, maintain, or extend in the future.

•	**Secure Programming Mindset:** I took care to write safe, predictable code that doesn’t rely on assumptions about the input or file system. This reduces the risk of unexpected behavior or data issues.

**These updates directly support the following course outcomes:**

•	**Outcome 1:** I wrote the code in a way that makes it easier for others to read, understand, and work with—whether they’re teammates or future maintainers.

•	**Outcome 2:** The new version is not only functional, but also well-documented and logically structured, which reflects professional software development standards.

•	**Outcome 3:** Rebuilding the app in Python shows I can design a computing solution that follows appropriate principles and makes smart trade-offs between simplicity and functionality.

•	**Outcome 4:** I used modern Python features and coding techniques that make the software easier to use and expand in the future.

•	**Outcome 5:** I made sure the design is stable and secure by validating inputs, handling errors, and providing users with clear feedback when something fails.

### Reflection on the Enhancement Process

&nbsp;&nbsp;&nbsp;&nbsp;Enhancing this artifact gave me the chance to approach the project from a different perspective than when I originally built it. In the C++ version, my focus was on meeting the assignment requirements and ensuring the program worked correctly. For the enhancement, I treated it as if I were delivering a tool that others might rely on, which meant paying closer attention to maintainability, usability, and scalability. That shift in focus guided every design choice I made, from adopting a class-based structure to making sure the program clearly communicates with the user at every step.

&nbsp;&nbsp;&nbsp;&nbsp;I also learned how valuable it is to design features with flexibility in mind. The new backup functionality is a good example—it works now by creating simple text files, but it’s built in a way that I could easily change the format, save location, or even connect it to a database in the future without rewriting the entire program. This kind of forward-looking design wasn’t something I prioritized in the original project, but it’s a habit I plan to carry forward.

&nbsp;&nbsp;&nbsp;&nbsp;Another key takeaway is how much the right tools can simplify the logic and reduce complexity. Using Python’s defaultdict allowed me to eliminate unnecessary checks and streamline the frequency-counting process, resulting in code that is both shorter and easier to read. This reinforced the idea that choosing the right data structures and language features from the start can save significant time and effort later. Overall, this enhancement not only improved the program itself but also strengthened my approach to software design. It reminded me that a well-built application should be easy to maintain, adaptable to future needs, and clear for both users and other developers to work with.
