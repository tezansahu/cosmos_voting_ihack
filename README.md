# Cosmos Election Protocol

## Ethereum-based Voting Platform for public governance 

***

### Overview:

Cosmos Election Protocol is a blockchain-based voting platform, which is made keeping the security and user experience in mind. The UX is as intuitive as a normal app, however not compromising on the scalability, transperancy & anonymity. 

The project is made keeping in mind general elections, though the UX and details can be easily modified to fit any specific use case:

- State Elections
- Municipal Elections
- Trade Unions
- Senate elections
- Proxy voting for publicly listed companies


### Problems Solved:

- __Transparency:__ As smart contracts are public, anyone can verify the logic for vote casting & result declaration used in realtime or post-election. Voters can verify if their votes were recorded correctly
- __Immutability:__ No more allegations like EVM Hacks. It is made secure enough to make sure there is no malicious activity possible once the vote is recorded on the blockchain.
- __Anonymity:__  No one can figure out who voted for whom, even after results are declared.
- __Intuitive UI/UX :__ No extra training required for the end users to cast votes
- __Increase in voter turnout:__ The voter doesn't have to be present physically in his constituency anymore to vote.
- __Automatic Voter ID:__ No more standing in queues to get Voter ID Card.
- __No more missing names from voter's list:__ Anyone who registered in phase 1 and is above 18 yrs of age will be able to vote.
- __Faster result declaration:__ Results will be available within a few hours of the end of the voting phase.

### Tech-Stack to be Used:
- Ethereum & Solidity (for blockchain & smart contracts)
- Angular (for front-end)
- Django (for back-end) 

### Setting up the project:

- Fire up a terminal & clone the repo:
    ```bash
    $ git clone https://github.com/tezansahu/cosmos_voting_ihack.git`
    $ cd cosmos_voting_ihack
    ```
- Start 4 terminals:
    - Terminal 1:
        ```bash
        $ ganache-cli
        ```
    - Terminal 2:
        ```bash
        $ cd dapp/
        $ truffle deploy --reset
        $ node setup.js
        ```
    - Terminal 3:
        ```bash
        $ cd django
        $ pip3 install -r requirements.txt
        $ cd vote
        $ python3 manage.py runserver
        ```
    - Terminal 4;
        ```bash
        $ cd dapp/
        $ npm start
        ```

- Now go to http://localhost:4200 to visit the project page

- The django admin page can be accessed at http://localhost:8000

***
<p align="center">Created with ❤️ by <a href="https://www.linkedin.com/in/tezan-sahu-a85802163/">Tezan Sahu</a> & <a href="https://www.linkedin.com/in/akash981/">Akash Kumar</a></p>