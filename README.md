# Password Generator and Encrypter
## password_creator.py is the main file. 
Functionality includes:
* Creating your custom password. 
* Running a check of that custom password against a list of commonly used passwords
* Generating a complex custom password based on user input of a number of characters for the password (with a warning message for short passwords)
* Encrypted the generated password using a simple substitution cipher
* Decrypting a ciphertext that was created using the above encryption


It is common knowledge for most these days that a strong password is necessary for security online.

A strong password consists of:

- A combination of numbers, letters and special characters
- A random ordering of characters (i.e. no consecutive letters or numbers)
- Definitely no common phrases or words (like ‘password’…)
- At least 16 characters 
[This reddit user](https://www.reddit.com/r/dataisbeautiful/comments/ifral7/oc_time_it_takes_to_crack_a_password_updated/) shared a great visual that describes perfectly what a strong password means:

![image](https://preview.redd.it/kqgnls4nzyi51.jpg?width=960&crop=smart&auto=webp&s=09ada6a85dd784af54771ec533aac2b83337cc04)
 
With that in mind, and as an introduction to some fundamentals of Python, I decided to implement a password generator as my first ever pet project.
I have made 2 password generators:
- v1.0 – provides the user with a 16 digit password that is guaranteed to be a random assortment of letters, capital letters, numbers and special characters
- v2.0 – provides a password based on the user input of how many digits they would like the password to be set for. It gives the user a warning if the password is less than 8 digits. 

