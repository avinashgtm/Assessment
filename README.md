# MNTN Assessment

## Public Api Info
For this excercise I have choosen a simple public api which takes in an ip address andd provides some info like from which city is the request being made, country etc

## What do tests do
I wrote few tests using pytest python framework verifying certain things that are mentioned in the docstrings of the test
 
## Running the tests
    ### Python 2.7 and git are already installed on the machine ###
1. Pull git@github.com:avinashgtm/Assessment.git and cd to the directory
2. Install python packages with the command : pip install -r requirements.txt
3. Execute the tests with the command : pytest --html=report.html

## Reading test report
After step 3 is executed successfully report.html should have been generated in the same directory, just open it in your browser it will show you what tests it ran

## Pros on this approach
1. Quick set up of test environment
2. Faster test execution
3. No cost involved on buying expensive licenses to thrid party test tools
4. Very light weight and easy call via CI/CD tool
5. In this exercise I am generating html report but there is also an option to generate junit style report which can be easily read via Jenkins for reporting

## Cons on this approach
1. Some technical know how is involved
2. Installing python packages, which can increase depending on how many will be used for testing the whole application
3. inadvertent security issues on using third party packcages