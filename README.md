# FraudDetect
### Setting Up and Running the Program
To run this program, first download it as a ZIP. You must use a Python version >= 3.6.0. Navigate to the "FraudDetect-master" directory via the command line. <br/>
Install the required dependencies:

```
pip install ipinfo
```

and 

```
pip install geopy
```
On line 18, replace my file path with the path to the actual file containing previous login attempts<br/>
To run the program enter `python3 fraud.py` in the command line and type in a new IP address to score when prompted.

### Follow Up Questions
* What circumstances may lead to false positives or false negatives when using solely this score?
  * Scoring new login attempts with just the distance between the new login attempt and the closest previous login attempt      will lead to false positives if a user is attempting to log in from very far away from where they normally log in from. For example, if the user is traveling in another country where there have been fraudulent login attempts, then if the user tries to log in, it will be flagged as fraudulent. This method of scoring will result in false negatives if a fraudulent login in attempt is made from an IP address that is very close to where most of the valid login in attempts from a user are made.
* What challenges are there with computing distances based on latitude/longitude? 
  * One of the challenges with computing distances based on latitude and longitude is that the equation uses trigonometry functions. Also, the values must be handled as radians. Fortunately, there are packages like geopy that have written these calculations for us.
  
### Further Considerations
Before starting to work, I spent a lot of time thinking about the data structure I wanted to use to store the previous login attempts from the file. This was challenging because I wanted my program to be efficient and the file could contain hundreds of thousands of attempts. I decided on a dictionary because it supports lookup in constant time, which is useful for checking if an attempt from a specific IP was fraudulent or valid.<br/>

To improve this program in the future. I would add more ways of scoring a login attempt. Defining whether or not a login attempt is fraudulent based on the validity of the previous attempt from the closest IP address to the IP address of the current attempt is not always accurate. This method is useful in some cases, so I would want to use it with other scoring methods. One other way of scoring login attempts could be by keeping track of how frequently an attempt is made from a certain IP address. This could be used to check if the other attempts from the IP address were valid or fraudulent. You could also keep track of the times requests were made from a specific IP address, which would easily show if someone was attempting a brute force attack. I would also like to improve this program by adding some error handling. In particular, I would like to  catch errors thrown by the ipinfo API when the user inputs an invalid IP address. Another way I would improve this program would be creating a way to detect if a user's login attempt was denied because they typed their password incorrectly. This may involve changing the way previous attempts are stored in the file. This is a problem because if the user typed their password incorrectly, then made another attempt from the same IP address, the attempt would be flagged as fraudulent.
