# What is SonarQube?

### SonarQube is an open-source platform for continuous inspection of code quality. It performs static code analysis to detect:

Bugs: Code Bugs <br>
Code Smells: Signs of poor code architecture that works well but can make code difficult to manage in longer run.<br>
Security Vulnerabilities: Any credentials expose in the code or vulnerable packages.<br>
Duplications: Repeated code block which can be consolidated.<br>
Coding Standard Violations: Suggestions as per best practice coding.<br>


# Code Testing

### Unit testing

Unit testing is like checking each individual piece of a machine to make sure it works correctly before assembling the whole machine. In programming, a unit test focuses on testing the smallest testable parts of your code - typically individual functions or methods.

Focuses on individual components or functions.<br>
Tests specific, small pieces of code.<br>
Typically written by developers.<br>
Checks if each part works correctly in isolation.<br>

```
def add_numbers(a, b):
    return a + b

# Unit test for the add_numbers function
def test_add_numbers():
    # Check if the function works with positive numbers
    assert add_numbers(2, 3) == 5, "Failed for positive numbers"
    
    # Check if the function works with negative numbers
    assert add_numbers(-1, -1) == -2, "Failed for negative numbers"
    
    # Check if the function works with zero
    assert add_numbers(0, 5) == 5, "Failed with zero"

# Run the test
test_add_numbers()
print("All unit tests passed!")
```

### Functional testing might also known as integration testing,

Functional testing is like testing the entire machine to make sure it does what it's supposed to do from the user's perspective. It checks if the entire system or application works correctly as a whole.

Focuses on the entire system or application.<br>
Tests how different components work together.<br>
Can be done by developers or dedicated QA testers.<br>
Checks if the system meets overall requirements.<br>


#### Functional tests are genrally carried by QA team. And it tests the whole applications testing with the real scenarios So in microservice arch we cant include the functional testing in the CICD pipeline as every service is doing a part of the application. So unit test cases are included in the CICD pipeline and then Functional testing carried out by dedicated team in other testing env.