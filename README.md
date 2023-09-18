# Bank Info

### About the project

A server program that, by card bin number, provides information about the bank that issued the card. 
#
### Recommendations for installation and initial start-up.
*Project+tests+docker:*
  1) Download the repository:<pre>`git clone https://github.com/VIadIen/Bank_info.git`</pre>
  2) Generate an image based on the dockerfile from the repository: <pre>`docker build -t <name_of_image> .`</pre>
  3) Start the container (it is recommended to use port 4000 for correct operation): <pre>`docker run -p 4000:4005 <name_of_image>`</pre> The server is available at: `http://localhost:4000/`
  4) For test:
     - Create virtual environment
     - Download packages from requirements.txt
     - Run the *test_unittest.py* and *test_pytest.py* files using the commands:<pre>`pytest test_unittest.py`</pre> and <pre>`pytest test_pytest.py`</pre>The server must be running during testing.

*Project+tests*
  1) Download the repository: <pre>`git clone https://github.com/VIadIen/Bank_info.git`</pre>
  2) Replace the port number from 4005 to 4000 in the "Bank_info/InfoBank/server.py" file. Run server.py using the <pre>python server.py</pre> The server is available at: `http://localhost:4000/`
  3) For test:
     - Create virtual environment
     - Download packages from requirements.txt
     - Run the *test_unittest.py* and *test_pytest.py* files using the commands:<pre>`pytest test_unittest.py`</pre> and <pre>`pytest test_pytest.py`</pre>The server must be running during testing.

*Docker*
  1) To load the container, use the command:<pre>`docker pull viadien/bank-info`</pre>

  2) To run the container, use the command:<pre>`docker run -p 4000:4005 --name &ltexample&gt viadien/bank-info`</pre> or <pre>`docker run -p 4000:4005 viadien/bank-info`</pre> The server is available at: `http://localhost:4000/`

## Good luck!

