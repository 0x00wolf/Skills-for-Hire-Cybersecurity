# Description:
This is code that I wrote while taking the "Practical Encryption and Cryptography Using Python' course on Pluralsight for the SfH program. The code presented in teh course was written in Python 2.7, and failed to compile in Python 3. 

## Authenticate v1-4
**The 1st version** of Authenticate was the original code in Python 2.7 from the Pluralsight platform. The original program had two modes, subscribe and login. Subscribe allowed for a username and password to be input. The username and a hash of the password would be written to a text file (the program could only save one user at a time). When selecting login the user would be prompted to input a username and password. The username would be matched to the saved username, and the password would be hashed and compared to the saved hash. If both matched the program printed that the user had logged in successfully.
**The 2nd version** is after I updated the code to work with Python 3.1.     

**The 3rd version** is after I implemented a number of upgrades. Multiple users can now be saved. If a user tries to use a previously selected username the program will indicate the name is taken. The passwords are salted before being hashed.   
**The 4th version** is the same code as the third but with comments explaining how everything works for my classmates in the SfH program who are new to programming.  
