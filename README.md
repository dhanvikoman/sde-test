# SDE Online Assessment

The purpose of this test is to evaluate your:

- development skills in a production environment
- ability to provide a solution given a specification using best practices
- design thinking
- coding style
- ability to containerize a solution using Docker

You may use any language you are comfortable with, as long as it is quick and simple to execute in Docker. If you're unfamiliar with Docker, just **be sure that your submission can be run within the command line**.

## Problem description

Given a JSON file which will define an array of **bond** objects (of arbitrary size), write a **command-line tool** to calculate the **spread** between each **corporate bond** and the nearest **government bond** benchmark, save these results in a JSON file, and express the spread in **basis points**, or **bps**. If any properties are missing from a bond object, do not include it in your calculations or output.

**Spread** is defined as the difference between the yield of a corporate bond and its government bond benchmark.

A government bond is a good **benchmark** if it is as close as possible to the corporate bond in terms of **years to maturity**, also known as **term** or **tenor**.

If there is a *tie* for closest government bond by **tenor**, break the tie by choosing the government bond with the *largest* **amount outstanding**.

To convert your difference to **basis points**, just scale your spread by 100 and display as an integer (truncate trailing decimals), e.g. if your spread comes out to 2.127, this will be expressed in your output file as "212 bps".

### Sample input

```json
{
  "data": [
    {
      "id": "c1",
      "type": "corporate",
      "tenor": "10.3 years",
      "yield": "5.30%",
      "amount_outstanding": 1200000
    },
    {
      "id": "g1",
      "type": "government",
      "tenor": "9.4 years",
      "yield": "3.70%",
      "amount_outstanding": 2500000
    },
    {
      "id": "c2",
      "type": "corporate",
      "tenor": "13.5 years",
      "yield": null,
      "amount_outstanding": 1100000
    },
    {
      "id": "g2",
      "type": "government",
      "tenor": "12.0 years",
      "yield": "4.80%",
      "amount_outstanding": 1750000
    }
  ]
}
```

### Sample output

```json
{
  "data": [
    {
      "corporate_bond_id": "c1",
      "government_bond_id": "g1",
      "spread_to_benchmark": "160 bps"
    }
  ]
}
```

### Explanation

The code written reads the json file from the parser argument that is passed while executing the command line. For executing here, I have used the sample_input.json file and thus the docker file has the same as the input. The script is a simple read and transform and write operation that gets the required values and then gives the output file. The time complexity in this case is O(N) because I am using a for loop to iterate through one dataframe i.e. it is of linear time complexity that depends on the number of corporate types that are there. 
The code is written in python and can be executed from the command line using the simple command which is:
$ python sde-test-solution.py sample_input.json output_file.json
The main logic that I used was to separate the corporate and government bonds and then compare the closeness of each corporate to each government bond and then get the smallest difference to determine the closeness of the two. Once the pairs have been identified, the yield is calculated and then the values are saved.
The output json is in the tabular schema that has the data portion represented as shown by the output.


