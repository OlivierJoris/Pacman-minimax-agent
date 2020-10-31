#!/bin/bash

echo -e "hminimax0.py\n"

echo -e "dumby"
python run.py --layout large_adv --agentfile hminimax0.py --ghostagent dumby
echo -e "greedy"
python run.py --layout large_adv --agentfile hminimax0.py --ghostagent greedy
echo -e "smarty"
python run.py --layout large_adv --agentfile hminimax0.py --ghostagent smarty

echo -e "hminimax1.py\n"

echo -e "dumby"
python run.py --layout large_adv --agentfile hminimax1.py --ghostagent dumby
echo -e "greedy"
python run.py --layout large_adv --agentfile hminimax1.py --ghostagent greedy
echo -e "smarty"
python run.py --layout large_adv --agentfile hminimax1.py --ghostagent smarty

echo -e "hminimax2.py\n"

echo -e "dumby"
python run.py --layout large_adv --agentfile hminimax2.py --ghostagent dumby
echo -e "greedy"
python run.py --layout large_adv --agentfile hminimax2.py --ghostagent greedy
echo -e "smarty"
python run.py --layout large_adv --agentfile hminimax2.py --ghostagent smarty